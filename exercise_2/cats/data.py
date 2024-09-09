def parse_cats_info(path: str) -> list:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.readlines()
            cats_list = [cat.strip() for cat in data]
            return cats_list
    except Exception:
        print('Oops... Something went wrong. Please, try again')