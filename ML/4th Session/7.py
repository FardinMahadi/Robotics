from datetime import datetime
from termcolor import cprint

def generate_palindrome_dates(n):
    count = 0
    year = datetime.today().year

    cprint("Next 50 palindrome dates:", "green", "on_red")

    while count < n:
        year_str = str(year).zfill(4)
        day = year_str[3] + year_str[2]  
        month = year_str[1] + year_str[0]  

        try:
            date_obj = datetime(year=int(year_str), month=int(month), day=int(day))
            if date_obj >= datetime.today():
                print(date_obj.strftime("%d.%m.%Y"))
                count += 1
        except ValueError:
            pass
        year += 1

generate_palindrome_dates(50)
