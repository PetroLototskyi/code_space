from pyfiglet import Figlet
import sys

def fonts():
    figlet = Figlet()
    fonts = figlet.getFonts()
    for font in fonts:
        print(font)

def main():
    if len (sys.argv) == 1:
        font=Figlet()
    elif len(sys.argv) == 3 and (sys.argv [1] == "-f" or sys.argv [1] == "--font"):
        fontName = sys.argv [2]
        try:
            font =Figlet(font=fontName)
        except Exception:
            print("Invalid usage")
            # fonts()
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)

    str=input("Enter the text: ")
    output =font.renderText(str)
    print (output)

if __name__=="__main__":
    main()

