import requests
import json

base_id = 'appXihEeZgqSVkQKW'
table_id = 'tblYvDEDGTorPlwaK'

# personal_access_token = 'pat7COO3Tiw4DGhYP.e29c8b4f571f926f81700620db30f968c8e0821f755defecef4ad0ea87e919fc' #scriptsampleproject
personal_access_token = 'patYhMo6CewMgB5RX.cff7c659d01c02565fba3ebbed65cc0f9f49855dd9eaad366820cb26824599d7'  # api


def create_headers():
    headers = {
        'Authorization': 'Bearer ' + str(personal_access_token),
        'Content-Type': 'application/json',
    }
    return headers


base_table_api_uri = 'https://api.airtable.com/v0/{}/{}'.format(base_id, table_id)

# List all records
headers = create_headers()
response = requests.get(base_table_api_uri, headers=headers)
# print(response.content)

'''
for i in response.json().get('records'):
    try:
        f_id = i['id']
        f_title = i['fields']['Title']
        f_img_url = i['fields']['img_url']
        f_body = i['fields']['body']
        f_summary = i['fields']['summary']
    except:
        pass
    print(f_id, f_title, f_img_url, f_body, f_summary, '\n')
'''

# Get Airtable records
table_record_ids = []
for i in response.json().get('records'):
    try:
        f_id = i['id']
        f_title = i['fields']['Title']
        f_img_url = i['fields']['img_url']
        f_body = i['fields']['body']
        f_summary = i['fields']['summary']
        f_posted = i['fields']['posted']
    except:
        pass
    table_record_ids.append(f_id)
    # print(f_id, f_title, f_img_url, f_body, f_summary, f_posted '\n')
# print(table_record_ids)

# Update Airtable records
'''
for i in table_record_ids:
    record_id = i
    base_table_api_url_for_update = 'https://api.airtable.com/v0/{}/{}/{}'.format(base_id, table_id, record_id)
    response_for_update = requests.patch(base_table_api_url_for_update, data='true', headers=headers)

    # headers = create_headers()
    # print(response_for_update.content)
    # print(response_for_update.json().get('records'))
'''

table_record_ids = []
table_record_dict = dict()
for i in response.json().get('records'):
    id = i.get('id')
    table_record_ids.append(id)
    table_record_dict[id] = False
print(table_record_dict, '\n')

posted_once = 1

while posted_once > 0:
    for id, posted in table_record_dict.items():
        if posted == False:
            table_record_dict[id] = True
            for i in response.json().get('records'):
                try:
                    s_id = id
                    s_title = i['fields']['Title']
                    s_img_url = i['fields']['img_url']
                    s_body = i['fields']['body']
                    s_summary = i['fields']['summary']
                except:
                    pass
            posted_once -= 1
        break
#print(s_id, s_title)
#print(table_record_dict)

