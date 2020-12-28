import downloader as dl
from time import sleep
import calc_rank as cr
import os
import glob
import getpass



KOSPI_fileList = ['data.csv', 'data (1).csv']
KOSDAQ_fileList = ['data (2).csv', 'data (3).csv']


dl._set_date()
dl._select_market()
sleep(15)

print(cr._merge_data_set(cr._extract_data_set(KOSPI_fileList[0]), cr._extract_data_set(KOSPI_fileList[1])))
print(cr._merge_data_set(cr._extract_data_set(KOSDAQ_fileList[0]), cr._extract_data_set(KOSDAQ_fileList[1])))
dl.close_window()

[os.remove(f) for f in glob.glob("/Users/"+getpass.getuser()+"/Downloads/*.csv")]

