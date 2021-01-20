# -*- coding: utf-8 -*-
import requests

CHANNEL_LIST = ["https://hooks.slack.com/services/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",
                "https://hooks.slack.com/services/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",
                "https://hooks.slack.com/services/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",
                "https://hooks.slack.com/services/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"]

#CHANNEL_LIST = ["https://hooks.slack.com/services/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"]


def send_message_to_slack(text):
    for channel in CHANNEL_LIST:
        url = channel
        payload = { "text" : text }
        requests.post(url, json=payload)
