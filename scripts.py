#problem_1
#exercise1:solve_me_first
def solveMeFirst(a,b):
	# Hint: Type return a+b below
    return a+b


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
#exercise2:hello_world
if __name__ == '__main__':
    print ("Hello, World!")
#exercise3:arithmetic operators
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a+b)
    print(a-b)
    print(a*b)
#exercise4:division
from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
print(a//b)
print(a/b)
#exercise5: loops
if __name__ == '__main__':
    n = int(raw_input())
    i=0
    while i<n:
        print(i**2)
        i=i+1
#exercise6: write a function 
def is_leap(year):
    leap = False
    if year%4==0:
        leap=True
        if year%100==0:
            leap=False
            if year%400==0:
                leap=True
    
    return leap

  year1=int(input())
  print(is_leap(year1))
#exercise7: Print Function
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    i=1
    STRING=""
    while i<=n:
        STRING=STRING+str(i)
        i=i+1
    print(STRING)
#exercise8: find the runner up score
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    list1=[]
    for c in arr:
        if c<=100 and c>=-100:
            list1.append(c)
        else:
            print("value",c,"not accepted")
    list1.sort()  
    max1=max(list1)
    i=-2
    while list1[i]==max1:
        i-=1 
    print(list1[i])    
#exercise9: Nested lists
if __name__ == '__main__':
    student_list=[]
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        couple=[name,score]
        student_list.append(couple)
student_list.sort(key=lambda x:x[0])
student_list.sort(key=lambda x:x[1])
second_lower=[]
if len(student_list)==2:
    print(student_list[1][0])
elif student_list[1][1]!=student_list[2][1]:
    second_lower=[student_list[1][0]]
else:
    second_lower=[student_list[1][0],student_list[2][0]]
print(second_lower[0])    
print(second_lower[1])
#exercise10: finding the percentage
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    marks_list=[]
    marks_list=(student_marks[query_name])
    sum=0
    for x in marks_list:
        sum=sum+x
average=(sum/3)
average=round(average,2)
print(average)
#exercise11: tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    tuple1=tuple(integer_list)
    if len(tuple1)==n:
        print(hash(tuple1))
    else:
        print("the lenght of integer list does not correspond to n")
#exercise12: sWAP cASE 
def swap_case(s):
    char_list=[]
    for char in s:
        if char.isupper()==True:
            char=char.lower()
            char_list.append(char)
        elif char.islower()==True:
            char=char.upper()
            char_list.append(char)
        elif char==" ":
            char_list.append(char)
        else:
            char_list.append(char)
    result=""
    for Char1 in char_list:
        result+=Char1
    return result

#exercise13:String Split and Join
def split_and_join(line):
    list_line=[]
    list_line=line.split(" ")
    result="-".join(list_line)
    return result
  #exercise14: What's your name
  def print_full_name(a, b):
    print("Hello",a,b,"! You just delved into python.")
  #exercise15: Mutations
  def mutate_string(string, position, character):
    list_char=list(string)
    list_char[position]=character
    s_new=""
    for char in list_char:
        s_new+=char
    return s_new

#exercise14: FIND A STRING 
def count_substring(string, sub_string):
   i=0
   cont=0
   string1=""
   while i<len(string):
       string1=string[i:(i+len(sub_string))]
       if string1.find(sub_string)!=(-1):
           cont+=1
       i=i+1
        
   return cont
#exercise15: string validators
if __name__ == '__main__':
    s = input()
    counter=0
    for char in s:
        if char.isalpha()==True or char.isdigit==True:
            counter+=1
    if counter!=0:
        print("True")
    else:
        print("False")
    counter=0
    for char in s:
        if char.isalpha()==True:
             counter+=1
    if counter!=0:
        print("True")
    else:
        print("False")
    counter=0
    for char in s:
        if char.isdigit()==True:
            counter+=1
    if counter!=0:
        print("True")
    else:
        print("False")
    counter=0
    for char in s:
        if char.islower()==True:
            counter+=1
    if counter!=0:
        print("True")
    else:
        print("False")
    counter=0
    for char in s:
        if char.isupper()==True:
            counter+=1
    if counter!=0:
        print("True")
    else:
        print("False")
    
        

#exercise16: text alignment
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
#exercise17: text wrap
def wrap(string, max_width):
    result=textwrap.fill(string,max_width)
    return result

#exercise18: Designer door mat
m,n=map(int,input().split())
string1=".|."
string2="welcome"
i=1
while i<(n/2):
    print (string1.center(m,"-"))
    string1=string1+".|."*2
    i=i+1
print(string2.center(m,"-"))
i=i+1
k=n-2
string1=".|."*k
while i<=n:
    print(string1.center(m,"-"))
    k=k-2
    string1=".|."
    string1=k*(string1)
    i=i+1

#exercise19: capitalize
def solve(s):
     list_s=s.split(" ")
     nome=""
     cognome=""
     for char in list_s[0]:
         nome+=char
     for char in list_s[1]:
         cognome+=char
     nome.capitalize()
     cognome.capitalize()
     result=nome.capitalize()+" "+cognome.capitalize()
     return result

#exercise20:introduction to sets
def average(array):
    set_plant=set(arr)
    sum_height=0
    plant_number=len(set_plant)
    for height_plant in set_plant:
      sum_height=sum_height+height_plant
    average_height=(sum_height/plant_number)
    return average_height
#exercise21: Symmetric difference
M=int(input())
l1=map(int,raw_input().split())
N=int(input())
l2=map(int,raw_input().split())
if len(l1)==M and len(l2)==N:
    set_A=set(l1)
    set_B=set(l2)
    set_diff1=set_A.difference(set_B)
    set_diff2=set_B.difference(set_A)
    set_Sym_diff=set_diff1.union(set_diff2)
    list_a=[]
    for element in set_Sym_diff:
        list_a.append(element)
    list_a.sort()
    for element in list_a:
        print(element)
else:
  print("you have put the wrong number of elements, please retry")

#exercise22: Set.add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
i=0
country_set=set()
while i<n:
  a=raw_input()
  a=a.upper()#so that there is no problem about upper and lower characters
  country_set.add(a)
  i+=1
country_list=[]
for country in country_set:
  if country in country_list:
    break
  else:
    country_list.append(country)
print(len(country_list))

#exercise23: set discard,remove and pop
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
list_a=map(int,raw_input().split())
set_a=set(list_a)
m=int(input())
operation_list=[]
number_list=[]
i=0
while i<m:
  operation=raw_input()
  operation_list.append(operation)
  i=i+1
values=[]
commands=[]
for item in operation_list:
    if item!="pop":
        values.append(int(item[-1]))
        commands.append(item[0:-2])
    else:
      commands.append(item)
i=0
j=0
k=0
while i<m:
    if commands[j]=="remove":
        val=values[k]
        set_a.remove(val)
        j=j+1
        k=k+1
    elif commands[j]=="discard":
        val=values[k]
        set_a.discard(val)
        j=j+1
        k=k+1
    elif commands[j]=="pop":
        set_a.pop()
        j=j+1
    i=i+1
for char in set_a:
    print(char)

#exercise24: set.union
x=int(input())
l_eng=map(int,input().split())
y=int(input())
l_fra=map(int,input().split())
english=set(l_eng)
french=set(l_fra)
english_or_french=english.union(french)
print(len(english_or_french))


#exercise25: set.intersection
x=int(input())
l_eng=map(int,input().split())
y=int(input())
l_fra=map(int,input().split())
english=set(l_eng)
french=set(l_fra)
english_or_french=english.union(french)
print(len(english_or_french))


#exercise26: No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
x=map(int,input().split())
list1=list(map(int,input().split()))
set_A=set(map(int,input().split()))
set_B=set(map(int,input().split()))

cont=0
for element in list1:
  if element in set_A:
    cont+=1
 
for element in list1:
  if element in set_B:
    cont=cont-1
print(cont)

#exercise27: set difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
english=set(map(int,input().split()))
m=int(input())
french=set(map(int,input().split()))
english_and_french=english.difference(french)
print(len(english_and_french))

#exercise28: set symmetric difference operations
n=int(input())
english=set(map(int,input().split()))
m=int(input())
french=set(map(int,input().split()))
english_and_french=english.symmetric_difference(french)
print(len(english_and_french))

#exercise29: Collections.counter
shoes_number=int(input())
shoes_instore=list(map(int,input().split()))
customers=int(input())
sum_price=0
for i in range(customers):
  request=list(map(int,input().split()))
  if request[0] in shoes_instore:
    sum_price=sum_price+request[1]
    shoes_instore.remove(request[0])
    
print(sum_price)

#exercise30: Default_dict_tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
A=[]
B=[]

i=0
for i in range(n):
    A.append(str(input()))
    i=i+1
i=0
for i in range(m):
    B.append(str(input()))
    i=i+1
for value in B:
    j=0
    index_list=[]
    while j<n:
        if value==A[j]:
            index_list.append(str(j+1))
            j=j+1
        else:
            j=j+1
    
    if len(index_list)==0:
        print(-1)
    
    else:
      string=index_list[0]
      for char in index_list[1:]:
           string=string+" "+char
      print(string)  
        
        
            

#exercise31: detect floating point number
import re
number=int(input())
values_list=["+","-","."]

for i in range(number):
    value=str(input())
    if value[0] in values_list and value[1] not in values_list and value[-1]!=".":
        x=bool(re.search("\.{1}\S",value))
        print(x)
    else:
      print(False)
#exercise32: re start and re end
import re


string=input()
substring=input()

i=0
j=0
count=0
k=len(substring)
while i<(len(string)):
    x=re.search(substring,string[j:k])
    if x:
       print((j,k-1))
       count+=1
    
    j=j+1
    k=k+1
    i=i+1
if count==0:
  print((-1,-1))    
     

#exercise33:validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())

for i in range(n):
    
    mobile_number=str(input())
    if len(mobile_number)==10:
    
        x=re.search("^[7,8,9]"+"\d",mobile_number)
        if x:
            print("YES")
        else:
            print("NO")
    else:
      print("NO")

#exercise34: validating credit card numbers

import re
n=int(input())
count=0
pre_status="Valid"
for i in range(n):
    credit_card=str(input())
    
    for number in range(1,len(credit_card)-1):
        if count!=4:
            if credit_card[number-1]==credit_card[number]:
                count=count+1
            else:
                count=0
        else:
            pre_status="Invalid"

    
   
    if (len(credit_card)==16 or len(credit_card)==19) and " " not in credit_card and pre_status!="Invalid" and "_" not in credit_card:
        x=re.search("^[4,5,6]",credit_card)
        if x:
            status="Valid"
            print(status)
        else:
            status="Invalid"
            print(status)
        
    else:
        print("Invalid")

#exercise35: array

def arrays(arr):
    result=map(float,arr)
    result.reverse()
    result=numpy.array(result)
    return result
  
#exercise36: zeros and ones
import numpy as np

x=map(int,raw_input().split())

array=np.zeros((x[0],x[1],x[2]), dtype=int)
print(array)
array=np.ones((x[0],x[1],x[0]), dtype=int)
print(array)

#exercise 37: exception
test_cases=int(input())

for i in range(test_cases):
    l1=list(input().split())
    x=l1[0]
    y=l1[1]
    try:
            print(int(int(x)/int(y)))
    except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
    except ValueError:
            z="'"+str(y)+"'".strip(" ") 
            print("Error Code: invalid literal for int() with base 10:",z)
    i=i+1

#exercise 38: Zipped!
N=list(map(int,input().split()))
student_number=N[0]
subject_number=N[1]
i=0
total_list=[]
for i in range (subject_number):
    mark_list=list(map(float,input().split()))
    total_list.append(mark_list)
subject_mark=list(zip(*total_list))
for i in range(student_number):
  marks_sum=sum(subject_mark[i])
  print(round(marks_sum/subject_number,1))
  i=i+1



    

	
	
#problem2

#exercise1: birthday cake candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_height=max(candles)
    result=0
    for x in candles:
        if x==max_height:
            result+=1
        
    return result
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#exercise2: number line jumps
import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    kangaroo1_position=x1
    kangaroo2_position=x2
    result=""
    while (kangaroo1_position!=kangaroo2_position)and kangaroo2_position<=100000000:
        kangaroo1_position=kangaroo1_position+v1
        kangaroo2_position=kangaroo2_position+v2
        if kangaroo1_position==kangaroo2_position:
            result="yes"
        else:
            result="no"
    return result.upper()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#exercise3 viral advertising
def viralAdvertising(n):
    shared=5
    cumulative=0
    i=0
    while i<n:
        floor_liked=shared/2
        liked=math.floor(floor_liked)
        cumulative=cumulative+liked
        shared=liked*3
        i=i+1
    return cumulative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
#exercise4: recursive digit sum
mport math
import os
import random
import re
import sys


def superDigit(n, k):
    sum1=0
    p=n*k
    if len(p)==1:
        sum1=p
    else:
        while len(p)!=1:
            sum1=0
            for x in p:
                sum1=sum1+int(x)
            p=str(sum1)
    return sum1
        
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
#exercise5: insertion sort part one
def insertionSort1(n, arr):
    val=arr[n-1]
    i=n-2
    while i>=0:
        if arr[i]>=val:
            arr[i+1]=arr[i]
            string_list=""
            for x in arr:
              x=str(x)
              string_list=string_list+x+" " 
            print(string_list)
            i=i-1      
        elif arr[i]<val:
            arr[i+1]=val
            string_list=""
            for x in arr:
              x=str(x)
              string_list=string_list+x+" "
            print(string_list)
            i=-1
    return arr





if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)










        








