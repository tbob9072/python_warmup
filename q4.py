'''
문제 4.
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과, 
과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
'''

a = int(input('kor: '))
b = int(input('eng: '))
c = int(input('math: '))
d = int(input('sci: '))
# 아래에 코드를 작성해 주세요.

if a < 90 :
    print("fail")
elif b <= 80 :
    print("fail")
elif c <= 85 :
    print("fail")
elif d < 80 :
    print("fail")
else :
    print("pass")


# python 에서는 &연산자 대신 and를 써야함
