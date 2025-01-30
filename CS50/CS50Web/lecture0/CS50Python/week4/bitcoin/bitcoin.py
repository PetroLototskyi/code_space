import json  # Demonstrates JSON
import sys
import requests

# Check if the number of command-line arguments is correct
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
else:
    # Try to convert the second command-line argument to a float
    try:
        amount = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

# Try to send a GET request to the specified URL
try:
    response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")

except requests.RequestException:
    print("Request is not successful")

# Parse the JSON response and calculate the current cost
object = response.json()
price = object["bpi"]["USD"]["rate_float"]
curent_cost = price * amount

# Print the current cost in USD format
print(
    f"${curent_cost:,.4f}"
)  # format USD to four decimal places with a thousands separator

# print(json.dumps(response.json(), indent=2)) # create nice print of the json
