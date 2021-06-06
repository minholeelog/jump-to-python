# Q1 홍길동 평균 점수 구하기

kor = 80
eng = 75
math = 55
total_avg = (kor + eng + math) / 3
print(f"Q1. 홍길동 평균: {total_avg}\n")

# Q2 자연수 13이 홀수인지 짝수인지 판별

num = 13
if num % 2 == 0:
    print(f"Q2. {num}: 짝수\n")
else:
    print(f"Q2. {num}: 홀수\n")

# Q3 홍길동 주민번호 분리하여 출력

pin = "881120-1068234"
birth_date = pin[:6]
unique_num = pin[7:]
print("Q3.")
print(f"생년월일: {birth_date}")
print(f"고유번호: {unique_num}\n")

# Q4 주민번호로 성별 판별

pin = "881120-1068234"
gender = pin[7:8]
print("Q4.");
if gender == "1":
    print("남\n")
elif gender == "2":
    print("여\n")

# Q5 replace

a = "a:b:c:d"
b = a.replace(":", "#")
print(f"Q5. {b}\n")

# Q6 sort

a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(f"Q6. {a}\n")

# Q7 join

a = ["Life", "is", "to", "short"]
result = " ".join(a)
print(f"Q7. {result}\n")

# Q8 튜플

a = (1, 2, 3)
a = a + (4,)
print(f"Q8. {a}\n")

# Q9 딕셔너리 특성

a = dict()
print(f"Q9. ③ a[[1]] = 'python': list는 가변성이기 때문에 딕셔너리의 키로 사용할 수 없음\n")

# Q10 딕셔너리

a = { "A": 90, "B": 80, "C": 70 }
result = a.pop("B")
print("Q10.")
print(a)
print(f"{result}\n")

# Q11 리스트 중복 제거

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a_set = set(a)
b = list(a_set)
print(f"Q11. {b}\n")

# Q12 변수 선언

a = b = [1, 2, 3]
a[1] = 4
print("Q12. 변수 a와 변수 b는 동일한 주소값을 가지기 때문에 a의 배열 요소를 변경할 경우 b의 배열 요소도 함께 변경된다.")
print(b)