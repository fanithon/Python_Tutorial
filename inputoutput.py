# 입력과 출력
# 01 화면 출력

# 파이썬에서는 print() 함수를 이용해 원하는 내용을 화면으로 출력할 수 있다.
# print() 
# 1. 출력형식을 지정하지 않는 기본 출력 방법
# 2. 다양한 형식으로 출력할 수 있는 형식 지정 출력 방법

# 01 - 1 / 기본 출력
# 문자열과 숫자를 출력하는 방법

print("Hello Python!") # print() 함수 안에 문자 및 숫자열 입력

# 문자열을 여러개 출력 하는 방법
print("Best","Python","book")

# 문자열 사이 구분 값을 설정하는 방법  (sep 인자 지정)
print("Best","Python","book",sep="-:*:-")

# 빈칸 없이 문자열을 연결하는 방법
print('abcd'+'efg')

# 문자열 연결 시 콤마(,)와 더하기 연산자 사용 방법
print("Best","Python","Book" +" :","This Book")

# 변수 저장 내용 출력 방법
x = 10
print(x)

# 주의 사항 : 문자열과 숫자는 더하기 연산자로 출력 불가
name = "James"
ID_num = 789
print("Name:", name + ",", "ID number:", ID_num)

# 여러줄로 출력하는 방법 개행문자"\n" 사용
print("James is my friend. \nHe is Korean.")

# 두 줄로 출력된 결과를 한 줄로 출력하는 방법 ( end 인자 지정 )
print("Welcome to ",end="")
print("Python!")

# 01 - 2 / 형식 지정 출력
# 나머지 연산자 (%) 를 이용한 형식 및 위치 지정
'''
print("%type" % data)
'''
# 문자열 - % s / 정수 - %d / 실수 - %f (실수의 경우 기본적으로 소수점 6자리까지 출력)
# data가 두 개 이상일 경우 data의 개수에 맞게 '%type' 순서대로 입력하고 튜플 형식으로 묶어서 사용
'''
print("%type %type" % (data1,data2))
'''

# %s를 이용해 문자열 출력
name = '민희'
print('%s는 나의 친구 입니다.' % name)

# %d 와 %f 를 이용한 정수/실수 출력
r = 3 # 변수 r에 정수 3을 할당
PI = 3.14159265358979 # 변수 PI에 실수 할당
print('반지름: %d, 원주율: %f' % (r,PI)) # 지정된 위치에 데이터 출력

# 01 - 3 / 형식 지정 문자열에서 출력 위치 지정
'''
print("{0} {1} {2} … {n}".format(data_0,data_1, … ,data_n))
'''
animal0 = 'cat'
animal1 = 'dog'
animal2 = 'fox'
print("Animal: {0},{1},{2}".format(animal0,animal1,animal2))
print("Animal: {},{},{}".format(animal0,animal1,animal2))

# 정수 실수 출력 위치 지정
name = "Bryan"
age = 11
a = 0.12312413545
fmt_string = "String: {}, Integer Number: {}, Floating Number:{}"
print(fmt_string.format(name,age,a))

# 01 - 4 / 형식 지정 문자열에서 숫자 출력 형식 지정
a = 0.120310598305
print("{0:.2f},{0:.5f}".format(a)) # 0:.2f - 2번째 소수점 / 0:5f - 5번째 소수점

# 숫자의 출력 형식 지정
'''
데이터(x)   출력형식    출력결과    설명
3           {N:2d}      3         정수를 공백 포함해 두 자리로 표시
3           {N:05d}     00003     정수를 다섯 자리로 표시, 앞의 공백은 0으로 채움
0.12345     {N.3f}      0.123     실수를 소수점 셋째 자리까지 표시
1000000     {N:,}       1,000,000 통화 표시처럼 천단위에 콤마(,) 표시
0.77777     {N:.1%}     77.7%     소수를 퍼센트(%)로 표시. %표시에서 소수점 자리수는 '.' 다음 숫자로 표시
'''

# 02 키보드 입력 - input() 함수
'''
data = input("String")
'''
# input으로 입력받은 '문자열'데이터 print() 함수로 출력 방법
Yourname = input()
print('당신의 이름은 {} 입니다.'.format(Yourname))

# input으로 입력받은 '정수' 데이터 print() 함수로 출력 방법
a = input()
area = int(a) **2
print('정사각형의 넓이: {}'.format(area))

# input으로 입력받은 '실수' 데이터 print() 함수로 출력 방법
b = input() 
area_b = float(b) **2
print("정사각형의 넓이: {}".format(area_b))

# 03 파일 읽고 쓰기
# 03 - 1 / 파일 열기 : 파이썬 내장 함수 open() 함수 사용
'''
f = open('file_name','mode')
'''
'''
*  파일 열기의 속성 *
mode  |  의미
r     | 읽기 모드로 파일 열기(default값)
w     | 쓰기 모드로 파일 열기, 같은 이름의 파일이 있으면 기존 내용 모두 삭제
x     | 쓰기 모드로 파일 열기, 같은 이름의 파일이 있을 경우 오류 발생
a     | 추가 모드로 파일 열기, 같은 이름의 파일이 없으면 w와 동일 기능
b     | 바이너리 파일 모드로 파일 열기
t     | 텍스트 파일 모드로 파일 열기(기본), 지정하지 않으면 기본적으로 텍스트 모드로 지정
'''
# mode는 혼합해서 사용 가능 
# f = open('file_name',rt) : 읽기모드이면서 텍스트 모드로 파일 열기

# 03 - 2 / 파일 쓰기
'''
f = open('file_name','w')
f.write(str)
f.close()
'''

