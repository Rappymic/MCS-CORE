"""

>>> # Type1
... print(10+20)
30

>>> # Type2
... x = 10
>>> y = 20
>>> print(x+y)
30

>>> # Type3 
>>> x = 10
>>> y = 20
>>> result = x+y
>>> print(result)
30


# Assignment opeartors
>>> x = 10  # We are assiging value 10 to variable x
>>> y = 20
>>> res = x+y
>>> x = x+y
>>> # x = +y  x += y
... x += y
>>> print(x)
50
>>> x = 10
>>> y = 20
>>> y = y+x
>>> print(y)
30
>>> y += x
>>> print(y)
40
>>>





# internal external 
35 marks 

# interal Fail external PASS -- PASS valid
# interal Pass External FAIL -- PASS valid   
# interanl PAss Exetrnal PASS - PASS valid 
# interal FAIL Exteranal FAIL - FAIL valid


# Guest  and
Water     Coffee  # Guest "Water and Coffee" 
True  and True    ==> True
True  and False   ==> False 
False and True    ==> False 
False and False   ==> False 

# Guest or
Coffee     Tea     # Guest  'Coffee or Tea'
True   or  True     ==> True
True   or  False    ==> True
False  or  True     ==> True
False  or  False    ==> False

# not
not True ==> False
not False => True 





OR AND NOT 
=============

Guest 
----------



Subjects:
---------
PASS    Tel Hind Eng Maths Sc soc
Fail    F   P    P    P    P   P
        P   P    F    P    P   P/F = Fail 
		
		
        P and Hindi and English and Maths and Scicen and Social 
PASS 

BTech   2   4-2  clered
        Python Linux 
		F      P      = True 
		F      F      = False
		P      P      = True 
		P      F      = True 
	
Guest : 
-----------
OR
=====
Host --> Cofffee OR Tea
              		
	Coffee Tea   
	True   True   --> True 
	True   False  --> True
	False  True   --> True
	False  False  --> False
	
AND
====
Guest --> Water AND Coffee 
          True      True   -- True 
	  True      False  -- False
	  False     True   -- False
	  False     False  -- False 
		  
NOT
-----
True - False
False - True
"""
