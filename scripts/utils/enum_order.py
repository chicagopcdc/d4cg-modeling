import json,re

def move_keys_to_end(d: dict, keys):
    for k in keys:
        if k in d:
            d[k] = d.pop(k)  # pop + reinsert moves it to the end
    return d


if __name__ == "__main__":
    with open("../schemas/pcdc/pcdc_v1.13.json", "r") as file_in:
        schema = json.load(file_in)
        for e in schema["enums"]:
            enum = schema["enums"][e]
            enum["permissible_values"] = dict(sorted(enum["permissible_values"].items())) #Sort alphabetically
            move_keys_to_end(enum["permissible_values"], ["Other", "Unknown", "Not Reported"])
        
        with open("../schemas/pcdc/pcdc_v1.13.json", "w") as file_out:
            json.dump(schema, file_out, indent=4)
       