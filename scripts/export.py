import sys, os, json, requests, urllib.parse, datetime, time, re, argparse, subprocess

subset_info = {
     "pcdc": {
        "pcdc": {
            "title": "PCDC Data Dictionary",
            "id": "1k2m4oAX3JdfYN2lIbpBiWFUNKZwXnQCiuns0e3Wid9o",
            "description": "The PCDC data dictionary is a full aggregation of concepts from modeling across all PCDC consortia."
        },
        "all": {
            "title": "Acute Lymphoblastic Leukemia (all) Data Dictionary",
            "id": "1sTygI0GtyaT2C0iZ9YzXTKRnAcELuV2BblaLGPG0EPc"
        },
        "aml": {
            "title": "Acute Myeloid Leukemia (aml) Data Dictionary",
            "id": "1_KyfeZNsepIxSU0Nzw5Mi8mk1PiKCWlSBjatw0AECQ0",
            "description": "The AML data dictionary is a consensus data schema built by an international group of pediatric acute myeloid leukemia experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Acute Myeloid Leukemia Consortium (INTERACT). It is based on the collective requirements of its contributors."
        },
        "cns": {
            "title": "Central Nervous System Tumors (cns) Data Dictionary",
            "id": "1DkLS3N0HunrK669Lw9XuQXNji0jZlgGEYUnOVQ4oj1k",
            "description": "The CNS data dictionary is a consensus data schema built by an international group of pediatric central nervous system tumor experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Central Nervous System Pediatric Research Consortium (INSPiRE). It is based on the collective requirements of its contributors."
        },
        "pre": {
            "title": "Cancer Predisposition (pre) Data Dictionary",
            "id": "1Y3oi63WVqH3iRllJI3F7lWvFmKinO3_hrbipnotto4I",
            "description": "The Cancer Predisposition data dictionary is a consensus data schema built by an international group of pediatric cancer predisposition experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Consortium for Childhood Cancer Predisposition (C3P). It is based on the collective requirements of its contributors."
        },
        "ews": {
            "title": "Ewing Sarcoma (ews) Data Dictionary",
            "id": "1VkTfEObeLSle-Ti_JZHaxh9jzmDqvuQ852wnTvdS3jI",
            "description": "The EWS data dictionary is a consensus data schema built by an international group of pediatric Ewing sarcoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Harmonization International Bone Sarcoma Consortium (HIBiSCus). It is based on the collective requirements of its contributors."
        },
        "fa": {
            "title": "Fanconi Anemia (fa) Data Dictionary",
            "id": "1v_RHahzeArrN_EYRt9b8eXfHoBOJkAOestaU1GCf5BY",
            "description": "The FA data dictionary is a consensus data schema built by an international group of pediatric Fanconi Anemia experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Fanconi Research Initiative for Education, Networking, and Data Sharing Consortium (FRIENDS). It is based on the collective requirements of its contributors."
        },
        "fprh": {
            "title": "Fertility Preservation and Reproductive Health (fprh) Data Dictionary",
            "id": "1YARokTGVcC-0Dgp8NsXgCKcaLK9WW0hf7xp48_EBFNs"
        },
        "gct": {
            "title": "Germ Cell Tumors (gct) Data Dictionary",
            "id": "1ePkD-21wWCokR1MClnMrSl0dpj-Dvgid0knn5jfYHCY",
            "description": "The GCT data dictionary is a consensus data schema built by an international group of pediatric germ cell tumor experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Malignant Germ Cell International Consortium (MaGIC). It is based on the collective requirements of its contributors."
        },
        "hl": {
            "title": "Hodgkin Lymphoma (hl) Data Dictionary",
            "id": "1H0DqYqYHKqH1KNK13cs14LKW6vpwKvDxzPMlW1tkm4U",
            "description": "The HL data dictionary is a consensus data schema built by an international group of pediatric Hodgkin lymphoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Hodgkin Lymphoma Data Collaboration (NODAL). It is based on the collective requirements of its contributors."
        },
        "lt": {
            "title": "Liver Tumors (lt) Data Dictionary",
            "id": "1pDNGV4RJpdJBATFhjCyzHfk_ONI2V9CKpkXU24EmpTY",
            "description": "The LT data dictionary is a consensus data schema built by an international group of pediatric liver tumor experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Children's Hepatic tumors International Collaboration (CHIC). It is based on the collective requirements of its contributors."
        },
        "nbl": {
            "title": "Neuroblastoma (nbl) Data Dictionary",
            "id": "1tdXKN6Al4xtEH2eoIdRM6vEMra1A3bdCQHQIv-IZy6k",
            "description": "The NBL data dictionary is a consensus data schema built by an international group of pediatric neuroblastoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Neuroblastoma Risk Group (INRG). It is based on the collective requirements of its contributors."
        },
        "npc": {
            "title": "Nasopharyngeal Carcinoma (npc) Data Dictionary",
            "id": "1wCkkkUyZOisXaeUba9gJF9oYt4cr-MMHkSP0PGkO7q8",
            "description": "The NPC data dictionary is a consensus data schema built by an international group of pediatric neuroblastoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Nasopharyngeal Carcinoma Global Partnership (NOBLE). It is based on the collective requirements of its contributors."
        },
        "nrsts": {
            "title": "Non-rhabdomyosarcoma Soft Tissue Sarcomas (nrsts) Data Dictionary",
            "id": "1gDTwDYylH0UakFcNoGBp6etUKKkLVCkZGr-P6NoyN5Y",
            "description": "The NRSTS data dictionary is a consensus data schema built by an international group of pediatric non-rhabdomyosarcoma soft tissue sarcoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Soft Tissue Sarcoma Consortium (INSTRuCT). It is based on the collective requirements of its contributors."
        },
        "os": {
            "title": "Osteosarcoma (os) Data Dictionary",
            "id": "15g8aOtaZ9DS7-mBO42AR18g0ScqlPHkalOiV457ddoU",
            "description": "The OS data dictionary is a consensus data schema built by an international group of pediatric osteosarcoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Harmonization International Bone Sarcoma Consortium (HIBiSCus). It is based on the collective requirements of its contributors."
        },
        "rb": {
            "title": "Retinoblastoma (rb) Data Dictionary",
            "id": "1CoAUFpToGsF63QExv547nGIWdkFPVSUVwMAiaZ7LcLo",
            "description": "The RB data dictionary is a consensus data schema built by an international group of pediatric retinoblastoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Global Retinoblastoma Alliance for Children (Global REACH). It is based on the collective requirements of its contributors."
        },
        "rms": {
            "title": "Rhabdomyosarcoma (rms) Data Dictionary",
            "id": "1hDLvT3O_VfsMuWNR2sWWlIWTyzY8sopYY4e7z5Z1wmQ",
            "description": "The RMS data dictionary is a consensus data schema built by an international group of pediatric rhabdomyosarcoma experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Soft Tissue Sarcoma Consortium (INSTRuCT). It is based on the collective requirements of its contributors."
        }
    },
     "predict": {
        "md": {
            "title": "Monogenic Diabetes (md) Data Dictionary",
            "id": "15ECEMspvSEbwH875PJF82B9A_vG7qh8j4PlSei0_P-w"
        }
    }
}

def parse_mappings(slot, target):
    parsed = ""
    mapping_types = ["exact", "close", "narrow", "broad"]
    for mt in mapping_types:
        key = f"{mt}_mappings"
        if key in slot:
            parsed += '\n'.join(slot[key])
    return parsed

def parse_notes(raw, target):
    parsed = ""
    try:
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
    except:
        print("Error parsing note: " + str(raw))
    return parsed.rstrip('\n')

def parse_type(slot):
    type = slot['range']
    if type in ["Subject", "Timing", "Person", "DataContributorPersonRecord"]:
        type = 'string'
    if 'Enum' in type:
        type = 'enum'
    return type

def parse_tier(target, slot):
    tier = "optional" #default
    if 'tier_mandatory' in slot['annotations']:
        #if target in slot['annotations']['tier_mandatory']:
            tier = 'mandatory'
    if 'tier_priority' in slot['annotations']:
        #if target in slot['annotations']['tier_priority']:
            tier = 'priority'
    return tier

def fetch_definition(raw):
    print("Fetching definition for: " + raw)
    if ":" in raw:
        system = raw.split(":")[0]
        code = raw.split(":")[1]
        if system == "ncit":
            return get_ncit_definition(code)
        elif system == "icdo":
            #Need to parse the SEER PDF and cache it
            return ""
        elif system == "icd10":
            return ""
        elif system == "SO":
            return get_so_definition(code)
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


def get_ncit_definition(code):
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
    
def get_so_definition(code):
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


def create_sheet(subset, id):
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
    name = datetime.datetime.now().strftime("%Y%m%d") + " " + subset
    existing_sheet = next((s for s in ss.sheets if s.title == name), None)
    if existing_sheet:
        print("...deleting existing sheet with same name (from an earlier run today)")
        existing_sheet.delete()
    return ss.createSheet(name)


def init_rows(commons, disease_group, parent, schema, target):
    rows = []
    rows.append(['info', 'Title', subset_info[commons][disease_group]['title']])
    rows.append(['info', 'Name', target])
    rows.append(['info','Description', schema['subsets'][target]['description']])
    if disease_group == "pcdc":
        rows.append(['info','Parent Model', 'n/a'])
    else:   
        rows.append(['info','Parent Model', parent])
    rows.append(['info','License','CC BY-NC 4.0'])
    rows.append(['info', 'Documentation', 'https://commons.cri.uchicago.edu/pcdc/'])
    rows.append([])
    rows.append(['RowType', 'VariableName', 'DataType', 'Tier', 'VariableDescription', 'VariableCode', 'PermissibleValue', 'ValueDescription', 'ValueCode', 'ImplementationNotes', 'SyntacticMappings', 'SemanticMappings'])
    rows.append([])
    return rows


#TODO add parsing for SyntacticMappings and SemanticMappings
def assemble(definitions, commons, disease_group, parent, schema, target):
    table_count = 0
    variable_count = 0
    start = time.time()
    print('...preparing tabular format')
    rows = init_rows(commons, disease_group, parent, schema, target)
    for c in schema['classes']:
        sclass = schema['classes'][c]
        if target in sclass['in_subset'] or disease_group == "pcdc":
            table_count += 1
            if 'domain' in sclass['annotations']:
                rows.append(['domain', sclass['annotations']['domain']])
            rows.append(['table', c, '', '', '', '', '', '', '', '\n'.join(sclass['comments'])])
            for s in sclass['slots']:
                slot = schema['slots'][s]
                if target in sclass['slot_usage'][s] or disease_group == "pcdc":
                    variable_count += 1
                    print(c + " " + s)
                    if definitions == "retrieve":
                        definition = fetch_definition(slot['slot_uri'])
                    else:
                        definition = ""
                    #Custom fields with no semantic code binding and a description field instead
                    if s in ["submitter_id", "subjects_submitter_id", "timings_submitter_id", "urls"]:
                        definition = slot["description"]
                    rows.append(['var', s, parse_type(slot), parse_tier(target, slot), definition, slot['slot_uri'], '', '', '', parse_notes(slot['comments'], target), parse_mappings(slot, target)])
                    if 'Enum' in slot['range']:
                        for value in schema['enums'][slot['range']]['permissible_values']:
                            pv = schema['enums'][slot['range']]['permissible_values'][value]
                            if definitions == "retrieve":
                                definition = fetch_definition(pv['meaning'])
                            else:
                                definition = ""
                            if target in pv['in_subset'] or disease_group == "pcdc":
                                rows.append(['pv', '', '', '', '','', value, definition, pv['meaning'], parse_notes(pv['comments'], target), parse_mappings(pv,target)])
            rows.append([]) 
            rows.append([])
    rows.append(['','Tables: ' + str(table_count)])
    rows.append(['','Variables: ' + str(variable_count)])
    print(elapsed_time(start))
    return rows
    

def export(subset, rows, id):
    #Create a new sheet object
    start = time.time()
    print('\n...creating sheet')
    new_sheet = create_sheet(subset, id)
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

#Code starts here d
if __name__ == '__main__':
    enforce_repo_root()
    print(
    """
    ▛▀▖▞▀▖▙▗▌   ▛▀▘▌ ▌▛▀▖▞▀▖▛▀▖▀▛▘
    ▌ ▌▚▄ ▌▘▌▄▄▖▙▄ ▝▞ ▙▄▘▌ ▌▙▄▘ ▌ 
    ▌ ▌▖ ▌▌ ▌   ▌  ▞▝▖▌  ▌ ▌▌▚  ▌ 
    ▀▀ ▝▀ ▘ ▘   ▀▀▘▘ ▘▘  ▝▀ ▘ ▘ ▘ 
    Use Ctrl+C to abort if needed
    ______________________________________________
    Usage: 
        python scripts/export.py [schema_path] [subset] --fast (optional)

    Examples: 
        - python scripts/export.py schemas/pcdc/pcdc_v1.13 aml_v1.8-live 
        - python scripts/export.py schemas/pcdc/pcdc_v2.0 pcdc_v2.0 --fast
    ______________________________________________
    """
    )
    parser = argparse.ArgumentParser(description="Export a schema subset as a Google Sheets data dictionary.")
    parser.add_argument("schema", help="Path to the schema JSON file.")
    parser.add_argument("subset", help="Subset of the schema that should be exported.")
    parser.add_argument("--fast", action="store_true", help="Skip the definition fetching.")
    args = parser.parse_args()
    if os.path.exists(args.schema):
        with open(args.schema, "r") as file_in:
            schema = json.load(file_in)
            if args.subset in schema["subsets"]:
                print("Exporting: " + args.subset + "\n")
                schema_path = args.schema.replace(".json","")
                parent = schema_path.split("/")[2]
                commons = schema_path.split("/")[1]
                disease_group = args.subset.split("_")[0].split("-")[0]
                if args.fast:
                    definitions = "skip"
                else:
                    definitions = "retrieve"
                if disease_group in subset_info[commons]:
                    rows = assemble(definitions, commons, disease_group, parent, schema, args.subset)
                    export(args.subset, rows, subset_info[commons][disease_group]["id"])
                else:
                        print("\nERROR: Subset metadata is not present in export.py for target: " + args.subset + "\n")
            else:
                print("\nERROR: Schema does not include this subset: " + args.subset + "\n")
    else:
        print("\nERROR: Schema not found locally: " + args.schema + "\n")
    
