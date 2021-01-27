# -*- coding: utf-8 -*-
import requests

MY_CHNNEL = "https://hooks.slack.com/services/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"


def send_message_to_me(error):
    url = MY_CHNNEL
    payload = {"text": error}
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        raise ValueError(
            f'슬랙메세지 전송 에러 코드 {response.status_code}, the response is:\n{response.text}'
        )


def send_message_to_slack(text, channels):
    for channel in channels:
        url = channel
        payload = {"text": text}
        print(f"origin: {url[0]}")
        response = requests.post(url[0], json=payload)
        if response.status_code != 200:
            print(f'url[1]:{url[1]}')
            send_message_to_me(
                f'**********************************\n{url[1]}에서 {response.text} 오류 발생\n**********************************')
            raise ValueError(
                f'{url[1]} Request to slack returned an error {response.status_code}, the response is:\n{response.text}'
            )
