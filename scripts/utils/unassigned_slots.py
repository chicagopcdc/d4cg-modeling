import sys,json


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\nExample usage: python unassigned_slots.py schemas/pcdc/pcdc_v1.13.json")
        sys.exit()
    target = sys.argv[1]
    with open(target, "r") as file_in:
        schema = json.load(file_in)
        for s in schema["slots"]:
            declared = False
            for c in schema["classes"]:
                for dclass in schema["classes"][c]["slots"]:
                    if s == dclass:
                        declared = True
            if not declared:
                print("Not declared: " + s)