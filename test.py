import requests

# Replace YOUR_WALLET_ADDRESS with the wallet address you want to check
wallet_address = "0x749076626Eb0b1d5b9BFfdB1F945B394944bED8E"

# Set up the API endpoint and parameters
api_endpoint = "https://api.opensea.io/api/v1/assets"
params = {"owner": wallet_address, "limit": 50}

# Send the API request and store the response in a variable
response = requests.get(api_endpoint, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Loop through the list of assets and print the name and image URL of each NFT
    for asset in response.json()["assets"]:
        print(asset["name"])
        print(asset["image_url"])
else:
    print("Error: Request failed with status code", response.status_code)
