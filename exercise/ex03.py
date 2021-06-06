# Q1 if 문
a = "Life is too short, you need python"

print("Q1. need\n")

# Q2 while 문 - 나머지 연산
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(f"Q2. {result}\n")

# Q3 while 문 - 삼각형 출력
print("Q3.")
i = 0
while True:
    i += 1
    if i > 5 :
        break
    print("*" * i + "\n")

# Q4 for 문 - 1부터 10까지의 합
print("Q4.")
for i in range(1,11):
    print(i)

# Q5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
avg = total / len(A)
print(f"\nQ5. A학급 평균: {avg}점\n")

# Q6 리스트 내포
numbers = [1, 2, 3, 4, 5]
result = [number * 2 for number in numbers if number % 2 == 1]
print(f"Q6. {result}")
