'''
def 함수명():  #()안에 필요한 경우에 전달값을 전달할 수도 있다 = 전달값 또는 파라미터 라고 한다
    수행할 문장

전달값(파라미터)
1. 여러 개 사용 가능(콤마로 구분)
2. 함수 내에서만 사용 
'''
def show_price(customer): #함수 정의
    print(f'사랑하는{customer}고객님')
    print('감성커트 가격은 15000 원입니다') #전체 한번에 수정 하려면 여기만 바꿔주면 다 수정됨
print()

#고객님 앞에 함수 추가
customer1 = '나장발'
show_price(customer1) #함수 호출

customer2 = '나수염'
show_price(customer2) #함수 호출