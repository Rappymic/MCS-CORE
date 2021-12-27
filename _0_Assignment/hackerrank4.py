"""Problem Statement -: Anirudh is attending an astronomy lecture. His 
professor who is very strict asks students to write a program to print the 
trapezium pattern using stars and dots as shown below . Since Anirudh is not 
good in astronomy can you help him? 

 

Sample Input:

N = 3

Output:

**.**

*…*

…..

*…*

**.**"""

n=int(input())
for i in range(n):
    print("*"*(n-1-i)+"."*(2*i+1)+"*"*(n-1-i))
for i in range(n-1):
    print("*"*(i+1)+"."*(2*(n-2-i)+1)+"*"*(i+1))