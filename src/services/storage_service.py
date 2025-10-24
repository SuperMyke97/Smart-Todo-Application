import json
from pathlib import Path


def append_json(file, data):
    if Path(file).exists():
        with open(file=file, mode='r', encoding="utf-8") as f:
            json_store = json.load(f)
            data['id']= f"{len(json_store) + 1}"
            json_store.append(data)
            return json_store
    
def store_json(file, data):
    with open(file=file, mode='w', encoding="utf-8") as f:
        json.dump(data, f)

if __name__ == '__main__':
    p = Path('./data.json')
    print(p)
    f = {1:'d', 2:'wa'}
    d = append_json(file=p, data=f)
    store_json(file=p, data=d)