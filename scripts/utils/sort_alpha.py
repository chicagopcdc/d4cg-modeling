import json, argparse, os


def sort_dict_with_exceptions(d, tail_order=("Other", "Unknown", "Not Reported")):
    """
    Return a new dict where:
      - keys are sorted alphabetically
      - specified tail keys (if present) are moved to the end in tail_order
    Values are preserved from the original dict.
    """
    # 1. Sort all keys
    sorted_keys = sorted(d.keys())
    
    # 2. Figure out which tail keys actually exist in this dict
    tail_keys = [k for k in tail_order if k in d]
    
    # 3. Keep all other keys in sorted order
    head_keys = [k for k in sorted_keys if k not in tail_keys]
    
    # 4. Rebuild the dict in the desired order, pulling values from original d
    new_keys = head_keys + tail_keys
    return {k: d[k] for k in new_keys}



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Schema Utils: alphabetize PVs and subsets")
    parser.add_argument("schema", help="Path to the schema JSON file.")
    args = parser.parse_args()
    if os.path.exists(args.schema):
        with open(args.schema, "r") as file_in:
            schema = json.load(file_in)
            #Alphabetize PVs with "tail values" at the end
            for enum in schema["enums"].values():
                enum["permissible_values"] = sort_dict_with_exceptions(enum["permissible_values"])
            #Alphabetize class subsets
            for sclass in schema["classes"].values():
                sclass["in_subset"] = sorted(sclass["in_subset"])
                #Alphabetize slot subsets
                for slot in sclass["slot_usage"].values():
                    slot["in_subset"] = sorted(slot["in_subset"])
                    #Alphabetize value subsets
                    for enum in schema["enums"].values():
                        for value in enum["permissible_values"].values():
                            value["in_subset"] = sorted(value["in_subset"])

        with open(args.schema, "w") as file_out:
            file_out.write(json.dumps(schema, indent=4))
            print("...done")
    else:
        print("schema not found: " + args.schema)

