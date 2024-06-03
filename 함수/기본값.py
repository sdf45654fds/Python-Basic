'''
기본값 = 전달값에 기본으로 사용되는 값
'''

#자동으로 is_vip값은 '기본값'인 False 설정 된다
def get_price(is_vip=False): #True:단골 손님, False:일반손님
    if is_vip == Ture:
        return 10000 #단골 손님
    else:
        return 15000 #일반 손님

'''    
price1 = get_price(True) #단골
price2 = get_price(False) #일반
price3 = get_price(False) #일반
price4 = get_price(False) #일반

위에 처럼 False를 적을 필요없이
price1 = get_price(True) #단골
price2 = get_price() #일반
price3 = get_price() #일반
price4 = get_price() #일반
이렇게 하면 된다 
왜? 기본값이 False로 설정 되어있기때문에 단골손님만 True로 적어주면 된다
'''
