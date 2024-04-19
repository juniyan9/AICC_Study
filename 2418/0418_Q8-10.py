# 06-2) 1000미만의 3과 5의 배수(중복 없이) 구해서 더하기

result = 0
# 초기화 => 변수를 0부터 시작한다고 선언하는 게 매우 중요! 
for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)
# 아 이게 sum이네! 3의 배수이거나 5의 배수일 때 result값에 넣어달라했으니까
# or 연산자를 썼기 때문에 따로 중복제거 안 해줘도 됨!!


# 교수님 풀이

# 06-3) 게시판 프로그램

# input(): 게시물 총 개수, 한 페이지에 보여줄 게시물 수
m = int(input("게시물 총 개수: "))
n = int(input("한 페이지에 보여줄 게시물 수: "))

pgnum = m // n + 1  
# 페이지 개수는 정수이므로 round 함수보다는 몫으로 접근하는 게 낫다
print(pgnum)

# 369 게임
# 1부터 시작해 숫자를 하나씩 센다.
# 3이나 6이나 9의 배수일 경우 박수를 친다.
# 지정 최대 숫자까지 도달하면 프로그램 종료.
# 함수로 해라(10)


n = int(input("숫자를 입력하세요: "))

for i in range(n+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        print("clap")
    else:
        print(i)



# 12명의 레벨테스트 점수 파이썬 리스트
# score 라는 이름의 변수에 할당.
score = [80, 60, 70, 50, 100, 95, 40, 75, 90, 65, 90, 100]
# 1. 전체 점수의 평균 구하는 코드
# 2. 전체 점수 중 가장 높은 점수를 구하는 코드
# 3. 전체 점수 중 가장 낮은 점수를 구하는 코드

total = sum(score)
count = len(score)

print("평균: ", total/count)
print("가장 높은 점수: ", max(score))
print("가장 낮은 점수: ", min(score))

# 기타 풀이
def avg(list_score):

   total = 0
   for i in list_score:
       total += i
   return total/len(list_score)

# <i에 대한 참고 내용>
# 리스트, 튜플, 집합 등의 반복 가능한(iterable) 객체를 순회할 때 사용됩니다. 
# 하지만 i를 리스트에만 제한해서 사용할 필요는 없습니다. 
# 어떠한 반복 가능한 객체에 대해서도 i를 사용할 수 있습니다.

# 예를 들어, i를 사용하여 딕셔너리의 키-값 쌍을 순회할 수도 있습니다
# 참고내용 끝

#    return sum(list_score)/len(list_score) <-- 위에 네 줄이랑 똑같은 결과 출력

print(avg(score))


# QUIZ 10
# 레벨 3 문제
# 다음과 같은 형태의 배열을
# > [a1,a2,a3...,an,b1,b2...bn]
# 다음과 같은 형태로 바꾸시오
# > [a1,b1,a2,b2,.....,an,bn]
# ( 문제 원문을 보니 should be in-place라 되어 있네요. )
# 입력을 저장하는 저장소 이외에 추가적인 저장장소를 사용치 않는다는게 제약조건입니다.

# 참고풀이

# 크기에 따른 배열 생성

array = []

size_of_list = int(input("배열 크기 입력 :"))

for a in range(1, size_of_list + 1):
    array.append("a" + str(a))

for b in range(1, size_of_list + 1):
    array.append("b" + str(b))


# 재배열

for i in range(size_of_list):
    array.insert(i * 2 + 1, array.pop(size_of_list + i))


    print(array)

    




