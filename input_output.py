'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

''' 
'''
                           #1-misol
a = input()
p = 4a
print(p)  
#---------------------------------------------------------------------
                           #2-misol
a = input()
s = a**2
print(s)
#---------------------------------------------------------------------
                           #3-misol
a = int(input())
b = int(input())
p = 2*(a+b)
s = a*b
print(p,s)
#---------------------------------------------------------------------
                           #4-misol
d = float(input())
r = d/2
pi = 3.14
l = 2*r*pi
print(l)
#---------------------------------------------------------------------
                           #5-misol
a = float(input())
v = a**3
s = 6*(a**2)
print(v,s)
#---------------------------------------------------------------------
                           #6-misol
a = float(input ()) 
b = float(input ()) 
c = float(input ()) 
v = a*b*c 
s = 2*(a*b + b*c + a*c) 
print (v, s)
#---------------------------------------------------------------------
                           #7-misol
r = float(input())
pi = 3.14
l = 2*r*pi
s = pi*r**2
print(l,s)
#---------------------------------------------------------------------
                           #8-misol
a = float(input())
b = float(input()) 
o = (a+b)/2
print(o)
#---------------------------------------------------------------------
                           #9-misol
import math 
a = float(input()) 
b = float(input())
g = math.sqrt(a*b)
print(g)
#---------------------------------------------------------------------
                           #10-misol
a = float(input())
b = float(input())
s = a+b, a-b, a*b, a/b
print(s)
#---------------------------------------------------------------------
                         ! #11-misol
import math
a = float(input())
b = float(input())
s = math.modf(a+b)
q = math.modf(a-b)
r = math.modf(a*b)
t = math.modf(a/b)
print(s,q,r,t)
#---------------------------------------------------------------------
                           #12-misol
import math
a = float(input())
b = float(input())
c = math.sqrt(a**2+b**2)
p = a+b+c
print(c,p)
#---------------------------------------------------------------------
                           #13-misol
r1 = float(input())
r2 = float(input())
pi = 3.14
s1 = r1**2*pi
s2 = r2**2*pi
s3 = s1-s2
print(s1,s2,s3)
#---------------------------------------------------------------------
                           #14-misol
l = float(input())
pi = 3.14
r = l/(2*pi)
s = pi*r**2
print(r,s)
#---------------------------------------------------------------------
                           #15-misol
from math import pi, sqrt
s = float(input())
r = sqrt(s/pi)
l = 2*pi*r 
d = 2*r
print(d,l)
#---------------------------------------------------------------------
                              #16-misol
x1 = float(input())
x2 = float(input())
x3 = x2-x1
print(x3)
#---------------------------------------------------------------------
                            #17-misol
a = float(input('A kemaning uzunligi:'))
b = float(input('B kemaning uzunligi:'))
c = float(input('C kemaning uzunligi:'))
ac = c-a
bc = c-b
print(ac,bc,ac+bc)
#---------------------------------------------------------------------
                                 #18-misol
a = float(input('A kemaning uzunligi:'))
b = float(input('B kemaning uzunligi:'))
c = float(input('C kemaning uzunligi:'))
ac = c-a
bc = b-c
print(ac,bc,ac*bc)
#---------------------------------------------------------------------                             
                                 # 20-misol 
import math

x1 = float(input('x1 ni kiriting: '))
y1 = float(input('y1 ni kiriting: '))
x2 = float(input('x2 ni kiriting: '))
y2 = float(input('y2 ni kiriting: '))
s = math.sqrt((x1-x2)**2+(y1-y2)**2)
print(s)
#---------------------------------------------------------------------

                             # 21-misol
from math import*

x1 = int(input('x1 ni kiriting: '))
y1 = int(input('y1 ni kiriting: '))
x2 = int(input('x2 ni kiriting: '))
y2 = int(input('y2 ni kiriting: '))
x3 = int(input('x3 ni kiriting: '))
y3 = int(input('y3 ni kiriting: '))

a = sqrt((x1-x2)**2+(y1-y2)**2)
b = sqrt((x1-x3)**2+(y1-y3)**2)
c = sqrt((x3-x2)**2+(y3-y2)**2)

p = (a+b+c)/2
p1 = a+b+c
s = sqrt(p*(p-a)*(p-b)*(p-c))

print(p1,s)

#---------------------------------------------------------------------

                              #22-misol
a = float(input('A ni kiriting: '))             
b = float(input('B ni kiriting: '))
# Agar o'zgaruvchi kiritib yech desa
# c = a
# a = b
# b = c

a,b=b,a
print(a,b)
#---------------------------------------------------------------------

                            #23-misol

a = float(input('A ni kiriting: '))             
b = float(input('B ni kiriting: '))
c = float(input('C ni kiriting: '))             
a,b,c=b,c,a
print(a,b,c)
#misolning javobi chalkashgan
#---------------------------------------------------------------------

                           #24-misol
                           
a = float(input('A ni kiriting: '))             
b = float(input('B ni kiriting: '))
c = float(input('C ni kiriting: '))    

c,b,a=b,a,c
print(c,b,a)
#---------------------------------------------------------------------

                        #25-misol

x = float(input('x ni kiriting:'))
y = 3*x**6-6*x-7

print(y)
#---------------------------------------------------------------------

                         #26-misol
x = float(input('x ni kiriting:'))
t = x-3
y = 4*t**6-7*t**3+2

print(y)
#---------------------------------------------------------------------

                     #29-misol

a = float(input('a ni kiriting: '))
a1 = a*a
a2 = a1*a1 
a3 = a2*a
print(a1,a2,a3)

#---------------------------------------------------------------------
                        #28-misol

a = float(input('a ni kiriting: '))
a1 = a*a
a2 = a1*a 
a1 = a1*a2
a2 = a1*a1
a1 = a1*a2
print(a1)

#---------------------------------------------------------------------

                       #29-misol

b = float(input('b burchakni kiriting:'))
r = b*3.14/180
print(r)

#---------------------------------------------------------------------1`

                          #30-misol
                          
r = float(input('b burchakni kiriting:'))
b = r*180/3.14
print(b)

#---------------------------------------------------------------------1

                            #31-misol

t_f = float(input('tempraturani kiriting:'))
t_c = (t_f-32)*5/9

print(t_c)

#---------------------------------------------------------------------1

                           #32-misol
                           
t_c = float(input('tempraturani kiriting:'))
t_f = (t_c*9/5+32)

print(t_f)                          

#---------------------------------------------------------------------1

                             #33-misol

x=float(input('x ni kiriting:'))                              
a=float(input('a ni kiriting:')) 
y=float(input('y ni kiriting:')) 

s = a/x
d = s*y
print(s,d)

#---------------------------------------------------------------------

                                #34-misol
                                
x=float(input('x ni kiriting:'))                              
a=float(input('a ni kiriting:')) 
y=float(input('y ni kiriting:')) 
b=float(input('b ni kiriting:'))
s = a/x
s1 = b/y
s3 = s-s1
print(s,s1,s3)

#---------------------------------------------------------------------

                                 #35-misol
                                 
t_q = float(input('qayiqning turg\'un suvdagi tezligi: '))
d_q = float(input('daryo oqimining tezligi:'))
t1_q = float(input('qayiqning ko\'ldagi harakat vaqti: '))
t2_q = float(input('qayiqning daryo oqimiga qarshi harakat vaqt:'))

u = (t_q - d_q)*t2_q+t1_q*t_q
print(u)

#---------------------------------------------------------------------

                                #36-MISOL

v = float(input('1-avtomobilning tezligi: '))
v2 = float(input('2-avtomobilning tezligi:'))
s = float(input('orasidagi masofa: '))
t = float(input('harakat vaqti: '))
u = v*t+v2*t+s
print(u)

#---------------------------------------------------------------------

                               #37-misol
                               
v = float(input('1-avtomobilning tezligi: '))
v2 = float(input('2-avtomobilning tezligi:'))
s = float(input('orasidagi masofa: '))
t = float(input('harakat vaqti: '))
u = s-(v*t+v2*t)
print(u)

#---------------------------------------------------------------------

                                #38-misol

v = float(input('a ni kiriting:'))
v2 = float(input('b ni kiriting:'))
x = -v2/v
print(x)

#---------------------------------------------------------------------

                                  #39-misol
from math import*
a = float(input('a ni kiriting:'))
b = float(input('b ni kiriting:'))
c = float(input('c ni kiriting:'))
D = sqrt(b**2-4*a*c)
x1 = (-b+D)/2*a
x2 = (-b-D)/2*a
print(x1,x2)

#---------------------------------------------------------------------

                                    #40-misol

a1 = float(input('a1 ni kiriting:'))
b1 = float(input('b1 ni kiriting:'))
c1 = float(input('c1 ni kiriting:'))
a2 = float(input('a2 ni kiriting:'))
b2 = float(input('b2 ni kiriting:'))
c2 = float(input('c2 ni kiriting:'))

y = (a1*c2-a2*c1)/(a1*b2-a2*b1)
x = (b2*c1-b1*c2)/(a1*b2-a2*b1)
print(x,y)

#---------------------------------------------------------------------
 '''                  # YOU CAN FINISH THIS LESSON
                           #CONGRATULATION

