'''
함수 define
어떤 동작을 수행하는 코드들의 묶음
여러 곳에서 사용되는 코드는 하나의 함수로

def 함수명():
    수행할 문장
'''

def show_price(): #함수 정의
    print('감성커트 가격은 15000 원입니다') #전체 한번에 수정 하려면 여기만 바꿔주면 다 수정됨
show_price() #함수 호출
print()

# 예) 함수 호출 전
customer1 = '나장발'
print(f'{customer1}고객님')
print('커트 가격은 10000 원입니다')

customer2 = '나수염'
print(f'{customer2}고객님')
print('커트 가격은 10000 원입니다')
print()

# 예) 함수 호출 후
customer1 = '나장발'
print(f'{customer1}고객님')
show_price() #함수 호출

customer2 = '나수염'
print(f'{customer2}고객님')
show_price() #함수 호출