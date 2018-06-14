def table(n,i)
    i=1
    print(n + '*' + i + '=' + (n*i))
    if i<=10:
        table(n,i+1)
    
