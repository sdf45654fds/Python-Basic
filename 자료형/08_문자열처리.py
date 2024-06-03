snack = '꿀꽈배기'
two = '2개'
juseyo = snack + two

juseyo = juseyo + '주세요' 
#문자열 처리 >>
juseyo += '주세요'
print(juseyo)

num = 3
num = num + 2
print(num)
#숫자열 처리>>
num += 2
print(num)
num -= 1
print(num)
num *= 2
print(num)
num /= 4
print(num)

# 길이를 알고 싶을 때 (length)
print(len(snack))
# 여러 줄 문자
snack = '''꿀꽈배기는
너무
맛있어요'''
print(snack)