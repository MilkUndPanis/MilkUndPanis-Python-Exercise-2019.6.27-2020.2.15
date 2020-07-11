#1
def printnum(n):
    if n>0:
        printnum(n-1)
        print(n)
def main():
    printnum(10)
main()
#2
def multiply(a,b):
    if b>0:
        return a+multiply(a,b-1)
    else:return 0
def main():
    print(multiply(4,7))
main()
#3
def star(n):
    if n>0:
        star(n - 1)
        for i in range(n):
            print('*',end='')
        print()
def main():
    star(6)
main()
#4
def max(list):
    n=len(list)-1
    m=list[n]
    if n>0:
        if list[n-1]>=m:
            del list[n]
            return max(list)
        else:
            del list[n-1]
            return max(list)
    else:
        return m
def main():
    list=[1,4,2,6,3,8]
    print(max(list))
main()
#5
def sum(list):
    if len(list)>0:
        return list[0]+sum(list[1:])
    else:
        return 0
def main():
    print(sum([1,2,3,4,5,8,7]))
main()
#6
def sum(n):
    if n>0:
        return n+sum(n-1)
    else:return 0
def main():
    print(sum(7))
main()
#7
def pow(base,power):
    if power>0:
        return base*pow(base,power-1)
    else:return 1
def main():
    print(pow(2,5))
main()
#8
import sys
sys.setrecursionlimit(100000)
def Ackermann(m,n):
    if m==0:
        return n+1
    elif n==0:
        return Ackermann(m-1,1)
    else:return Ackermann(m-1,Ackermann(m,n-1))
def main():
    print(Ackermann(4,0))
    print(Ackermann(4,1))#Stack Overflow
main()

