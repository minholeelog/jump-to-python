# Q1. 홀짝 판별 함수
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
three = 3
print(f"Q1. {three}는 홀수입니다. {is_odd(3)}")

# Q2. 입력값 평균 구하기
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)
print(f"Q2. 입력값 평균: {avg_numbers(1,2,3,4)}")

#  Q3. 두 수의 합 구하기
input1 = int(input("Q3. 첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))
total = input1 + input2
print(f"두 수의 합은 {total}입니다.")

# Q4. 
print('Q4. print("you","need","python") => comma로 띄어쓰기 구분')

# Q5. 파일 입출력
f1 = open("./test1.txt", "w")
f1.write("Life is too short")
f1.write("\n")
f1.close()

f2 = open("./test1.txt", "r")
print(f2.read())

# Q6. 파일 수정
user_input = input("Q6. 저장할 내용을 입력하세요:")
f = open("test1.txt", "a")
f.write(user_input)
f.write("\n")
f.close()

# Q7. 파일 수정
f = open("./test2.txt", "r")
body = f.read()
f.close()
body = body.replace("java", "python")
f = open("./test2.txt", "w")
f.write(body)
f.close()