import sys, json, subprocess, argparse


subset_info = {
    "all": "The ALL data dictionary is a consensus data schema built by an international group of pediatric acute lymphoblastic leukemia experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Children's Oncology Group (COG). It is based on the collective requirements of its contributors.",
    "aml": "The AML data dictionary is a consensus data schema built by an international group of pediatric acute myeloid leukemia experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Acute Myeloid Leukemia Consortium (INTERACT). It is based on the collective requirements of its contributors.",
    "cns": "The CNS data dictionary is a consensus data schema built by an international group of pediatric central nervous system tumor experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Central Nervous System Pediatric Research Consortium (INSPiRE). It is based on the collective requirements of its contributors.",
    "pre": "The Cancer Predisposition data dictionary is a consensus data schema built by an international group of pediatric cancer predisposition experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Consortium for Childhood Cancer Predisposition (C3P). It is based on the collective requirements of its contributors.",
    "ews": "The EWS data dictionary is a consensus data schema built by an international group of pediatric Ewing sarcoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Harmonization International Bone Sarcoma Consortium (HIBiSCus). It is based on the collective requirements of its contributors.",
    "fa": "The FA data dictionary is a consensus data schema built by an international group of pediatric Fanconi Anemia experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Fanconi Research Initiative for Education, Networking, and Data Sharing Consortium (FRIENDS). It is based on the collective requirements of its contributors.",
    "fprh": "The FPRH data dictionary is a consensus data schema built by an international group of pediatric fertility preservation and reproductive health experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Reproductive Health Outcomes and Preservation Evaluation Collaborative (Reproductive HOPE). It is based on the collective requirements of its contributors.",
    "gct":"The GCT data dictionary is a consensus data schema built by an international group of pediatric germ cell tumor experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Malignant Germ Cell International Consortium (MaGIC). It is based on the collective requirements of its contributors.",
    "hl": "The HL data dictionary is a consensus data schema built by an international group of pediatric Hodgkin lymphoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Hodgkin Lymphoma Data Collaboration (NODAL). It is based on the collective requirements of its contributors.",
    "lt": "The LT data dictionary is a consensus data schema built by an international group of pediatric liver tumor experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Children's Hepatic tumors International Collaboration (CHIC). It is based on the collective requirements of its contributors.",
    "nbl": "The NBL data dictionary is a consensus data schema built by an international group of pediatric neuroblastoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Neuroblastoma Risk Group (INRG). It is based on the collective requirements of its contributors.",
    "npc": "The NPC data dictionary is a consensus data schema built by an international group of pediatric neuroblastoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Nasopharyngeal Carcinoma Global Partnership (NOBLE). It is based on the collective requirements of its contributors.",
    "nrsts": "The NRSTS data dictionary is a consensus data schema built by an international group of pediatric non-rhabdomyosarcoma soft tissue sarcoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Soft Tissue Sarcoma Consortium (INSTRuCT). It is based on the collective requirements of its contributors.",
    "os": "The OS data dictionary is a consensus data schema built by an international group of pediatric osteosarcoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Harmonization International Bone Sarcoma Consortium (HIBiSCus). It is based on the collective requirements of its contributors.",
    "rb": "The RB data dictionary is a consensus data schema built by an international group of pediatric retinoblastoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Global Retinoblastoma Alliance for Children (Global REACH). It is based on the collective requirements of its contributors.",
    "rms": "The RMS data dictionary is a consensus data schema built by an international group of pediatric rhabdomyosarcoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Soft Tissue Sarcoma Consortium (INSTRuCT). It is based on the collective requirements of its contributors.",
    "md":"The MD data dictionary is a consensus data schema built by an international group of monogenic diabetes experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the PREDICT Consortium. It is based on the collective requirements of its contributors."
}

def openTasks(schema_file, task_file):
    with open(schema_file, "r") as f1:
        schema = json.load(f1)
        subsets = []
        with open(task_file, "r") as f2:
            tasks = f2.read()
            for task in tasks.split("\n"):
                if task:
                    ll = task.split("\t")
                    if ll[0] == "Source":
                        continue
                    source = ll[0]
                    if source not in subsets:
                        subsets.append(source)
                    level = ll[1].strip()
                    action = ll[2].strip()
                    target = ll[3].strip()
                    value = ll[4].strip()
                    func = ACTIONS.get(action)
                    if func:
                        func(schema, level, target, value)
                    else:
                        print(f"Unknown action: {action}")
                        exit()
            for s in subsets:
                disease_group = s.split("_")[0]
                if disease_group in subset_info:
                    schema["subsets"][s] = {
                        "description": subset_info[disease_group]
                    }
                else:
                    print("ERROR: No description found in update.py for: " + disease_group + "\n")
                    sys.exit()
            return schema
        

def newClass(schema, level, target, value):
    if value not in schema["classes"]:
        schema["classes"][value] = {
            "slots":[],
            "comments":[],
            "in_subset":[],
            "annotations": {
                "domain": "",
                "sequence_group": ""
            }
        }
    

def setSlotAttribute(schema, level, target, value):
    schema["classes"][target]["slots"].append(value)
    

def setSubset(schema, level, target, value):
    if level == "class":
        schema["classes"][target]["in_subset"].append(value)
    if level == "slot":
        schema["slots"][target]["in_subset"].append(value)
    if level == "enum":
        enum = target.split("|")[0]
        schema["enums"][enum]["in_subset"].append(value)
    if level == "value":
        enum = target.split("|")[0]
        pv = target.split("|")[1]
        schema["enums"][enum]["permissible_values"][pv]["in_subset"].append(value)
    

def setDomain(schema, level, target, value):
    schema["classes"][target]["annotations"]["domain"] = value
    

def newSlot(schema, level, target, value):
    if value not in schema["slots"]:
        schema["slots"][value] = {
            "slot_uri": "",
            "range": "",
            "comments": [],
            "in_subset": [],
            "annotations": {
                "sequence_group": ""
            }
        }
    

def setSlotUri(schema, level, target, value):
    schema["slots"][target]["slot_uri"] = value
    

def setRange(schema, level, target, value):
    schema["slots"][target]["range"] = value
    

def newEnum(schema, level, target, value):
    if value not in schema["enums"]:
        schema["enums"][value] = {
            "in_subset": [],
            "permissible_values": {}
        }
    else:
        print(f"Enum {value} already exists, skipping reinitialization.")
    

def newValue(schema, level, target, value):
    if value not in schema["enums"][target]["permissible_values"]:
        schema["enums"][target]["permissible_values"][value] = {
            "meaning": "",
            "comments": [],
            "in_subset": [],
            "annotations": {
                "sequence_group": ""
            }
        }


def setMapping(schema, level, target, value):
    mapping_type, mapping_value = value.split("|", 1)
    if level == "value":
        enum, pv = target.split("|", 1)
        pv_dict = schema["enums"][enum]["permissible_values"][pv]
        key = f"{mapping_type}_mappings"
        pv_dict.setdefault(key, []).append(mapping_value)
    elif level == "slot":
        slot_dict = schema["slots"][target]
        key = f"{mapping_type}_mappings"
        slot_dict.setdefault(key, []).append(mapping_value)
    

def setComment(schema, level, target, value):
    if level == "slot":
        schema["slots"][target]["comments"].append(value)
    elif level == "class":
        schema["classes"][target]["comments"].append(value)
    elif level == "value":
        enum = target.split("|")[0]
        pv = target.split("|")[1]
        schema["enums"][enum]["permissible_values"][pv]["comments"].append(value)
    else:
        print("setComment, invalid level")
    

def setSequenceGroup(schema, level, target, value):
    if level == "class":
        schema["classes"][target]["annotations"]["sequence_group"] = value
    if level == "slot":
        schema["slots"][target]["annotations"]["sequence_group"] = value
    if level == "value":
        enum = target.split("|")[0]
        pv = target.split("|")[1]
        schema["enums"][enum]["permissible_values"][pv]["annotations"]["sequence_group"] = value
    

def setTier(schema, level, target, value):
    tier = value.split("|")[0]
    source = value.split("|")[1]
    if level == "class":
        level = "classes"
    if level == "slot":
        level = "slots"
    if tier == "mandatory":
        if "tier_mandatory" in schema[level][target]["annotations"]:
            schema[level][target]["annotations"]["tier_mandatory"] = schema[level][target]["annotations"]["tier_mandatory"] + "," + source
        else:
            schema[level][target]["annotations"]["tier_mandatory"] = source
    elif tier == "priority":
        if "tier_priority" in schema[level][target]["annotations"]:
            schema[level][target]["annotations"]["tier_priority"] = schema[level][target]["annotations"]["tier_priority"] + "," + source
        else:
            schema[level][target]["annotations"]["tier_priority"] = source
    elif tier == "optional":
        if "tier_optional" in schema[level][target]["annotations"]:
            schema[level][target]["annotations"]["tier_optional"] = schema[level][target]["annotations"]["tier_optional"] + "," + source
        else:
            schema[level][target]["annotations"]["tier_optional"] = source
    else:
        print("unknown tier " + value)
    

def setMeaning(schema, level, target, value):
    enum = target.split("|")[0]
    pv = target.split("|")[1]
    schema["enums"][enum]["permissible_values"][pv]["meaning"] = value
    

def changeDomain(schema, level, target, value):
    schema["classes"][target]["annotations"]["domain"] = value
    

def changeSequenceGroup(schema, level, target, value):
    if level == "class":
        schema["classes"][target]["annotations"]["sequence_group"] = value
    if level == "slot":
        schema["slots"][target]["annotations"]["sequence_group"] = value
    if level == "value":
        enum = target.split("|")[0]
        pv = target.split("|")[1]
        schema["enums"][enum]["permissible_values"][pv]["annotations"]["sequence_group"] = value
    

def changeSlotUri(schema, level, target, value):
    schema["slots"][target]["slot_uri"] = value
    

def changeRange(schema, level, target, value):
    if "|" in target:
        slot = target.split("|")[1]
    else:
        slot = target
    schema["slots"][slot]["range"] = value
    

def changeMeaning(schema, level, target, value):
    enum = target.split("|")[0]
    pv = target.split("|")[1]
    schema["enums"][enum]["permissible_values"][pv]["meaning"] = value
    

ACTIONS = {
    "newClass()": newClass,
    "setSlotAttribute()": setSlotAttribute,
    "setSubset()": setSubset,
    "setDomain()": setDomain,
    "newSlot()": newSlot,
    "setSlotUri()": setSlotUri,
    "setRange()": setRange,
    "newEnum()": newEnum,
    "newValue()": newValue,
    "setMapping()": setMapping,
    "setComment()": setComment,
    "setSequenceGroup()": setSequenceGroup,
    "setTier()": setTier,
    "setMeaning()": setMeaning,
    "changeDomain()": changeDomain,
    "changeSequenceGroup()": changeSequenceGroup,
    "changeSlotUri()": changeSlotUri,
    "changeRange()": changeRange,
    "changeMeaning()": changeMeaning,
}

def enforce_repo_root():
    try:
        # Get the top-level directory of the current Git repo
        repo_root = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
    except subprocess.CalledProcessError:
        print("Error: Not inside a Git repository.")
        sys.exit(1)

    # Compare to current working directory
    cwd = os.getcwd()
    if os.path.abspath(cwd) != os.path.abspath(repo_root):
        print(f"\nPlease run this script from the repository root:\n   {repo_root}\n")
        print(f"   You are currently in:\n   {cwd}\n")
        sys.exit(1)

#Code starts here
if __name__ == '__main__':
    enforce_repo_root()
    print(
    """
    ▛▀▖▞▀▖▙▗▌   ▌ ▌▛▀▖▛▀▖▞▀▖▀▛▘▛▀▘
    ▌ ▌▚▄ ▌▘▌▄▄▖▌ ▌▙▄▘▌ ▌▙▄▌ ▌ ▙▄ 
    ▌ ▌▖ ▌▌ ▌   ▌ ▌▌  ▌ ▌▌ ▌ ▌ ▌  
    ▀▀ ▝▀ ▘ ▘   ▝▀ ▘  ▀▀ ▘ ▘ ▘ ▀▀▘

    Use Ctrl+C to abort if needed
    ______________________________________________
    Usage: 
        python update.py [schema_path] [task_file_path]

    Examples: 
        - python update.py schemas/pcdc/pcdc_v1.8.json tasks/ews-taskfile-20240912.tsv
    ______________________________________________
    """
    )
    parser = argparse.ArgumentParser(description="Apply the changes in a task file to a schema.")
    parser.add_argument("schema", help="Path to the schema JSON file.")
    parser.add_argument("task_file", help="Path to the task file.")
    args = parser.parse_args()
    updated = openTasks(args.schema, args.task_file)
    with open(args.schema, "w") as file_out:
        file_out.write(json.dumps(updated, indent=4))