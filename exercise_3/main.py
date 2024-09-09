import sys
from pathlib import Path
from colorama import Fore

path_string = sys.argv[1]

path = Path(path_string)

def file_color_string(filename:str) -> None:
    print(f'This is file {Fore.BLUE} {filename} {Fore.RESET}')

def folder_color_string(filename:str) -> None:
    print(f'This is folder {Fore.YELLOW} {filename} {Fore.RESET}')



def parse_folder(path: str) -> None:
    try:
        for file in path.iterdir():
            if file.is_dir():
                folder_color_string(file.name)
                parse_folder(file)
            elif file.is_file():
                file_color_string(file.name)
    except FileNotFoundError:
        print(f'{Fore.RED} BAD PATH TO FOLDER!!! {Fore.RESET}')
parse_folder(path)