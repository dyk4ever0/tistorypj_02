import requests
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


def get_translate(text):
    client_id = os.getenv("PAPAGO_ID")  # <-- client_id 기입
    client_secret = os.getenv("PAPAGO_SECRET")  # <-- client_secret 기입

    data = {'text': text,
            'source': 'en',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id": client_id,
              "X-Naver-Client-Secret": client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if rescode == 200:
        send_data = response.json()
        print("sd",send_data)
        trans_data = send_data['message']['result']['translatedText']
        print("td", trans_data)
        return trans_data
    else:
        print("Error Code:", rescode)
