# 01 간단한 사칙 연산

# 덧셈
print(1+1)

# 뺼셈
print(5-2)

# 곱셈
print(15*2)

# 나눗셈 - 파이썬에서 나눗셈 연산은 실수로 처리
# 정수 - 자연수(1,2,3, - )와 자연수의 음수, 그리고 0으로 이루어진 집합
# 실수 - 유리수와 무리수로 이뤄진 집합
print(10/2)

# 실수 연산
print(1.2+5.3)
print(3.5 - 5.0)
print(1.4*2)
print(5/2)

# 복합 연산
print(2+3*4)
print(3/2*4-5/2)
print(10/5+(5-2)*2)
print((5*4-15) + ((5-2)*(9-7)))

# * 함수 
# type() - 자료의 형식을 알려주는 함수
type(3)
type(1.5)

# 02 거듭제곱과 나머지
# 거듭제곱
print(2*2*2*2*2) # 정수의 제곱
print(1.5*1.5)  # 실수의 제곱도 가능

# 쉬운 표현
print(2**5)
print(1.5**2)

# 제곱근 계산 
print(2**(1/2)) # 2의 제곱근

# 나머지 계산
print( 13 % 5 )

# 몫 계산
print( 13 //5 )

# 03 과학적 표기법
print(3 * 10 ** 8) # 정수로 출력
print(3e8) # 위의 쉬운 표현
print(1 * 10**-4) 
print(1e-4) # 위의 쉬운 표현
a = 3 * 10 ** 8
b = 3e8 
print(a, type(a)) # 변수 설정시 실수로 출력
print(b, type(b)) # 변수 설정시 정수로 출력

# 출력 숫자에 들어간 0의 개수에 따라 출력 여부 다름
print(1e16) # 과학적 표기법
print(1e-5) # 과학적 표기법

# 05 논리 연산 및 비교 연산
print(True,type(True))
print(False,type(False))

# 논리연산자
'and' 'A and B' 'A와 B 모두 참일 떄만 참이고, 나머지는 거짓'
'or' 'A or B' 'A와 B 중 하나라도 참이면 참이고, 둘 다 거짓이면 거짓'
'not' 'not A' 'A가 참이면 거짓이고, 거짓이면 참'

print(True and True) # 참
print(True and False) # 거짓
print(True or False) #참
print(not True) # 반대

# 비교연산자
'==' '같다' "a==b / a와 b는 같다"
'!=' '같지않다' "a!=b / a와 b는 같지 않다"
'<' '작다' "a<b / a는 b보다 작다"
'>' '크다' "a>b / a는 b보다 크다"
'<=' '작거나 같다' "a>=b / a는 b보다 작거나 같다"
'>=' '크거나 같다' "a<=b / a는 b보다 크거나 같다"

print(5==3)
print(5!=3)
print(5<3)
print(5>3)
print(5<=3)
print(5>=3)