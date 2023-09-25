Week-of-0926(Week03Materials).txt

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

Miscellaneous Python features that may be deemed as important :

* Exception handling
* The use of 'type()'
* The issue of NULL (C/C++), null (Java), nil (Lisp/Scheme), and None (Python)
* 16 Finxter puzzles (for you to ponder upon along the way)
* Try to memorize
  - %
  - slice
* Python dictionary vs. C++/Java hashmap
* List as a universal data structure - a detailed exposition
* Numbers, formatted string, and formatted print (Python-printf) - a detailed exposition

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～


～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

                              Exception handling

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

Python's exception handling mechanism is much like Java's exception handling mechanism. The following article is adequate in introducing this topic.   ( Java : try-throw-catch-para ; Python : try-raise-except-as )

     https://python-course.eu/python-tutorial/errors-and-exception-handling.php

Important points :

1. Printing the error message that comes with the exception event

def F() :
  x = int( "four" )

try :
  F()
except ValueError as e :
  print( "The error was :", e )

OUTPUT:
The error was : invalid literal for int() with base 10: 'four'

2. Custom-made exception

class MyException( Exception ) :
  pass

raise MyException( "Construct an appropriate error message ON THE SPOT and put it in here" )

3. Emphasis again

When raising an exception, construct an appropriate error message on the spot and then put it "in" the being raised exception-event.


～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

                             The use of 'type()'

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

Use 'type( <thing> )' to find out about the type of some THING.
```sh
>>> type( 5 )
<class 'int'>

>>> type( 3.5 )
<class 'float'>

>>> type( 0 )
<class 'int'>

>>> type( 0.0 )
<class 'float'>

>>> type( 'hi' )
<class 'str'>

>>> type( '''hi
... hello
... ''')
<class 'str'>

>>> a = 5
>>> type( a )
<class 'int'>

>>> a = 3.5
>>> type( a )
<class 'float'>

>>> type( None )
<class 'NoneType'>

>>> type( NotImplemented )
<class 'NotImplementedType'>

>>> type( (5) )
<class 'int'>

>>> type( (5,) )
<class 'tuple'>

>>> type( a + 3 )
<class 'float'>

>>> type ( 5 > 3 and 3 )
<class 'int'>                # ？？？

>>> type( 5 > 3 and 3 > 1 )
<class 'bool'>

>>> ( 5 > 3 and 3 ) + 10
13
```

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

   The issue of NULL (C/C++), null (Java), nil (Lisp/Schem), and None (Python)

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

First, some explanation of NULL (C/C++), null (Java), nil (Lisp/Schem) ...

# "No such name (in the current name space)" vs. "this name is not bound to any object at the moment"

'None' vs. '()' vs. '[]'     # while '(5)' is ambiguous, '()' is not.  # 'None' is intended to represent "No value"

```py
>>> type( None )
<class 'NoneType'>
                            # <----------------- 這裡的空行是額外加的。下面亦同。
>>> type( () )
<class 'tuple'>

>>> type( [] )
<class 'list'>

>>> None
>>> if None :
...   print( 'YES' )
... else :
...   print( 'NO' )
... 
NO

>>> True and None            # No value
>>> None and True            # No value
>>> True or None             # Has value
True

>>> None or True             # Has value
True

>>> abc                      # 'abc' not defined
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'abc' is not defined

>>> abc=None

>>> abc
>>> print(abc)               # 'abc' is defined to have no value
None
```

# hsia : an engineering solution at best

https://learnpython.com/blog/null-in-python/   # 'None' in Python  # Google : Python null value

#####################

# Actually, Python has () and [] too ...

```py
>>> if 5 :            # Any non-null thing is True
...   print( 'YES' )
... else :
...   print( 'NO' )
... 
YES

>>> if () :            # However, () is considered to be False ...
...   print( 'YES' )
... else :
...   print( 'NO' )
... 
NO

>>> if [] :            # So is []
...   print( 'YES' )
... else :
...   print( 'NO' )
... 
NO

# But how about ANDing or ORing these four : True, False, (), [], and None

>>> True and ()
()

>>> False and ()
False

>>> () and True
()

>>> () and False
()

>>> () or True
True

>>> () or False
False

>>> True or ()
True

>>> False or ()
()

>>> () or []
[]               # <-------------------

>>> [] or ()
()               # <-------------------

>>> () and 5
()

# 找不出以上的完整規律(何時是'()')...

>>> () or [] + [5]
[5]

>>> [] or () + (5,)
(5,)

>>> () or ( [] + [5] )
[5]

>>> () + (5)                 # <------------------ what is this any way???
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "int") to tuple
```

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

           Sixteen Finxter puzzles (for you to ponder upon along the way)

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

(Puzzle 1-1) Easy: The first one should be easy if you're already beyond beginner level in Python:

```py
text = "Python is cool"
split_text = text.split(" ")
join_text = "_".join(split_text)
print(join_text)
```

-> Python_is_cool

-----

(Puzzle 1-2) Intermediate: The second one is harder for beginners but straightforward for intermediates:

```py
def func(num):
  if num == 0:
    return 1
  else:
    return num * func(num-1)

print(func(5))
```

-> 120

-----

(Puzzle 1-3) Hard: The third puzzle can only be solved by more advanced-level coders. Can you?

```py
result = (lambda x, y : x&y)(5,7)
print(bin(result))
```

-> 0b101

-----------------------------------------------------

 (Puzzle 2-1) Intermediate: What is the output of this code?

```py
t = [0, 1, 2]
t.extend([])
t.append([[]])

print(len(t))
```

-> 4
(t = [0, 1, 2, [[]]])

-----

(Puzzle 2-2) Intermediate: Similar in difficulty level - what's the output?

```py
my_list=[('i','f'), ('h','i','gh'), ('o','n'), ('so','x'),
         ('ge','t'), ('Y','e'), ('mo','r','e')]
print(''.join([t[1] for t in my_list]))
```

-> finxter

-----
 
(Puzzle 2-3) Hard: The third puzzle can only be solved by more advanced-level coders. If you're not a Python master I bet you won't be able to solve it.

```py
count = 0

def increment(n):
    count += n
    
increment(5//2 ** 2)
print(count)
```

-> 
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in increment
UnboundLocalError: local variable 'count' referenced before assignment
```

----------------------------------------------

(Puzzle 3-1) Easy: What is the output of this code?

```py
string = 'ppy!'
fruit = 'a'.join(list(string))

print(fruit)
```

-> papaya!

-----

(Puzzle 3-2) Intermediate: What's the output here?

```py
xs = [[1, 2], [3, 4]]
ys = list(xs)

print(xs[0] is ys[0])
```

-> True

-----

(Puzzle 3-3) Hard: I really like this one - I'd say it's hard for intermediate-level coders but easy for experienced coders. What's the output?

```py
t = [2, '32', 2, '252']
t.extend('42')  # t = [2, '32', 2, '252', '4', '2']
print(t.count('2'))
```

-> 1

 -------------------------------------------------------

(Puzzle 4-1) Easy: What is the output of this code?


```py
x = 0

if False or [False] or (False):
  x += 1

print(x)
```

-> 1

-----

(Puzzle 4-2) Intermediate: What's the output here?

```py
d = {0:'Peter', 1:'Tom', 2:'Mary'}
x = d.setdefault(2, 'John')

print(x)
```

-> Mary

-----

(Puzzle 4-3) Hard: And what's the output of this tough one?

```py
class A:
    var = 1

class B(A):
    pass

class C:
    var = 3

class D(B, C):
    pass

print(D.var)
```

-> 1

-------------------------------------------------------

Puzzle 5-1 : What's the output of this code?

```py
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers if n % 2 == 1]
print(squares)
```

-> [1, 9, 25]

-----

Puzzle 5-2 : What's the output of this code?

```py
first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'c': 4, 'd': 5}
third_dict = {'a': 6, 'e': 7}

combined_dict = {**first_dict, **second_dict, **third_dict}
print(len(combined_dict))
```

-> 5
(combined_dict = {'a': 6, 'b': 2, 'c': 4, 'd': 5, 'e': 7})

-----

Puzzle 5-3 : What's the output of this code?

```py
x = "global"

def outer_function():
    x = "outer"

    def inner_function():
        nonlocal x
        x = "inner"
        print(x)

    inner_function()
    print(x)

outer_function()
print(x)
```

->
```
inner
inner
global
```

-------------------------------------------------------

Puzzle JustOne :

```py
fruits = ["Orange", "Strawberry", "Kiwi", "Pineapple", "Mango"]
vitamin_c = [43.2, 58.8, 92.7, 47.8, 36.4]

max_vitamin_c = 0
max_fruit = None
max_index = None

for index, (fruit, vitamin_c) in enumerate(zip(fruits, vitamin_c)):
    if vitamin_c > max_vitamin_c:
        max_vitamin_c = vitamin_c
        max_fruit = fruit
        max_index = index

# Fruit with highest vitamin C with index
print(max_index, max_fruit, max_vitamin_c)
```

-> 2 Kiwi 92.7

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

                              Try to memorize - %

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

a%b 與 a//b (當有小數與負數的時候...)

```py
print( f"4.2%0.5 = {4.2%0.5 : 5.3}" ) 
print( f"4.2//0.5 = {4.2//0.5 : 5.3}" ) 

print( f"-4.2%0.5 = {-4.2%0.5 : 5.3}" ) 
print( f"-4.2//0.5 = {-4.2//0.5 : 5.3}" ) 

print( f"4.2%-0.5 = {4.2%-0.5 : 5.3}" ) 
print( f"4.2//-0.5 = {4.2//-0.5 : 5.3}" ) 

print( f"-4.2%-0.5 = {-4.2%-0.5 : 5.3}" )
print( f"-4.2//-0.5 = {-4.2//-0.5 : 5.3}" ) 
```

The key : a = a//b * b + a%b

```py
>>> print( f"4.2%0.5 = {4.2%0.5 : 5.3}" ) 
4.2%0.5 =   0.2
>>> print( f"4.2//0.5 = {4.2//0.5 : 5.3}" ) 
4.2//0.5 =   8.0
>>> 
>>> 
>>> print( f"-4.2%0.5 = {-4.2%0.5 : 5.3}" ) 
-4.2%0.5 =   0.3
>>> print( f"-4.2//0.5 = {-4.2//0.5 : 5.3}" ) 
-4.2//0.5 =  -9.0
>>> 
>>> 
>>> print( f"4.2%-0.5 = {4.2%-0.5 : 5.3}" ) 
4.2%-0.5 =  -0.3
>>> print( f"4.2//-0.5 = {4.2//-0.5 : 5.3}" ) 
4.2//-0.5 =  -9.0
>>> 
>>> 
>>> print( f"-4.2%-0.5 = {-4.2%-0.5 : 5.3}" ) 
-4.2%-0.5 =  -0.2
>>> print( f"-4.2//-0.5 = {-4.2//-0.5 : 5.3}" ) 
-4.2//-0.5 =   8.0
```

1. a//b 是介於 ceiling與floor之間，取較小的那個


   |             |ceiling|floor|a%b|
   | --- | --- | --- | --- |
   |4.2//0.5|   9    |  8    | 0.2 |
   |-4.2//0.5 |     -8 |       -9 |      0.3 |
   |4.2//-0.5 |     -8  |      -9  |    -0.3 |
   |-4.2//-0.5 |     9  |       8  |    -0.2 |

2. a%b 是 b - a//b * b

How to memorize?

What are the printouts?

```py
  print( f"-10%3 = {-10%3}" ) # 2
  print( f"10%-3 = {10%-3}" ) # -2
  print( f"-10%-3 = {-10%-3}" ) # -1
```

```py
print( "4.2%0.5 = ", 4.2%0.5 )    # 0.5乘以n的最小正餘數 : 0.2
print( "-4.2%0.5 = ", -4.2%0.5 )  # 0.5乘以n的最小正餘數 : 0.3
print( "-10%3 = ", -10%3 )        # 3乘以n的最小正餘數   : 2
```

1. a//b df= "比較小的那個" (假設是c)
2. a%b  df= a - ( c * b )         # This may be the only "all purpose" way of understanding what '%' means in Python

```py
>>> print( -4.2//-0.5 )   # min( 8, 9 ) = 8
8.0
>>> print( -4.2%-0.5 )    # -4.2 - 8*(-0.5)
-0.20000000000000018
```

# This is to satisfy the requirement that      a//b + a%b   =   a

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

                         Try to memorize - slice

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

```py
>>> a = ( 10, 20, 30, 40, 50, 60, 70, 80, 90 )

>>> #############################
>>> a[ 2:5 ]
(30, 40, 50)
>>> a[ 2:-2 ]
(30, 40, 50, 60, 70)
>>> a[ -2:2 ]
()
>>> a[ -2:-1 ]
(80,)
>>> #####
>>> a[ 2:5: ]
(30, 40, 50)
>>> a[ 2:-2: ]
(30, 40, 50, 60, 70)
>>> a[ -2:2: ]
()
>>> a[ -5:-2: ]
(50, 60, 70)
>>> #############################
>>> a[ 2:7:2 ]
(30, 50, 70)
>>> a[ 7:2:2 ]
()
>>> a[ 2:7:-2 ]
()
>>> a[ 7:2:-2 ]
(80, 60, 40)
>>> a[ -2:-7:-2 ]
(80, 60, 40)
>>> a[ -7:-2:-2 ]
()
>>> a[ -2:-7:2 ]
()
>>> a[ -7:-2:2 ]
(30, 50, 70)
>>> a[ 2:-2:2 ]
(30, 50, 70)
>>> a[ -2:2:-2 ]
(80, 60, 40)
>>> a[ 2:-2:-2 ]
()
>>> a[ -2:2:2 ]
()
>>> #############################
>>> a[ 2::2 ]
(30, 50, 70, 90)
>>> a[ 2::-2 ]
(30, 10)
>>> a[ -2::2 ]
(80,)
>>> a[ -2::-2 ]
(80, 60, 40, 20)
>>> a[ :2:2 ]
(10,)
>>> a[ :2:-2 ]
(90, 70, 50)
>>> a[ :-2:2 ]
(10, 30, 50, 70)
>>> a[ :-2:-2 ]
(90,)
>>> #############################
>>> a[ 0: ]
(10, 20, 30, 40, 50, 60, 70, 80, 90)
>>> a[ -1: ]
(90,)
>>> #####
>>> a[ :2 ]
(10, 20)
>>> a[ :-2 ]
(10, 20, 30, 40, 50, 60, 70)
>>> a[ 2: ]
(30, 40, 50, 60, 70, 80, 90)
>>> a[ -2: ]
(80, 90)
>>> #############################
>>> a[ ::2 ]
(10, 30, 50, 70, 90)
>>> a[ ::-2 ]
(90, 70, 50, 30, 10)
>>> a[ :2: ]
(10, 20)
>>> a[ :-2: ]
(10, 20, 30, 40, 50, 60, 70)
>>> a[ 2:: ]
(30, 40, 50, 60, 70, 80, 90)
>>> a[ -2:: ]
(80, 90)
>>> #############################
>>> a[ : ]
(10, 20, 30, 40, 50, 60, 70, 80, 90)
>>> a[ :: ]
(10, 20, 30, 40, 50, 60, 70, 80, 90)
>>> #############################
```

How to memorize???

a[ 起點：終點：increment ]

# 'a' = 'a[:]' = 'a[::]'

規矩：
1. Default方向是 由左往右; increment的default為1(亦即由左往右)
2. 欄位一與欄位二沒寫的要(依照欄位三所specify之方向或default的往右方向)尊重有寫的！(欄位三沒寫就是default的往右方向)
3. 「欄位一+欄位二所explicitly specify之方向」與「欄位三所explicitly/implicitly specifies之方向」必須要一致！如果不一致，就印empty content
   # 欄位一與欄位二只要有一個沒寫(不管欄位三有沒有寫)、方向性的一致性就沒有問題！因為欄位一與欄位二沒寫的必須(依照方向)尊重有寫的。
4. 一旦方向決定了(一致性也OK)，欄位一與欄位二的defaults就是依照此方向而言的「extreme起點」與「extreme終點」(起點的極值與終點的極值)
5. 印起點、依照increment印下一個、直至終點(如果終點是explicitly specifies者、就不含終點; 如果終點是implicitly specifies者、就包括終點)

ＳＯＰ
1. 先看欄位三所述之方向：正數是往右、負數是往左，沒寫就是(default的)往右。
2. 方向一決定、就知道欄位一與欄位二「誰是起點、誰是終點」
3. 起點如果沒寫，那就是依照此方向而言的「extreme起點」(此方向起點的極值)。終點如果沒寫，那就是依照此方向而言的「extreme終點」(此方向終點的極值)。
4. 如果起點與終點的值都有specify，其所述之方向必須與欄位三所述之方向一致，否則就是empty。
5. 印起點、依照increment(其default為1)印下一個、直至終點(如果終點是explicitly specify者、就不含終點; 如果終點是default的極值、就包括終點)

###################################################################################################################

# Meaning of "a slice is a genuine copy of the original"

```py
>>> a = [ 10, 20, 30, 40, 50, 60, 70, 80, 90 ]
>>> b = a
>>> c = a[ : ]

>>> b
[10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> c
[10, 20, 30, 40, 50, 60, 70, 80, 90]

>>> b[5] = 99

>>> b
[10, 20, 30, 40, 50, 99, 70, 80, 90]
>>> a
[10, 20, 30, 40, 50, 99, 70, 80, 90]
>>> c
[10, 20, 30, 40, 50, 60, 70, 80, 90]

>>> #####

>>> a = [ 10, 20, 30, [ 40, 50 ], 60, 70, 80, 90 ]
>>> b = a
>>> c = a[ : ]

>>> a[3][1] = 99

>>> a
[10, 20, 30, [40, 99], 60, 70, 80, 90]
>>> b
[10, 20, 30, [40, 99], 60, 70, 80, 90]
>>> c
[10, 20, 30, [40, 99], 60, 70, 80, 90]

>>> a[1] = 111

>>> a
[10, 111, 30, [40, 99], 60, 70, 80, 90]
>>> b
[10, 111, 30, [40, 99], 60, 70, 80, 90]
>>> c
[10, 20, 30, [40, 99], 60, 70, 80, 90]
```

# Well, a slice is only a SHALLOW copy of the original !


～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

                    Python dictionary vs. C++/Java hashmap

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

### C++ HashMap ###

```cpp
#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
    map<int, string> Players;

    Players.insert(std::pair<int, string>(2, "Lin Dan"));
    Players.insert(std::pair<int, string>(1, "Chen Long"));

    cout << "Number of Players " << Players.size() << endl;
    for (map<int, string>::iterator it = Players.begin(); it != Players.end(); ++it) {
        cout << (*it).first << ": " << (*it).second << endl;
    }
}
```

### C++ HashMap example - END ###

### Corresponding Python code ###

```py
>>> players = {}   # OR : players = dict()
>>> players = dict()
>>> players
{}
>>> players[2] = "Lin Dan"
>>> players[1] = "Chen Long"
>>> print( len( players ) )
2
>>> for key, value in players.items() :
...   print( key, ': ', value )
...
2 :  Lin Dan
1 :  Chen Long
```

### Corresponding Python code - END ###







～～～～～～～～～～～～～～～～～～ break ～～～～～～～～～～～～～～～～～～







～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

           List as a universal data structure - a detailed exposition

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

1. Some preliminaries ...

What is a list (or for that matter, S-expression) for in Lisp/Scheme, and how is it implemented？

The notion of atom in Lisp/Scheme ...

How is everything implemented in Lisp/Scheme？

2. Now, Python tuples and lists ...

Regarding Lisp-styled lists ("tuples"), with the addition of a mutable version ("lists")

tuples ( Lisp styled lists - immutable )
https://www.tutorialsteacher.com/python/python-tuple

3. Understanding Python tuples and lists from the perspective of Lisp/Scheme ...

# ( append t1 t2 )  # OurScheme

```py
>>> t1 = ( 1,2,3 )
>>> t2 = ( 4,5,6 )
>>> t1 + t2
(1, 2, 3, 4, 5, 6)
>>> t2 + ( 7, )     # why is it the case that a one-element tuple has to be expressed as >>(7,)<< whereas a one-element list can be just as >>[7]<< ?
(4, 5, 6, 7)

# ( Nth n t1 ) ### a generalization of 'car' of OurScheme ### ( car t1 ) df= ( Nth 1 t1 )

>>> t1 = ( 1,2,3,4,5,6 )
>>> t1[ 3 ]         # ( Nth 3 t1 )
4
>>> t1[-2]          # Hmmmm.... (有點麻煩)  ### ( Nth (- (length t1) 1 ) t1 )
5

# ( Part start end t1 ) ### generalized 'cdr' of OurScheme  ### the idea of "slice"
# however, notice the difference between 'Part' and 'RemaingPart' ('cdr' is the latter)
# ( cdr t1 ) df= ( RemainingPart 2 t1 ) ### For Python, this is ??? i.e., t1[ ????? ]

>>> t1 = ( 1,2,3,4,5,6 )
>>> t1[ 1 : 3 ]
(2, 3)
>>> t1[ 3 : ]
(4, 5, 6)
>>> t1[ : 3 ]
(1, 2, 3)

# ( cons ( car a ) b )

>>> print(a)
((1, 2), 3, 4)
>>> print(b)
(5, 6, 7)
>>> c = a[ 0 : 1 ] + b     # 這事實上是append而不是cons，But ... (隨便啦！) # Python沒有cons的counterpart ### ( cons <elt> <list> )
>>> print(c)
((1, 2), 5, 6, 7)

# ( cons ( Nth 3 a ) b )   # generalized '( cons (car a ) b )'

>>> d = a[ 2 : 3 ] + b     # how about 'd = a[2] + b' ???
>>> print(d)
(4, 5, 6, 7)

# Values of 'a' and 'b' and 'c' remain unchanged (since 'a' 'b' 'c' 'd' are just NAMES OF VALUES and a list (in OurScheme) is a value)

>>> print(a)
((1, 2), 3, 4)
>>> print(b)
(5, 6, 7)
>>> print(c)
((1, 2), 5, 6, 7)
```

重點：value vs. name-of-a-value

```py
# Anyone who implements OurScheme would know how this (i.e., OurScheme-list, AKA Python-tuple) is implemented!

# 'in' and 'not in' # ( ElementOf a t1 )  ; 'nil' means "NO"

>>> t1 = ( 1,2,3,4,5,6 )
>>> 5 in t1
True
>>> 10 in t1
False
>>> 4 not in t1
False
>>> 10 not in t1
True

# ( define a '( 1,2,3,4,5,6,7 ) )

>>> a = ( 1,2,3,4,5,6,7 )

# ( define b
#          ( append
#            ( append
#              ( Part 1 3 a )         # OR : ( list ( car a ) ( car ( cdr a ) ) )
#              ( list 30 )
#            )
#            ( RemainingPart 4 a )    # OR : ( cdr ( cdr ( cdr a ) ) )
#          )
# )

>>> b = a[ 0 : 2 ] + ( 30, ) + a[ 3 : ]    # >>(30)<< is just >>30<< (and '(' and ')' are just paren.) ; >>(30,)<< is the list >>(30)<<

>>> b
(1, 2, 30, 4, 5, 6, 7)

>>> c = ( 'a','b','c','d','e' )

>>> d = a[ 0 : 2 ] + ( c, ) + a[ 3 : ]

>>> d
(1, 2, ('a', 'b', 'c', 'd', 'e'), 4, 5, 6, 7)

>>> a    # 'a' is still the name of the same value
(1, 2, 3, 4, 5, 6, 7)

>>> c    # 'c' is still the name of the same value
('a', 'b', 'c', 'd', 'e')

# ( eval '( Nth 1 c ) )  # ( eval '( car c ) ) # the evaluation of a Lisp expression (= atom or function call)

>>> eval( c[0] )   # 'a'                       # the evaluation of a Python expression (non-statement)
(1, 2, 3, 4, 5, 6, 7)

>>> eval( c[1] )   # 'b'
(1, 2, 30, 4, 5, 6, 7)

>>> eval( c[2] )   # 'c'
('a', 'b', 'c', 'd', 'e')

>>> eval( c[3] )   # 'd'
(1, 2, ('a', 'b', 'c', 'd', 'e'), 4, 5, 6, 7)

>>> e = d + d
>>> e
(1, 2, ('a', 'b', 'c', 'd', 'e'), 4, 5, 6, 7, 1, 2, ('a', 'b', 'c', 'd', 'e'), 4, 5, 6, 7)

>>> d    # 'd' is still the name of the same value
(1, 2, ('a', 'b', 'c', 'd', 'e'), 4, 5, 6, 7)

>>> eval( c[4] )   # 'e'
(1, 2, ('a', 'b', 'c', 'd', 'e'), 4, 5, 6, 7, 1, 2, ('a', 'b', 'c', 'd', 'e'), 4, 5, 6, 7)
```

---------------------------------------------------------------------

In theory, tuples (Lisp-styled lists) are all we need.
Lists (imperative-language-styled lists) are probably for execution efficiency ...

Python-tuples are for functional-language-styled thinking.
Python-lists are for imperative-language-styled thinking.

---------------------------------------------------------------------

lists (mutable Lisp styled lists)
https://www.tutorialsteacher.com/python/python-list

```py
# same as tuples, with '(' and ')' being replaced by '[' and ']'

# but with the following additions

>>> list1.append( newElement )     # vs. C's 'int_a << 2' # the difference is ...
>>> list1.insert( index, newElement )
>>> list1[ index ] = newElement
>>> list1.remove[ existingElement ]  # # question about efficiency
>>> del list1[ index ]
>>> del list1
>>> list1.pop()           # remove the last one
>>> list1.pop(0)          # the 'pop' we know
>>> list1.pop( i )        # remove( index )
```

```py
list.append() # Add one new item to the end
list.extend() # Adds all the items of the specified iterable (list, tuple,
              # set, dictionary, string) to the end of the list.
list.clear()
list.copy()
list.count()
list.index()
list.insert()
list.pop()
list.remove()
list.reverse()
list.sort()
```

重點：value of a variable  # OR : the binding of a name

Q : a = b

```py
>>> a1 = [ 1,2,3,4,5 ]
>>> a1
[1, 2, 3, 4, 5]

>>> b1 = a1
>>> b1
[1, 2, 3, 4, 5]

>>> a1[3] = 10
>>> a1
[1, 2, 3, 10, 5]

>>> b1
[1, 2, 3, 10, 5]       # <---------- Look here

>>> b1 = b1 + [ 'a', 'b', 'c' ]
>>> b1
[1, 2, 3, 10, 5, 'a', 'b', 'c']

>>> a1
[1, 2, 3, 10, 5]

>>> a1[3] = 200
>>> a1
[1, 2, 3, 200, 5]

>>> b1
[1, 2, 3, 10, 5, 'a', 'b', 'c']  # <---------- Look again
```

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

Numbers, formatted string, and formatted print (Python-printf) - a detailed exposition

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

                                  1. Numbers

```py
>>> 11
11
>>> 011
  File "<stdin>", line 1
    011
    ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
```

############### Good! ###############

# the three below can have any number of digits !

```py
>>> 0b11  # Binary literal         --- 0b… --- binary (only 0 and 1 allowed in …)
3
>>> 0o11  # Octal literal          --- 0o… --- octal (only 0~7 allowed in …)
9
>>> 0x11  # Hexadecimal literal    --- 0x… --- hexadecimal (0~9, a~f allowed in …)
17

>>> 0x020f
527

# 大小寫皆可

>>> 0xFF
255
>>> 0xff
255
```

-----

# strings (including characters) # there are no characters, only strings

```py
>>> 'C'
'C'
>>> type( 'C' )
<class 'str'>

>>> chr( 99 )      # notice the name : 'chr' (originated from Pascal)
'c'
>>> type( chr( 99 ) )
<class 'str'>

                   # --- '\．．．' ---

>>> '\103'         # must be exactly three three octal digits in specifying (the ASCII code of) a character
'C'
>>> '\1031'
'C1'

                   # --- '\x．．' ---

>>> '\x43'         # must be exactly two hexadecimal digits in specifying (the ASCII code of) a charater
'C'
>>> '\x431'
'C1'

                   # --- '…\N{…}…' ---
                   # --- '…\u．．．．…' ---
                   # --- '…\U．．．．．．．．…' ---
```

```
\N{name}           Unicode-character named name in the Unicode database
\uxxxx             Unicode-character with 16-bit hex value xxxx       # exactly four hex digits are required
\Uxxxxxxxx         Unicode-character with 32-bit hex value xxxxxxxx   # exactly eight hex digits are required
```

```py
>>> '\N{comma}'
','
>>> '\u8207'
'與'
>>> '\u8205'
'舅'

>>> 'a\u8207A'
'a與A'

>>> '\u0043'
'C'

>>> '\u82071\u82052\1013\x434'
'與1舅2A3C4'

>>> '\u020f'       # code point : 527
'ȏ'
>>> '\u020F'
'ȏ'
>>> 0x020f
527
>>> chr(527)
'ȏ'
>>> chr(0x020f)
'ȏ'
```

# Unicode doesn’t tell you how to get actual bits from text — just code points. It doesn’t tell you enough about how to convert text to binary data and vice versa.

# Unicode is an abstract encoding standard, not an encoding.

# The Unicode standard (a map of characters to code points) defines several different encodings from its single character set.

# UTF-8 as well as its lesser-used cousins, UTF-16 and UTF-32, are encoding formats for representing Unicode characters as binary data of one or more bytes per character.


----------------------------------------------------------------------------------------------------

                                        2. Formatted string

-----

repr( ... ) df= how is >>...<< represented (when the system is to print >>...<<< as a string)

# Below can be either "..." or '...'

"..."     # ordinary string (with the use of '\' as C-style escape)

r"..."    # raw string (= '...' of shell script ; '\' is not a special char.)  # either 'r' or 'R'

u"..."    # unicode string (???)                                               # either 'u' or 'U'

b"..."    # bytes (i.e., and not a string ; a consecutive sequence of bytes)   # either 'b' or 'B'

f"..."    # formated string (with the use of '{' and '}' enclosing expressions)  # just like first argument of 'printf' # either 'f' or 'F'

-----

'!s' calls str() on the result, '!r' calls repr(), and '!a' calls ascii().

```py
>>> f"To see {a} is to believe what {10 + 20*a} can do"      # <-------------- main spirit of formatted strings ---------------
'To see 123 is to believe what 2470 can do'

>>> f", except in the case of {a!r} and {a!s} and {(20+3)!a}."
', except in the case of 123 and 123 and 23.'
```

-----

```py
>>> import decimal
>>> value = decimal.Decimal("12.34567")
>>> width = 10
>>> precision = 5

>>> f"the value of 'value' is {value:{width}.{precision}}"      # note that '{...}' can be neste
"the value of 'value' is     12.346"
```

----------------------------------------------------------------------------------------------------

```py
>>> today = datetime(year=2017, month=1, day=27)
>>> f"{today:%B %d, %Y}" # using date format specifier
'January 27, 2017'

>>> number = 1024
>>> f"{number:#0x}" # using integer format specifier
'0x400'
```

----------------------------------------------------------------------------------------------------

                                   3. Formatted print (Python-printf)

# Not really formatted print ; just printing a formatted string ...

```py
>>> print( f"the value of 'value' is {value:{width}.{precision}}" )
the value of 'value' is     12.346
```
----------------------------------------------------------------------------------------------------
```py
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))   # <----------------------------------
We are the knights who say "Ni!"

>>> print('{0} and {1}'.format('word1', 'word2'))                  # <----------------------------------
word1 and word2
>>> print('{1} and {0}'.format('word1', 'word2'))                  # <----------------------------------
word2 and word1

>>> print('This {food} is {adjective}.'.format( food='dish', adjective='very dilicious' ) )
This dish is very dilicious.

>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
The story of Bill, Manfred, and Georg.

>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table)
...      )
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

----------------------------------------------------------------------------------------

# A second kind of formatted string in Python (second kind of Python-printf)

################## More in the spirit of C-printf ##################

# Meaning of '%' : a place-holder with print-format-spec.

```py
>>> "This is %f of %f in Python." % (20, 30)           # <------------------------------ printf( "This is %f of %f in Python.", 20, 30 )
'This is 20.000000 of 30.000000 in Python.'

>>> "This is %d of %d in Python." % (20, 30)
'This is 20 of 30 in Python.'

>>> "This is %7.3f of %5.2F in Python." % (10/3, 17/3)
'This is   3.333 of  5.67 in Python.'
```

             %[flags][width][.precision][code]
             where
             flags : Left justify (“-”), Include numeric sign (“+”), Fill in with zeroes (“0”)
             code  : d, f, e, g


----------------------------------------------------------------------------------------------------

# Formatted string revisited

```py
>>> x = 7718

>>> "%d" % x
'7718'

>>> "%-6d" % x
'7718 '

>>> "%06d" % x
'007718'

>>> x = 1.23456789

>>> "%d" % x
'1'

>>> "%f" % x
'1.234568'

>>> "%e" % x
'1.234568e+00'

>>> "%g" % x
'1.23457'

>>> "%g" % (x * 10000000)
'1.23457e+07'
```

# Well, this again makes the above "formatted print"「the printing of a formatted string」, which is rightfully what things are in Python.

# ("There is no formatted-print. There is only printing of formatted-strings.")

----------------------------------------------------------------------------------------------------------------

                                      4. Other miscellaneous things to know ...

# Python does not view 'int' and 'char' as the same thing, nor does it implicitly convert (i.e., coerce) an int to a char or a char to an int ;
# chr() and ord() are provided for the user to explicitly convert between chars and ints ;

```py
>>> print( b'This is' )
b'This is'
>>> print( 'This is' )
This is

>>> type( b'This is' )
<class 'bytes'>
>>> type( b'This is'[0] )
<class 'int'>
>>> b'This is'[0]
84

>>> type( 'This is' )
<class 'str'>
>>> type('This is'[0])
<class 'str'>
>>> 'This is'[0]
'T'

>>> chr(84)
'T'
>>> ord('T')
84

>>> chr( b'This is'[0] )
'T'
>>> ord( 'This is'[0] )
84

>>> int('T')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'T'

>>> str(84)
'84'
```

---------------

```py
>>> 'This is'.encode( "UTF-8" )
b'This is'
>>> ('This is'.encode( "UTF-8" )).decode( "UTF-8" )
'This is'
>>> 'This is'.encode( "UTF-8" ).decode( "UTF-8" )
'This is'

>>> b'ci\xc3\xa0o'.decode( "utf-8" )
'ciào'

>>> '\uc3a0'
'쎠'

>>> 'à'.encode( "utf-8" )
b'\xc3\xa0'
>>> tt = 'à'.encode( "utf-8" )
>>> tt[0]
195
>>> tt[1]
160
>>> tt[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: index out of range
```

-----------------------------------

```py
>>> 'This' ' ' 'is' ' ' 'a' ' ' 'book'
'This is a book'            # string concatenation of this kind is done by the parser (during "compile time")

>>> ( 'This is how Python is able to '        # Comment here okay
... 'handle very very                '        # for very long string extendex across lines
... 'long strings.'                           # END of long string
... )
'This is how Python is able to handle very very                long strings.'
```

-----------------------------------

Google : how do I print with no newline in Python
Better : Python print without newline

Ref. : library.pdf, p. 19


