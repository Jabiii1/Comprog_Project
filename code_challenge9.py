def cc9():
    print("--------For Loops--------")
    
    for x in range(1, 11):
        print("  " * x , end =" ")  
        for y in range(x, 11):
            print("*", end = " ")  
        print()    