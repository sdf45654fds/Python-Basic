'''
open
'''

f = open('list.txt', 'w', encoding='utf8') #쓰기 모드로 파일 열기
f.write('김xx\n') #문장 입력
f.write('정xx\n') #문장 입력
f.write('허xx\n') #문장 입력
f.close() #파일 닫기

f = open('list.txt', 'r', encoding='utf8') #읽기 모드로 파일 열기
contents = f.read() #파일 내용 다 읽어오기
print(contents)
f.close() #파일 꼭 닫기!

#한 줄씩 읽기
f = open('list.txt', 'r', encoding='utf8')
for line in f:
    print(line, end='')
f.close