# -*- coding: utf-8 -*-
import pandas as pd
import send_msg as sm
import getpass, os
import json

'''

1.csv 파일 읽기
2.종목명, 순매수거래량 추출
3.종목명으로 정렬하기
4.기관 외인 데이터프레임 합치기
5.1~4에 대해서 2(KOSPI, KOSDAQ)번 반복
'''
# 데이터 파일 읽기 KOSPI 기관, KOSPI 외인, KOSDAQ 기관, KOSDAQ 외인
filePath = '/Users/' + getpass.getuser() + '/Downloads/'
filePath = '/Users/rexsmac/workspace/projects/hermestock/'


def count_file():
    file_list = os.listdir(filePath)
    file_list = [file for file in file_list if file.endswith(".csv")]
    return len(file_list)


def rename_file():
    file_list = os.listdir(filePath)
    file_list = [file for file in file_list if file.endswith(".csv")]
    file_list.sort(key=lambda s: os.path.getmtime(os.path.join(filePath, s)))
    for idx, file in enumerate(file_list):
        src = os.path.join(filePath, file)
        dst = 'data_' + str(idx) + '.csv'
        dst = os.path.join(filePath, dst)
        os.rename(src, dst)


def extract_data_set(file):
    dataset = pd.read_csv(filePath + file, thousands=',', encoding='cp949')
    dataset = dataset[["종목명", "거래대금_순매수"]]
    dataset.astype({'거래대금_순매수': 'int32'}).dtypes
    dataset = dataset.sort_values('거래대금_순매수', ascending=False)
    return dataset


def merge_data_set(dataset1, dataset2, channels):
    dataset = pd.merge(dataset1.head(10), dataset2.head(10), how='inner', on='종목명')
    #sm.send_message_to_slack(dataset.to_string(), channels)
    dataset['거래대금_순매수'] = dataset['거래대금_순매수_x'] + dataset['거래대금_순매수_y']
    print(dataset)
    dataset = dataset.sort_values('거래대금_순매수', ascending=False)
    dataset = dataset[["종목명", "거래대금_순매수"]]
    sm.send_message_to_slack(dataset.to_string(), channels)
    return dataset


def read_channels(env):
    config_path = './config.json'
    if env != 'live':
        config_path = './config_dev.json'

    with open(config_path) as f:
        config = json.load(f)
    channels = []
    for i in config['channels']:
        channel = []
        for j in i:
            channel.append(i[j])
        channels.append(channel)

    return channels


def read_date(env):
    config_path = './config.json'
    if env != 'live':
        config_path = './config_dev.json'

    with open(config_path) as f:
        config = json.load(f)
    date = config['date']
    return date