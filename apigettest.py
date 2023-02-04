import requests

# Your Airtable base ID
base_id = 'appXihEeZgqSVkQKW'

# Your Airtable API key
airtable_api_key = 'pat60o2Q8kg7yd3wI.db721e91bf04c06bf71ae46de5ea7550fe0cc2ffc0ae5883a910f0edae9e88af' #jan4

# The name of the table you want to retrieve data from
table_name = "Table 1"

# The URL of the Airtable API
url = f"https://api.airtable.com/v0/{base_id}/{table_name}"

# Set the headers for the API request
headers = {
    "Authorization": f"Bearer {airtable_api_key}",
    "Content-Type": "application/json",
}

print(headers)

# Make the API request to retrieve the records
response = requests.get(url, headers=headers)

# Check the response status code to see if the request was successful
if response.status_code == 200:
    print("API key is valid")
else:
    print("API key is not valid. Response code:", response.status_code)
