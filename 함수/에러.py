'''
에러가 무엇인지 왜 발생했는지 알기 위해
except와 :(콜론) 사이에 Exception as err을 적은뒤 print를 통해 err 을 출력해본다 
'''

num1 = 3
num2 = 0
try:
    result = num1 / num2
    print(f'연산 결과는 {result}입니다')
except:
    print('에러가 발생했어요')

#구글에서 python exceptions 검색하면 다양한 에러 종류 설명 확인 가능
try:
    result = num1 / num2 
    print(f'연산 결과는 {result}입니다')
except ZeroDivisionError:    #ZeroDivisionError: #num2가 0이라면?
    print('0으로 나눌 수 없어요')
except TypeError:    #TypeError:  #num2가 문자열 '0'이라면?
    print('값의 형태가 이상해요')
except Exception as err:    #Exception as err / print(,err) #에러 내용 확인
    print('에러가 발생했어요: ',err)

