def main():
    M_D = 31
    M_M = 12
    M_Y = 2024
    months = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October","November", "December"
    ]

    month_dict = {month: str(index+1).zfill(2) for index, month in enumerate(months)}


    while True:
        date = input("Date: ")
        if "/" in date:
            try:
                month, day, year = date.split("/")
                if int(day) > M_D or int(month) > M_M or int(year) > M_Y:
                    continue
                day = fix_sp(day)
                month = fix_sp(month)
                year = fix_sp(year)
                day = day.zfill(2)
                month=month.zfill(2)
                print(f"{year}-{month}-{day}")
            except (ValueError, EOFError):
                pass
            else:
                break
        elif "," in date:
            try:
                month, day, year = date.split(" ")
                day = day[:-1]
                if int(day) > M_D or month not in months or int(year) > M_Y:
                    continue
                day = day.zfill(2)
                print(f"{year}-{month_dict[month]}-{day}")
            except (ValueError, EOFError):
                pass
            else:
                break

def fix_sp(s):
    if " " in s:
        s = s.replace(" ", "")
    return s
main()

