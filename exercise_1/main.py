from salaries.functions import total_salary
from pathlib import Path

path = Path('salaries/salaries.txt')


def main():
    print(total_salary(path))



if __name__ == '__main__':
    main()