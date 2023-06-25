# 1. dictionary 선언
data = {'마우스' : 'mouse', '모니터' : 'monitor'}

# 2. key와 value로 출력
print(data.keys(), data.values())

# 3.
en_data = {'environment': '환경', 'company': '회사', 'government': '정부, 정치', 'face': '얼굴'} # dict 선언
keys = en_data.keys() # key 값만
values = en_data.values() # value 값만
print(list(keys), '\n', list(values)) # 각각 리스트로 변환 후 출력

# 4. 
for item in data.keys():
    print(item, ":" , data[item]) # 마우스 : mouse, 모니터 : monitor
    
# 5.
actor_info = {'actor_details': {'생년월일': '1971-03-01',
                '성별': '남',
                '직업': '배우',
                '홈페이지': 'https://www.instagram.com/madongseok'},
                'actor_name': '마동석',
                'actor_rate': 59361,
                'date': '2017-10',
                'movie_list': ['범죄도시', '부라더', '부산행']}

print ("배우 이름:", actor_info['actor_name'])
print ("홈페이지:", actor_info['actor_details']['홈페이지'])
print ("출연 영화 갯수:", len(actor_info['movie_list'])) 
