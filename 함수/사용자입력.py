'''
input() 이라는 내장함수를 이용해 사용자 입력을 받을 수 있다

'''

#예약자분 성함이 어떻게 되시나요?
name = input('예약자분 성함이 어떻게 되시나요?') #입력된 값을 name 변수에 넣고 다음 문장 실행
print(name)

'''
#총 몇 분이세요?/
num = input('총 몇 분이세요?')
#최대 4명까지 가능
if num > 4:
    print('죄송하지만 저희 식당은 최대 4분 까지만 예약 가능합니다')

위 코드 사용 후 에러발생
'>' not supported between instances of 'str' and 'int'
= str과 int 사이에 비교 연산 불가능 (4는 int인데 입력받은 num은 str이기 때문)
input()으로 받은 입력값은 항상 문자열 형태로 저장된다 -> 형변환 사용
'''

#형 변환 사용
num = int(input('총 몇 분이세요?'))
if num > 4:
        print('죄송하지만 저희 식당은 최대 4분 까지만 예약 가능합니다')