def is_even_or_odd(num):
    if num % 2 == 0:
        return "짝수입니다."
    else:
        return "홀수입니다."

num = int(input("숫자를 입력하세요: "))
print(is_even_or_odd(num))