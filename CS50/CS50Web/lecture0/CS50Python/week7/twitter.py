# Extracts Twitter username from URL using str.replace
'''
url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
'''
# Extracts Twitter username from URL using str.removeprefix
'''
url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")
'''
# Uses re.sub

import re
'''
url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
#re.sub(pattern, repl, string, count=0, flags=0)

print(f"Username: {username}")
'''
# Uses capture group


url = input("URL: ").strip()

# matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
if matches:
    print("Username:", matches.group(1))
    #if we have (?:www\.) the ?: will use but not return result and we will have only one groop insted of 2
    
