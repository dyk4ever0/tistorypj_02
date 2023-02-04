import requests
import json

# Your Airtable base ID
base_id = 'appXihEeZgqSVkQKW'

# personal_access_token = 'pat7COO3Tiw4DGhYP.e29c8b4f571f926f81700620db30f968c8e0821f755defecef4ad0ea87e919fc' #scriptsampleproject
# personal_access_token = 'patYhMo6CewMgB5RX.cff7c659d01c02565fba3ebbed65cc0f9f49855dd9eaad366820cb26824599d7'  # api
# personal_access_token = 'patrjZ7pZvEiF5G7i.b912c0560ea2aa1066d29aab5479edcfafe2e6899fc798cc41716e4608cec8c0' #apinew
personal_access_token = 'pat60o2Q8kg7yd3wI.db721e91bf04c06bf71ae46de5ea7550fe0cc2ffc0ae5883a910f0edae9e88af' #jan4

# Your Airtable API key
airtable_api_key = personal_access_token

# The name of the table you want to update
table_name = "Table 1"

# The URL of the Airtable API
url = f"https://api.airtable.com/v0/{base_id}/{table_name}"

# Set the headers for the API request
headers = {
    "Authorization": f"Bearer {airtable_api_key}",
    "Content-Type": "application/json",
}
# check
print(headers)

# Make the API request to retrieve the records
response = requests.get(url, headers=headers)

# Check the response status code to see if the request was successful
if response.status_code == 200:
    # Get the records from the response
    records = response.json()["records"]

    # Loop through the records to find the first one with a value of "false" in the "posted" column
    for record in records:
        if record["fields"]["posted"] == "false":
            record_id = record["id"]

            # The new value you want to set in the "posted" column
            new_value = "true"

            # Construct the API endpoint URL for updating the record
            url = f"https://api.airtable.com/v0/{base_id}/{table_name}/{record_id}"

            # Define the data you want to update in the record
            data = {
                "fields": {
                    "posted": new_value,
                }
            }

            # Make the API request using the PATCH method
            response = requests.patch(url, headers=headers, json=data)

            # Check the response status code to see if the request was successful
            if response.status_code == 200:
                print("Record updated successfully")
                break
            else:
                print(f"Failed to update record. Response code: {response.status_code}")
            break
    else:
        print("No record found with a value of 'false' in the 'posted' column")
else:
    print(f"Failed to retrieve records. Response code: {response.status_code}")