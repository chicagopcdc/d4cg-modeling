import sys, os, json, time
from datetime import datetime
from utils import load_sheet


class TaskManager:
    def __init__(self):
        self.tasks = ["Source\tLevel\tAction\tTarget\tValue\n"]

    def add(self, task):
        if task and task not in self.tasks:
            self.tasks.append(task)

    def extend(self, task_list):
        for t in task_list:
            self.add(t)

    def write(self, filename):
        """Write tasks to file."""
        with open(filename, "w") as f:
            f.writelines(self.tasks)

    def __iter__(self):
        return iter(self.tasks)


def sync(dictionary):
    task_manager = TaskManager()
    parent = dictionary["info"]["parent_model"]
    if os.path.exists("schemas/" + parent + ".json"):
        with open("schemas/" + parent + ".json", "r") as schema_file:
            schema = json.load(schema_file)
            for table in dictionary["tables"]:
                t_name = table['name']
                if t_name in schema["classes"]:
                    checkClass(task_manager, dictionary["info"]['name'],table, schema["classes"][t_name])
                    for variable in table["variables"]:
                        var_name = variable['name']
                        if var_name in schema["slots"]:
                            #Slots are defined as class attributes and as slot objects
                            checkSlot(task_manager, dictionary["info"]['name'], variable, schema["slots"][var_name])
                            if variable["permissible_values"]:
                                enum_name = "".join(word.capitalize() for word in variable['name'].lower().split('_')) + "Enum"
                                if "Yes" in variable["permissible_values"] and "No" in variable["permissible_values"]:
                                    enum_name = "YesNoEnum"
                                if enum_name in schema["enums"]:
                                    checkEnum(task_manager, dictionary["info"]['name'], enum_name, schema["enums"][enum_name])
                                    for permissible_value in variable["permissible_values"]:
                                        pv_name = permissible_value['value']
                                        if pv_name in schema["enums"][enum_name]["permissible_values"]:
                                            checkValue(task_manager, dictionary["info"]['name'], enum_name, permissible_value, schema["enums"][enum_name]["permissible_values"][pv_name])
                                        else:
                                            proposeValue(task_manager, dictionary["info"]['name'], enum_name, permissible_value)
                                else:
                                    proposeEnum(task_manager, dictionary["info"]['name'], enum_name, variable)
                        else:
                            proposeSlot(task_manager, dictionary["info"]['name'], variable)
                else:
                    proposeClass(task_manager, dictionary["info"]['name'], table)
    else:
        print("\nERROR: A schema for parent model: {parent} does not yet exist.")
    return task_manager

def format_note(note, source):
    note = note.replace('"', "'")
    if "ConsortiumNote" in note:
        note = f"({source}) {note}"
    if "D4CGNote" not in note and "ConsortiumNote" not in note:
        note = f"({source}) ConsortiumNote: {note}"
    return note

def checkClass(task_manager, source, table, schema_class):
    #Check slot attributes
    for variable in table['variables']:
        if variable['name'] not in schema_class["slots"]:
            task_manager.add(f"{source}\tclass\tsetSlotAttribute()\t{table['name']}\t{variable['name']}\n")
    #Check mappings
    for mapping in table['mappings']:
        if mapping and 'mappings' in schema_class:
            if mapping not in schema_class['mappings']:
                task_manager.add(f"{source}\tclass\tsetMapping()\t{table['name']}\t{mapping.strip()}\n")
    #Check comments
    for note in table['implementation_notes']:
        if note:
            note = format_note(note, source).strip()
            if note not in schema_class['comments']:
                    task_manager.add(f"{source}\tclass\tsetComment()\t{table['name']}\t{note}\n")
    #Check in_subset
    if source not in schema_class["in_subset"]:
        task_manager.add(f"{source}\tclass\tsetSubset()\t{table['name']}\t{source}\n")
    #Check domain
    if table['domain'] != schema_class['annotations']['domain']:
        task_manager.add(f"{source}\tclass\tchangeDomain()\t{table['name']}\t{table['domain']}\n")
    #Check sequence_group
    if table['sequence_group'] and table['sequence_group'].isdigit() and table['sequence_group'] != schema_class['annotations']['sequence_group']:
        task_manager.add(f"{source}\tclass\tchangeSequenceGroup()\t{table['name']}\t{table['sequence_group'].strip()}\n")

def proposeClass(task_manager, source, table):
    task_manager.add(f"{source}\tclass\tnewClass()\t-\t{table['name']}\n")
    #slot attributes
    for variable in table["variables"]:
        task_manager.add(f"{source}\tclass\tsetSlotAttribute()\t{table['name']}\t{variable['name']}\n")
        proposeSlot(task_manager, source, variable)
    #comments
    for note in table['implementation_notes']:
        if note:
            task_manager.add(f"{source}\tclass\tsetComment()\t{table['name']}\t{format_note(note, source).strip()}\n") 
    #in_subset
    task_manager.add(f"{source}\tclass\tsetSubset()\t{table['name']}\t{source}\n")
    #domain
    task_manager.add(f"{source}\tclass\tsetDomain()\t{table['name']}\t{table['domain']}\n")
    #sequence_group
    #TODO function to initialize missing sequence_groups 
    if table['sequence_group'] and table['sequence_group'].isdigit():
        task_manager.add(f"{source}\tclass\tsetSequenceGroup()\t{table['name']}\t{table['sequence_group'].strip()}\n")
    #slot objects
    for variable in table["variables"]:
        proposeSlot(task_manager, source, variable)


legacy_types = {
    'code': "enum",
    "number": "decimal",
    "numeric": "decimal"
}

def checkSlot(task_manager, source, variable, schema_slot):
    #Check slot_uri
    if variable['code'] and variable['code'] != schema_slot["slot_uri"]:
        task_manager.add(f"{source}\tslot\tchangeSlotUri()\t{variable['name']}\t{variable['code'].strip()}\n")
    #Check range 
    range = variable["type"]
    if range and range not in ["enum", "string", "decimal", "integer"]:
        range = legacy_types[range]
    if range != "enum" and range != schema_slot["range"]:
        task_manager.add(f"{source}\tslot\tchangeRange()\t{variable['name']}\t{range}\n")
    #Check tier
    if variable['tier'] == 'mandatory':
        if 'tier_mandatory' in schema_slot['annotations']:
            if source not in schema_slot['annotations']['tier_mandatory'].split(","):
                task_manager.add(f"{source}\tslot\tsetTier()\t{variable['name']}\t{variable['tier']}|{source}\n")      
        else:
            task_manager.add(f"{source}\tslot\tsetTier()\t{variable['name']}\t{variable['tier']}|{source}\n")  
    if variable['tier'] == 'priority':
        if 'tier_priority' in schema_slot['annotations']:
            if source not in schema_slot['annotations']['tier_priority'].split(","):
                task_manager.add(f"{source}\tslot\tsetTier()\t{variable['name']}\t{variable['tier']}|{source}\n")
        else:
            task_manager.add(f"{source}\tslot\tsetTier()\t{variable['name']}\t{variable['tier']}|{source}\n")
    if variable['tier'] == 'optional':
        if 'tier_optional' in schema_slot['annotations']:
            if source not in schema_slot['annotations']['tier_optional'].split(","):
                task_manager.add(f"{source}\tslot\tsetTier()\t{variable['name']}\t{variable['tier']}|{source}\n")
        else:
            task_manager.add(f"{source}\tslot\tsetTier()\t{variable['name']}\t{variable['tier']}|{source}\n")
    #Check mappings
    mapping_types = ["exact", "close", "narrow", "broad"]
    for m in variable['mappings']:
        for mt in mapping_types:
            key = f"{mt}Match"
            if key in m:
                if f"{mt}_mappings" in schema_slot:
                    if not schema_slot[f"{mt}_mappings"] or source not in schema_slot[f"{mt}_mappings"]:
                        task_manager.add(f"{source}\tslot\tsetMapping()\t{variable['name']}\t{mt}|{m}\n")
                else:
                    task_manager.add(f"{source}\tslot\tsetMapping()\t{variable['name']}\t{mt}|({source}) {m}\n")       
    #Check comments
    for note in variable['implementation_notes']:
        if note:
            note = format_note(note, source).strip()
            if note not in schema_slot['comments']:
                    task_manager.add(f"{source}\tslot\tsetComment()\t{variable['name']}\t{note}\n")
    #Check in_subset
    if source not in schema_slot["in_subset"]:
        task_manager.add(f"{source}\tslot\tsetSubset()\t{variable['name']}\t{source}\n")
    #Check sequence_group
    if variable['sequence_group']  and variable['sequence_group'].isdigit() and variable['sequence_group'] != schema_slot['annotations']['sequence_group']:
        task_manager.add(f"{source}\tslot\tchangeSequenceGroup()\t{variable['name']}\t{variable['sequence_group'].strip()}\n")

def proposeSlot(task_manager, source, variable):
    task_manager.add(f"{source}\tslot\tnewSlot()\t-\t{variable['name']}\n")
    #slot_uri
    if variable['code']:
        task_manager.add(f"{source}\tslot\tsetSlotUri()\t{variable['name']}\t{variable['code'].strip()}\n")
    #range
    if variable["permissible_values"]:
        enum_name = "".join(word.capitalize() for word in variable['name'].lower().split('_')) + "Enum"
        if "Yes" in variable["permissible_values"] and "No" in variable["permissible_values"]:
            enum_name = "YesNoEnum"
        task_manager.add(f"{source}\tslot\tsetRange()\t{variable['name']}\t{enum_name}\n")
        proposeEnum(task_manager, source, enum_name, variable)
    else:
        range = variable["type"]
        if range not in ["enum", "string", "decimal", "integer"]:
            range = legacy_types[range]
        task_manager.add(f"{source}\tslot\tsetRange()\t{variable['name']}\t{range}\n")
    #comments
    for note in variable['implementation_notes']:
        if note:
            note = format_note(note, source).strip()
            task_manager.add(f"{source}\tslot\tsetComment()\t{variable['name']}\t{note}\n")
    #in_subset
    task_manager.add(f"{source}\tslot\tsetSubset()\t{variable['name']}\t{source}\n")
    #sequence_group
    if variable['sequence_group'] and variable['sequence_group'].isdigit():
        task_manager.add(f"{source}\tslot\tsetSequenceGroup()\t{variable['name']}\t{variable['sequence_group'].strip()}\n")
    #tier
    if variable['tier'] == 'mandatory':
        task_manager.add(f"{source}\tslot\tsetTier()\t{variable['name']}\t{variable['tier']}|{source}\n")
    if variable['tier'] == 'priority':
        task_manager.add(f"{source}\tslot\tsetTier()\t{variable['name']}\t{variable['tier']}|{source}\n")
    if variable['tier'] == 'optional':
        task_manager.add(f"{source}\tslot\tsetTier()\t{variable['name']}\t{variable['tier']}|{source}\n")
    #Check mappings
    mapping_types = ["exact", "close", "narrow", "broad"]
    for m in variable['mappings']:
        for mt in mapping_types:
            key = f"{mt}Match"
            if key in m:
                task_manager.add(f"{source}\tslot\tsetMapping()\t{variable['name']}\t{mt}|{m}\n")

def checkEnum(task_manager, source, enum_name, schema_enum):
    #Check in_subset
    if source not in schema_enum["in_subset"]:
        task_manager.add(f"{source}\tenum\tsetSubset()\t{enum_name}\t{source}\n")

def proposeEnum(task_manager, source, enum_name, variable):
    task_manager.add(f"{source}\tenum\tnewEnum()\t-\t{enum_name}\n")
    task_manager.add(f"{source}\tenum\tsetSubset()\t{enum_name}\t{source}\n")
    for value in variable["permissible_values"]:
        proposeValue(task_manager, source, enum_name, value)

def checkValue(task_manager, source, enum_name, value, schema_value):
    #Check meaning
    if value['code'] and value['code'] != schema_value["meaning"]:
        task_manager.add(f"{source}\tvalue\tchangeMeaning()\t{enum_name}|{value['value']}\t{value['code'].strip()}\n")
    #Check comment
    for note in value['implementation_notes']:
        if note:
            note = format_note(note, source).strip()
            if note not in schema_value['comments']:
                task_manager.add(f"{source}\tvalue\tsetComment()\t{enum_name}|{value['value']}\t{note}\n")
    #Check in_subset
    if source not in schema_value["in_subset"]:
        task_manager.add(f"{source}\tvalue\tsetSubset()\t{enum_name}|{value['value']}\t{source}\n")
    #Check sequence_group
    if value['sequence_group'] and value['sequence_group'].isdigit() and value['sequence_group'] != schema_value['annotations']['sequence_group']:
        task_manager.add(f"{source}\tvalue\tchangeSequenceGroup()\t{enum_name}|{value['value']}\t{value['sequence_group'].strip()}\n")

def proposeValue(task_manager, source, enum_name, value):
    task_manager.add(f"{source}\tvalue\tnewValue()\t{enum_name}\t{value['value']}\n")
    #meaning
    if value['code']:
        task_manager.add(f"{source}\tvalue\tsetMeaning()\t{enum_name}|{value['value']}\t{value['code'].strip()}\n")
    #comments
    for note in value['implementation_notes']:
        if note:
            note = format_note(note, source).strip()
            task_manager.add(f"{source}\tvalue\tsetComment()\t{enum_name}|{value['value']}\t{note}\n")
    #in_subset
    task_manager.add(f"{source}\tvalue\tsetSubset()\t{enum_name}|{value['value']}\t{source}\n")
    #sequence_group
    if value['sequence_group'] and value['sequence_group'].isdigit():
        task_manager.add(f"{source}\tvalue\tsetSequenceGroup()\t{enum_name}|{value['value']}\t{value['sequence_group'].strip()}\n")
    #Check mappings
    mapping_types = ["exact", "close", "narrow", "broad"]
    for m in value['mappings']:
        for mt in mapping_types:
            key = f"{mt}Match"
            if key in m:
                task_manager.add(f"{source}\tslot\tsetMapping()\t{enum_name}|{value['value']}\t{mt}|{m}\n")

gsheets_ids = {
    "pcdc": {
        "aml": "1_KyfeZNsepIxSU0Nzw5Mi8mk1PiKCWlSBjatw0AECQ0",
        "cns": "1DkLS3N0HunrK669Lw9XuQXNji0jZlgGEYUnOVQ4oj1k",
        "pre": "1Y3oi63WVqH3iRllJI3F7lWvFmKinO3_hrbipnotto4I",
        "ews": "1VkTfEObeLSle-Ti_JZHaxh9jzmDqvuQ852wnTvdS3jI",
        "fa": "1v_RHahzeArrN_EYRt9b8eXfHoBOJkAOestaU1GCf5BY",
        "fprh": "1YARokTGVcC-0Dgp8NsXgCKcaLK9WW0hf7xp48_EBFNs",
        "gct": "1ePkD-21wWCokR1MClnMrSl0dpj-Dvgid0knn5jfYHCY",
        "hl": "1H0DqYqYHKqH1KNK13cs14LKW6vpwKvDxzPMlW1tkm4U",
        "lt": "1pDNGV4RJpdJBATFhjCyzHfk_ONI2V9CKpkXU24EmpTY",
        "nbl": "1tdXKN6Al4xtEH2eoIdRM6vEMra1A3bdCQHQIv-IZy6k",
        "npc": "1wCkkkUyZOisXaeUba9gJF9oYt4cr-MMHkSP0PGkO7q8",
        "nrsts": "1gDTwDYylH0UakFcNoGBp6etUKKkLVCkZGr-P6NoyN5Y",
        "os": "15g8aOtaZ9DS7-mBO42AR18g0ScqlPHkalOiV457ddoU",
        "rb": "1CoAUFpToGsF63QExv547nGIWdkFPVSUVwMAiaZ7LcLo",
        "rms": "1hDLvT3O_VfsMuWNR2sWWlIWTyzY8sopYY4e7z5Z1wmQ"
    },
    "predict": {
        "md": "15ECEMspvSEbwH875PJF82B9A_vG7qh8j4PlSei0_P-w"
    }
}

def elapsed_time(start):
    seconds = time.time() - start
    m, s = divmod(seconds, 60)
    return f"{int(m)}m {s:.2f}s"

#Code starts here
if __name__ == '__main__':
    print(
    """
    ▛▀▖▞▀▖▙▗▌   ▞▀▖▌ ▌▙ ▌▞▀▖
    ▌ ▌▚▄ ▌▘▌▄▄▖▚▄ ▝▞ ▌▌▌▌  
    ▌ ▌▖ ▌▌ ▌   ▖ ▌ ▌ ▌▝▌▌ ▖
    ▀▀ ▝▀ ▘ ▘   ▝▀  ▘ ▘ ▘▝▀ 
                      
    Use Ctrl+C to abort if needed
    ______________________________________________
    Usage: 
        python sync.py [commons] [scope] [version]

    Examples: 
        - python sync.py pcdc single aml_v1.5
        - python sync.py pcdc full pcdc_v1.8
    ______________________________________________
    """
    )
    if len(sys.argv) != 4:
        print("\nERROR: Incorrect number of parameters included\n")
        sys.exit()
    commons = sys.argv[1]
    scope = sys.argv[2]
    version = sys.argv[3]

    if scope == "single":
        print("\nSyncing a single dictionary: " + version)
        disease_group = version.split("_")[0]
        if disease_group in gsheets_ids[commons]:
            start = time.time()
            print("...loading sheet")
            sheet = load_sheet.load(gsheets_ids[commons][disease_group], version, scope)
            print(elapsed_time(start))   
            if sheet != None:
                start = time.time()
                print("...parsing sheet")
                dictionary = load_sheet.parse(sheet)
                print(elapsed_time(start))   
                if dictionary:
                    start = time.time()
                    print("...syncing sheet to schema")
                    task_manager = sync(dictionary)
                    print(elapsed_time(start))
                    task_manager.write("tasks/" + disease_group + "-taskfile-" + datetime.today().strftime("%Y%m%d") + ".tsv")
            else:
                print("\nERROR: The target was not found in this spreadsheet\n") 
        else:
            print("\nERROR: Unknown disease group: " + disease_group)
    
    elif scope == "full":
        print("No support for syncing full. Sync individuals instead for now.")
        """
        print("\nParsing all dictionaries with a parent model of: {version}...")
        dictionaries = []
        for disease_group in gsheets_ids[commons]:
            print("\n[  {disease_group}  ]\n...loading sheet")
            sheet = load_sheet.load(gsheets_ids[commons][disease_group], version, scope)
            if sheet == None:
                print("The target was not found in this spreadsheet\n")
                continue
            print("...parsing sheet")
            dictionaries.append(load_sheet.parse(sheet))
            print("...done!\n")
            for dictionary in dictionaries:
                start = time.time()
                print("...syncing sheet to schema: " + dictionary["info"]["name"])
                task_manager = sync(dictionary)
                print(elapsed_time(start))
                task_manager.write("tasks/" + disease_group + "-taskfile-" + datetime.today().strftime("%Y%m%d") + ".tsv")
        """
    else:
        print("\nERROR: Invalid scope: " + scope)