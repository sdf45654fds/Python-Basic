'''
리스트= 여러 개의 값을 저장, 서로 관련있는 연속적인 데이터들을 관리하는데 사용
리스트 = [값1,값2,..] (인덱스를 순서대로 관리)
똑같은 값 중복 허용
숫자 문자 불리언 아무 값 섞여도 허용
빈 리스트 = [] (대괄호만)
'''

#리스트 해당하는 값 출력
my_list = ['오예스', '몽쉘', '초코파이']
print(my_list[0])

#리스트에 포함되어있는 값이 있는지 확인
print('몽쉘' in my_list)

#리스트에 포함되어있는 값이 몇개인지 확인 (len)
print(len(my_list))

#리스트 수정
my_list[1] = '몽쉘카카오' #값 수정
print(my_list)

#슬라이싱
my_list = ['오예스','몽쉘','초코파이']
print(my_list[0:2])

#다른 리스트에 있는 값을 합치기 (extend)
your_list = ['빅파이','오뜨']
my_list.extend(your_list) #리스트 확장
print(my_list)

'''
insert()  = 원하는 위치에 값 추가
pop()     = 원하는 위치(또는 마지막)의 값 삭제
clear()   = 모든 값 삭제
sort()    = 값 순서대로 정렬
reverse() = 순서 뒤집기
copy()    = 리스트 복사
count()   = 어떤 값이 몇 개 있는지
index()   = 어떤 값이 어디에 있는지
등등
'''

'''
리스트는 중복값이 허용이 되는데 중복값을 제거해야 할때도 있음
my_list = ['오예스','몽쉘','초코파이','초코파이','초코파이']
my_set = set(my_list) //괄호 속에 리스트를 넣어서 세트로 변경 가능 
-> 세트는 중복값을 허용하지 않기 때문에 변경하는 과정에서 중복된 값은 사라지고 하나만 남게된다
my_list = list(my_set) //괄호 속에 세트를 넣어서 리스트로 변경

 !!세트는 순서도 보장하지 않기때문에 순서가 뒤죽박죽 섞인다 -> 순서가 중요하면 딕셔너리로 한다
'''