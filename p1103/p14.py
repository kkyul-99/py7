# 로또 맞추기 프로그램
# 로또 3개를 자동번호 추출로 입력받아,
# 몇개가 맞는지 출력하시오.

import random
lotto = random.sample(range(1,46),6)
print("당첨번호:",lotto)

my_lottos = []
def rand_lottos():
    for i in range(6):
        rand_lottos = random.sample(range(1,46),6)
        my_lottos.append(rand_lottos)
        print("자동번호 {}: {}".format(i+1,rand_lottos))

counts = []
def check_lottos():
    for my_lotto in my_lottos: # 6개 묶음 로또번호
        count = 0
        for i in my_lotto: # 1개 묶음 로또번호
            if i in lotto: # 1개 번호가 로또에 있는지 확인
                count += 1
        counts.append(count)
    print("맞힌개수:",counts)


rand_lottos()
check_lottos()
