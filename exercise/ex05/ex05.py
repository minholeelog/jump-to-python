# q1 class

class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal1 = UpgradeCalculator()
cal1.add(10)
cal1.minus(7)
print(f"q1. {cal1.value}")

# q2 class

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(60)
print(f"q2. {cal2.value}")

# q3 결과값 예측

# all([1, 2, abs(-3)-3])
print(f"q3-1. False, 1 = True, 2 = True, 0 = False")
# chr(ord("a")) == "a"
print(f"q3-2. True, ord('a') = 97, chr(97) = 'a'")

# q4 filter, lambda
result = list(filter(lambda x:x > 0, [1,-2,3,-5,8,-3] ))
print(f"q4. {result}")

# q5 진법 변환
value = "0xea"
hex_to_int = int(value, 16)
print(f"q5. {hex_to_int}")

# q6 map, lambda
value = list(map(lambda x:x*3, [1,2,3,4]))
print(f"q6. {value}")

# q7 min, max
a = [-8,2,7,5,-3,5,0,1]
result = max(a) + min(a)
print(f"q7. {result}")

# q8 round
result = round(17/3, 4)
print(f"q8. {result}")

# q9 strftime
import time
current_time = time.strftime("%Y/%m/%d %H:%M:%S")
print(f"q9. {current_time}")

# q10 random
import random
result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)
result.sort()
print(f"q11. {result}")