# 08 객체와 클래스
# 변수와 함수를 한꺼번에 다를 수 있는 객체 (Object) 와 클래스(Class)

# 08 - 01 / 클래스 선언과 객체 생성
# A ) 객체 (Object) 란?
# 프로그래밍 언어에서 객체를 만들 떄는 주로 현실 세계를 반영해서 만든다. 
# 객체는 속성(상태,특징)과 행위(행동,동작,기능)로 구성된 대상을 의미한다. | 객체 = 변수 + 함수
# '변수' - 객체의 특징인 속성
# '함수' - 객체가 할 수 있는 일인 행동

# 객체지향 프로그래밍 ( Object - Oriented Programming , OOP ) - 객체를 만들고 이용할 수 있는 기능을 제공하는 프로그래밍 언어

# B ) 클래스 (Class) 선언
# 객체의 공통된 속성과 행위를 변수와 함수로 정의하는데 우선적으로 클래스 선언을 해야한다.
# 즉, 클래스는 객체를 만들기 위한 기본 틀이고, 객체는 기본틀을 바탕으로 만들어진 결과이다.

# 클래스 선언을 위한 기본 구조
'''
class 클래스명():
    [변수1] # 클래스 변수
    [변수2]
    ...
    def 함수1(self[, 인자1, 인자2, ... , 인자n]): # 클래스 함수 / # self는 객체 생성 후에 자신을 참조하는데 이용
        <코드 블록>
        ...
    def 함수2(self[, 인자1, 인자2, ... , 인자n]):
        <코드 블록>
        ...
'''

# C ) 자전거 예시를 통한 객체 생성 및 활용
# 자전거의 속성 : 바퀴 크키 (Wheel_size) , 색상 (Color)
# 자전거의 동작 : 지정된 속도로 이동(move), 좌/우회전(turn), 정지(stop)

class Bicycle(): # 클래스 선언
    pass

# 선언 된 클래스로부터 클래스의 객체를 생성하는 방법
my_bicycle = Bicycle()

my_bicycle # 객체 실행 시 객체의 클래스와 객체를 생성할 때 할당 받은 메모리의 주솟값을 출력
'Out: <__main__.Bicycle object at 0x00000211A66CEBD0>' 

# 객체에 속성을 설정하는 방법
' 객체명.변수명 = 속성값 '
my_bicycle.wheel_size = 26
my_bicycle.color = 'black'

# 객체의 변수에 접근해서 속성을 가져오는 방법
print("바퀴크기:", my_bicycle.wheel_size)
print("자전거 색상:", my_bicycle.color)

# Bicycle 클래스에 함수 추가
class Bicycle():

    def move(self, speed): # 지정된 속도로 이동 함수
        print("자전거: 시속 {0}킬로미터로 전진".format(speed))
    
    def turn(self, direction): # 좌/ 우 방향 전환 동작 함수
        print("자전거: {0} 회전".format(direction))

    def stop(self): # 정지 동작 함수
        print("자전거({0}, {1}) : 정지".format(self.wheel_size, self.color))

# 메서드 호출 방법
' 객체명.메서드명([인자1,인자2,...,인자n])' 
# 메서드명은 클래스에서 정의한 함수명 
# 메서드를 호출할 때 인자는 클래스에서 정의한 함수의 인자만큼 필요

my_bicycle = Bicycle() # Bicycle 클래스의 인스턴스인 my_bicycle 객체 생성

my_bicycle.wheel_size = 26 # 객체의 속성1 설정
my_bicycle.color = 'black' # 객체의 속성2 설정

my_bicycle.move(30) # 객체의 메서드 호출
my_bicycle.turn('좌')
my_bicycle.stop()

# 1개의 클래스를 만들면 객체는 필요한 만큼 얼마든지 만들 수 있다.

my_bicycle2 = Bicycle()

my_bicycle2.wheel_size = 28 
my_bicycle2.color = 'red'

my_bicycle2.move(18)
my_bicycle2.turn('우')
my_bicycle2.stop()

# D ) 객체 초기화
# 초기화 함수 : __init_()를 구현하면 객체를 생성하는 것과 동시에 속성값을 지정할 수 있다.
# __init__ 함수는 클래스의 객체가 생성될 때 자동으로 실행되기 때문에 함수에 초기화하려는 인자를 정의하면 객체를 생성할 때 속성 초기화 가능 

# Bicycle 클래스에서 __init__()함수를 추가한 코드
class tuning_Bicycle():

    def __init__(self,wheel_size,color):
        self.wheel_size = wheel_size
        self.color = color
    
    def move(self,speed):
        print("자전거: 시속 {0}km로 전진".format(speed))

    def turn(self,direction):
        print("자전거: {0} 회전".format(direction))

    def stop(self):
        print("자전거 ({0},{1}): 정지".format(self.wheel_size,self.color))

my_bicycle3 = tuning_Bicycle(18,'blue')

my_bicycle3.move(30)
my_bicycle3.turn("좌")
my_bicycle3.stop()