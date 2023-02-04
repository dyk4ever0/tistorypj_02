from tistory_util import *
import requests
import json
from translator import get_translate

# Tistory category ID
blog_name = "powerupupupup.tistory.com"
category_id = "1076872"
k_category_id = "1077786"

# Airtable base ID
base_id = 'appXihEeZgqSVkQKW'
table_id = 'tblYvDEDGTorPlwaK'

# scriptsampleproject
# personal_access_token = 'pat7COO3Tiw4DGhYP.e29c8b4f571f926f81700620db30f968c8e0821f755defecef4ad0ea87e919fc'
# api
# personal_access_token = 'patYhMo6CewMgB5RX.cff7c659d01c02565fba3ebbed65cc0f9f49855dd9eaad366820cb26824599d7'
# apinew
# personal_access_token = 'patrjZ7pZvEiF5G7i.b912c0560ea2aa1066d29aab5479edcfafe2e6899fc798cc41716e4608cec8c0'
# jan4
personal_access_token = 'pat60o2Q8kg7yd3wI.db721e91bf04c06bf71ae46de5ea7550fe0cc2ffc0ae5883a910f0edae9e88af'

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
            url1 = f"https://api.airtable.com/v0/{base_id}/{table_name}/{record_id}"
            url2 = 'https://api.airtable.com/v0/{}/{}'.format(base_id, table_id)

            # Define the data you want to update in the record
            data = {
                "fields": {
                    "posted": new_value,
                }
            }

            # Make the API request using the PATCH method
            response = requests.patch(url1, headers=headers, json=data)

            # Make the API request using the GET method
            response2 = requests.get(url2, headers=headers)
            s_id = record_id
            s_title = record["fields"]["Title"]
            s_body = record["fields"]["body"]
            s_img_url = record["fields"]["img_url"]
            s_summary = record["fields"]["summary"]

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

'''
def create_headers():
    headers = {
        'Authorization': 'Bearer ' + str(personal_access_token),
        'Content-Type': 'application/json',
    }
    return headers

base_table_api_url = 'https://api.airtable.com/v0/{}/{}'.format(base_id, table_id)
# List all records
headers = create_headers()
response = requests.get(base_table_api_url, headers=headers)
# print(response.content, '\n')

# Get Airtable records
table_record_ids = []
for i in response.json().get('records'):
    try:
        f_id = i['id']
        f_title = i['fields']['Title']
        f_img_url = i['fields']['img_url']
        f_body = i['fields']['body']
        f_summary = i['fields']['summary']
    except:
        pass
    table_record_ids.append(f_id)
    # print(f_id, f_title, f_img_url, f_body, f_summary, '\n')
# print(table_record_ids, '\n')

table_record_ids = []
table_record_dict = dict()
for i in response.json().get('records'):
    id = i.get('id')
    table_record_ids.append(id)
    table_record_dict[id] = False
# print(table_record_dict, '\n')
# print(table_record_ids)

s_id = ''
for i in response.json().get('records'):
    try:
        if s_id == i['id']:
            s_title = i['fields']['Title']
            s_img_url = i['fields']['img_url']
            s_body = i['fields']['body']
            s_summary = i['fields']['summary']
    except:
        pass
'''


def writer():
    title = f"{s_title}({s_id})"

    content = f'''
    <p data-ke-size="size16">🧸 Title 🧸</p>
    <p data-ke-size="size16">{s_title}</p>
    <p data-ke-size="size16">&nbsp;</p>
    <p data-ke-size="size16">🧸 Image 🧸</p>
    <p data-ke-size="size16"><img src="{s_img_url}" alt=""/></p>
    <p data-ke-size="size16">&nbsp;</p>
    <p data-ke-size="size16">🧸 body 🧸</p>
    <p data-ke-size="size16">{s_body}</p>
    <p data-ke-size="size16">&nbsp;</p>
    <p data-ke-size="size16">🧸 summary 🧸</p>
    <p data-ke-size="size16">{s_summary}</p>
    <p data-ke-size="size16">&nbsp;</p>
    <p data-ke-size="size16">Thanks! Happy DX Journey 💫</p>
    '''

    return title, content


def korean_writer():
    explanation_kr_title = get_translate(s_title)
    explanation_kr_body = get_translate(s_body)
    explanation_kr_summary = get_translate(s_summary)

    title_2 = f"{explanation_kr_title}({s_id})"

    content_2 = f'''
    <p data-ke-size="size16">🧸 안녕하세요, 오늘은 어떤 DX 소식이 기다리고 있을까요? 사진과 함께 감상해주세요! 🧸</p>
    <p data-ke-size="size16">✨ 짜잔-! ✨</p>
    <p data-ke-size="size6">&nbsp;</p>
    <p data-ke-size="size16">제목: {explanation_kr_title}</p>
    <p data-ke-size="size16">🧸 이미지 🧸</p>
    <p data-ke-size="size16"><img src="{s_img_url}" alt=""/></p>
    <p data-ke-size="size16">&nbsp;</p>
    <p data-ke-size="size16">🧸 설명 🧸</p>
    <p data-ke-size="size16">{explanation_kr_body}</p>
    <p data-ke-size="size16">&nbsp;</p>
    <p data-ke-size="size16">🧸 요약입니다 🧸</p>
    <p data-ke-size="size16">{explanation_kr_summary}</p>
    <p data-ke-size="size16">&nbsp;</p>
    <p data-ke-size="size16">감사합니다! 행복한 DX 생활 되세요 :) 💫</p>
    '''

    return title_2, content_2


if __name__ == "__main__":
    title, content = writer()

    blog_write(
        blog_name=blog_name,
        category_id=category_id,
        title=title,
        content=content,
        tag='API, Automation, chatGPT, OpenAI, Python'
    )

    title_2, content_2 = korean_writer()

    blog_write(
        blog_name=blog_name,
        category_id=k_category_id,
        title=title_2,
        content=content_2,
        tag='API, Automation, chatGPT, OpenAI, Python'
    )
