#Age calculator
from datetime import datetime

def age_calculator(year):
    today = datetime.now()
    current_year = today.year
    birth_year = year.year
    age = current_year - birth_year
    if birth_year > current_year:
        print("BYE_BYE")
    else:
        print("Age is :" +age)
    print(today)
    
year = datetime(2027,2,26)
age_calculator(year)