import sys,json


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\nExample usage: python linkml_checks.py schema/pcdc/pcdc_v2.0.json")
        sys.exit()
    target = sys.argv[1]
    with open(target, "r") as file_in:
        schema = json.load(file_in)
        #Check for undeclared slots
        for s in schema["slots"]:
            declared = False
            for c in schema["classes"]:
                for dclass in schema["classes"][c]["slots"]:
                    if s == dclass:
                        declared = True
            if not declared:
                print("Undeclared slot: " + s)
        #Check for unaffiliated enums
        for e in schema["enums"]:
            affiliated = False
            for s in schema["slots"]:
                if schema["slots"][s]["range"] == e:
                    affiliated = True
            if not affiliated:
                print("Unaffiliated enum: " + e)