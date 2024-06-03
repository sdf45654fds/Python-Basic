'''
전역변수 = 함수 밖에서 만든거
함수 밖에서나 안에서나 어디서든 사용가능

'''

message = '나는야 전역 변수' #전역변수
print(message) 
print()

# !주의! 지역변수
def no_secret():
    message = '이러면 지역 변수' #지역변수
    print(message) # '이러면 지역 변수'출력
print()

# 지역변수 안에서 전역변수 사용하는 법 (global)
def no_secret2():
    global message #전역변수
    print(message)
    message = '오 진짜 전역 변수!!' #전역 변수 값 변경

#변경 된 전역 변수 값
no_secret2()
print(message)