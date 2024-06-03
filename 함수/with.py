'''
open()을 이용해 파일을 열어주면 꼭 close()로 닫아줘야 함
위에 조건을 자동으로 해주는 기능 = with (블럭을 벗어나면 자동으로 닫아줌)
'''

f = open('list.txt', 'w', encoding='utf8')
#->
with open('list.txt', 'w', encoding='utf8') as f:
    f.write('김xx\n')
    f.write('정xx\n')
    f.write('허xx\n')
    #f.close() 쓸 필요없음
