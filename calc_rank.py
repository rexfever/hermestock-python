import pandas as pd
import getpass

'''

1.csv 파일 읽기
2.종목명, 순매수거래량 추출
3.종목명으로 정렬하기
4.기관 외인 데이터프레임 합치기
5.1~4에 대해서 2(KOSPI, KOSDAQ)번 반복
'''
# 데이터 파일 읽기 KOSPI 기관, KOSPI 외인, KOSDAQ 기관, KOSDAQ 외인
filePath = '/Users/'+getpass.getuser()+'/Downloads/'


def _extract_data_set(file):
    dataset = pd.read_csv(filePath + file, thousands=',')
    dataset = dataset[["종목명", "순매수거래대금"]]
    dataset.astype({'순매수거래대금': 'int32'}).dtypes
    dataset = dataset.sort_values('순매수거래대금', ascending=False)
    return dataset


def _merge_data_set(dataset1, dataset2):
    dataset = pd.merge(dataset1.head(10), dataset2.head(10), how='inner', on='종목명')
    print(dataset)
    dataset['순매수거래대금'] = dataset['순매수거래대금_x'] + dataset['순매수거래대금_y']
    dataset = dataset.sort_values('순매수거래대금', ascending=False)
    dataset = dataset[["종목명", "순매수거래대금"]]
    return dataset
