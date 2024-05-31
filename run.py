import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Baiana-orders')

sales = SHEET.worksheet('orders')

data = sales.get_all_values()

#print(data)

def print_title():
    print("""
    888888b.            d8b                            d8b                
    888  "88b           Y8P                            88P                
    888  .88P                                          8P                 
    8888888K.   8888b.  888  8888b.  88888b.   8888b.  "   .d8888b        
    888  "Y88b     "88b 888     "88b 888 "88b     "88b     88K            
    888    888 .d888888 888 .d888888 888  888 .d888888     "Y8888b.       
    888   d88P 888  888 888 888  888 888  888 888  888          X88       
    8888888P"  "Y888888 888 "Y888888 888  888 "Y888888      88888P'       
                          888                                             
                          888                                             
                          888                                             
    .d88b.  888d888  .:d88888  .d88b.  888d888 .d8888b                    
    d88""88b 888P"   d88" 888 d8P  Y8b 888P"   88K                        
    888  888 888     888  888 88888888 888     "Y8888b.                   
    Y88..88P 888     Y88b 888 Y8b.     888          X88                   
    "Y88P"  888      "Y888888 "Y8888  888      88888P'  
    """)

    print("\nWelcome to Baiana's Ordering System! Here, you can order some of our delicious food.\n")

def select_food():
    # Define the menu itens and their keys.
    menu_options = {
        "1": "Coxinha",
        "2": "Croquete",
        "3": "Quibe",
        "4": "Rissol",
        "5": "Pastel",
        "6": "Pão queijo"
    }

    # Print out the menu itens to the user
    print("Please choose an item from the menu by entering the corresponding number:")
    for key, value in menu_options.items():
        print(f"{key}: {value}")

    while True:
        try:
            # Get input from user
            choice = input("Enter your choice (1-6):\n ")

            # check user input for validity and runs ask_quantity function if the input is valid
            if choice in menu_options:
                print(f"\nYou have selected: {menu_options[choice]}\n")
                ask_quantity()
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 6.\n")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.\n")

                

def ask_quantity():
    while True:
        try:
            # Ask the user to enter a number starting from 6, since 6 is min. that can be ordered
            number = int(input("Please enter a number starting from 6: "))
            
            # Check if the number is valid and if not loops back to the question
            if number >= 6:
                print(f"Thank you! You have ordered: {number}\n")
                break
            else:
                print("\nInvalid input. The number must be 6 or greater.\n")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.\n")

def main():
    print_title()
    select_food()

main()