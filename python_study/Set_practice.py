# 1. 선언
number1 = {1, 2, 3}
number2 = {1, 9, 9}
# 2. 하나 데이터 추가 add, 여러데이터 update 사용
number1.add(4)
number1.update([5,6])
print(number1) # {1,2,3,4,5,6}

# 3. 특정 데이터 삭제
number1.remove(4)

# 4. 집합
print(number1 & number2)
print(number1 - number2)
print(number1 | number2)

