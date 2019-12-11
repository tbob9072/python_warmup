'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('input Num: '))
# 아래에 코드를 작성해 주세요.

if number % 2 == 0 :
    print("even number")
else :
    print("odd number")

# 1 값이 True이기 때문에 == 0 은 생략하고 홀수를 출력해주면됨
# if number % 2 :
#   print("odd number")
# else :
#   print("even number")
    