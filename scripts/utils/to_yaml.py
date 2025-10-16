import sys, json, yaml

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("\nExample usage: python to_yaml.py schemas/pcdc/pcdc_v2.0.json schemas/pcdc/pcdc_v2.0.yaml")
        sys.exit()
    target = sys.argv[1]
    out_file = sys.argv[2]

    with open(target, "r") as json_schema:
        schema = json.load(json_schema)

    with open(out_file, "w") as yaml_schema:
        yaml.dump(schema, yaml_schema, sort_keys=False, indent=4)
