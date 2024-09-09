from .data import parse_cats_info

def get_cats_info(path:str) -> list[dict]:
    cats = parse_cats_info(path)
    cats_info = []
    for cat in cats:
        id, name, age = cat.split(',')
        cats_info.append({
            'id' : id,
            'name' : name,
            'age' : int(age)
        })
    return cats_info

