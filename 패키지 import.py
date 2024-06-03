#1번
import 모듈.goodjob
모듈.goodjob.say()
print()

#2번
from 모듈 import goodbye
goodbye.bye()
print()

#두개 다 갖다 쓸 때 ,로 구분
from 모듈 import goodjob,goodbye
goodjob.say()
goodbye.bye()