import random # 선언, random 클래스 가져와서 쓰겠다
print(random.random()) # 0.000000000 <= x < 1.000000000
print(random.randrange(1,11)) # 1,10 사이의 숫자를 랜덤으로 가져옴.
print(random.randint(1,11)) # 1,10 사이의 숫자를 랜덤으로 가져옴.
# 해당리스트에서 n개를 랜덤으로 가져옴.
print(random.sample([1,2,3,4,5],4)) # 중복 불가능
print(random.choices([1,2,3,4,5],k=4)) # 중복 가능
# 해당리스트 순서를 랜덤으로 조정
a_list = [1,2,3,4,5]
random.shuffle(a_list)
print(a_list)
