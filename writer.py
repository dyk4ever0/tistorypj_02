from tistory_util import *
import requests
import json

blog_name = "powerupupupup.tistory.com"
category_id = "1076872"

base_id = 'appXihEeZgqSVkQKW'
table_id = 'tblYvDEDGTorPlwaK'

# scriptsampleproject
# personal_access_token = 'pat7COO3Tiw4DGhYP.e29c8b4f571f926f81700620db30f968c8e0821f755defecef4ad0ea87e919fc'
# api
personal_access_token = 'patYhMo6CewMgB5RX.cff7c659d01c02565fba3ebbed65cc0f9f49855dd9eaad366820cb26824599d7'


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

target_record = ['rec07rezMVj5tZKvC', 'rec0BLy3KNMPS33y9', 'rec428rQ0f0JB201O', 'rec4GTJEeSmA69UEf',
                 'rec4p3TF1BGyprTF3', 'recC24EI5ynJrAngd', 'recCc7UKulBh1yBk3', 'recNIZNi1EUPc9FMM',
                 'recQyXqEMnQMT8887', 'recRvUij4Kafv3kXe', 'recRwja6zOsWscp1q', 'recSnhmyBhGGua0qw',
                 'recTCJL6I9Zv1WutZ', 'recU9eq8xaR1VrCyj', 'recUlF0Gv7yaDJAQR', 'recXDdiq2Kzbj27Vi',
                 'recYP584flKdRIjLd', 'recYS6i6EkQWkMhRZ', 'recZyjotGWApH1hvZ', 'recaGZvHZv2q8py3Y',
                 'rece7RQadCwJrqceA', 'recenQXjtL0FUUd7W', 'rech1G7JrwIaRELti', 'rechoBxcOYDErZSPL',
                 'reckbNiJ1UOhVDsm6', 'recnquJO6YFfPWuDe', 'recoI8QeAGeGvUp9q', 'recpVasJRNVB32ivJ',
                 'recr3ZkXiyVoXF018', 'recud7bjFegOafXjQ', 'recvVdP4E0G2XlD5m', 'recwsG97XNmCgnz0m',
                 'recxrUPIoyoh97Geh']

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


if __name__ == "__main__":
    title, content = writer()

    blog_write(
        blog_name=blog_name,
        category_id=category_id,
        title=title,
        content=content,
        tag='API, Automation, chatGPT, OpenAI, Python'
    )
