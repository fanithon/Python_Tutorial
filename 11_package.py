# 11 데이터 분석을 위한 패키지
# 11 - 01 배열 데이터를 효과적으로 다루는 NumPy
# A ) 배열 생성하기
import numpy as np

# B ) 시퀀스 데이터로부터 배열 생성
'''
arr_obj = np.array(seq_data)
'''

# 리스트로부터 NumPy의 1차원 배열을 생성하는 예
data1 = [0,1,2,3,4,5]
a1 = np.array(data1)
a1
a1.dtype

# 정수와 실수가 혼합된 리스트 데이터로 numpy 배열 생성
data2 = [0.1,5,4,12,.5]  # 실수가 혼합 되어있을 떄엔 모두 실수로 변환
a2 = np.array(data2)
a2
a2.dtype

# seq_data 부분에 직접 리스트를 넣어 배열 객체 생성
np.array([0.5,2,.01,8])

# 다차원 배열 생성 ( 2차원 )
np.array([[1,2,3],[4,5,6],[7,8,9]])

# C ) 범위를 지정해 배열 생성
'''
arr_obj = np.arange([start,],stop[, step])
'''
np.arange(0,10,2)
np.arange(1,10)
np.arange(5) # start가 0인 경우 start 생략 가능

# 배열의 형태를 확인하는 방법
b1 = np.arange(12).reshape(4,3) # ndarray.shape
b1.shape

b2 = np.arange(5)
b2.shape
# 행렬 변형
np.arange(12).reshape(4,3)

# 범위의 시작과 끝을 지정하고 데이터의 개수를 지정해 Numpy 배열을 생성
# linspace()
'''
arr_obj = np.linspace(start, stop[, num])
'''

# 1부터 10까지의 10개 데이터 생성
np.linspace(1,10,10)

# 0부터 pi까지 동일한 간격으로 나눈 20개의 데이터 생성
np.linspace(0,np.pi,20) # np.pi는 Numpy 에서 파이를 입력할 때 이용

# D ) 특별한 형태의 배열 생성
'''
arr_zero_n = np.zeros(n)
arr_zero_mxn = np.zeros((m,n))
arr_one_n = np.ones(n)
arr_one_mxn = np.ones((m,n))
'''

# zero()함수로 원소의 개수가 10개(n=10)인 1차원 배열 생성
np.zeros(10)

# zero()를 이용해 3 X 4 의 2차원 배열 생성
np.zeros((3,4))

# ones()로 1차원 배열과 2차원 배열 생성
np.ones(5) # 1차원 배열
np.ones((3,4)) # 2차원 배열

# 단위행렬 (Identity matrix) 생성방법
# n X n 인 정사각형 행렬에서 주 대각선이 모두 1이가 나머지는 0인 행렬을 의미
'''
arr_I = np.eye(n) 
'''
np.eye(3)

# 5) 배열의 데이터 타입 변환
# 원소인 Numpy배열을 생성
np.array(['1.5','0.62','2','3.14','3.141592'])
# Numpy 배열의 형 변환 - astype()
'''
num_arr = str_arr.astype(dtype)
'''

str_ar1 = np.array(['1.567','0.123','5.123','9','8'])
num_a1 = str_ar1.astype(float)
num_a1

str_ar1.dtype
num_a1.dtype

# 6) 난수 배열의 생성
'''
rand_num = np.random.rand([d0, d1, ..., dn])
rand_unm = np.random.randint([low,] high[,size])
'''
# Numpy 난수 생성 예시
np.random.rand(2,3)
np.random.rand()
np.random.rand(2,3,4)

# 지정 범위 정수 난수 배열
np.random.randint(10,size=(3,4)) # 0 ~ 10 사이의 난수를 3 X 4 배열로 출력
np.random.randint(1,30) # 1~ 30 사이의 난수 출력

# 7 ) 배열의 연산
# 7 -1 ) 기본연산
arr1 = np.arange(10,50,10)
arr2 = np.arange(1,5,1)

arr1 + arr2
arr1 - arr2
arr1 * arr2
arr1 / arr2
arr2 * 2
arr2 ** 2
arr1 / (arr2**2)
arr1 > 20

# 7 -2 ) 통계를 위한 연산
arr3 = np.arange(5)

[arr3.sum(), arr3.mean()] # arr3의 합과 평균
[arr3.std(), arr3.var()] # arr3의 표준편차와 분산
[arr3.min(), arr3.max()] # arr3의 최솟값과 최댓값

arr4 = np.arange(1,5)
arr4.cumsum() # arr4의 누적합
arr4.cumprod() # arr4의 누적 곱

# 7 -3 ) 행렬 연산
# 선형 대수( Linear algebra ) 를 위한 행렬(2차원 배열) 연산도 지원
'''
행렬 연산                   | 사용 예
행렬곱(Matrix product)      | A.dot(B) / np.dot(A,B)
전치행렬(transpose Matrix)  | A.transpose() / np.transpose(A)
역행렬(inverse Matrix)      | np.linalg.inv(A)
행렬식(determinant)         | np.linalg.det(A)
'''
A = np.arange(0,4).reshape(2,2)
B = np.array([3,2,0,1]).reshape(2,2)
A.dot(B) # 행렬곱
np.dot(A,B) 
np.transpose(A) # 전치행렬 ( 행열 변환 )
A.transpose()
np.linalg.inv(A) # 역행렬
np.linalg.det(A) # 행렬식

# 7-4 ) 배열의 인덱싱과 슬라이싱
# A ) 배열의 인덱싱
a1 = np.arange(0,60,10)
a1[0]
a1[4]
a1[5] = 70 # 원소 변경도 가능
a1 

# 1차원 배열 인덱싱
a1[[1,3,4]]

# 2차원 배열
a2 = np.arange(10,100,10).reshape(3,3)
a2

a2[0,2]
a2[2,2] = 95 # 2 * 2 에 위치한 값 변경 
a2[1] # 1에 위치한 행 출력

# 2차원 배열의 여러 원소를 선택하는 방법
'''
배열명[[행위치1,행위치2,...,행위치n],[열위치1,열위치2,...,열위치n]]
'''
a2[[0,2],[0,1]] # a2배열의 (0,0) 위치 값인 10과 (2,1)의 값인 80을 출력

# 조건에 맞는 배열을 선택하는 방법
a = np.arange(1,7,1)
a[a>3] # 3보다 큰 a의 값을 출력
a[(a%2)==0] # 짝수인 값만 출력

#  B ) 배열의 슬라이싱

b1 = np.arange(0,60,10)
b1[1:4]
b1[:3]
b1[2:]
b1[2:5] = np.array([25,35,45])
b1[3:6] = 77
b1

# 2차원 배열의 슬라이싱
b2 = np.arange(10,100,10).reshape(3,3)
b2[1:3,1:3]
b2[:3,1:]
b2[1][0:2]
b2[0:2,1:3] = np.array([[25,35],[55,65]])