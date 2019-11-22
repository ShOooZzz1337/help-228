count=0
n=int(input())
if n>=3 and n<=1000:
    res = input().split()[:n]
    res1=[]
    for i in range (n):
        res[i]=int(res[i])
        res1.append(res[i])
    for j in range (n-2):
        if (res1[j]==4 or res1[j]==5):
            if (res1[j+1]==4 or res1[j+1]==5):
                if (res1[j+2]==4 or res1[j+2]==5):
                    count+=1
                    j+=3
                else: j+=3
            else: j += 2
        else: j+=1
    print(count)
