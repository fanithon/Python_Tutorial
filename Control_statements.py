#제어문

# 01 조건에 따라 분기하는 if문
# 01 - 1 / 단일 조건에 따른 분기 (if) 
# if문을 이용해 변수 x의 값이 90보다 크거나 같으면 'pass'를 출력
x = 95
if x >=95:
    print('pass')

# 01 - 2 / 단일 조건 및 그 외 조건에 따른 분기 ( if ~ else )
# 변수 x의 데이터가 90보다 크거나 같으면 'pass'를 출력 90보다 작으면 'fail' 출력
x = 75
if x >= 90:
    print('pass')
else:
    print('fail')

# 01 - 3 / 여러 조건에 따른 분기 ( if ~ elif ~ else )
# x >= 90 = 'Very good' / x>= 80 = "Good" / x < 80 = "Bad"
x = 85
if x >= 90:
    print('Very good')
elif 80 <= x < 90:
    print("Good")
else:
    print('Bad')

# 01 - 4 / 중첩 조건에 따른 분기
x = 89
if x >= 90: # 조건문 1
    if x == 100: # 조건문 1-1 
        print('Perfect')
    else:
        print('Very Good')
elif 80 <= x < 90: # 조건문 2
    print('Good')
else:
    print('Bad')

# 02 지정된 범위만큼 반복하는 for문
# 02 - 1 / 반복문의 필요성 : 동일 코드 반복없이 효율적 코드 작성 가능

# 02 - 2 / for문의 구조
# 반복 범위가 끝나지 않을 때 까지 코드블록을 반복 실행
# for < 반복 변수> in < 반복 범위 >:
#   <코드블록>

# 02 -3 / 반복 범위 지정
# 리스트 이용 01
for a in [0,1,2,3,4,5]:
    print(a)
# 리스트 이용 02
myFriends = ['James','Robert','Lisa','Mary']
for BF in myFriends:
    print(BF)

# range() 함수 이용 | range(start,stop,step)
print(range(0,10,1))
print(list(range(1,11,1))) # 리스트 변환하여 자료구조 생성

for a in range(1,11,1): # for문을 사용한 <반복범위> 지정
    print(a)

# 02 - 3 / 중첩 for문
# for <반복 변수1> in <반복 범위1>: 반복 범위1[0] 출력
#   for <반복 변수2> in <반복 범위2>: 반복 범위2 모두 출력 후 반복변수1 재실행 
#   <코드 블록>
x = ['x1','x2']
y = ['y1','y2']

print('x y')
for X in x:
    for Y in y:
        print(X,Y)

# 02 - 4 / 여러 개의 리스트 다루기
names = ['James','Robert','Lisa','Mary']
scores = [95,96,97,94]
for j in range(len(names)):
    print(names[j],scores[j])

# zip함수를 활용 코드 예시
# zip함수 : 같은 길이위 데이터를 하나로 묶어주는 함수
for name, score in zip(names,scores):
    print(name,score)

# 03 조건에 따라 반복하는 while문
# 03 -1 / while 문의 구조
''' while <조건문>:   <조건문>을 만족하면 <코드블록> 계속 수행
    <코드블록>        <조건문>을 불만족시 while문 탈출
'''

# while문 예시
' 자연수 1부터 순차적으로 더해서 출력하다가 합이 20보다 크면 멈춰'
i = 0
sum = 0
print(i,sum)

while (sum<20):   # 조건 검사
    i = i+1       # i를 1씩 증가
    sum = sum + i # 이전의 sum과 현재 i를 더해서 sum을 갱신
    print(i,sum)  # i와 sum을 출력 / 조건이 넘을 경우 최종 값 출력

# 무한 반복 while문
'''
while True:
    print('while test')
'''

# 04 반복문을 제어하는 break와 continue
# 04 -1 / 반복문을 빠져나오는 break
# 반복문 (for / while 동일 ) 안에서 break 만날 시 탈출
# while문에서 break로 탈출 
k=0
while True:
    k += 1
    if k > 3:
        break
    print(k)
# for문에서 break로 탈출
for k in range(10):
    if k>2:
        break
    print(k)

# 04 -2 / 다음 반복을 실행하는 continue
# continue : 반복문의 "처음" 으로 돌아가서 다음 반복을 진행
for k in range(5):
    if k==2:
        continue
    print(k)

# while문에서 break와 continue 혼용
k = 0
while True:
    k +=1
    if k==2:
        print('continue next')
        continue
    if k>4:
        break
    print(k)
# 05 간단하게 반복하는 한 줄 for문
# comprehension : list/set/dict 내 실행 가능한 한 줄 for문 지원

# 05 - 1 / list comprehension basic model
'''
[<반복 실행문> for <반복 변수> in <반복 범위>]
'''
num = [1,2,3,4,5]
square = []
for i in num:
    square.append(i**2)
print(square)

# 숏코딩 작성법
num = [1,2,3,4,5]
square = [i**2 for i in num]
print(square)

# 조건문을 포함한 리스트 컴프리헨션
'''
[<반복 실행문> for <반복 변수> in <반복 범위> if <조건문>]
'''
square = []
for i in num:
    if i>=3:
        square.append(i**2)
print(square)

# 숏코딩 작성법
num=[1,2,3,4,5]
square=[i**2 for i in num if i>=3]
print(square)

