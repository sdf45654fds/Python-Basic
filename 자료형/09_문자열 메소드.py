''' 
메소드 = 클래스 내에 정의된 어떤 동작, 기능을 하는 코드들의 묶음
문자열.메소드(..)
'''

letter = 'how are YOU?'
#01 모든 내용을 소문자로 (lower)
print(str('01. ') + letter.lower())
#02 모든 내용을 대문자로 (upper)
print(str('02. ') + letter.upper())
#03 첫 글자만 대문자로 (capitalize)
print(str('03. ') + letter.capitalize())
#04 각 단어들의 첫 글자만 대문자로 (title)
print(str('04. ') + letter.title())
#05 대소문자를 뒤바꾸려면 (swapcase)
print(str('05. ') + letter.swapcase())
#06 문자열을 뛰어쓰기 기준으로 나누려면 (split)
print(letter.split())
#07 '???'가 몇 번 쓰였는지 횟수 확인 (count)
print(letter.count('how'))
#08 '??'로 시작하는지 확인 (startswith)
s = '나도고등학교'
print(s.startswith('나도')) #결과는 불리언 형태로 True,False로 나옴
#09 '??'로 끝나는지 확인 (endswith)
print(s.endswith('고등학교')) #결과는 불리언 형태로 True,False로 나옴
#10 앞뒤로 불필요한 문자 제거 (strip)
ss = '...나도고등학교...'
print(ss.strip('.'))
#11 문자열 일부를 변경 (replace)
print(s.replace('고등학교','고교'))
#12 특정 글자가 어디 있는지 확인하려면 (find)
print(s.find('학교'))
#13 다른 문자들 사이에 가운데로 넣고 싶다면 (center()메소드에 총 길이)
print(s.center(10,'-'))

#등등 더 많은 정보는 구글에 'python 내장형' 검색
