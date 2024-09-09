from cats.functions import get_cats_info
from pathlib import Path

path = Path('cats/cats.txt')

def main():
    print(get_cats_info(path))


if __name__ == '__main__':
    main()