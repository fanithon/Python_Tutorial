# 12 / 구조적 데이터 표시와 처리에 강한 Pandas
# 12 - 01 ) 구조적 데이터 생성하기
# A ) Series를 활용한 데이터 생성
import pandas as pd

# Series()를 이용한 SEries 형식의 데이터 생성 방법
'''
s = pd.Series(seq_data)
'''

s1 = pd.Series([10,20,30,40,50])
s1 # 출력시 data ([10,20,30,40,50]) 앞에 index가 함께 표시

# Series 데이터는 index와 values를 분리해서 가져올 수 있음
# Series 데이터를 s라고 할떄 index는 's.index' / values는 's.values'로 가져올 수 있다.
s1.index # 행의 시작 과 끝을 출력
s1.values # 데이터를 출력 = 출력결과가 Numpy와 동일

s2 = pd.Series(['a','b','c',1,2,3])
s2

# 데이터가 없는 경우 Numpy를 import한 후 np.nan으로 데이터가 없다고 표현 가능
import numpy as np
s3 = pd.Series([np.nan,10,30])  # np.nan을 통해 index=0의 데이터가 없음을 표현 = 데이터를 위한 자리(index)는 있지만 데이터가 없다.
s3 

# Series 데이터를 생성할 때 인자로 index 추가하는 방법
index_date = ['2018-10-17','2018-10-18','2018-10-09','2018-10-10']
s4 = pd.Series([200,195,np.nan,205],index = index_date) # index를 변수에 대입 후 index에 숫자가 아닌 지정 데이터로 대입
s4

# 딕셔너리를 이용한 데이터와 index 입력
s5 = pd.Series({'국어':100,'영어':80,'수학':95})
s5

# B) 날짜 자동 생성 : date_range
'''
pd.date_range(start=None, end=None, periods=None, feeq="D")
'''

pd.date_range(start='2023-02-01',end='2023-02-28') # 날짜 데이터의 형식은 모두 yyyy-mm-dd로 출력

pd.date_range(start='2023-02-01', periods=28) # 날짜 지정하지 않고 periods 파라미터로 날짜 생성 가능

pd.date_range(start='2023-01-01', periods=4,freq='2D') # 2일씩 증가하는 4개의 날짜 생성
pd.date_range(start='2023-01-01',periods=4,freq='W') # 1주일 단위 증가하는 4개의 날짜 생성
pd.date_range(start='2023-01-01',periods=12,freq='2BM') # 2개월 월말 주기로 12개의 날짜를 생성
pd.date_range(start='2023-01-01',periods=4,freq='QS') # 분기 시작일을 기준으로 4개의 날짜 생성
pd.date_range(start='2023-01-01',periods=3,freq='AS') # 첫날을 기준으로 1년 주기로 3개의 날짜 생성

# date_range()를 통한 시간 생성
pd.date_range(start='2023-01-01 01:00', periods=10, freq='H') # 기준 시간부터 1시간 주기로 10개의 시간 생성
pd.date_range(start='2023-01-02 08:00', periods=10, freq='BH') # 업무 시간을 기준으로 1시간 주기로 10개의 시간 생성
pd.date_range(start='2023-01-02 08:00', periods=4, freq='30min') # 30분 단위로 4개의 시간 생성
pd.date_range(start='2023-01-02 08:00', periods=4, freq='30T') # 30분 단위로 4개의 시간 생성 / 위와 동일하나 min을 T로 대체 가능하고 출력 또한 'T'로 된다.
pd.date_range(start='2023-01-01 10:00:00', periods=4, freq='10S') # 10초단위로 4개의 시간 생성

index_date = pd.date_range(start='2023-01-01',periods=4,freq='M')
flowershop_income = pd.Series([100,180,300,480],index=index_date)
flowershop_income

# C) DataFrame을 활용한 데이터 생성
'''
df = pd.DataFrame(data[, index = index_data, columns=columns_data])
'''

pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])

# Numpy의 배열 데이터를 입력해 생성한 DataFrame
data_list = np.array([[10,20,30],[40,50,60],[70,80,90]])
pd.DataFrame(data_list)

# index와 columns 지정
data =([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
index_date = pd.date_range('2023-01-01',periods=4)
column_list = ['A','B','C']
df = pd.DataFrame(data=data,index=index_date,columns=column_list)
df

# 딕셔너리타입의 데이터로 DataFrame 생성하기
table_data = {'연도':[2019,2020,2021,2022],
              '고객유치수':[1000,3000,13000,20000],
              '매출액':[10000000,50000000,120000000,200000000]}
pd.DataFrame(table_data)

df = pd.DataFrame(table_data, columns=['연도','고객유치수','매출액'])
df.index
df.columns
df.values

# 12 - 02 ) 데이터 연산
table_data3 = {'봄':[256.5,264.3,215.9,223.2,312.9],
               '여름':[770.6,567.5,599.8,387.1,446.2],
               '가을':[363.5,231.2,293.1,247.7,381.6],
               '겨울':[139.3,59.9,76.9,109.1,108.1]}
column_list = ['봄','여름','가을','겨울']
index_list = ['2012','2013','2014','2015','2016']

df3 = pd.DataFrame(data=table_data3,columns=column_list,index=index_list)
df3.describe()

df3
df3.mean() # columns를 기준으로 평균값 출력 ( 기본값 / axis=0 )
df3.mean(axis=1) # index를 기준으로 평균값을 출력