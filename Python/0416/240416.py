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
# pop()함수는 리스트의 마지막 요소를 리턴하고 삭제

a=[1,2,3,4]
while a:
    print(a.pop())
# 더 이상 삭제할 요소가 없을 때까지 반복하고, 다 삭제했으면 프로그램을 종료하라는 뜻

if[1,2,3]:
    print("참")
else:
    print("거짓")

print(bool([1,2,3]))
print(bool([]))
# bool([])는 빈 리스트인 []를 불리언 값으로 변환하는 것을 의미.
# 파이썬에서 빈 리스트는 거짓(false)로 간주됨. 따라서 print(bool([]))는 거짓(false)를 반환.
print(bool(0))
print(bool(3))

a=[1,2,3,4,5,6,7,7]
b=a
print(b)
print(id(a))
print(id(b))
print(a is b)
# 주소가 곧 본체이다.
# b에다 a 넣어주면 주소까지 다 복제해오는 것.

a[1]=15
print(a)
print(b)
# a 변수 값을 b에 넣으면서 주소만 서로 다르게 하는 방법
# 1번 방법
b=a[:]
print(id(a))
print(id(b))
# 2번 방법
b=a.copy()
print(id(b))
print(b is a)
# 주소가 달라서 ▲는 false를 리턴. 주소가 곧 본체.









