import sys, os, json, requests, urllib.parse, datetime, time, re

subset_info = {
     "pcdc": {
        "all": {
            "title": "Acute Lymphoblastic Leukemia (all) Data Dictionary",
            "id": "1sTygI0GtyaT2C0iZ9YzXTKRnAcELuV2BblaLGPG0EPc",
        },
        "aml": {
            "title": "Acute Myeloid Leukemia (aml) Data Dictionary",
            "id": "1_KyfeZNsepIxSU0Nzw5Mi8mk1PiKCWlSBjatw0AECQ0",
        },
        "cns": {
            "title": "Central Nervous System Tumors (cns) Data Dictionary",
            "id": "1DkLS3N0HunrK669Lw9XuQXNji0jZlgGEYUnOVQ4oj1k",
        },
        "pre": {
            "title": "Cancer Predisposition (pre) Data Dictionary",
            "id": "1Y3oi63WVqH3iRllJI3F7lWvFmKinO3_hrbipnotto4I",
        },
        "ews": {
            "title": "Ewing Sarcoma (ews) Data Dictionary",
            "id": "1VkTfEObeLSle-Ti_JZHaxh9jzmDqvuQ852wnTvdS3jI",
        },
        "fa": {
            "title": "Fanconi Anemia (fa) Data Dictionary",
            "id": "1v_RHahzeArrN_EYRt9b8eXfHoBOJkAOestaU1GCf5BY",
        },
        "fprh": {
            "title": "Fertility Preservation and Reproductive Health (fprh) Data Dictionary",
            "id": "1YARokTGVcC-0Dgp8NsXgCKcaLK9WW0hf7xp48_EBFNs",
        },
        "gct": {
            "title": "Germ Cell Tumors (gct) Data Dictionary",
            "id": "1ePkD-21wWCokR1MClnMrSl0dpj-Dvgid0knn5jfYHCY",
        },
        "hl": {
            "title": "Hodgkin Lymphoma (hl) Data Dictionary",
            "id": "1H0DqYqYHKqH1KNK13cs14LKW6vpwKvDxzPMlW1tkm4U",
        },
        "lt": {
            "title": "Liver Tumors (lt) Data Dictionary",
            "id": "1pDNGV4RJpdJBATFhjCyzHfk_ONI2V9CKpkXU24EmpTY",
        },
        "nbl": {
            "title": "Neuroblastoma (nbl) Data Dictionary",
            "id": "1tdXKN6Al4xtEH2eoIdRM6vEMra1A3bdCQHQIv-IZy6k",
        },
        "npc": {
            "title": "Nasopharyngeal Carcinoma (npc) Data Dictionary",
            "id": "1wCkkkUyZOisXaeUba9gJF9oYt4cr-MMHkSP0PGkO7q8",
        },
        "nrsts": {
            "title": "Non-rhabdomyosarcoma Soft Tissue Sarcomas (nrsts) Data Dictionary",
            "id": "1gDTwDYylH0UakFcNoGBp6etUKKkLVCkZGr-P6NoyN5Y",
        },
        "os": {
            "title": "Osteosarcoma (os) Data Dictionary",
            "id": "15g8aOtaZ9DS7-mBO42AR18g0ScqlPHkalOiV457ddoU",
        },
        "rb": {
            "title": "Retinoblastoma (rb) Data Dictionary",
            "id": "1CoAUFpToGsF63QExv547nGIWdkFPVSUVwMAiaZ7LcLo",
        },
        "rms": {
            "title": "Rhabdomyosarcoma (rms) Data Dictionary",
            "id": "1hDLvT3O_VfsMuWNR2sWWlIWTyzY8sopYY4e7z5Z1wmQ",
        }
     },
     "predict": {
        "md": {
            "title": "Monogenic Diabetes (md) Data Dictionary",
            "id": "15ECEMspvSEbwH875PJF82B9A_vG7qh8j4PlSei0_P-w",
        }
    }
}

def parseMappings(slot, target):
    parsed = ""
    mapping_types = ["exact", "close", "narrow", "broad"]
    for mt in mapping_types:
        key = f"{mt}_mappings"
        if key in slot:
            parsed += '\n'.join(slot[key])
    return parsed

def parseNotes(raw, target):
    parsed = ""
    for note in raw:
        if "ConsortiumNote" in note:
            # Match anything inside the first pair of parentheses
            match = re.match(r"\(([^)]+)\)", note)
            if target == match.group(1):
                match = re.search(r"(ConsortiumNote.*)", note)
                if match:
                    parsed += match.group(1) + '\n'
                else:
                    print('ERROR: cannot parse ConsortiumNote: ' + raw)
                    sys.exit()
        
        else:
            parsed += note + '\n'
    return parsed.rstrip('\n')

def parseType(slot):
    type = slot['range']
    if type in ["Subject", "Timing"]:
        type = 'string'
    if 'Enum' in type:
        type = 'enum'
    return type

def parseTier(target, slot):
    tier = "optional" #default
    if 'tier_mandatory' in slot['annotations']:
        #if target in slot['annotations']['tier_mandatory']:
            tier = 'mandatory'
    if 'tier_priority' in slot['annotations']:
        #if target in slot['annotations']['tier_priority']:
            tier = 'priority'
    return tier

def fetchDefinition(raw):
    print("Fetching definition for: " + raw)
    if ":" in raw:
        system = raw.split(":")[0]
        code = raw.split(":")[1]
        if system == "ncit":
            return getNCItDefinition(code)
        elif system == "icdo":
            #Need to parse the SEER PDF and cache it
            return ""
        elif system == "icd10":
            return ""
        elif system == "SO":
            return getSequenceOntologyDefinition(code)
        elif system == "SCTID":
            return ""
        elif system == "CPT":
            #Licensing issues
            return ""
        else:
            print("ERROR: Unknown terminology: " + system)
            return ""
    else:
        return ""


def getNCItDefinition(code):
    base_url = "https://api-evsrest.nci.nih.gov/api/v1/concept/ncit"
    url = f"{base_url}/{code}"
    params = {"include": "definitions"}
    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()
        return data["definitions"][0]["definition"]
    except Exception as e:
        print(f"ERROR: no NCIt summary found online for {code}")
        print(e)
        return ""
    
def getSequenceOntologyDefinition(code):
    code = code.replace(":", "_")
    # Build the full IRI
    term_iri = f"http://purl.obolibrary.org/obo/{code}"
    # URL‐encode the IRI
    encoded_iri = urllib.parse.quote(term_iri, safe="")
    url = f"https://www.ebi.ac.uk/ols/api/ontologies/so/terms?iri={encoded_iri}"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        return data["description"][0]
    except Exception as e:
        print(f"ERROR: no NCIt summary found online for {code}")
        print(e)
        return ""


def createSheet(target, id):
    # ----- IGNORE BLOCK, CUSTOM CODE TO ENABLE AN AUTH FOLDER ---- #
    orig_dir = os.getcwd()
    # Change to auth folder where pickle files are
    os.chdir('scripts/auth')
    import ezsheets 
    try:
        ss = ezsheets.Spreadsheet(id)
        ss.IGNORE_QUOTA = True
    except ezsheets.EZSheetsException as e:
        print("Ezsheets error: " + str(e))
        os.chdir(orig_dir)
        return
    os.chdir(orig_dir)
    # -------------------------------------------------------- #
    name = datetime.datetime.now().strftime("%Y%m%d") + " " + target
    existing_sheet = next((s for s in ss.sheets if s.title == name), None)
    if existing_sheet:
        print("...deleting existing sheet with same name (from an earlier run today)")
        existing_sheet.delete()
    return ss.createSheet(name)


#TODO add parsing for SyntacticMappings and SemanticMappings
#TODO add ordering by SequenceGroup
def export(commons, disease_group, parent, schema, target, id):
    table_count = 0
    variable_count = 0
    start = time.time()
    print('...preparing tabular format')
    # Add in the headers
    rows = []
    rows.append(['info', 'Title', subset_info[commons][disease_group]['title']])
    rows.append(['info', 'Name', target])
    rows.append(['info','Description', schema['subsets'][target]['description']])
    rows.append(['info','Parent Model', parent])
    rows.append(['info','License','CC BY-NC 4.0'])
    rows.append(['info', 'Documentation', 'https://commons.cri.uchicago.edu/pcdc/'])
    rows.append([])
    rows.append(['RowType', 'VariableName', 'DataType', 'Tier', 'VariableDescription', 'VariableCode', 'PermissibleValue', 'ValueDescription', 'ValueCode', 'ImplementationNotes', 'SyntacticMappings', 'SemanticMappings'])
    rows.append([])
    for c in schema['classes']:
        if target in schema['classes'][c]['in_subset']:
            table_count += 1
            rows.append(['domain', schema['classes'][c]['annotations']['domain']])
            rows.append(['table', c, '', '', '', '', '', '', '', '\n'.join(schema['classes'][c]['comments'])])
            for s in schema['classes'][c]['slots']:
                slot = schema['slots'][s]
                if target in slot['in_subset']:
                    variable_count += 1
                    print(c + " " + s)
                    definition = fetchDefinition(slot['slot_uri'])
                    #Custom fields with no semantic code binding and a description field instead
                    if s in ["submitter_id", "subjects_submitter_id", "timings_submitter_id"]:
                        definition = slot["description"]
                    rows.append(['var', s, parseType(slot), parseTier(target, slot), definition, slot['slot_uri'], '', '', '', parseNotes(slot['comments'], target), parseMappings(slot, target)])
                    if 'Enum' in slot['range']:
                        for value in schema['enums'][slot['range']]['permissible_values']:
                            pv = schema['enums'][slot['range']]['permissible_values'][value]
                            if target in pv['in_subset']:
                                rows.append(['pv', '', '', '', '','', value, fetchDefinition(pv['meaning']), pv['meaning'], parseNotes(pv['comments'], target), parseMappings(pv,target)])
            rows.append([]) 
            rows.append([])
    rows.append(['','Tables: ' + str(table_count)])
    rows.append(['','Variables: ' + str(variable_count)])
    print(elapsed_time(start))
    #Create a new sheet object
    start = time.time()
    print('\n...creating sheet')
    new_sheet = createSheet(target, id)
    print(elapsed_time(start)) 
    #Add rows to the new sheet
    start = time.time() 
    print('\n...exporting tabular format to new sheet')
    new_sheet.updateRows(rows)
    print(elapsed_time(start))


def elapsed_time(start):
    seconds = time.time() - start
    m, s = divmod(seconds, 60)
    return f"{int(m)}m {s:.2f}s"

#Code starts here d
if __name__ == '__main__':
    print(
    """
    ▛▀▖▞▀▖▙▗▌   ▛▀▘▌ ▌▛▀▖▞▀▖▛▀▖▀▛▘
    ▌ ▌▚▄ ▌▘▌▄▄▖▙▄ ▝▞ ▙▄▘▌ ▌▙▄▘ ▌ 
    ▌ ▌▖ ▌▌ ▌   ▌  ▞▝▖▌  ▌ ▌▌▚  ▌ 
    ▀▀ ▝▀ ▘ ▘   ▀▀▘▘ ▘▘  ▝▀ ▘ ▘ ▘ 
    Use Ctrl+C to abort if needed
    ______________________________________________
    Usage: 
        python export.py [schema] [subset]

    Examples: 
        - python export.py pcdc_v1.13 aml_v1.8-live
    ______________________________________________
    """
    )
    if len(sys.argv) == 3:
        parent = sys.argv[1]
        parent_file = "schemas/pcdc/" + parent + ".json"
        if os.path.exists(parent_file):
            target = sys.argv[2]
            with open(parent_file, "r") as schema_file:
                schema = json.load(schema_file)
                if target in schema["subsets"]:
                    print("Exporting: " + target + "\n")
                    commons = parent.split("_")[0]     
                    disease_group = target.split("_")[0].split("-")[0]
                    if disease_group in subset_info[commons]:
                        export(commons, disease_group, parent, schema, target, subset_info[commons][disease_group]["id"])
                    else:
                            print("\nERROR: Subset metadata is not present in export.py for target: " + target + "\n")
                else:
                    print("\nERROR: Parent schema does not include this target: " + target + "\n")
        else:
            print("\nERROR: Parent schema not found locally: " + parent_file + "\n")
    else:
         print("\nERROR: Incorrect number of parameters included\n")
