'''
키워드값 = 전달값의 대상을 정해 주는 거
'''

def get_price(is_vip = False,
              is_birthday = False,
              is_membership = False,
              card = False,
              review = False,
              first_time = False):
#review값만 True로 하고 싶다면
    price = get_price(review = True)
#때마침 생일이라 birthday도 True로 하고 싶다면
    price = get_price(review = True, is_birthday = True) #키워드값은 콤마로 구분, 순서 무관