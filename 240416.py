# 240416

# 파이썬 유치원반 문제 #17
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('/'.join(interest))

#18
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('\n'.join(interest))

#19
string = "삼성전자/LG전자/Naver"
# interest = [string[0:4], string[5:9], string[10:15]]
# 이거는 너무 길어지니까
interest=string.split("/")
print(interest)
interest = []
# ▲interest는 []리스트라고 선언한 것.
interest.append(string[0:4])
# ▼append는 []리스트의 내장함수!
interest.append(string[5:9])
interest.append(string[10:15])
print(interest)

# 딕셔너리
# dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# print(dic.keys('name'))

a = {0: 'a', 1:'b', 2:'c'}
a[3]='d'
print(a)
print(a[2])

# 질문
# >>> for k in a.keys():
# ...    print(k)
# ...
# name
# phone
# birth

# 집합을 튜플화
s1 = set([1,2,3])
t1=tuple(s1)
print(t1)

s1={1,2,3,4,5,6}
print(s1)

s2={4,5,6,7,8,9}
print(s2-s1)
print(s1&s2)
print(s1.intersection(s2))
# add와 update는 직접 프린트는 안되고 집합 요소만 변경해줌.
# 그래서 print(s1)해야 더해지고 변경된 내용이 업데이트되어 나옴!
s1.add(9)
s1.update([7,8])
print(s1)

s3=set("gorgeous")
s4=set("iconic")
print(s3&s4)
# ▲교집합
s5=s3-s4
print(s5)
print(s3|s4)
# ▲▼합집합
print(s3.union(s4))

# 아래는 모두 따옴표가 없으므로 Boolean 값
a=True
b=False

print(type(a))
c=1.1
print(type(c))

print(1==1)
print(1>2)

a=[1,2,3]
print(a.pop())
# pop()함수는 리스트의 마지막 요소를 제거

a=[1,2,3,4]
while a:
    print(a.pop())