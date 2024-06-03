'''
예외처리  에러가 발생했을 때 프로그램이 올바르게 동작할 수 있도록 해주는 것

try:
    수행 문장
except:
    에러 발생 시 수행 문장
else:
    정상 동작 시 수행 문장
finally:
    마지막으로 수행할 문장 #에러 여부 상관없이 동작
'''
num1 = 3
num2 = 3
try:
    result = num1 / num2 #만약 num2 = 3 이라면?
    print(f'연산 결과는 {result}입니다')
except:
    print('에러가 발생했어요')
else:
    print('정상 동작했어요')
finally:
    print('수행 종료')

'''
1.
try:
    수행 문장
except:
    에러 처리

2.
try:
    수행 문장
finally:
    마지막 수행
# try 끝에 무조건 except나 finally가 와야한다

3. # try수행 문장 후 에러일 시 except / 정상일 시 else가 동작 후 종료
try:
    수행 문장
except:
    에러 처리
else:
    정상 동작

4. # try수행 문장 후 에러일 시 except가 동작하고 마지막 finally동작 후 종료 / 정상일 시 else가 동작한 후 마지막 finally 동작 후 종료
try:
    수행 문장
except:
    에러 처리
else:
    정상 동작
finally:
    마지막 수행
'''