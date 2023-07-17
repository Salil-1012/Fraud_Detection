def febonnaci_series(x):
    a = 0
    b = 1
    c = a+b
    print(a,end=" ")
    print(c,end=" ")
    for i in range(x):
        a=b
        b = c
        c = a+b
        print(c,end=" ")
       
    
febonnaci_series(10)