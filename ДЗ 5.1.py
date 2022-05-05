inp = input()
if len(inp) <= 1:
    print(inp)
else:
    while int(inp) >= 10:
        inp = eval('*'.join(list(str(inp))))
    else:
        print(inp)


    
