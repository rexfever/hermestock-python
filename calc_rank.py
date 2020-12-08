import glob
import os
import pandas as pd

'''

1.csv 파일 읽기
2.종목명, 순매수거래량 추출
3.종목명으로 정렬하기
4.기관 외인 데이터프레임 합치기
5.1~4에 대해서 2(KOSPI, KOSDAQ)번 반복
'''
# 데이터 파일 읽기 KOSPI 기관, KOSPI 외인, KOSDAQ 기관, KOSDAQ 외인
filePath = '~/Downloads/'
KOSPI_fileList = ['data.csv', 'data (1).csv']
KOSDAQ_fileList = ['data (2).csv', 'data (3).csv']

'''
data_ki = pd.read_csv("/Users/rexsmac/Downloads/data.csv", thousands=',')
data_fo = pd.read_csv("/Users/rexsmac/Downloads/data (1).csv", thousands=',')

data_ki = data_ki[["종목명", "순매수거래대금"]]
data_ki.astype({'순매수거래대금': 'int32'}).dtypes
data_ki = data_ki.sort_values('종목명', ascending=False)

data_fo = data_fo[["종목명", "순매수거래대금"]]
data_fo.astype({'순매수거래대금': 'int32'}).dtypes
data_fo = data_fo.sort_values("종목명", ascending=False)
'''


def _extract_data_set(file):
    dataset = pd.read_csv(filePath + file, thousands=',')
    dataset = dataset[["종목명", "순매수거래대금"]]
    dataset.astype({'순매수거래대금': 'int32'}).dtypes
    dataset = dataset.sort_values('순매수거래대금', ascending=False)
    return dataset


def _merge_data_set(dataset1, dataset2):
    dataset = pd.merge(dataset1.head(10), dataset2.head(10), how='inner', on='종목명')
    dataset['순매수거래대금'] = dataset['순매수거래대금_x'] + dataset['순매수거래대금_y']
    dataset = dataset.sort_values('순매수거래대금', ascending=False)
    dataset = dataset[["종목명", "순매수거래대금"]]
    return dataset


print(_merge_data_set(_extract_data_set(KOSPI_fileList[0]), _extract_data_set(KOSPI_fileList[1])))
print(_merge_data_set(_extract_data_set(KOSDAQ_fileList[0]), _extract_data_set(KOSDAQ_fileList[1])))

'''
merge = pd.merge(data_ki, data_ye, how='inner', on='종목명')
merge['순매수거래대금'] = merge['순매수거래대금_x'] + merge['순매수거래대금_y']

merge = merge.sort_values('순매수거래대금', ascending=False)
merge = merge[["종목명", "순매수거래대금"]]
'''

'''
        dataset = pd.merge(data_ki.head(10), data_fo.head(10), how='inner', on='종목명')
        tmp = tmp.sort_values('순매수거래대금', ascending=False)


def _read_csv(fileList):

    for file in fileList:
        tmp = pd.read_csv(filePath + file, thousands=',')
        tmp = tmp[["종목명", "순매수거래대금"]]
        tmp.astype({'순매수거래대금': 'int32'}).dtypes
        tmp = tmp.sort_values('종목명', ascending=False)
        dataset = pd.merge(data_ki.head(10), data_fo.head(10), how='inner', on='종목명')
        tmp = tmp.sort_values('순매수거래대금', ascending=False)
    return tmp


# print(data_ki)
data_ki = data_ki[["종목명", "순매수거래량"]]
data_ki.astype({'순매수거래량': 'int32'}).dtypes
data_ki = data_ki.sort_values('순매수거래량', ascending=False)
# print(data_ki)

data_fo = data_fo[["종목명", "순매수거래량"]]
data_fo.astype({'순매수거래량': 'int32'}).dtypes
data_fo = data_fo.sort_values('순매수거래량', ascending=False)
'''
'''
(1) pandas DataFrame의 칼럼 이름 바꾸기
    :  df.columns = ['a', 'b']
    :  df.rename(columns = {'old_nm' : 'new_nm'), inplace = True)
'''
'''
merge = pd.merge(data_ki.head(10), data_fo.head(10), how='inner', on='종목명')
merge.columns = ['종목', '기관', '외국인']

# print(merge)
'''

# 다운로드 된 파일 삭제
#  os.remove(f) for f in glob.glob("~/Downloads/*.csv")