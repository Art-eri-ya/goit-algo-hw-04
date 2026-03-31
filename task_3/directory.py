import sys
import pathlib
from colorama import Fore, Style


def display_tree(path, indent=""):
    items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    
    for el in path.iterdir():
        if el.is_dir():
            print(f"{indent}{Fore.BLUE}{el.name}/{Style.RESET_ALL}")
            display_tree(el, indent + "    ")
        if el.is_file():
            print(f"{indent}{Fore.GREEN}{el.name}{Style.RESET_ALL}")

def main():
    if len(sys.argv) < 2:
        print(Fore.YELLOW + "Error: can' be identified as a directory path")
        return

    target_path = pathlib.Path(sys.argv[1])

    if not target_path.exists() or not target_path.is_dir():
        print(Fore.RED + "Error: Invalid directory path.")
        return

    print(Fore.GREEN + f"Structure for: {target_path}")
    display_tree(target_path)

if __name__ == "__main__":
    main()





