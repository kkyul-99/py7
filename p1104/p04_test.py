import p04_stuFunc

while True:
    p04_stuFunc.screen_print()
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    if choice == 1:
        p04_stuFunc.stu_input()
    
    elif choice == 2:
        p04_stuFunc.stu_print()
    
    elif choice == 3:
        p04_stuFunc.stu_modify()
    
    elif choice == 4:
        p04_stuFunc.stu_delete()
    
    elif choice == 5:
        p04_stuFunc.rank()
    
    elif choice == 0:
        p04_stuFunc.exit()
        break
