# As discussed in the chapter, string formatting could be used to simplify the 
# dateconvert2 . py program. Go back and redo this program making use 
# of the string-formatting method.
# Converts a date in form "mm./dd/yyyy" to "month day, year"

def main() : 
    # get the date 
    dateStr= input("Enter a date (mm/dd/yyyy) : ") 
    
    # split into components 
    monthStr, dayStr, yearStr =  dateStr.split("/") 
    # convert monthStr to the month name 
    months = ["January", "February", "March", "April", 
            "May", "June" , "July" , "August" , 
            "September", "October", "November", "December"]
    
    monthStr = months[int(monthStr)-1] 
    # output result in month day, year format 
    print(f"The converted date is: {monthStr}, {dayStr}, {yearStr}") 
main()