# 09 문자열과 텍스트 파일 데이터 다루기
# 09 - 01 / 문자열 다루기
# A ) 문자열 분리하기
# split() - 문자열을 나누고 싶을 때 사용하는 메서드
'''
str.split([sep]) # sep의 경우 꼭 입력하지 않아도 됨
'''

# 예시
cofee_menu_str = '에스프레소,아메리카노,카페라테,카푸치노'
cofee_menu_str.split(",")

'에스프레소,아메리카노,카페라테,카푸치노'.split(",") # 문자열을 변수 할당 없이 나누는 방법
'에스프레소 아메리카노 카페라테 카푸치노'.split()    # 공백 구분자를 갖고 있는 문자열을 나누는 방법

# 문자열 분리 시 maxsplit 인자를 추가 시 원하는 횟수만큼 문자열을 분리할 수 있다.
'''
str.split([sep,]maxsplit=숫자)
'''
# 예시
'에스프레소 아메리카노 카페라테 카푸치노'.split(maxsplit=2)
# 인자로 지정한 maxsplit=2 로 인해 앞에서부터 2개의 공백(sep)까지만 문자열을 나눠 결과적으로 3개의 항목이 담긴 리스트를 반환

# 예시 2 
phone_number = "+82-01-234-6789"        # 국가 번호가 포함된 전화번호
split_num = phone_number.split("-", 1)  # 국가 번호와 나머지 번호 분리

print(split_num)
print("국내전화번호 : {0}".format(split_num[1]))

# B ) 필요없는 문자열 삭제하기
# strip() - 문자열에서 앞뒤 공백 혹은 개행문자와 같이 불피요한 부분을 지워야할 떄 사용
# 문자열(str)의 앞 뒤에서 시작해서 지정한 문자(chars)외 다른 문자를 만날 때까지 지정 문자를 모두 삭제한 문자열을 반환
# 지정 문자가 없는 경우 문자열 그대로 반환 / 지정 문자가 여러 개일 경우 순서 상관없음
'''
str.strip([chars])
'''

# 예시
'aaaaPythonaaaa'.strip('a')

test_str = 'aaaabbbPythonbbbaaa'
temp1 = test_str.strip('a')
print(temp1)
temp1.strip('b')

test_str.strip('ab') # 필요없는 지정문자 한번에 제거 1
test_str.strip('ba') # 필요없는 지정문자 한번에 제거 2

test_str_multi = '###*!!!!...Python is powerful.!...##*!!'
test_str_multi.strip('#*!.')

'aaaaBallaaaa'.strip('a') # strip 메서드는 문자열 앞뒤에서 지정문자 외 다른 문자를 만날 떄 까지만 지정한 문자를 삭제하기 때문에 'Ball'의 'a'는 삭제되지 않는다.

str_lr = "000Python is easy to learn.000"
print(str_lr.strip('0'))   # 지정 문자 전체 삭제
print(str_lr.lstrip('0'))  # 왼쪽의 지정 문자 삭제
print(str_lr.rstrip('0'))  # 오른쪽이 지정 문자 삭제

# 리스트 내 모든 항목에 공백을 제거 하기 위한 코드 구현
coffee_menu = "  에스프레소,아메리카노,  카페라테    ,카푸치노  "
coffee_menu_list = coffee_menu.split(',')
coffee_menu_list

coffee_list = [] # 빈 리스트 생성
for coffe in coffee_menu_list:
    temp = coffe.strip() # 문자열의 공백 제거
    coffee_list.append(temp)
print(coffee_list)

# C ) 문자열 연결하기
# Join() = 문자열을 항목으로 갖는 시퀀스(seq)의 항목 사이에 구분자 문자열(str)을 모두 넣은 후 문자열을 반환
'''
str.join(seq)
'''

# 예시
address_list = ['서울시','서초구','반포대로','201(반포동)']
address_list

a = " "
a.join(address_list)
" ".join(address_list)   # 변수 지정하지 않고도 사용 가능
"//".join(address_list) # 구분자 문자열 (//)로 연결해서 문자열 변환

# D ) 문자열 찾기
# find() - 문자열에서 원하는 단어를 찾을 떄 사용할 수 있는 메서드
'''
str.find(search_str) # 문자열은 0부터 시작하며 / 문자열을 찾을 수 없으면 -1 을 반환한다. 
'''

str_f = 'Python Code.'
print("찾는 문자열이 위치", str_f.find('Python'))
print("찾는 문자열이 위치", str_f.find('Code'))
print("찾는 문자열이 위치", str_f.find('n'))
print("찾는 문자열이 위치", str_f.find('easy'))

'''
str.find(search_str, start, end) # 시작 위치와 끝 위치를 추가로 지정하여 검색 가능
str.find(search_str, start)      # 시작 위치만 지정해서 검색 번위를 설정도 가능 
'''

str_f_se = 'Python is powerful. Python is easy to learn'

print(str_f_se.find("Python", 10, 30)) # 시작 위치와 끝 위치 지정
print(str_f_se.find("Python", 35))     # 찾기 위한 시작 위치 지정

# count() - 문자열이 몇번 나오는지 확인 하는 메서드
'''
str.count(search_str)
str.count(search_str,start,end)
str.count(search_str,start)
'''
str_c = "Python is powerful. Python is easy to learn. Python is open"

print("Python의 개수는?",str_c.count("Python"))
print("poweful의 개수는?",str_c.count("powerful"))
print("Ipython의 개수는?",str_c.count("IPython"))

# startswith() - 문자열이 지정된 문자열로 시작하는지 검사할때 사용하는 메서드
'''
str.startswith(prefix)
str.startswith(prefix,start)
str.startswith(prefix,start,end)
'''
# endswith() - 문자열이 지정된 문자열로 끝나는지 검사할 때 사용하는 메서드
'''
str.endswith(prefix)
str.endswith(prefix,start)
str.endswith(prefix,start,end)
'''

# D ) 문자열 바꾸기
# replace() - 지정한 문자열을 찾아서 바꾸는 메서드
'''
str.replace(old,new[, count])
'''

str_a = 'Python is fast. Python is friendly. Python is open'
print(str_a.replace('Python','Ipython'))
print(str_a.replace('Python','Ipython',2)) # 파라미터에 변경 횟수 지정 가능

str_b = '[Python] [is] [fast]'
str_b1 = str_b.replace('[','') # 문자열에서 '[' 을 제거
str_b2 = str_b1.replace(']','') # 문자열에서 ']' 다시 을 제거
print(str_b)
print(str_b1)
print(str_b2)

# E ) 문자열의 구성 확인하기
# 문자열의 구성을 확인하기 위한 메서드
'''
메서드      설명                                        
isalpha()   문자열이 숫자, 특수 문자, 공백이 아닌 문자로 구성돼 있을 떄만 True, 그 밖에는 False반환
isdigit()   문자열이 모두 숫자로 구성돼 있을 떄만 True, 그 밖에는 False 반환
isalnum()   문자열이 특수 문자나 공백이 아닌 문자와 숫자로 구성돼 있을 떄만 True, 그 밖에는 False 반환 
isspace()   문자열이 모두 공백 문자로 구성돼 있을 떄만 True, 그 밖에는 False 반환
isupper()   문자열이 모두 로마자 대문자로 구성 돼 있을 때만 True, 그 밖에는 False 반환
islower()   문자열이 모두 로마자 소문자로 구성 돼 있을 떄만 True, 그 밖에는 False 반환
'''

# F ) 대소문자로 변경하기
# upper() - 대문자로 변경 / lower() - 소문자로 변경