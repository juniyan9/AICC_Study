# 옷가게 할인 받기
    # 나의 풀이
def solution(price):
    answer = 0
    if 300000> price >= 100000:
        answer = price*0.95
    elif 500000 > price >= 300000:
        answer = price*0.9
    elif price >= 500000:
        answer = price*0.8
    else:
        answer = price
    return int(answer)

    # 다른 사람 풀이
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
        


# 중앙값 구하기
def solution(array):
    answer = 0
    array.sort()
    for i in array:
        answer = array[(len(array)//2)]
    return answer


# 숨어있는 숫자의 덧셈(1)
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer