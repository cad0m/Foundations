import requests
import sys

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("put a float")
else:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit()

response_json = response.json()
price = response_json["bpi"]["USD"]["rate_float"]


print(f"${price*n:,.4f}")
