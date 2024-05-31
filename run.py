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

#sales = SHEET.worksheet('orders')

#data = sales.get_all_values()

#print(data)


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
 .d88b.  888d888  .d88888  .d88b.  888d888 .d8888b                    
d88""88b 888P"   d88" 888 d8P  Y8b 888P"   88K                        
888  888 888     888  888 88888888 888     "Y8888b.                   
Y88..88P 888     Y88b 888 Y8b.     888          X88                   
 "Y88P"  888      "Y88888  "Y8888  888      88888P'  
""")

print("\nWelcome to Baiana's Ordering System! Here, you can order some of our delicious food. How can we serve you today?")