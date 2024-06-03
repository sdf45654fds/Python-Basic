'''
단어가 있고 그 뜻이 항상 함께 있다
단어 = key , 뜻 = value
key 중복 허용 x
중괄호 사용
딕셔너리 ={key1:value1, key2:value2,...} 
:로 키와 밸류 구분 
,로 다음 키와 밸류 구분
'''

'''
예)
key   = 이름, 나이, 키, 몸무게
value = 나도, 7세, 120cm, 23kg
딕셔너리 = {'이름':'나도', '나이':7, '키':120, '몸무게':23} ->보기 불편하면 줄바꿈을 해도 괜찮 
'''

person = {
    '이름':'나도',
    '나이':7,
    '키':120,
    '몸무게':23
}
#key에 해당하는 value 확인
print(person['이름'])
print(person['나이'])

#key에 해당하는 value 확인2
#print(person['별명']) # key안에 '별명'이 없으므로 에러발생
print(person.get('별명')) # get은 접근명령어인데 없는 key에 접근하면 None 출력

#새로운 key 생성
person['최종학력'] = '유치원'

#존재하는 key의 value값 변경
person['키'] = 130

#여러 key의 value값을 변경하려면 .update({})
person.update({'키':140, '몸무게':26})

#특정 key:value 를 삭제하려면 .pop()
person.pop('몸무게')

#모든 데이터를 삭제하려면 .clear()

#어떤 key가 있는지 확인 .keys()
print(person.keys())

#어떤 value들이 있는지 확인 .values()
print(person.values())

#key:value 모두 확인 .items()
print(person.items())

'''
--메소드--
fromkeys() = 제공된 keys를 통해 새로운 딕셔너리 생성 및 반환
popitem() = 마지막으로 추가된 데이터 삭제
setdefault() = key에 해당하는 value 반환, key가 없다면 새로 만들고 default value 설정 및 반환
'''

'''
딕셔너리로 순서 보장받으면서 리스트 중복값 제거
my_list = ['오예스','몽쉘','초코파이','초코파이','초코파이']
my_dic = dict.fromkeys(my_list) //리스트에서 중복이 제거된 '오예스','몽쉘','초코파이'를 key로 가지는 딕셔너리 생성됨
print(my_dic)  //value 값은 None으로 설정됨
my_list = list(my_dic) //딕셔너리를 리스트로 다시 감싸면 key값들만 뽑아서 다시 리스트로 변환됨
print(my_list)
'''