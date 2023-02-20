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
class Bicycle():

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

#08 - 02 ) 클래스를 구성하는 변수와 함수

# A ) 클래스에서 사용하는 변수
# 클래스에서 사용하는 변수는 위치에 따라 클래스 변수( Class Variable ) 과 인스턴스 변수 (Instance Variable)로 구분 된다.
# 클래스 변수 = 클래스 내에 있지만 함수 밖에서 '변수명 = 데이터' 형식으로 정의한 변수 / 클래스에서 생성한 모든 객체가 고통으로 사용 가능
# 인스턴스 변수 = 클래스 내의 함수 안에서 'self.변수명 = 데이터' 형식으로 정의한 변수 / 클래스 내의 모든 함수에서 'self.변수명'으로 접근 가능

# 클래스 변수와 인스턴스 변수를 사용한 자동차 클래스 예

class Car():
    instance_count = 0 # 클래스 변수 생성 및 초기화

    def __init__(self, size, color):
        self.size = size # 인스턴스 변수 생성 및 초기화
        self.color = color # 인스턴스 변수 생성 및 초기화
        Car.instance_count += 1 # 클래스 변수 이용
        print("자동차 객체의 수 :{0}".format(Car.instance_count))

    def move(self):
        print("자동차 {0} & {1}가 움직입니다.".format(self.size,self.color))

# 사용 방법
car1 = Car('small','white')
car2 = Car('Big','black')

print("Car 클래스의 총 객체 개수 : {}".format(Car.instance_count))

car1.move()
car2.move()

# 이름이 같은 클래스 변수와 인스턴스 변수가 있는 경우의 예
class Car2():
    count = 0 # 클래스 변수 생성 및 초기화

    def __init__(self, size, num):
        self.size = size #인스턴스 변수 생성 및 초기화
        self.count = num   #인스턴스 변수 생성 및 초기화
        Car2.count += 1  #클래스 변수 이용
        print("자동차 객채의 수: Car.count = {0}".format(Car2.count))
        print("인스턴수 변수 초기화 : self.count {0}".format(self.count))

    def move(self):
        print("자동차 {0} & {1}가 움직입니다.".format(self.size,self.count))

car1 = Car2("Big",20)
car2 = Car2("Small",30)

car2.move()
car1.move()


# B ) 인스턴스 메서드
# 인서턴스 메서드는 각 객체에서 개별적으로 동작하는 함수를 만들고자할 때 사용 하는 함수
# 인스턴스 메서드는 함수 정의 시 첫 인자로 self가 필요로 한다. ( self는 클래스의 인스턴스(객체) 자신을 가리킨다.)

'''
기본 구조
class 클래스명():
    def 함수명(self[, 인자1,인자2, ... 인자n]):
        self.변수명1 = 인자1
        self.변수명2 = 인자2
        self.변수명3 = 인자3
        ...
        self.변수명n = 인자n
        <코드 블록>
'''

# 인스턴스 메서드는 다음과 같이 객체 생성 후 호출이 가능하다.
'''
객체명 = 클래스명()
객체명.메서드명([인자1,인자2,인자3,...,인자n])
'''

# 인스턴스 메서드를 사용한 자동차 클래스 예시

class Car():
    instance_count = 0 # 클래스 변수 생성 및 초기화 

    # 초기화 함수
    def __init__(self, size, color):
        self.size = size # 인스턴스 변수 생성 및 초기화
        self.color = color # 인스턴스 변수2 생성 및 고히ㅘ
        Car.instance_count += 1 # 클래스 변수 이용
        print("자동차 객체의 수 : {0}".format(Car.instance_count))

    # 인스턴스 메서드
    def move(self, speed):
        self.speed = speed # 인스턴스 변수 생성
        print("자동차({0} & {1})가 ".format(self.size, self.color), end='')
        print("시속 {0}km 전진".format(self.speed))

    # 인스턴스 메서드
    def auto_cruise(self):
        print("자율주행모드")
        self.move(self.speed) # move() 함수의 인자로 인스턴스 변수를 입력

# 인스턴스 메서드 실행을 위해 객체 생성 후 move()와 auto_cruise() 메서드를 호출

car1 = Car("Small","red") # 객체 생성 (Car1)
car2 = Car("Big","green") # 객체 생성 (car2)

car1.move(80)  # 객체(car1)의 move()메서드 호출
car2.move(100) # 객체(car2)의 move()메서드 호출

car1.auto_cruise() # 객체(car1)의 auto_cruise() 메서드 호출
car2.auto_cruise() # 객체(car2)의 auto_cruise() 메서드 호출

# C ) 정적 메서드
# 클래스의 객체와는 무관하게 독립적으로 동작하는 함수를 만들고 싶을떄 이용하는 함수 ( 주로 날짜 및 시간 정보 제공 , 환율 정보 제공, 단위 변환에 사용 )
# self를 사용하지 않으며 정적 메서드 안에서는 인스턴스 메서드나 인스턴스 변수에 접근 불가능
# 함수 앞에 데코레이터(Decorator)인 @staticmethod를 선언하여 정적 메서드임을 표시
'''
class 클래스명():
    @staticmethod
    def 함수명([인자1,인자2,인자3,...,인자n]):
        <코드 블록>
'''    

# 객체 생성 후 클래스명을 이용해 바로 메서드 호출
'''
클래스명.메서드명([인자1,인자2,인자3,...,인자n]):
'''

# 앞서 만든 코드에 정적 메서드 check_type() 추가
class Car():
    instance_count = 0 # 클래스 변수 생성 및 초기화 

    # 초기화 함수
    def __init__(self, size, color):
        self.size = size # 인스턴스 변수 생성 및 초기화
        self.color = color # 인스턴스 변수2 생성 및 고히ㅘ
        Car.instance_count += 1 # 클래스 변수 이용
        print("자동차 객체의 수 : {0}".format(Car.instance_count))

    # 인스턴스 메서드
    def move(self, speed):
        self.speed = speed # 인스턴스 변수 생성
        print("자동차({0} & {1})가 ".format(self.size, self.color), end='')
        print("시속 {0}km 전진".format(self.speed))

    # 인스턴스 메서드
    def auto_cruise(self):
        print("자율주행모드")
        self.move(self.speed) # move() 함수의 인자로 인스턴스 변수를 입력

# 정적 메서드
    @staticmethod
    def check_type(model_code):
        if(model_code >=20):
            print("이 자동차는 전기차입니다.")
        elif(10<=model_code< 20):
            print("이 자동차는 가솔린차입니다.")
        else:
            print("이 자동차는 디젤차입니다.")

# 정적 메서드 호출
Car.check_type(25)
Car.check_type(5)    

# 클래스 메서드
# 클래스 변수를 사용하기 위한 함수 | 클래스 메서드를 사용하기 위해서는 함수 앞에 데코레이터(Decorator)인 @classmethod를 지정해야한다.
# 클래스 전체에서 관리해야 할 기능이 있을 때 주로 이용

'''
class 클래스명():
    @classmethod
    def 함수명(cls[,인자1,인자2,...,인자n]):
        <코드 블록>
'''
# 호출 방법
'''
클래스명.메서드명([인자1,인자2,...,인자n]):
'''

# 기존 메서드에 클래스 메서드인 count_instance()를 추가
# 앞서 만든 코드에 정적 메서드 check_type() 추가

class Car():
    instance_count = 0 # 클래스 변수 생성 및 초기화 

    # 초기화 함수
    def __init__(self, size, color):
        self.size = size # 인스턴스 변수 생성 및 초기화
        self.color = color # 인스턴스 변수2 생성 및 고히ㅘ
        Car.instance_count += 1 # 클래스 변수 이용
        print("자동차 객체의 수 : {0}".format(Car.instance_count))

    # 인스턴스 메서드
    def move(self, speed):
        self.speed = speed # 인스턴스 변수 생성
        print("자동차({0} & {1})가 ".format(self.size, self.color), end='')
        print("시속 {0}km 전진".format(self.speed))

    # 인스턴스 메서드
    def auto_cruise(self):
        print("자율주행모드")
        self.move(self.speed) # move() 함수의 인자로 인스턴스 변수를 입력

# 정적 메서드
    @staticmethod
    def check_type(model_code):
        if(model_code >=20):
            print("이 자동차는 전기차입니다.")
        elif(10<=model_code< 20):
            print("이 자동차는 가솔린차입니다.")
        else:
            print("이 자동차는 디젤차입니다.")

# 클래스 메서드
    @classmethod
    def count_instance(cls):
        print("자동차 객체의 개수: {0}".format(cls.instance_count))

# 클래스 메서드 호출 방법 

Car.count_instance() # 객체 생성 전에 클래스 메서드 호출
car1 = Car('small','red') # 첫 번쨰 객체 생성
Car.count_instance()      # 클래스 메서드 호출

car2 = Car("Big","Green") # 두 번쨰 객체 생성
Car.count_instance()      # 클래스 메서드 호출

'Out 결과값을 보면 알 수 있뜻이 클래스 변수 instance_count의 값이 1씩 증가하는 걸 확인할 수 있다.'

# 08 - 03 객체와 클래스를 사용하는 이유
# 코드 작성과 관리가 편하기 떄문에 사용
# 규모가 큰 ㅍ로그램을 만들 때는 클래스와 객체를 많이 이용
# 게임의 캐릭터와 같이 유사한 객체가 많은 프록램을 만들 때도 주로 클래스와 객체를 이용해 코드를 작성

# 클래스와 객체를 사용하지 않고 코드 작성
robot_name = 'R1' # 로봇 이름
robot_pos  =  0   # 로봇의 초기 위치

def robot_move():
    global robot_pos
    robot_pos +=1
    print("{0} position: {1}".format(robot_name,robot_pos))

robot_move()

# 개선 코드
class Robot():
    def __init__(self, name, pos):
        self.name = name # 로봇 객체의 이름
        self.pos = pos   # 로봇 객체의 위치

    def move(self):
        self.pos +=1
        print("{0} position: {1}".format(self.name,self.pos))

# 객체 생성 및 메서드 실행
robot1 = Robot('R1',0)
robot2 = Robot("R2",10)

robot1.move()
robot2.move()

# 클래스 선언 이후 로봇이 필요할 때마다 로봇 객체만 생성하면 된다.

# 08 - 04 / 클래스 상속
# 이미 만들어진 클래스의 변수와 함수를 그대로 이어 받고 새로운 내용만 추가해서 클래스를 선언할 수 있다.
# 객체 지향 프로그래밍에서는 이어받기를 상속이라고 지칭함

# 부모 클래스에서 상속받는 자식 클래스를 선언하는 형식
'''
class 자식 클래스(부모 클래스 이름):
    <코드 블록>
'''
# 부모 클래스에서 정의한 함수와 자식 클래스의 정의한 함수 이름이 같은 경우 부모 클래스의 함수를 호출하는 방법
' 부모 클래스 이름.함수명()  혹은  super.함수명()' #을 사용해야 하는데 초기화 함수 __init__()에서 많이 사용

# 앞서 선언한 자전거 클래스를 상속하여 접는 자전거 클래스인 FoldingBicycle 생성
class FoldingBicycle(Bicycle):

    def __init__(self, wheel_size, color, state): # FoldingBicycle 초기화
        Bicycle.__init__(self,wheel_size,color)   # Bycicle의 초기화 재사용
        # super.__init__(wheel_size,color) 로도 대체 가능
        self.state = state # 자식 클래스에서 새로 추가한 변수

    def fold(self):
        self.state = 'folding'
        print("자전거: 접기, state = {0}".format(self.state))

    def unfold(self):
        self.state = 'Unfolding'
        print("자전거: 펴기, state = {0}".format(self.state))

# 상속 메서드 호출
foldingBicycle = FoldingBicycle(27, 'white','unfolding') # 객체 생성

foldingBicycle.move(20) #부모 클래스의 메서드 호출
foldingBicycle.fold()   #자식 클래스의 메서드 호출
foldingBicycle.unfold()

# 상속 메서드 관련 정리
# 기존에 생성된 클래스의 변수와 함수를 이용할 수 있으므로 코드의 재사용성이 좋아진다.
# 만약 유사한 클래스를 여러개 만들어야 할 경우 공통 부분은 부모 클래스로 구현하여 기획하고 상속하는 자식 클래스를 구현한다면 좀 더 간편하게 코드 구현이 가능
