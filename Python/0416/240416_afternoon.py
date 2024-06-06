# <QUIZ #3>
# # 예) 현금을 1000원 갖고 있다.
# # 200원짜리 과자를 구매하면 잔돈은 얼마일까?
# cash = 1000
# snack = 200
# charge = cash - snack
# print("잔돈 = %d원" % charge)

# 문제 1) 가로가 4이고 세로가 2인 삼각형의 넓이 출력
# 문제 2) 월급이 100원이다. 세금 10%를 제외한 연봉 출력
# 문제 3) 100초를 1분 40초로 출력
# 문제 4) 800원에서 500원을 제외한 100원의 개수 출력

# 1
w=4 
h=2
a=w*h/2
print("넓이는 %d 입니다" % a)

# 2
p = 100
tr = 0.1
y = 12 * p * (1 - tr)
# 수학처럼 곱셈 기호(*) 생략하면 안됨.
print("연봉 = %s 원입니다" % y)

# 3
m=100//60
n=100%60
print("100초는 %d분 %s초이다." % (m, n))
# m,n을 또 튜플로 묶어야함!!!

# 4
c1=800
c2=500
coin=c1%c2/100
print("100원짜리 %d개" % coin)

# <QUIZ #4>
# 주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

# (데이터)
# 이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

# 1김씨와 이씨는 각각 몇 명 인가요?
# 2."이재영"이란 이름이 몇 번 반복되나요?
# 3.중복을 제거한 이름을 출력하세요.
# 4.중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.

# 1
names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

# 수업풀이
print(names.count("이"))
print(names[0][0])
sung = []
for i in names:
    #print(i[0])
    sung.append(i[0])
    # i[0](각 이름을 돌면서 찾은 첫번째 글자)을 sung 리스트에 추가해라
print("이름은:", names)
print(sung)
print("김씨:", sung.count("김"), "명")
print("이씨:", sung.count("이"), "명")
# 대상 리스트.count(세고 싶은 대상) <--매우 유용

#GPT 풀이
kim_count = sum(1 for name in names if name.startswith('김'))

print("김씨 성을 가진 사람의 수는 %s명입니다." % kim_count)

lee_count = sum(1 for name in names if name.startswith('이'))

print("이씨 성을 가진 사람의 수는 %s명입니다." % lee_count)

# for문 풀이
# nameList 성에 이씨 찾기
# result = 0
# for i in nameList:

#     if( i[0] == '이'):
#     result += 1
    
#  print(result)

#2
leejycount = names.count('이재영')

print("이재영이라는 이름은", names.count("이재영"),"번 반복됩니다.")

#3
names_list = names.split(",")
print(names_list)
print(set(names_list))

#4
newlist = list(set(names_list))
newlist.sort()
# sort()는 정렬만해주고 출력 안해줌.
# sort()로 정렬하고 리스트 자체를 다시 출력해야 함
print(newlist)
# sort()는 키가 하나만 있을 때는 정렬이 먹힘.(이 문제의 경우 키가 이름밖에 없음. 나이라던지 다른 키 없음)
# sorted()가 더 안정적이긴 하다고.. 하심






