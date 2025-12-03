import sys, json, argparse, signal
from datetime import datetime
from utils import sheets_helper

narrow_scraps = {}
def enum_check(target_slot_name, target_schema, source_slot_name, source_schema):
    logic = {}
    target_range = target_schema["slots"][target_slot_name]["range"]
    source_range = source_schema["slots"][source_slot_name]["range"]
    if "Enum" in target_range and "Enum" in source_range:
        target_pvs = []
        for pv in target_schema["enums"][target_range]["permissible_values"]:
            value = target_schema["enums"][target_range]["permissible_values"][pv]
            #Only map PVs that are live
            if any(v and v.endswith("-live") for v in value.get("in_subset", [])):
                target_pvs.append(pv)
        no_match_target_pvs = list(target_pvs)
        if source_slot_name not in narrow_scraps:
            source_pvs = list(source_schema["enums"][source_range]["permissible_values"].keys())
            no_match_source_pvs = list(source_pvs)
        else:
            source_pvs = list(narrow_scraps[source_slot_name])
            no_match_source_pvs = list(narrow_scraps[source_slot_name])
            narrow_scraps.pop(source_slot_name, None)
        #Iterate once through target permissible values, remove all direct matches (no mappings required)
        for tpv in target_pvs:
            if tpv in source_pvs:
                no_match_target_pvs.remove(tpv)
                no_match_source_pvs.remove(tpv)
        #Iterate over the unmatched target pvs and map each to an unmatched source pv
        for tpv in no_match_target_pvs:
            pv_map_prompt = ""
            valid_options = ["n"]
            for i,spv in enumerate(no_match_source_pvs):
                valid_options.append(str(i))
                pv_map_prompt += "[" + str(i) + "]\t" + spv + "\n"
            smatch = ""
            while smatch not in valid_options:
                smatch = input("-- Value Mapping --\n" +
                            "Enter the number for the source value that should map to the target value: \033[1m" + tpv + "\033[0m\n" + 
                            pv_map_prompt + 
                            "[n] if this target value has no source value\n")
            if smatch != "n":
                logic[tpv] = no_match_source_pvs.pop(int(smatch))
        if no_match_source_pvs:
            narrow_scraps[source_slot_name] = no_match_source_pvs
    else:
        logic["TODO"] = "Complex logic required, either source or target slots are not enumerated."
        return logic
    return logic


def get_valid_slot(target_slot_name, source_schema):
    source_class_name = input("Which class in the source schema will the source slot be found in?\n").strip()
    while source_class_name not in source_schema["classes"]:
        source_class_name = input(source_class_name + " was not found. Please try again.\n").strip()
    source_class = source_schema["classes"][source_class_name]
    #Check for a slot match in the new source class
    if target_slot_name in source_class["slots"]:
        source_slot_name = target_slot_name
    else:
        source_slot_name = input("...and what is the name of the source slot?\n")
        while source_slot_name not in source_class["slots"]:
            source_slot_name = input(source_slot_name + " was not found in " + source_class_name + ". Please try again.\n")
    return source_class_name + "." + source_slot_name


def simple_map(target_slot, target_schema, source_schema):
    source_slot = get_valid_slot(target_slot.split(".")[1], source_schema)
    map = {
        "type": "simple",
        "target": target_slot,
        "predicate": "skos:exactMatch",
        "source": source_slot
    }
    logic = enum_check(target_slot.split(".")[1], target_schema, source_slot.split(".")[1], source_schema)
    if logic:
        map["logic"] = logic
    return map


def broad_map(target_slot, target_schema, source_schema):
    sources = []
    broad_maps = []
    complete_list = False
    while not complete_list:
        print("Source slots to be merged into " + target_slot + ":\n" + str(sources))
        add_another = input("Add another source slot? (y) yes (n) no\n").strip()
        if add_another == "y":
            source_slot = get_valid_slot(target_slot.split(".")[1], source_schema)
            sources.append(source_slot)
            map = {
                "type": "complex",
                "target": target_slot,
                "predicate": "skos:broadMatch",
                "source": source_slot
            }
            logic = enum_check(target_slot.split(".")[1], target_schema, source_slot.split(".")[1], source_schema)
            if logic:
                map["logic"] = logic
            broad_maps.append(map)
        elif add_another == "n":
            complete_list = True
        else:
            continue
    return broad_maps


def narrow_map(target_slot, target_schema, source_schema):
    source_slot = get_valid_slot(target_slot.split(".")[1], source_schema)
    map = {
        "type": "complex",
        "target": target_slot,
        "predicate": "skos:narrowMatch",
        "source": source_slot
    }
    logic = enum_check(target_slot.split(".")[1], target_schema, source_slot.split(".")[1], source_schema)
    if logic:
        map["logic"] = logic
    return map


def add_mapping(target_slot, mapping):
    target_class_name = target_slot.split(".")[0]
    if target_class_name not in mappings:
        mappings[target_class_name] = {}
    mappings[target_class_name][target_slot] = mapping

def main(target_schema, source_schema):
    already_mapped = False
    if mappings:
        last_class = next(reversed(mappings))
        if last_class != "skipped":
            pickup_slot = next(reversed(mappings[last_class]))
            already_mapped = True
    #Loop through classes in the target schema
    for target_class_name in target_schema["classes"]:
        #The target class name is not in the source schema
        if target_class_name not in source_schema["classes"] and not already_mapped:
            #Was it renamed?
            renamed = ""
            while renamed not in ["y", "n"]:
                renamed = input("The class: \033[1m" + target_class_name + "\033[0m\n was not found in the source. Has it been renamed?\n" + 
                    "(y) yes, slots for this class draw from a single source class\n" + 
                    "(n) no, slots for this class draw from multiple source classes and should be mapped individually\n")
            if renamed == "y":
                source_class_name = input("What was it called in the source schema?\n").strip()
                while source_class_name not in source_schema["classes"]:
                    source_class_name = input("\033[1m" + source_class_name + "\033[0m\n was not found. Please try again.\n").strip()
        else:
            #If it wasn't renamed then target and source will have the same class name
            source_class_name = target_class_name
        #Loop through the slots in this target class and map each to a source slot
        for target_slot_name in target_schema["classes"][target_class_name]["slots"]:
            #Skip the slot if there is no live data behind it (no need to map)
            if not any(s and s.endswith("-live") for s in target_schema["slots"][target_slot_name].get("in_subset", [])):
                continue
            target_slot = target_class_name + "." + target_slot_name
            if target_slot in mappings["skipped"]:
                continue
            #If this is a resumed mapping session, and this slot was already mapped, then skip it
            if already_mapped:
                if target_slot == pickup_slot:
                    already_mapped = False
            else:
                if target_slot_name in source_schema["classes"][source_class_name]["slots"] and renamed == "y":
                    #Automatically map, no user-input required
                    map = {
                        "type": "simple",
                        "target": target_slot,
                        "predicate": "skos:exactMatch",
                        "source": source_class_name + "." + target_slot_name
                    }
                    logic = enum_check(target_slot_name, target_schema, target_slot_name, source_schema)
                    if logic:
                        map["logic"] = logic
                else:
                    #No automatic match, user-input required
                    type = ""
                    while type not in["x", "s", "c"]:
                        type = input("No match in the source schema for: \033[1m" + target_slot + "\033[0m\n" +
                                    "-- Mapping Type --\n" +
                                    "(s) simple \"one-to-one\" renaming\n" +
                                    "(c) complex composition or decomposition\n" +
                                    "(b) add a blank mapping for this slot to be filled manually\n" +
                                    "(x) do not include in the mapping file\n").strip()
                    if type == "x":
                        mappings["skipped"].append(target_slot)
                        print("\n")
                    if type == "b":
                        add_mapping(target_slot, {
                            "type": "TODO",
                            "target": target_slot,
                            "predicate": "",
                            "source": ""
                        })
                        print("\n")
                    if type == "s":
                        add_mapping(target_slot, simple_map(target_slot, target_schema, source_schema))
                        print("\n")
                    if type == "c":
                        complex_type = ""
                        while complex_type not in ["b", "n"]:
                            complex_type = input("-- Complex Mapping Type --\n" +
                                                "(b) broadMatch - the target slot is a combination of two or more source slots\n" +
                                                "(n) narrowMatch - two or more target slots are drawing from a single source slot\n")
                        if complex_type == "b":
                            broad_maps = broad_map(target_slot, target_schema, source_schema)
                            for m in broad_maps:
                                add_mapping(target_slot, m)
                        if complex_type == "n":
                            add_mapping(target_slot, narrow_map(target_slot, target_schema, source_schema))
    return mappings


#CHAT-GPT generated function
def handle_interrupt(sig, frame):
    # handler function for Ctrl+C
    print("\n\nSaving progress before quitting...")
    with open("mappings/partial-results-" + datetime.today().strftime("%Y%m%d") + ".json", "w") as f:
        json.dump(mappings, f, indent=4, ensure_ascii=False)
    print("Progress saved to partial_results.json. Exiting gracefully.")
    sys.exit(0)

# register the handler
signal.signal(signal.SIGINT, handle_interrupt)

mappings = {
    "skipped": []
}

#Code starts here
if __name__ == '__main__':
    sheets_helper.enforce_repo_root()
    print(
        """
        ▛▀▖▞▀▖▙▗▌   ▙▗▌▞▀▖▛▀▖
        ▌ ▌▚▄ ▌▘▌▄▄▖▌▘▌▙▄▌▙▄▘
        ▌ ▌▖ ▌▌ ▌   ▌ ▌▌ ▌▌  
        ▀▀ ▝▀ ▘ ▘   ▘ ▘▘ ▘▘  
                        
        Use Ctrl+C to abort if needed
        ______________________________________________
        Usage: 
            python map.py [target_schema_path] [source_schema_path]

        Examples: 
            - python map.py schemas/pcdc/pcdc_v2.0 schemas/pcdc/pcdc_v1.13
        ______________________________________________
        """
        ) 
    parser = argparse.ArgumentParser(description="Create a mapping file to pull data into the target format from the source format.")
    parser.add_argument("target_schema_path", help="Path to the target schema JSON file.")
    parser.add_argument("source_schema_path", help="Path to the source schema JSON file.")
    parser.add_argument("--resume", help="Path to a partially completed mappings file.")
    args = parser.parse_args()
    #Open the target schema
    with open(args.target_schema_path) as f:
        target_schema = json.load(f)
    #Open the source schema
    with open(args.source_schema_path) as f:
        source_schema = json.load(f)
    if args.resume:
        #Resume the mappings
        with open(args.resume) as f:
            mappings = json.load(f)
            main(target_schema, source_schema)
    else:
        #Initialize the mappings
        main(target_schema, source_schema)
    #Get the versions from the path
    target_version = args.target_schema_path.split("_")[1]
    source_version = args.source_schema_path.split("_")[1]
    #Save the initial mappings locally
    with open("mappings/" + source_version + "_to_" + target_version + "_" + datetime.today().strftime("%Y%m%d"), "w") as f:
        json.dump(mappings, f, indent=4, ensure_ascii=False)
    print("...done!")