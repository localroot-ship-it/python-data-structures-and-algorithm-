#count the number of digits in a integer
n=5873
num=n
c=0
while num>0:
    last_digit=n%10
    print(last_digit)
    num=num//10
    c=+1
# checking palindrome of mumber or  (reverse)
n=1234
num= n
result=0
while num>0:
    ld=num%10
    result=(result*10)+ld
    num=num//10
print(result)

#check armstrong number
n=153
num=n
total=0
nod=len(str(n))
while num>0:
    ld=num%10
    total=total+(ld**nod)
    num=num//10