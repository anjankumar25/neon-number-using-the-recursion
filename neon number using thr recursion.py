def aa(a,vh=0):
    if a == 0:
        return vh
    
    e=a%10
    vh=vh+e
    
    return aa(a//10,vh)
n=int(input("enter the :"))
v=n*n
vp=aa(v)
if n == vp:
     print(f"{vp} is an neon number number")
else:
    print(f"{vp} is not aneon number")
