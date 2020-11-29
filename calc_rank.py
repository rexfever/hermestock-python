# 데이터 파일 읽기 KOSPI 기관, KOSPI 외인, KOSDAQ 기관, KOSDAQ 외인
data_ki = pd.read_csv("./data.csv", thousands=',')
data_fo = pd.read_csv("./data (1).csv", thousands=',')

data_ki = data_ki[["종목명", "순매수거래량"]]
data_ki.astype({'순매수거래량': 'int32'}).dtypes
data_ki = data_ki.sort_values('순매수거래량', ascending=False)
data_ki.set_option('colheader_justify', 'right')
print(data_ki)

data_fo = data_fo[["종목명", "순매수거래량"]]
data_fo.astype({'순매수거래량': 'int32'}).dtypes
data_fo = data_fo.sort_values('순매수거래량', ascending=False)

'''
(1) pandas DataFrame의 칼럼 이름 바꾸기
    :  df.columns = ['a', 'b']
    :  df.rename(columns = {'old_nm' : 'new_nm'), inplace = True)
'''

merge = pd.merge(data_ki.head(10), data_fo.head(10), how='inner', on='종목명')
merge.columns = ['코스피', '기관', '외국인']

print(merge)

# 다운로드 된 파일 삭제
[os.remove(f) for f in glob.glob("/Users/rexsmac/Downloads/*.csv")]


