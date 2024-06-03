'''
지역변수 = 함수 내에서 정의된 변수
'''

#가능
def secret():
    message = '이건 나만의 비밀' #secret함수 내에서 정의
    print(message) #값 출력 가능
    message = '함수 내에서는 자유롭게 수정 가능'

#불가능
def please():
    message = '이건 나만의 비밀'
print(message)

#위에서 사용한 message랑은 다른 지역변수이기 때문에 값이 다름
def wait():
    message = '이렇게 하면 되지?'
    print(message)