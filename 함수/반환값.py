'''
함수 내에서 처리된 결과를 반환

def 함수명(전달값):
    수행할 문장
    return 반환값

반환값
1.여러 개 반환 가능(콤마로 구분, 튜플)
2.반환되는 즉시 함수 탈출
반환하는 키워드 = return
'''

def get_price(): #함수 정의
    return 15000
print()

price = get_price() #함수 호출
price = 15000
print(f'커트 가격은 {price}원입니다') #15000
print()

# 단골 손님은 가격을 10000원으로 설정
def get_price(is_vip): # True : 단골 손님, False : 일반 손님
    if is_vip == True:
        return 10000 #단골 손님
    else:
        return 15000 #일반 손님

price = get_price(True) #단골 손님
print(f'커트 가격은 {price}원입니다') 

price = get_price(False) #일반 손님
print(f'커트 가격은 {price}원입니다')