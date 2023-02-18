# 07 함수
# 함수(function) : 특정 기능을 수행하는 코드의 묶음
# 이점 1. 같은 기능을 수행하는 코드를 반복해서 작성할 필요가 없어짐
# 이점 2. 코드가 깔끔해지고 한번 만든 코드를 재사용할 수 있어서 코드를 작성하기가 편해짐

# 07 - 1 - a / 함수 정의와 호출
'''
  입력    > 기능(연산) >    출력
input = x > funtion() > output = y
'''
# 07 - 2 - b / 함수의 기본 구조
'''
함수의 기본 구조
def 함수명([인자1,인자2, . . . , 인자n]):
    <코드 블록>
    [return <반환값>]
'''
# 인자도 반환 값도 없는 함수
def my_func():
    print("Myfirstfunction!")

my_func()

# 인자는 있으나 반환 값이 없는 함수
# 예시 1 )
def my_friend(friendname):
    print("{}는 나의 친구입니다.".format(friendname))

my_friend("철수")

# 예시 2)
def student_info(name,school_id,hp_num):
    print('-'*50)
    print('-학생이름 :', name)
    print('-학급번호 :',school_id)
    print('-핸드폰번호 :',hp_num)

student_info('현아','14','010-1234-5678')
student_info('철수','18','010-9873-9283')

# 인자도 있고 반환 값도 있는 함수
# 예시 1 ) 
def my_calc(x,y):
    z = x*y
    return z

my_calc(99,3)

# 예시 2 ) 리스트,세트,튜플,딕셔너리로도 사용 가능
def student_info(student_info1):
    print("*"*55)
    print('* 이름 :',student_info1[0])
    print("* 학급번호 :", student_info1[1])
    print("* 핸드폰번호 ", student_info1[2])
    print("*"*55)

student_info1 = ['영희','7','010-7777-7777']
student_info(student_info1)

# 07 - 2 / 변수(variable) 의 유효 범위 (scope)
# 변수 ( Variable )
# 전역 변수 ( Global Variable ) : 함수 밖에서 정의한 변수는 코드 내 어디서나 사용 가능
# 지역 변수 ( Local Variable ) : 함수 안에서 정의한 변수는 함수 안에서만 사용 가능

# 유효 범위 ( Scope )
' 스코핑 룰 ( Scoping_rule ) / LGB 룰 ( Local/Global/Built_in Rule) : 어떤 변수를 호출하면 지역 > 전역 > 내장 영역 순서대로 변수가 있는지 확인' 
# 지역 영역 ( Local Scope ) : 지역 변수를 저장하는 이름 공간
# 전역 영역 ( Global Scope ) : 전역 변수를 저장하는 이름 공간
# 내장 영역 ( Built-in Scope ) : 파이썬 자체에서 정의한 이름 공간

# 예시 ) 
a = 5 # 전역 변수
def func_1():
    a = 1
    print('[func1] 지역변수 a =',a)

def func_2():
    a = 2
    print('[func2] 지역변수 a =',a)

def func_3():
    print('[func3] 전역변수 a =',a)

def func_4():
    global a # 전역 변수 사용
    a = 4    # 전역 변수 값 변경
    print("[func4] 전역 변수 a =",a)

func_1() # 지역 변수 출력
func_2() # 지역 변수 출력
func_3() # 전역 변수 출력 ( 초기값 5 )
func_4() # 전역 변수 값 재지정하여 변경 된 전역 변수로 출력 ( 출력값 : 4 )

# 07 - 03 / 람다(lambda) 함수
# 구성이 단순해 간단한 연산을 하는데 종종 사용
'''
lambda <인자> : <인자 활용 수행 코드>
<인자> 전달시 <인자 활용 수행 코드> 수행 후 결과 바로 반환 / <인자> = 콤마(,)로 구분해 여러개 사용 가능

(lambda <인자> : <인자 활용 수행 코드>) (<인자>)

lambda_function = lambda <인자> : <인자 활용 수행 코드>
lambda_function(<인자>)
'''
# 기본 코드 예시)
(lambda x : x**2) (3)

# 람다함수 반복 사용 방법 ( 변수에 할당 )
mySquare = lambda x : x**2
mySquare(11)

# 여러개의 인자를 입력받아 연산 결과를 출력하는 람다함수
mySimpleFunc = lambda x,y,z : 2*x + 3*y + z
mySimpleFunc(1,1,2)

# 07 - 04 / 유용한 내장 함수
# 07 - 04 - a / 형 변환 함수
# int() - 정수로 변환
[int(0.123),int(3.3423434),int(-1.91203),int('2334'),int('-98309')]
# float() - 실수로 변환
[float(0),float(123),float(-339)]
# str() - 문자형으로 변환
[str(123),str(-339),str(-0.3449),str(1.344)]

# 리스트 , 튜플 , 세트형으로 변환
# list() - 튜플/세트를 리스트로 변환
# tuple() - 리스트/세트를 튜플로 변환
# set() - 리스트/튜플을 세트로 변환
list_data = ['abc',1,2,'def']
tuple_data = 'abc',1,2,'def'
set_data = {'abc',1,2,'def'}

[type(list_data),type(tuple_data),type(set_data)]
# 튜플을 리스트로 변환하고, 형태 확인
print(list(tuple_data),type(list(tuple_data)))
# 리스트를 튜플로 변환하고, 형태 확인
print(tuple(list_data),type(tuple(list_data)))

# bool 함수
# True - ( 양의 정수, 음의 정수, 양의 실수, 음의 실수, 문자 등 값이 있는 모든 경우 ) True 반환
# False - ( 0 , None, Null ) 값이 없는 경우 모두 False 반환

# 활용 방법
def print_name(name):
    if bool(name):
        print("입력된 이름:",name)
    else:
        print("이름을 입력하시오")

print_name('영희')
print_name("")

# 최솟값과 최댓값을 구하는 함수
# 최솟값 - min()
# 최댓값 - max()

my_num = [1,2,4,4,5,5,55,13,4,24,13,241,24]
min(my_num)  # 최솟값 1 출력
max(my_num)  # 최댓값 241 출력

my_Str = 'iuhojaokz' # 문자열에 대해서도 최솟값 최댓값 구할 수 있음
[min(my_Str),max(my_Str)]

# 참고사항 - 로마자 알파벳의 경우 A ~ Z , a ~ z 순서대로 크기가 큼
my_str = ['Abc','abc','bcd','efg']
[min(my_str),max(my_str)]

# 절댓값과 전체 합을 구하는 함수
# abs(): 절댓값  - 양수/음수를 구분하지 않는 절댓값 출력
# sum(): 전체 합
[abs(10),abs(-10)]

sumlist=[1,2,3,4,5,6,7,8,9,10]
sum(sumlist)

# 항목의 개수를 구하는 함수
# len() : 항목의 개수를 구하는 함수
len("ab cd") # 문자열의 개수 출력 ( 출력 값 : 5 )
len([1,2,3,4,5,6,7,8,8,9]) # 리스트 내 개수를 출력 ( 출력 값 : 10 ) * 리스트 / 튜풀 / 세트 / 딕셔너리 동일

# 내장 함수의 활용
scores = [90,80,85,90] #과목 별 시험 점수

score_sum = 0 # 총점 계산을 위한 변수 초깃값 설정
subject_num = 0 # 과목 수 계산을 위한 초깃 값 설정
for score in scores:
    score_sum += score # 과목 별 점수 전체 합산
    subject_num += 1 # 과목 수 계산

average = score_sum / subject_num # 평균( 총점 / 과목 수 ) 구하기
print('총점: {0}, 평균: {1}'.format(score_sum,average))