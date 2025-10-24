# 산술연산자
# + : 더하기, - : 빼기, * : 곱하기, / : 나누기
# // : 몫, % : 나머지, ** : 제곱
# print(10+20)
# print(10-20)
# print(10*20)
# print(10/20)
# print(10/3)  # 3.333333
# print(10//3) # 3
# print(10%3)  # 1 나머지
# print(10**3) # 10*10*10 = 1000

# 두수를 입력받아 위의 연산을 출력하시오.
# +,-,*,/,//,%,**

# num = int(input("숫자를 입력하세요."))
# num2 = int(input("숫자를 입력하세요."))
# print(num+num2)
# print(num-num2)
# print(num*num2)
# print(num/num2)  # 3.333333
# print(num//num2) # 3
# print(num%num2)  # 1 나머지
# print(num**num2) # 10*10*10 = 1000

### 780원 동전으로 교환을 하려고 해요.
### 500, 100, 50, 10원 동전 몇개로 교환해야 할까요?
# 값/500-1(몫) 나머지/100-2(몫) 나머지50-1(몫) 나머지10-3(몫)
# coin = 123456700
# money1 = coin//500    #500원 몫 - 개수
# money2 = coin%500
# money3 = money2//100 #100원 몫 - 개수
# money4 = money2%100
# money5 = money4//50 #50원 몫 - 개수
# money6 = money4%50
# money7 = money6//10 #10원 몫 - 개수

# print("500원 동전 : %d 개" % money1)
# print("100원 동전 : %d 개" % money3)
# print("50원 동전 : %d 개" % money5)
# print("10원 동전 : %d 개" % money7)



coin = 1597000
# 50000원,10000원,5000원,1000원
money1 = coin//50000   #50000원 몫 - 개수
money2 = coin%50000
money3 = money2//10000 #10000원 몫 - 개수
money4 = money2%10000
money5 = money4//5000  #5000원 몫 - 개수
money6 = money4%5000
money7 = money6//1000  #1000원 몫 - 개수
money8 = money6%1000   # 동전으로 교환

print("50000원 지폐 : %d 장" % money1)
print("10000원 지폐 : %d 장" % money3)
print("5000원 지폐 : %d 장" % money5)
print("1000원 지폐 : %d 장" % money7)
print("1000원 동전 : %d 개" % money8)
