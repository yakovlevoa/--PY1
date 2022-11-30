import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(csv_data, separate=',', new_line='\n') -> list[dict]:
    with open(csv_data) as f:
        lines = f.read().split(new_line)
        headers = lines[0].split(separate)
        rows = [lines[i].split(separate) for i in range(1, len(lines) - 1)]
        json_data = []
        for value in rows:
            json_data.append({headers[i]: value[i] for i in range(0, len(headers))})
        return json_data


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
