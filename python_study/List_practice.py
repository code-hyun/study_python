# 1. List 변수 선언
location = ['수원시', '화성시', '인천시']
print(location)

# 2. List 추가
location.append('광주광역시')
print(location)


# 3. List 마지막 출력
location[-1]
print(location[-1])

# 4. List 제거
location.remove('인천시') # 특정 location 제거
del location[1] # 인덱스 번호로 제거
print(location)

# 5. List 추가
location.insert(2, '대구')
print(location)

# 6. List 정렬
number = [6, 5, 2, 3, 7, 1]
number.sort()
print(number) # [1 ,2, 3, 5, 6, 7]