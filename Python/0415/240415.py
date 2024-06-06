a = "Life is too short."
print(a.upper().lower().replace(" ",",").split(","))

l = [1, 3, 5, 7, 9]
print(l)

a=[]
b=[1, 2, 3]
c=['life', 'is', 'too', 'short.']
d=[1,2,'life','too short']
e=[1,2,['Life','is']]

a=[1,2,3, ['a', 'b', 'c']]
print(a[-1][0])

a=[1,2,3]
print(a*3)
print(len(a))

print(type(a[2]))
print(str(type(a[2])))
print(str(a[2])+"살")

a = [1, 2, 3]
a.append("안녕하세요")
print(a)

a = "Scoopy is a dog."
print(a.index('k'))



# <QUIZ #2 리스트>
# Q. 슬라이싱을 사용해서 홀수만 출력하라.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [1, 3, 5, 7, 9]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
print(nums[::])
# Q. 리스트 특정데이터 잘라내기
# 문제) price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라.
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 다음 소스 코드를 완성하여 리스트 [5, 3, 1, -1, -3, -5, -7, -9]가 출력되게 만드세요. 
# 리스트를 만들 때는 range를 사용해야 합니다.
# l=[5, 3, 1, -1, -3, -5, -7, -9]
a=list(range(5,-10,-2)) 
# step: 음수 = 내림차순 
 
print(a)


# <파이썬 유치원반>
a='HELLO'
b=[1,2,3,4,5]

# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.

nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자 Naver
print(interest[0]+interest[2])
print(interest[0],interest[2])
# 파이썬에서 +는 띄어쓰기 없음, 쉼표는 띄어쓰기 있음

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('/'.join(interest))
