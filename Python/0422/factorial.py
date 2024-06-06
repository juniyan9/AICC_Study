def fac(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
        # 위에 식이 for문 안에 있으므로 result 값끼리 서로 곱해나가는 거라고 한다
        print(result)
#     return result

# print(fac(4))