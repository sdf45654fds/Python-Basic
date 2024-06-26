'''
값이 바뀔 일이 없거나, 바뀌면 안되는 경우 사용
튜플 = 읽기전용 리스트 (수정불가)
중복 허용
아무 값 다 허용
순서 보장
수정 불가 제외하고는 리스트와 비슷
소괄호를 통해 선언 -> 선언 후 추가,삭제,수정 불가
--메서드--
count() = 어떤 값이 몇 개 있는지
index() = 어떤 값이 어디에 있는지
'''
my_tuple = ('오예스','몽쉘','초코파이') #패킹
(pie1, pie2, pie3) = my_tuple #언패킹 my_tuple에 있는 값을 순서대로 pie1,2,3에 집어넣음

# *을 사용해서 나머지들을 전부 (*others)에 집어넣음 !!주의!! *안에 있는 값은 튜플이 아닌 리스트형태로 됨
numbers=(1,2,3,4,5,6,7,8,9,10)
(one,two,*others)=numbers  # (1,2, 3~10)
(one,*others,ten)=numbers  # (1, 2~9 ,10)
(*others,nine,ten)=numbers # (1~8 ,9,10)

'''
튜플 수정 방법
my_tuple = ('오예스', '몽쉘')  //튜플선언
my_list = list(my_tuple)  //리스트를 적고 튜플을 소괄호로 감싸면 리스트 형태로 변경
my_list.append('초코파이')  //리스트에서 제공하는 append() 메소드를 이용해 값을 추가
my_tuple = tuple(my_list) //튜플을 적고 리스트를 소괄호로 감싸면 튜플 형태로 변경됨
 튜플을 리스트로 리스트를 튜플로 감싸면 된다
'''