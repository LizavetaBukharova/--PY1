import json

INPUT_FILE = "input_11.csv"

def csv_to_list_dict(filename) -> list[dict]:
    with open(filename) as f:
        keys = []
        values = []
        lists_ = f.readlines()
        all_list = 0
        for y in lists_:
            all_list += 1
            value_all = all_list - 1
        keys_all = lists_[0].rstrip().split(",")
        for i in lists_[1:]:
            values.append(i.rstrip().split(","))
        for x in values:
            for g in range(value_all):
                d = {k: v for k, v in zip(keys_all, values[g])}
                keys.append(d)
            return keys


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
