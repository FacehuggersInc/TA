import os, time
import pickle, time, os
from pathlib import Path
from colorama import Fore, Back, Style


#Functions
def wait(sec):
    """Wait a set amount of time (sec)."""
    time.sleep(sec)

def hold():
    """Hold the screen from refeshing with an Input, that isnt going to be saved to any varibale."""
    input("\n[...] Press [ENTER] to continue")

def clear_screen():
    """Clear windows console."""
    os.system("CLS")

#Display
def tabTitle(title = str, text = str):
    os.system(f'title {title} / {text}')

def dimmedText(text = str):
    print(Style.DIM + text + Style.RESET_ALL)

def title1(text = str):
    text = text.upper()
    print(f"\n{text}")

def title2(text = str):
    text = text.upper()
    print(f"\n    {text}")

#Input
def prompt(title = str, acceptNumbers = bool):
    print(f"\n  [!] {title}")
    answer = input(f"  [?] ")
    if acceptNumbers:
        if answer.isnumeric():
            answer = int(answer)
    return answer

def promptOptions(title = str, options = [], optionSym = "*"):
    while True:
        print(f"\n  [!] {title}\n")
        for option in options:
            print(f"    {optionSym} {option}")
        user_input = input(f"\n  [?] ")
        if not user_input in options:
            print("\nPlease check your choices spelling and try again (case sensitive).")
        else:
            return user_input

def numSelectOptions(title = str, options = []):
    i = 0
    for option in options:
        i += 1
        print(f"  [{i}] | {option}")
    user_input = prompt(
        f"{title}\n      - Name or Number Only   - Case Sensitive", False)
    if user_input.isnumeric():
        user_input = options[int(user_input) - 1]
    return user_input

def decision(title = str, yesOption = str, noOption = str):
    while True:
        print(f"\n  [!] {title}")
        print(f"     Y | {yesOption}")
        print(f"     N | {noOption}")
        decision = input(f"\n  [?] ").lower().strip()
        if decision == "y" or decision == "n":
            return decision
        else:
            print(f"\nPlease enter either Y or N.")

#Save and Load
def save(location, foldername, data, filename, extension):
    newFile = filename + extension
    if foldername == "" or foldername == " " or foldername == "none" or foldername == "None":
        newLoc = newFile
    else:
        try:
            os.makedirs(foldername)
            newLoc = foldername + "/" + newFile 
        except FileExistsError:
            newLoc = foldername + "/" + newFile
    my_path = Path(location) / newLoc
    with my_path.open('wb') as fp:
        pickle.dump(data, fp)


def load(location,foldername, filename, extension, ifFailedVar):
    newFile = filename + extension
    if foldername == "" or foldername == " " or foldername == "none" or foldername == "None":
        newLoc = newFile
    else:
        newLoc = foldername + "/" + newFile
    try:
        my_path = Path(location) / newLoc
        with my_path.open('rb') as fp:
            return(pickle.load(fp))
    except:
        print("[sAl] Failed to load character.")
        return ifFailedVar












