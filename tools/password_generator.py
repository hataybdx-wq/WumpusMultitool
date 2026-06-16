import random
import string
from colorama import Fore  
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
def generate_password():

    while True:
        try:
            length = int(input(f"{Fore.RED}[*] {Fore.GREEN}Enter Desired Password Length {Fore.YELLOW}(Minimum = 4, Maximum = 100,000): "))  # Use f-string for formatting
            if length < 4:
                print(f"{Fore.RED} [!] Password Must Be At Least 4 Characters. Please Try Again.")
            elif length > 100000:
                print(f"{Fore.RED} [!] Password Length Cannot Exceed 100,000 Characters. Please Try Again.")
            else:
                break
        except ValueError:
            print(f"{Fore.RED}[!] Invalid Input. Please Enter a Number")

    include_uppercase = input(f"{Fore.RED}[*] {Fore.GREEN}Include Uppercase Letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input(f"{Fore.RED}[*] {Fore.GREEN}Include Numbers? (y/n): ").strip().lower() == 'y'
    include_specials = input(f"{Fore.RED}[*] {Fore.GREEN}Include Special Characters? (y/n): ").strip().lower() == 'y'

    if include_specials:
        specials_input = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Special Characters to Include (Leave Empty for All): ").strip()
        specials_pool = specials_input if specials_input else string.punctuation
    else:
        specials_pool = ''

    print()

    if not (include_uppercase or include_numbers or include_specials):
        print(f"{Fore.RED}[!] You Must Select at Least One Character Set (Uppercase, Numbers, or Special Characters). ")

    lowercase_pool = string.ascii_lowercase
    uppercase_pool = string.ascii_uppercase if include_uppercase else ''
    numbers_pool = string.digits if include_numbers else ''

    character_pool = lowercase_pool + uppercase_pool + numbers_pool + specials_pool

    password = []
    if include_uppercase:
        password.append(random.choice(uppercase_pool))
    if include_numbers:
        password.append(random.choice(numbers_pool))
    if include_specials:
        password.append(random.choice(specials_pool))
    password.append(random.choice(lowercase_pool))  

    remaining_length = length - len(password)
    if remaining_length > 0:
        password += random.choices(character_pool, k=remaining_length)

    random.shuffle(password)

    
    final_password = ''.join(password)
    print(f"\n{Fore.RED}[+] {Fore.GREEN}Generated Password: {Fore.MAGENTA}{final_password}\n")
    return final_password

def run():
    generate_password()
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()
