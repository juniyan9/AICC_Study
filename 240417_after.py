# QUIZ#6. (중급)
# 다음과 같은 기능을 하는 코드를 작성해보세요
# 1. 루프를 1부터 10까지 반복합니다. 
#    (=i에는 1부터 10까지의 값이 반복해서 들어갑니다)
# 2. i를 그대로 출력하지 않고, 두 배로 늘려서 출력합니다. (i * 2)
# 3. 반복문 안에서 출력하지 않고, 반복문 안에서 값을 모아뒀다가 
#    반복문이 끝나면 밖에서 출력합니다. 
#     이를 위해서는 빈 리스트를 만든 뒤(double_list = []), 
#     리스트의 .append 기능을 사용해서 값을 집어넣습니다.
# 4. 여기서 i가 5일 경우는 반복을 한 번만 skip하고 
#    다음 반복(i가 6일 경우)을 재시작합니다.
# 5. 그리고 i가 8일 경우는 반복문을 강제로 종료시킵니다.


#나 + 눈높이 선생님 가르침
i = 0
double_list = []
while i < 11:

    i = i + 1
    if i == 5 : 
        continue
    if i > 7:
        break
    double_list.append(i * 2)  

print(double_list)


# 교수님 풀이
double_list = []

for i in range(1, 10+1):
    if i == 5:
        continue
    if i == 8:
        break

    double = i * 2
    print(i, "==*2==", double)

print(double_list)



# QUIZ#7 (고급 : 도움없이)
# 콜라츠 추측 (3n+1 문제)
# 3n + 1 문제는 다음과 같습니다.
# - n이 홀수면 3을 곱한 뒤 1을 더하고
# - n이 짝수면 2로 나눕니다.
# - 마지막으로 n이 1이 되면 프로그램을 종료합니다.
# 참고 : 콜라츠 추측 산식
# f(x) = n/2 (if n is even)
#      = 3n+1 (if n is odd)

# 윤경님 풀이
n = int(input("숫자를 입력하세요: "))

while n != 1:
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n = (n // 2)
        # /만 하면 그냥 나누기로 돼서 결과가 소수점까지 나옴. 
        # // 하면 몫을 구하는 거라 정수 부분만 얻을 수 있음.
    print(n)

# 이건희님 풀이
    n = int(input())
nList = []

while n != 1:
    if n % 2 != 0:
        n = 3 * n + 1
    else:
        n = n // 2
    nList.append(n)
len(nList)


      