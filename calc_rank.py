import glob
import os
import pandas as pd

'''
1.csv 파일 읽기
2.종목명, 순매수거래량 추출
3.종목명으로 정렬하기
4.기관 연기금 데이터프레임 합치기

'''
# 데이터 파일 읽기 KOSPI 기관, KOSPI 외인, KOSDAQ 기관, KOSDAQ 외인
filePath = '/Users/rexsmac/Downloads/'
#fileList = ['data.csv', 'data (1).csv', 'data (2).csv', 'data (3).csv', 'data (4).csv', 'data (5).csv']
fileList = ['data.csv', 'data (1).csv']
data_ki = pd.read_csv("/Users/rexsmac/Downloads/data.csv", thousands=',')
data_ye = pd.read_csv("/Users/rexsmac/Downloads/data (1).csv", thousands=',')
data_fo = pd.read_csv("/Users/rexsmac/Downloads/data (1).csv", thousands=',')


data_ki = data_ki[["종목명", "순매수거래대금"]]
data_ki.astype({'순매수거래대금': 'int32'}).dtypes
data_ki = data_ki.sort_values('종목명', ascending=False)
data_ki = data_ki.sort_values('순매수거래대금', ascending=False)
print(data_ki)

data_ye = data_ye[["종목명", "순매수거래대금"]]
data_ye.astype({'순매수거래대금': 'int32'}).dtypes
data_ye = data_ye.sort_values("종목명", ascending=False)

merge = pd.merge(data_ki, data_ye, how='inner', on='종목명')
merge['순매수거래대금'] = merge['순매수거래대금_x'] + merge['순매수거래대금_y']
merge = merge.sort_values('순매수거래대금', ascending=False)
merge = merge[["종목명", "순매수거래대금"]]
#print(merge)


'''
        dataset = pd.merge(data_ki.head(10), data_fo.head(10), how='inner', on='종목명')
        tmp = tmp.sort_values('순매수거래대금', ascending=False)


def _read_csv():

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

# 다운로드 된 파일 삭제
# [os.remove(f) for f in glob.glob("/Users/rexsmac/Downloads/*.csv")]
'''