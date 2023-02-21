# 10 모듈
# 10 - 04 / 내장 모듈

# A ) 난수 발생 모듈
'''
import random
random.random모듈함수()
'''

import random
random.random() # 0~1 사이의 실수 중에서 임의의 숫자를 생성
'''
random 모듈의 함수      설명                                        사용 예
random()              0.0 <= 실수 <1.0 범위의 임의의 실수를 반환     random.random()
randint(a,b)          a <= 정수 <= b 범위의 임의의 정수 반환         random.randit(1,6)
randrange([start, ]   range([start,] stop[,step])에서의 임의의      random.randrange(0,10,2)
stop[step,]))         정수를 반환
choice(seq)           공백이 아닌 시퀀스(seq)에서 임의의 항목 반환    random.choice([1,2,3])
sample(population,k)  시퀀스로 이뤄진 모집단(population)에서 중복되지 random.sample([1,2,3,4,5],2)
                      않는 k개의 인자를 반환
'''

dice1 = random.randint(1,6) #임의의 정수가 생성
dice2 = random.randint(1,6) #임의의 정수가 생성
print('두개의 주사위 숫자: {0}, {1}'.format(dice1,dice2))

random.randrange(0,11,2) # 0부터 10까지 임의의 짝수를 발생 시키는 코드

num1 = random.randrange(1, 10, 2) # (1 ~ 9) 중 임의의 홀수 선택
num2 = random.randrange(0,100,10) # (0 ~ 99) 중 임의의 10단위 숫자 선택
print('num1 : {0}, num2 : {1}'.format(num1,num2))

menu = ['탕수육','짜장면','닭갈비','돈가스','제육볶음']
random.choice(menu)

random.sample([1,2,3,4,5],2) #모집단(population) list에서 2개의 임의 숫자 선택

# B ) 날짜 및 시간 관련 처리 모듈
# datetime() : 날짜와 시간을 다룰 수 있는 파이썬 내장 모듈
# date클래스 - 날짜를 표현 / time클래스 - 시간을 표현 / datetime클래스 - 날짜와 시간을 표현

# date 클래스

import datetime

set_day = datetime.datetime(2023,2,22)
print(set_day)

print('{0}/{1}/{2}'.format(set_day.year,set_day.month,set_day.day))

# datetime 모듈의 date 객체는 타입이 date로 객체끼리 연산을 할 수 있다.
day1 = datetime.datetime(2022,9,1)
day2 = datetime.datetime(2023,2,22)
diff_day = day2-day1
print(diff_day,type(day1),type(diff_day))

# 오늘 날짜를 반환하는 클래스 메서드 today()
print(datetime.date.today())

today = datetime.date.today()
special_day = datetime.date(2022,9,1)
print(special_day - today)

# time  클래스
set_time = datetime.time(15,30,45)
print(set_time)

print('{0}:{1}:{2}'.format(set_time.hour,set_time.minute,set_time.second))

# 날짜와 시간을 모두 다룰 수 있는 datetime 클래스
set_dt = datetime.datetime(2022,2,22,00,58,55)
print(set_dt)

print("날짜: {0}/{1}/{2}".format(set_dt.year,set_dt.month,set_dt.day))
print("시간: {0}:{1}:{2}".format(set_dt.hour,set_dt.minute,set_dt.second))

now = datetime.datetime.now() # 현재 시각을 구하는 방법
print(now)

print("Date & Time : {:%Y-%m-%d, %H:%M:%S}".format(now))

from datetime import date, time, datetime

print(date(2023,2,22))

print(time(15,30,45))

print(datetime(2023,2,22,1,3,15))

print(datetime.now())

# C ) 달력 생성 및 처리 모듈
# calender() : 다양한 형태로 달력을 생성하고 출력

import calendar
print(calendar.calendar(2022))

print(calendar.calendar(2022,m=4)) # 달의 출력 양식을 변경하고 싶을 땐 'm=숫자' 파라미터를 추가

print(calendar.month(2022,1)) # 지정연도의 특정 월만 표시하려면 다음과 같이 month()함수를 이용

calendar.monthrange(2022,2) # 그달 1일이 시작하는 요일과 그달의 날짜 수를 알고 싶을 떄 monthrange() 사용 
'Out: (1,28) - 화요일이 시작하는 요일이고 총 28일이다.'

calendar.firstweekday() # 달력에서의 일주일의 시작 요일을 구하려면 사용하는 함수

calendar.setfirstweekday(calendar.SUNDAY) # 달력의 시작일을 월요일에서 일요일로 변경
print(calendar.month(2023,2)) # 셋팅 값 출력 ( '일요일'부터 시작되는 캘린더 반환)

#isleap(year) : 어떤 연도가 윤년인지 확인하는 메서드
print(calendar.isleap(2020)) # 'Out : True - 2020년은 윤년이다.'
print(calendar.isleap(2022)) # 'Out : False - 2022년은 윤년이 아니다.'

