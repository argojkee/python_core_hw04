
def parse_file(path: str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.readlines()
            return [user.strip() for user in data]
    except Exception:
        print('Oops... Something went wrong. Please try again')

