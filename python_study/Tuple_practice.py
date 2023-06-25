# 1. 튜플 덧셈과 곱셈
data1 = ('a', 'b', 'c')
data2 = ('e', 'f')
print(data1 * 3 , data1 + data2) # ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c') ('a', 'b', 'c', 'e', 'f')

# 2. 값 두개 출력
def test(a,b):
    quot = a // b
    rem = a % b
    return quot, rem

quot, rem = test(3, 10)
print(quot, rem)

# 3. 마지막 튜플 값 출력
data = ('a', 'b' 'c', 'd', 'e')
print(data[0], data[-1]) # a, e

# 4. 튜플 데이터를 리스트 데이터로 변환 후 tuple-test를 데이터 마지막에 추가하고 다시 튜플로 변환
tuple_data = ('test_1', 'test_2', 'test_3') # 튜플 선언
list_data = list(tuple_data) # 튜플을 리스트로 변환

list_data.append('tuple-test') # 리스트 추가
data = tuple(list_data) # 튜플로 변환
print(data)