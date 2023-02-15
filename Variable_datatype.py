# 변수와 자료형
# 변수 : 자료를 넣을 수 있는 상자로 컴퓨터의 임시 저장 공간(메모리)에 저장
# 변수 설정 규칙
# 1. 변수명은 문자, 숫자, 밑줄기호(_)를 이용해 사용
# 2. 숫자로 시작하는 변수명 생성 불가 
# 3. 대소문자 구분
# 4. 공백을 포함할 수 없음 ( 밑줄기호 '_' 를 이용)
# 5. 밑줄 기호 이외에는 다른 기호 사용 불가
# 6. 예약어는 변수명으로 할당 불가 ( None, True, False, and 등 )

# 01 변수 ( Variable ) 
abc = 12340
print(abc)

print(abc* 1/2)
print(abc* 1/4)
print(abc* 1/5)

# 02 문자열 ( String Type )
# 문자열을 표시하기 위해서는 시작과 끝에 " " 혹은 ' ' 를 지정

print("String test")
print('String test')

# 문자열을 변수에 저장한 후 print() 함수로 출력
string1 = "String Test 1"
string2 = 'String Test 2'
print(string1)
print(string2)
type(string1)
type(string2)

# 문자열에 큰따옴표나 작은따옴표도 포함하기
string3 = 'This is a "double" quotation test'
string4 = "THis is a 'double' quotation test"
print(string3)
print(string4)

# 문자열에 큰따옴표와 작은따옴표를 모두 포함하고 있을 경우
long_string1 = '''[삼중 작은따옴표를 사용한 예]
파이썬에서는 삼중 따옴표로 여러 행의 문자 입력 가능
큰따옴표(")와 작은따옴표(')도 입력 가능'''
long_string2 = """[삼중 큰따옴표를 사용한 예]
파이썬에서는 삼중 따옴표로 여러행의 문자 입력 가능
큰따옴표(")와 작은따옴표(')도 입력 가능"""
print(long_string1)
print(long_string2)

# 문자열 다루기
a = 'Enjoy '
b = 'python!'
c = a + b
print(c)
print(a * 3)

# 03 리스트 ( List )
# 리스트 만들기 : 리스트 대괄호([])를 이용해서 만듬
# 리스트에서 각 항목은 '변수명[i]'로 저장되고 시작 숫자는 0부터 임
# 변수명[0] = 90 / 변수명[1] = 95 / 변수명[2] = 80 / 변수명[3] = 85
# 변수명[-1] = 85 ( 역순으로도 저장이 가능하다 )
student_score = [90,95,80,85]
student_score
type(student_score)
student_score[0]
student_score[1]
student_score[2]
student_score[-1]

# 리스트내 특정 항목을 변경하는 방법 : 변수 설정하듯이 해당 인덱스를 지정하여 변경
student_score[1] = 100
student_score

# 리스트에는 다양한 type를 혼합하여 저장도 가능하다. (* 리스트 내 리스트도 할당 가능 )
myFriends = ['Bryan','Lisa','Mary']
sample = [0,2,3.14,'python','program',True,False,myFriends]
sample

# 리스트 다루기
# 리스트 더하기
list_con1 = [1,2,3,4]
list_con2 = [5,6,7,8]
list_con = list_con1 + list_con2 # 리스트 연결
print(list_con)

# 리스트 곱하기
print(list_con1 * 3) # 리스트 반복

# 리스트 중 일부 가져오기 - Slicing
list_data = [0,1,2,3,4,5,6,7,8,9]
print(list_data)
print(list_data[0:3])
print(list_data[4:8])
print(list_data[:3])
print(list_data[7:])
print(list_data[::2])

# 리스트에서 항목 삭제하기
print(list_data)
del list_data[6]
print(list_data)

# 리스트에서 항목의 존재 여부 확인하기
list_data1 = [1,2,3,4,5]
print(5 in list_data1) # 리스트 내 '5'가 존재하므로 True 출력
print(99 in list_data1) # 리스트 내 '99' 가 존재하지 않으므로 False 출력

# 리스트 메서드 활용
# append() | 리스트에서 항목 하나를 맨 마지막에 추가 
print(myFriends)
myFriends.append('John')
print(myFriends)

# insert() | 리스트에서 원하는 위치에 데이터를 삽입
print(myFriends)
myFriends.insert(0,'Jenny')
print(myFriends)

# extend() | 리스트에서 항목 여러개를 맨 마지막에 추가
print(myFriends)
myFriends.extend(['Laura','Betty'])
print(myFriends)

# sort() | 숫자나 문자열로 구성된 리스트 항목을 순방향으로 정렬
print(myFriends)
myFriends.sort()
print(myFriends)

# reverse() | 숫자나 문자열로 구성된 리스트 항목을 역방향으로 정렬
print(myFriends)
myFriends.reverse()
print(myFriends)

# 04 튜플
# 리스트와 유사하게 데이터 여러개를 하나로 묶는데 사용한다. 하지만 튜플로 지정 된 자료는 항목을 변경할 수 없다.
tuple1 = (1,2,3,4)
tuple2 = 1,2,3,4

# 인자 하나만 있는 상태로 튜플 생성
tuple3 = 9, # 반드시 콤마(,) 필요
tuple4 = (10,) # 반드시 콤마(,) 필요

# 튜플 메서드
tuple6 = ('a','b','c','d','e','f')
tuple6.index('e') # 'e'와 일치하는 튜플의 위치는 다섯번째 이므로 4를 반환  (N-1)

tuple7 = ('a','a','a','b','b','c','d')
tuple7.count('a') # tuple7 내 'a'의 개수를 반환 ( 3 )

# 05 세트
# 튜플과 유사한 데이터 타입으로 수학의 집합 개념을 파이썬에서 이용할 수 있도록 만든 데이터  * 교집합 / 합집합 / 차집합을 구하는 메서드 사용 가능 *
# 튜플과 다른점 : 1. 데이터의 순서가 없음 2. 데이터를 중복해서 쓸 수 없음 
set1 = {1,2,3}
print(set1,type(set1))

# 세트의 교집합, 합집합, 차집합 구하기
A = {1,2,3,4,5,6,7,8}   # Set A
B = {4,5,6,7,8,9,10}    # Set B
# 세트의 교집합
A.intersection(B)
A & B               # 코드로 사용
# 세트의 합집합
A.union(B) # 세트는 중복해서 쓸 수 없으므로 {1,2,3,4,5,6,7,8,9,10} 을 출력
A | B               # 코드로 사용
# 세트의 차집합
A.difference(B) # A와 B에서 중복되는 숫자는 제거하고 {1,2,3} 출력
A-B                 # 코드로 사용

# 리스트, 튜플, 세트 간 타입 변환
a = [1,2,3,4,5]
b = (1,2,3)
c = set(a)
print(c,type(c)) # list인 a를 set 형태로 변환
d = tuple(a)
print(d,type(d)) # list인 a를 tuple 형태로 변환
e = list(c)
print(e,type(e)) # set 형태인 c를 list 형태로 변환

# 06 딕셔너리
# 딕셔너리는 사전과 유사하게 구성돼 있음. 표제어(Key)와 설명(Value)로 지정하여 쌍으로 구성 * 딕셔너리는 인덱스 대신 키를 이용해 값을 다룸 *

# 딕셔너리 만들기
country_capital = {'영국':'런던','프랑스':'파리','한국':'서울','호주':'멜버른'}
print(country_capital,type(country_capital))

country_capital['영국']

# 딕셔너리 다루기
# 딕셔너리에 데이터 추가하고 변경하기
country_capital['독일']='베를린'
country_capital['호주']='캔버라'
country_capital
# 딕셔너리에서 데이터 삭제하기
del country_capital['호주'] # 키 값을 지정하여 데이터 삭제
country_capital

# 딕셔너리 메서드 활용
# keys() | 딕셔너리에서 keys 전체를 '리스트' 형태로 변환
country_capital.keys()
# values() | 딕셔너리에서 values 전체를 '리스트' 형태로 변환
country_capital.values()
#items() | 딕셔너리에서 키와 값의 쌍을 (key,value)처럼 튜플 형태로 변환
country_capital.items()
#update() | 딕셔너리에 데이터('dict_dat2') 추가
country_capital2 = {'호주':'캔버라'}
country_capital.update(country_capital2)
country_capital
#clear() | 딕셔너리에 데이터 전체 삭제
country_capital2
country_capital2.clear()
country_capital2
