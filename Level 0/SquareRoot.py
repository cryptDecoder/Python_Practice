




def squreroot(n):

    if(n == 0 and n == 1):
        return n
    else:
        i = 1
        result = 1
        while(result <= n):
            i+= 1
            result = i * i
        return i - 1
pass

no = int(input("\n Enter the number :"))
print(squreroot(no))
