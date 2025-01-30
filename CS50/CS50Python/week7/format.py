# Reformats "last, first" as "first last"

import re
'''
name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")
'''
name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name): # Uses walrus ":=" operator |    #(.+) -- will return value to matches
    #walrus ":=" operator allow to asign and ask boolian question simultaniosly
    name = matches.groups(2) + " " + matches.groups(1)
print(f"hello, {name}")
