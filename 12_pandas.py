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

# 12 - 03 ) 데이터를 원하는 대로 선택하기
KTX_data = {'경부선 KTX':[39060, 39896, 42005, 43621,41702,41266,32427],
            '호남선 KTX':[7313,6967,6873,6626,8675,10622,9228],
            '경전선 KTX':[3627,4168,4088,4424,4606,4984,5570],
            '전라선 KTX':[309,1771,1954,2244,3146,3945,5766],
            '동해선 KTX':[np.nan,np.nan,np.nan,np.nan,2395,3786,6667]}
col_list=['경부선 KTX','호남선 KTX','경전선 KTX','전라선 KTX','동해선 KTX']
index_list = ['2011','2012','2013','2014','2015','2016','2017']

df_KTX= pd.DataFrame(KTX_data,columns=col_list,index=index_list)
df_KTX

df_KTX.index
df_KTX.columns
df_KTX.values

# 데이터 중 일부만 보면서 분석 후 코드를 작성하면 편리
df_KTX.head() # df.head(n) - 컬럼명 + 상위 순서 5개 인덱스(default value) 확인 | n에 숫자 입력시 원하는 만큼 확인 가능
df_KTX.tail() # df.tail(n) - 컬럼명 + 하위 순서 5개 인덱스(default value) 확인 | 상동

# DataFrame 데이터 내 연속 구간 행 데이터를 선택하는 방법
'''
DataFrame_data[행_시작위치:행_끝위치]
'''
df_KTX[1:2]
df_KTX[2:5]

# DataFrame 데이터 생성 시 index를 지정시 행을 선택도 가능
'''
DataFrame_data.loc[index_name]
'''
df_KTX.loc['2011']

# DataFrame 데이터에서 index 항목 이름으로 구간을 지정해서 연속된 구간의 행을 선택도 가능하다
'''
DataFrame_data.loc[start_index_name:end_index_name]
'''
df_KTX.loc['2013':'2016']

# DataFrmae 하나의 열만을 서낵하려면 다음과 같이 하나의 columns 항목 이름을 지정
df_KTX['경부선 KTX']

# DataFrame 열 선택 후 index 범위 지정 후 데이터 확인
df_KTX['경부선 KTX']['2012':'2014']
df_KTX['경부선 KTX'][2:5]

# DataFrame 데이터 중 하나의 원소만 선택하는 방법
df_KTX.loc['2016']['호남선 KTX']
df_KTX.loc['2016','호남선 KTX']
df_KTX['호남선 KTX']['2016']
df_KTX['호남선 KTX'][5]
df_KTX['호남선 KTX'].loc['2016']

# DataFrame의 전치 구하는 방법
df_KTX.T
# DataFrame 데이터 변수 df_KTX 열 항목 지정 후 열의 순서 변경
df_KTX[col_list]

# 12 - 03 ) 데이터 통합하기
# A ) 세로 방향으로 통합하기
'''
DataFrame_data1.append(DataFrame_data2 [,ignore_index=True])
세로 방향으로 DataFrame_data1에 data2가 추가돼서 DataFrame데이터로 반환 
ignore_index=True 미 입력시 DataFrame 데이터에는 기존의 데이터 index가 그대로 유지
'''

df1 = pd.DataFrame({'Class1':[95,92,98,100],
                    'Class2':[91,93,97,99]})
df2 = pd.DataFrame({'Class1':[87,89],
                    'Class2':[85,90]})
df1.append(df2, ignore_index=True) # append 후 index를 순차적으로 증가하게 하려면 파라미터를 부여

df3 = pd.DataFrame({'Class1':[96,83]})
df2.append(df3, ignore_index=True) # 열이 비어있는 경우 Nan으로 채워짐

# B ) 가로 방향으로 통합하기
'''
DataFrame_data1.join(DataFrame_data2)
'''

df4 = pd.DataFrame({'Class3':[93,91,95,98]})
df1.join(df4)

# index 라벨 지정 된 DataFrame의 경우에도 index가 같으면 Join()을 이용해 데이터 추가 가능
index_label=['a','b','c','d']
df1a = pd.DataFrame({'Class1':[95,92,98,100],
                     'Class2':[91,93,97,99]}, index=index_label)
df4a = pd.DataFrame({'Class3':[93,91,95,97]}, index=index_label)
df1a.join(df4a)

# C ) 특정 열을 기준으로 통합하기
'''
DataFrame_left_data.merge(DataFrame_right_data)
'''
df_A_B = pd.DataFrame({'판매월':['1월','2월','3월','4월'],
                       '제품A':[100,150,200,130],
                       '제품B':[90,110,140,170]})
df_C_D = pd.DataFrame({'판매월':['1월','2월','3월','4월'],
                       '제품C':[112,141,203,134],
                       '제품D':[90,110,140,170]})
df_A_B.merge(df_C_D) # 두 데이터 프레임에 모두 있는 것이 '판매월'인 열 데이터이므로 이를 중심으로 데이터를 통합 시 사용

# 두개의 DataFrame 데이터가 특정 열을 기준으로 일부만 공통된 값을 갖는 경우에 통합하려면 merge() 선택 인자를 지정하면 됨
'''
DataFrame_left_data.merge(DataFrame_right_data, how=merge_method, on=key_label)
'''
''''
how 선택 인자    설명
left           왼쪽 데이터는 모두 선택하고 지정된 열(key)에 값이 있는 오른쪽 데이터를 선택
right          오른쪽 데이터는 모두 선택하고 지정된 열(key)에 값이 있는 왼쪽 데이터를 선택
outer          지정된 열(key)을 기준으로 왼쪽과 오른쪽 데이터를 모두 선택
inner          지정된 열(key)을 기준으로 왼쪽과 오른쪽 데이터 중 공통 항목만 선택(기본값)
'''
df_left = pd.DataFrame({'key':['A','B','C'], 'left':[1,2,3]})
df_right = pd.DataFrame({'key':['A','B','D'], 'right':[4,5,6]})
df_left.merge(df_right, how='left',on='key')
df_left.merge(df_right, how='right',on='key')
df_left.merge(df_right, how='outer',on='key')
df_left.merge(df_right, how='inner', on='key')

# 12 - 03 ) 데이터 파일을 읽고 쓰기
# A ) 표 형식의 데이터 파일을 읽기
# read_csv()
'''
DataFrame_data = pd.read_csv(file_name [, options])
'''

# B ) 표 형식의 데이터를 파일로 쓰기
# to_csv()
'''
DataFrame_data.to_csv(file_name, [, options])
'''
df_WH = pd.DataFrame({'Weight':[62,67,55,74],
                      'Height':[165,177,160,180]},
                      index=['ID_1','ID_2','ID_3','ID_4'])
bmi = round(df_WH['Weight']/(df_WH['Height']/100)**2,1)
df_WH['BMI'] = bmi
df_WH.to_csv(r'C:\Users\hwan\Desktop\study\01.Python Tutorial\Python_Tutorial\myPycode\DataFrame.csv')

df_pr = pd.DataFrame({'판매가격':[2000,3000,5000,10000],
                      '판매량':[32,53,40,25]},
                      index=['P1001','P1002','P1003','P1004'])
df_pr.index.name='제품번호'
file_name = 'C:\Users\hwan\Desktop\study\01.Python Tutorial\Python_Tutorial\myPycode\DataFrame_cp949.csv'
df_pr.to_csv(file_name, sep="", encoding='cp949')