Week-of-1024(Week06Materials).txt

---

Parameter passing
* What are there
* How to remember (rules)
* How to use

Concept of unpacking

Relating to C's va_list

How to print without a newline

---

                         Parameter passing in Python

https://towardsdatascience.com/four-types-of-parameters-and-two-types-of-arguments-in-python-357ccfdea3db


--------------------------------------------------------------------------------------------------------------------------------

ㄧㄧㄧ Terminology ㄧㄧㄧ

para.    df= formal para. (of a function definition)
argument df= actual para. (of a function call)

--------------------------------------------------------------------------------------------------------------------------------

ㄧㄧㄧ C/C++/Java ㄧㄧㄧ

The correspondence between the list of arguments and the list of parameters is by position (and position only).
# i.e., no keyword arguments in function calls

# note : C++ supports defaulted parameters though.

--------------------------------------------------------------------------------------------------------------------------------

ㄧㄧㄧ Basic rule ㄧㄧㄧ
```
Function call       :    F( plain-arguments, keyword-arguments )   # keyworded arguments always go BEHIND positional arguments
                            ^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^
                            pos. important   pos. irrelevant

                         注意：已經對應到的positional argument不能再以keyword argument對應之
                              例： def F( a, b, c = 10) : ...  不能用  F( 100, 200, b = 300 ) 呼叫之
```

----- BUT be aware of the appearance of '*' and/or '/' in the parameter list of a function definition ----------------
```py
def F2( other-paras, *, paras-that-must-be-passed-with-the-use-of-keywords ) : ...              # ('*'之後的)pass時必須用keyword
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        pos. irrelevant

def F3( paras-are-matched-by-position-only, /, other-paras ) : ...                              # ('/'之前的)pass時不可用keyword
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        pos. important

def F4( paras-that-are-matched-by-position-only, /, *, paras-that-must-be-passed-with-the-use-of-keywords )
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        pos. important                                 pos. irrelevant
```
----- END - be aware of the appearance of '*' and/or '/' in the parameter list of a function definition --------------

--------------------------------------------------------------------------------------------------------------------------------

ㄧㄧㄧ Basic rule ㄧㄧㄧ

Function definition :    def F( plain-paras, defaulted-paras )   # defaulted paras always go BEHIND paras with no defaults
                                ^^^^^^^^^^^  ^^^^^^^^^^^^^^^
                                positions are always important
```sh
>>> def F( a = 10, b ) :
  File "<stdin>", line 1
    def F( a = 10, b ) :
                     ^
SyntaxError: non-default argument follows default argument       # hsia : should say 'parameter' instead of 'argument'

>>> def F( a, b, c = 10, d = 20 ) :
...   print( 'a = ' + str( a ) )
...   print( 'b = ' + str( b ) )
...   print( 'c = ' + str( c ) )
...   print( 'd = ' + str( d ) )
... 
>>> F( 100, 200 )
a = 100
b = 200
c = 10
d = 20
>>> F( 100, 200, 300 )
a = 100
b = 200
c = 300
d = 20
>>> F( 100, 200, 300, 400 )
a = 100
b = 200
c = 300
d = 400
>>> F( d = 400, c = 300, b = 200, a = 100 )
a = 100
b = 200
c = 300
d = 400
>>> F( 100, c = 300, b = 200, d = 400 )
a = 100
b = 200
c = 300
d = 400

>>> F( 100, c = 300, a = 10000 )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: F() got multiple values for argument 'a'

>>> F( 100, c = 300 )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: F() missing 1 required positional argument: 'b'

>>> F( 100, c = 300, b = 200 )
a = 100
b = 200
c = 300
d = 20
```
--------------------------------------------------------------------------------------------------------------------------------

ㄧㄧㄧ First added complexity ㄧㄧㄧ
```py
def F5( ..., *aTuple, ... ) : ...
```
  *aTuple : the corresponding (variable number of) NON-KEYWORDED arguments are packed as a tuple (named 'aTuple')

### "*aTuple allows us to pass a variable number of non-keyworded arguments to a Python function." ###

Warning : All parameters BEHIND '*para' can only correspond to keyword arguments (they no longer can correspond to positional arguments)
### This is because '*para' will "eat up" all (the remaining) positional arguments and make them one tuple parameter (named 'para') ###

In other words : any parameter BEHIND '*para' must be either defaulted (and thus need not correspond to any argument) or correspond to a keyword argument.

Note also that once a keyword argument appears in a function call, the arguments behind it can only be keyword arguments.

```sh
>>> def F( *a, b ) :     # 'a' is a tuple ; 'b' must correspond to a keyword argument when 'F' is called
...   return sum(a), b
...
>>> F( 10, 20, 30 )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: F() missing 1 required keyword-only argument: 'b'

>>> def F( a, b = 10, *c ) :   # '*c' goes BEHIND a defaulted para ; okay
...   return b + 33
...
>>> F( 10, 20, 30, 40 )
53

>>> def F( a, *b, c = 10 ) :   # '*b' goes BEFORE a defaulted para ; we must use a keyword argument in call if we want to override its default value
...   return c + 33
...
>>> F( 100, 200, 300, 400 )    # since '*b' packs all remaining positional parameters into a tuple named 'b'
43
>>> F( 100, 200, 300, c = 400 )
433

>>> def F( a, *b, c = 10 ) :
...   return sum(b), c
...
>>> F( 100, 200, c = 300, a = 400 )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: F() got multiple values for argument 'a'

>>> F( 100, 200, 345, c = 123 )
(545, 123)

>>> def F( a, *b, c = 10 ) :
...   print( sum(b) )
...   print( c )
...   return c + 10000
... 
>>> F(10, 20, 30)
50
10
10010

>>> F( 10, 20, 30, c = 40, 50 )
  File "<stdin>", line 1
    F( 10, 20, 30, c = 40, 50 )
                              ^
SyntaxError: positional argument follows keyword argument

>>> def F( a, *b, c = 10, d ) :      # the value of 'c' is 10, unless there is a corresponding keyword argument ; 'd' must have a corresponding keyword arg.
...   print( 'a = ' + str( a ) )
...   print( 'sum(b) = ' + str( sum(b) ) )
...   print( 'c = ' + str( c ) )
...   print( 'd = ' + str( d ) )
... 
>>> F( 10, 20, 30, 40, d = 50 )      # no keyword argument corresponding to the parameter 'c' ; okay (since 'c' is defaulted)
a = 10
sum(b) = 90
c = 10
d = 50

>>> F( 10, 20, 30, 40, 50 )          # no keyword argument corresponding to the parameter 'd' ; not okay
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: F() missing 1 required keyword-only argument: 'd'
```

There is nevertheless a small surprise in the above！！！

In the above definition of F(), we see that the rule "There should be NO non-defaulted parameters behind a defaulted parameter" has been broken. Why is it so? Well, this rule is in place because the system must be able to decide about positional correspondence (between arguments and parameter) without encountering any ambiguity. Since there is now an additional rule that says "for each parameter 'p' behind '*para', it must be the case that either 'p' is defaulted or the corresponding argument (in a corresponding function call) is a keyword argument," it is now okay to have non-defaulted parameers behind a defaulted parameter ＩＦ the non-defaulted parameter is ＢＥＨＩＮＤ '*para'. Because the argument (in a corresponding function call) corresponding to 'p' must be a keyword argument now (and cannot be a positional argument).

```sh
# Nonetheless, the system still has to deal with the following.

>>> def F( a, b, c = 10, d = 20 ) :
...   print( a, b, c, d )
... 
>>> 
>>> F( 100, 200, 300 )    # All correspondence is by position (from left to right)
100 200 300 20

# Ambiguity occurs in cases like >>def F( a, b = 10, c, d = 20, e)<<  # which arg. should correspond to what para. for this call >>F(1, 2, 3, 4)<< ???
```


--------------------------------------------------------------------------------------------------------------------------------

ㄧㄧㄧ Second added complexity ㄧㄧㄧ

```sh
def F5( ..., **aHashmap) : ...

  **aHashmap : the corresponding (variable number of) KEYWORD arguments are packed as a hashmap (named 'aHashmap')

### "**aHashmap allows us to pass a variable number of keyword arguments to a Python function." ###

>>> def F( a, b, c, d, **e ) :
...   return a + b + c +d, sum( tuple( e.values() ) )
...
>>> F( 10, 200, e = 300, f = 4000, c = 555, g = 50000, d = 333 )
(1098, 54300)
```


Rule : '**kwpara' must go last in the para. list     
```
# Rationale of the rule : This rule is necessary, because 'kwpara' will "eat up" all the REMAINING keyword arguments (once it starts to "eat"), unless the to-be-eaten keyword arguments already found their counterparts in the parameter list. We must give all the potentially "may be eaten" keyword arguments a chance to find their potentially-may-exist counterparts first (if their counterparts do exis) before they get "eaten."
```

```sh
>>> def F( a = 10, b = 20, **c ) :
...   print( a, b )
...   print( c )
... 
>>> F( 30, x = 100, y = 200, b = 300, z = 400 )
30 300
{'x': 100, 'y': 200, 'z': 400}

>>> def F( *a, **b ) :
...   return sum( a ), sum( tuple( b.values() ) )
... 
>>> F( 10, 20, 30, 40, a = 50, b = 60, c = 70 )
(100, 180)
```

Rule : there can be at most one '*para' and at most one '**kwpara' in a para. list.

Note : both '*para' and 'kwpara' can accommodate the case of "zero or more arguments"

```sh
>>> def F( *a, **b ) :
...   for item in a :
...     print( a, ' ', end = '' )
...   print()
...   for key, value in b.items() :
...     print( 'key :', key, '; value :', value )
...   print()
...
>>> F()

>>> def F( *a, b, **c ) :
...   return sum( a ), sum( tuple( c.values() ) )
... 
>>> F( 10, 20, 30, 40, a = 50, b = 60, c = 70 )   # 'b = 60' corresponds to the parameter 'b' ; the remaining keyword arguments ('a = 50' and 'c = 70') correspond to the parameter 'c'
(100, 120)
```

--------------------------------------------------------------------------------------------------------------------------------

The extra rules concerning the use of '*a' and '**c' :

1. There can be at most one '*para' and at most one '**kwpara' in a parameter list.

2. If '**kwpara' appears in a parameter list, then it has to be the last one in the parameter list. (Hence, '*para' can only appear before it.)

3. Any parameter BEHIND '*para' must be either defaulted (and thus need not correspond to any argument), or correspond to a keyword argument, or '**kwpara'.

--------------------------------------------------------------------------------------------------------------------------------

Thus, suppose ＮＯＮＥ of '*' and '/' appears in the parameter list.

The parameter list of a function definition should look like :

  def F( paras-with-no-default-values, paras-with-default-values, *para, para-with-default-values, **kwpara )

  OR

  def F( paras-with-no-default-values, *para, either-paras-with-no-default-value-but-correspond-to-keyword-arg-OR-paras-with-default-values, **kwpara )

When a parameter list contains '*' and/or '/', the situation is more complex.

  Meaning of '*' : the paras. behind it can only correspond to keyword paras (if they are to correspond to any paras.)

  Meaning of '/' : the paras. before it can only correspond to positional paras (it they are to correspond to any paras.)

--------------------------------------------------------------------------------------------------------------------------------

```sh
>>> def F( a, b, c = 3, d = 5, *e, f = 7, g = 11, **h ) :
...   print( 'a = ' + str( a ) )
...   print( 'b = ' + str( b ) )
...   print( 'c = ' + str( c ) )
...   print( 'd = ' + str( d ) )
...   print( 'sum( e ) = ' + str( sum( e ) ) )
...   print( 'f = ' + str( f ) )
...   print( 'g = ' + str( g ) )
...   print( 'sum( tuple( h.values() ) ) = ' + str( sum( tuple( h.values() ) ) ) )
... 
>>> 
>>> F( 10, 20, 30, 40, 50, 60, g = 70, x = 100, y = 200, f = 80 )
a = 10
b = 20
c = 30
d = 40
sum( e ) = 110
f = 80
g = 70
sum( tuple( h.values() ) ) = 300

>>> F( 10, 20, c = 33, d = 44, A = 50, B = 60, g = 70, x = 100, y = 200, f = 80 )
a = 10
b = 20
c = 33
d = 44
sum( e ) = 0
f = 80
g = 70
sum( tuple( h.values() ) ) = 410

>>> def F( a, b = 10, /, c = 20 ) :  # '/'之前的在pass時不可用keyword
...   print( 'a = ' + str( a ) )
...   print( 'b = ' + str( b ) )
...   print( 'c = ' + str( c ) )
... 
>>> 
>>> F( 100, c = 200 )
a = 100
b = 10
c = 200

>>> F( 100, b = 200, c = 300 )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: F() got some positional-only arguments passed as keyword arguments: 'b'

>>> def F( a, *, b, c = 10 ) :       # '*'之後的在pass時必須用keyword
...   print( 'a = ' + str( a ) )
...   print( 'b = ' + str( b ) )
...   print( 'c = ' + str( c ) )
... 
>>> 
>>> F( 3, b = 5 )
a = 3
b = 5
c = 10

>>> F( 3, 5 )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: F() takes 1 positional argument but 2 were given
```

--------------------------------------------------------------------------------------------------------------------------------

Rule summary

1. ㄧㄧㄧ Basic rule ㄧㄧㄧ

Function call       :    F( plain-arguments, keyword-arguments )   # keyworded arguments always go BEHIND positional arguments
                            ^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^
                            pos. important   pos. irrelevant

                         注意：已經對應到的positional argument不能再以keyword argument對應之
                              例： def F( a, b, c = 10) : ...  不能用  F( 100, 200, b = 300 ) 呼叫之


Function definition :    def F( plain-paras, defaulted-paras )     # defaulted paras always go BEHIND paras with no defaults
                                ^^^^^^^^^^^  ^^^^^^^^^^^^^^^
                                positions are always important


2. ㄧㄧㄧ Argument packing ㄧㄧㄧ

(a) At most one '*para' and at most one '**kwpara' (in a parameter list)

(b) '**kwpara' can only be the last one in a parameter list. (Hence, '*para' can only appear before it.)

(c) Any parameter BEHIND '*para' must be either 
    * defaulted (and thus need not correspond to any argument), or 
    * correspond to a keyword argument, or 
    * '**kwpara' (the last one).

3. ㄧㄧㄧ Mandatory position/keyword correspondence ㄧㄧㄧ

(a) '/'之前的(parameter)在pass時不可用keyword-argument pass   # 如果那小子(那個parameter)有default-value，也可以選擇根本不pass argument過去

(b) '*'之後的(parameter)在pass時必須用keyword-argument pass   # 如果那小子(那個parameter)有default-value，也可以選擇根本不pass argument過去

(a)重新來過   :  '/'之前的(parameter)要pass (argument過去)就只能用position的方式pass

(b)重新來過   :  '*'之後的(parameter)要pass (argument過去)就只能用keyword的方式pass

4. 範例

```sh
  def F( a, b, c = 3, d = 5, *e, f = 7, g = 11, **h ) : 
    ...

  def F( a, b = 10, /, c = 20 ) :  
    ...

  def F( a, *, b, c = 10 ) : 
    ...

  def F( a, b, /, *, c, d = 30 ) :

  def F( a, b, c = 3, /, d = 5, *e, f = 7, g = 11, **h ) : 
    ...

  def F( a, b, c = 3, /, d = 5, *, f = 7, g = 11, **h ) :
    ...

  def F( a, b, c, /, d, *, f, g = 11, **h ) :
    ...

  Syntax error 

    def F( a, b, c = 3, /, *, d = 5, *e, f = 7, g = 11, **h ) :
                                     ^ Invalid syntax at '*' of '*e'


    def F( a, b, c = 3, /, d = 5, *e, *, f = 7, g = 11, **h ) :
                                      ^ Invalid syntax at '*' of '*,'

    def F( a, b, c = 3, d = 5, *e, /, *, f = 7, g = 11, **h ) :
                                   ^ Invalid syntax at '/'

  5. Surprises

  >>> def F( a, b = 10, /, *, c, d = 30 ) :
  ...   print( a, b, c, d )
  ... 
  >>> F( 11, c = 25 )
  11 10 25 30

  # The one above is a surprise that we more or less have discussed earlier.
  
  >>> def F( a, b = 10, c, d = 30 ) :
    File "<stdin>", line 1
      def F( a, b = 10, c, d = 30 ) :
                           ^
  SyntaxError: non-default argument follows default argument
  
  # The above "surprise" also seems to indicate the following.

  >>> def F( a, b = 10, /, *, c = 55, d ) :
  ...   print( a, b, c, d )
  ... 
  >>> F( 11, d = 22 )
  11 10 55 22

  # But how about the situation below?

  >>> def F( a, b = 10, /, c = 55, d ) :
    File "<stdin>", line 1
      def F( a, b = 10, /, c = 55, d ) :
                                     ^
  SyntaxError: invalid syntax

  # And the situation below?
  
  >>> def F( a, b = 10, *, c = 55, d ) :
  ...   print( a, b, c, d )
  ... 
  >>> F( 2, 80, d = 100 )
  2 80 55 100


  # Why is it so, folks？？？
```


--------------------------------------------------------------------------------------------------------------------------------






～～～～～～～～～～～～～～～～～～ break ～～～～～～～～～～～～～～～～～～






--------------------------------------------------------------------------------------------------------------------------------

Python's idea of using '*para' in a parameter list (to pack the corresponding caller arguments in a tuple named 'para') originates from C's 'va_list' (which was used, e.g., for defining printf()).

--------------------------------------------------------------------------------------------------------------------------------

### An example of the 'va_list' of C      # va_list = "Variable number of Arguments in a LIST"

### https://learn.microsoft.com/zh-tw/cpp/c-runtime-library/reference/va-arg-va-copy-va-end-va-start?view=msvc-170

// crt_va.c
// Compile with: cl /W3 /Tc crt_va.c
// The program below illustrates passing a variable
// number of arguments using the following macros:
//      va_start            va_arg              va_copy
//      va_end              va_list

```c
# include <stdio.h>
# include <stdarg.h>
# include <math.h>

double Deviation( int first, ... ) ;    // '...' signifies the use of a  va_list in this function ('*para' of Python) // note that '...' has to be the last one

int main( void ) {

    // Call Deviation() with 3 integers (-1 is used as terminator). 
    printf( "Deviation is: %f\n", Deviation( 2, 3, 4, -1 ) ) ;

    // Call Deviation() with 4 integers (-1 is used as terminator). 
    printf( "Deviation is: %f\n", Deviation( 5, 7, 9, 11, -1 ) ) ;

    // Call Deviation() with just the -1 terminator. 
    printf( "Deviation is: %f\n", Deviation( -1 ) ) ;

} // main()

/* Returns the standard deviation of a list of integers ; Caller must use -1 to terminate this list of integers */
double deviation( int first, ... )  { // 'first' is the first one of the list we need to process ('first' itself is not in the va_list)

    int count = 0 ;
    int num = first ;  // <-----------
    double mean = 0.0, sum = 0.0 ;

    va_list marker ; // to mark where we are now at on the call stack
    va_list copy ;   // a copy of the initial marker value (since we will need to perform a second pass)

    // Initializes 'marker' to retrieve the additional arguments behind the 'first' argument.
    // https://cplusplus.com/reference/cstdarg/va_start/
    va_start( marker, first ) ;     // <----------- let 'marker' point to (the start of) the one behind (the value of) 'first' on the call stack

    va_copy( copy, marker ) ;       // keep a copy of where the 'marker' is right now (since we will need to do a second pass)

    while ( num != -1 ) {

        sum += num ;
        count++ ;

        num = va_arg( marker, int ) ;  // <----------- get one integer and put it in 'num' ; then advance 'marker' 

    } // while num NOT -1

    va_end( marker ) ;                // 收尾 so as to facilitate a normal call return.  // <-----------

    mean = sum ? ( sum / count ) : 0.0 ;

   // Do a second pass (i.e., scan (the relevant part of) the call stack again)

    num = first ;                     // prepare for the calculation of the deviation 

    sum = 0.0 ;
    while ( num != -1 ) {

        sum += (num - mean) * (num - mean) ;

        num = va_arg( copy, int ) ;  // get one integer and put it in 'num' ; then advance the 'copy'

    } // while num NOT -1

    va_end( copy ) ;                 // 收尾 so as to facilitate a normal call return

    return count ? sqrt( sum / count ) : 0.0 ;

} // Deviation()
```

--- Output ---

Deviation is: 0.816497
Deviation is: 2.236068
Deviation is: 0.000000

######### END - C example (for the use of a variable argument list) ##########

--------------------------------------------------------------------------------------------------------------------------------

Python's dictionary corresponds to hashmap of C++ and Java and the concept of "associative array" in PL.

--------------------------------------------------------------------------------------------------------------------------------

### C++ HashMap ###

```c
#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {

    map<int, string> Players;

    Players.insert( std::pair<int, string>( 2, "Chang San" ) ) ;
    Players.insert( std::pair<int, string>( 1, "Wang Wu" ) ) ;

    cout << "Number of Players " << Players.size() << endl ;

    for ( map<int, string>::iterator it = Players.begin() ; it != Players.end() ; ++it ) {
        cout << (*it).first << ": " << (*it).second << endl ;
    } // for

} // main()
```

### END - C++ HashMap example ###

### Corresponding Python code ###

```sh
>>> players = {}   # OR : players = dict()
>>> players = dict()
>>> players
{}
>>> players[2] = "Chang San"
>>> players[1] = "Wang Wu"
>>> print( len( players ) )
2
>>> for key, value in players.items() :
...   print( key, ': ', value )
...
2 :  Chang San
1 :  Wang Wu
```

### END - Corresponding Python code ###

重點：

  PL的associative array是以字串作為array-index (只是由integer-index "進化" 到 字串-index "而已")、只不過這個array並無size的限制

  Python的dictionary則是可以用任何型別的東西作為index、而且可以同一個dictionary之中各個entry的index的型別都不一樣
  Python的dictionary也一樣無size限制(this is a matter of course！ 要知道它的 "同儕" 可是tuple與list！)

  不過：
    Python系統本身在使用dictionary存資料時依舊是偏重以字串作為index

  同時：
    Python系統非常重用dictionary ; Many important Python "stuff" are stored as dictionaries # 當然是指「以字串作為index的dictionaries」

--------------------------------------------------------------------------------------------------------------------------------

Therefore, we had better understand a little bit more about Python dictionaries. Now is a good time to do it.

--------------------------------------------------------------------------------------------------------------------------------

From library.pdf ...

The following examples all return a dictionary equal to { "one": 1, "two": 2, "three": 3 } :

```sh
>>> a = { 'one': 1, 'two': 2, 'three': 3 }
>>> b = dict( one = 1, two = 2, three = 3 )       
>>> c = dict( zip( ['one', 'two', 'three'], [1, 2, 3] ) )
>>> d = dict( [ ('two', 2), ('one', 1), ('three', 3) ] )
>>> e = dict( { 'three': 3, 'one': 1, 'two': 2 } )

>>> a
{'one': 1, 'two': 2, 'three': 3}

>>>> e
{'three': 3, 'one': 1, 'two': 2}

>>> for key, value in a.items() :
...   print( key, ":", value )
... 
one : 1
two : 2
three : 3

>>> for key in e :
...   print( key, ":", e[key] )
... 
three : 3
one : 1
two : 2

>>> c
{'two': 2, 'one': 1, 'three': 3}

>>> d
{'two': 2, 'one': 1, 'three': 3}

>>> e
{'two': 2, 'one': 1, 'three': 3}
```

########### A long-time question by hsia ###########

### How do we specify an array (or linked list) of C-styled-structs in Python ???

```sh
>>> b = [ { 'id' : '10827359', 'name': 'Tom', 'age' : 22, 'score' : 85 }, { 'id' : '10827372', 'name': 'Peter', 'age' : 23, 'score' : 70 } ]
>>> b[1]['score'] = 75

>>> b
[{'id': '10827359', 'name': 'Tom', 'age': 22, 'score': 85}, {'id': '10827372', 'name': 'Peter', 'age': 23, 'score': 75}]

>>> b[0], b[1] = b[1], b[0]

>>> b
[{'id': '10827372', 'name': 'Peter', 'age': 23, 'score': 75}, {'id': '10827359', 'name': 'Tom', 'age': 22, 'score': 85}]

### ??? How about this ??? ###
>>> a = { '10827359' : { 'name': 'Tom', 'age' : 22, 'score' : 85 }, '10827372': { 'name': 'Peter', 'age' : 23, 'score' : 70 }  }
>>> a['10827372']['score'] = 75
```

####################################################

```sh
>>> help( dict )

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  ... # for our current need, we need not look at the special methods
 |
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, default is returned if given, otherwise KeyError is raised
 |  
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |      
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ...
```

To get a deeper feel of the concept of Python dictionaries, let's try to sort the content of a dictionary as an exercise.

# Why Python-dict itself does not provide a 'sort()' method？？？

# Google : how do i sort the items of a dictionary in python
# https://sparkbyexamples.com/python/python-sort-dictionary-by-key/
# also see https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/

```sh
>>> my_dict = { 'Apple' : 5, 'papaya' : 6, 'kiwi' : 4, 'pomegranate' : 11, 'strawberry' : 10 }

>>> print( my_dict )
{'Apple': 5, 'papaya': 6, 'kiwi': 4, 'pomegranate': 11, 'strawberry': 10}

>>> print( type( my_dict ) )
<class 'dict'>

>>> my_dict.items()    # a view of the content of 'my_dict'
dict_items([('Apple', 5), ('papaya', 6), ('kiwi', 4), ('pomegranate', 11), ('strawberry', 10)])

>>> view_of_my_dict = my_dict.items()   # the two are physically connected from now on

>>> view_of_my_dict
dict_items([('Apple', 5), ('papaya', 6), ('kiwi', 4), ('pomegranate', 11), ('strawberry', 10)])

>>> my_dict['Apple'] = 7

>>> my_dict
{'Apple': 7, 'papaya': 6, 'kiwi': 4, 'pomegranate': 11, 'strawberry': 10}

>>> view_of_my_dict
dict_items([('Apple', 7), ('papaya', 6), ('kiwi', 4), ('pomegranate', 11), ('strawberry', 10)])

############ what 'sorted()' is and how to use it ############

>>> help( sorted )     # the function we are going to use for sorting purposes

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.

### preliminary

>>> a = [ 10, 80, 7, 50 ]

>>> sorted( a )    # returns a new list
[7, 10, 50, 80]

>>> a              # 'a' itself remains unchanged
[10, 80, 7, 50]

>>> a.sort()       # call the 'sort()' method of 'a' if we want 'a' itself to be sorted

>>> a
[7, 10, 50, 80]

### more advanced

>>> a = ( ( 'Apple', 5 ), ( 'papaya', 6 ), ( 'kiwi', 4 ) )

>>> sorted( a )
[('Apple', 5), ('kiwi', 4), ('papaya', 6)]

>>> def GetSecondOf( item ) :
...   return item[1]
... 
>>> 
>>> a
(('Apple', 5), ('papaya', 6), ('kiwi', 4))

>>> sorted( a, key = GetSecondOf )
[('kiwi', 4), ('Apple', 5), ('papaya', 6)]

>>> a
(('Apple', 5), ('papaya', 6), ('kiwi', 4))

### continued ...

>>> a = [ ('Apple', 5), ('papaya', 6), ('kiwi', 4) ]    # only a list-object has the 'sort()' method (a tuple-object does not have it)

>>> a
[('Apple', 5), ('papaya', 6), ('kiwi', 4)]

>>> a.sort( key = GetSecondOf )

>>> a
[('kiwi', 4), ('Apple', 5), ('papaya', 6)]
```

############ END - What 'sorted()' is and how to use it ############

```sh
>>> # Sort the (view of a) dictionary by key in ascending order (and then use the result to produce a new dictionary)

>>> new_dict = dict( sorted( my_dict.items() ) ) 

>>> new_dict
{'Apple': 7, 'kiwi': 4, 'papaya': 6, 'pomegranate': 11, 'strawberry': 10}

>>> my_dict
{'Apple': 7, 'papaya': 6, 'kiwi': 4, 'pomegranate': 11, 'strawberry': 10}

###

>>> # Sort the (view of a) dictionary by key in descending order (and then use the result to produce a new dictionary)

>>> new_dict = dict( sorted( my_dict.items(),  reverse = True ) ) 

>>> new_dict
{'strawberry': 10, 'pomegranate': 11, 'papaya': 6, 'kiwi': 4, 'Apple': 7}

>>> my_dict
{'Apple': 7, 'papaya': 6, 'kiwi': 4, 'pomegranate': 11, 'strawberry': 10}

###

>>> # Sort the keys of a dictionary and then produce a new dictionary from the result and the original dictionary using dict comprehension

>>> my_dict.keys()
dict_keys(['Apple', 'papaya', 'kiwi', 'pomegranate', 'strawberry'])

>>> keys = list( my_dict.keys() )

>>> keys
['Apple', 'papaya', 'kiwi', 'pomegranate', 'strawberry']

>>> keys.sort()

>>> new_dict = { key : my_dict[key] for key in keys }

>>> new_dict
{'Apple': 7, 'kiwi': 4, 'papaya': 6, 'pomegranate': 11, 'strawberry': 10}

>>> my_dict
{'Apple': 7, 'papaya': 6, 'kiwi': 4, 'pomegranate': 11, 'strawberry': 10}

###

>>> # Only sort the keys of a dictionary

>>> sorted( my_dict )
['Apple', 'kiwi', 'papaya', 'pomegranate', 'strawberry']

###

>>> # Sort the (view of a) dictionary by value in ascending order (and then use the result to produce a new dictionary)

>>> my_dict
{'Apple': 7, 'papaya': 6, 'kiwi': 4, 'pomegranate': 11, 'strawberry': 10}

>>> my_dict.items()
dict_items([('Apple', 7), ('papaya', 6), ('kiwi', 4), ('pomegranate', 11), ('strawberry', 10)])

>>> sorted( my_dict.items(), key = lambda item: item[1] )
[('kiwi', 4), ('papaya', 6), ('Apple', 7), ('strawberry', 10), ('pomegranate', 11)]

>>> new_dict = dict( sorted( my_dict.items(), key = lambda item: item[1] ) )

>>> new_dict
{'kiwi': 4, 'papaya': 6, 'Apple': 7, 'strawberry': 10, 'pomegranate': 11}

>>> my_dict
{'Apple': 7, 'papaya': 6, 'kiwi': 4, 'pomegranate': 11, 'strawberry': 10}

########################## Time to find the answer for a previous question raised in class ###########################

>>> help( print )
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

--------------------------------------------------------------------------------------------------------------------------------

                                            Concept of unpacking

--------------------------------------------------------------------------------------------------------------------------------

```sh
# '*' is the "unpacking" operator for iterables (e.g., tuple/list/the-list-of-keys-of-a-dictionary) ;
# '**' is the unpacking operator for dictionaries ; used either for redefining a new dictionary or for passing a list of keyword arguments
# 
# That is, '*a' means "a unpacked" and '**d' means "d (normally a dictionary) unpacked"
# '*a' and '**d' are used for passing a list of (the unpacked) things as arguments when calling a function, including defining a new list/tuple/dictionary.

>>> y
(3, 30)

>>> print( y )
(3, 30)

>>> print( *y )     # = print( y[0], y[1] )
3 30

>>> sum( y )
33

>>> sum( *y )       # = sum( y[0], y[1] )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable

>>> d = { 'k1':10, 'k2':20, 'k3':30 }

>>> *d
  File "<stdin>", line 1
SyntaxError: can't use starred expression here

>>> **d
  File "<stdin>", line 1
    **d
    ^
SyntaxError: invalid syntax

>>> def F( k1, k2, k3 ) :
...   print( type( k1 ) )
...   print( k1, k2, k3 )
... 
>>>

>>> F( **d )        # = F( k1 = 10, k2 = 20, k3 = 30 )
<class 'int'>
10 20 30

>>> F( *d )         # = F( 'k1', 'k2', 'k3' )
<class 'str'>
k1 k2 k3

>>> ( *d, )         # = ( 'k1', 'k2', 'k3' )
('k1', 'k2', 'k3')

>>> [ *d ]          # = [ 'k1', 'k2', 'k3' ]
['k1', 'k2', 'k3']

>>> { *d }          # the specification of a set
{'k2', 'k3', 'k1'}

>>> type( { *d } )
<class 'set'>

>>> { **d }         # = dict( k1 = 10, k2 = 20, k3 = 30 )  # OR implicitly deciding to use ':' instead of '=' upon seeing the enclosing '{' and '}'？？？
{'k1': 10, 'k2': 20, 'k3': 30}

>>> print( *d )     # = print( 'k1', 'k2', 'k3' )
k1 k2 k3

>>> print( **d )    # = print( k1 = 10, k2 = 20, k3 = 30 )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'k1' is an invalid keyword argument for print()

>>> players = { 2 : 'Chang San', 3 : 'Lee Four' }
>>> players
{2: 'Chang San', 3: 'Lee Four'}

>>> more_players = { 4 : 'Wang Wu', 2 : 'Lee Who' }
>>> more_players
{4: 'Wang Wu', 2: 'Lee Who'}

>>> team = { **more_players, **players, 5 : 'Liu Seven' }
>>> team
{4: 'Wang Wu', 2: 'Chang San', 3: 'Lee Four', 5: 'Liu Seven'}


#####


# '*' can also appear on the left hand side of an assignment symbol ('='). Just think of an assignment as a function call！！！

>>> first, second = (10, 20)
>>> first
10
>>> second
20

>>> first, *rest = (10, 20, 30, 40)
>>> first
10
>>> rest
[20, 30, 40]

>>> *firstOnes, last = (10, 20, 30, 40)
>>> firstOnes
[10, 20, 30]
>>> last
40

>>> car, *cdr = ( (1, 2), 3, (4, 5) )
>>> car
(1, 2)
>>> cdr
[3, (4, 5)]

>>> a, b, *c, d = range( 20 )   # just replace 'range(20)' with any iterable
>>> a
0
>>> b
1
>>> c
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
>>>
>>> d
19

# An application of the use of the unpacking operator ('*') on the left hand side of an assignment statement

>>> sentence = "This will be the start of a beautiful friendship."

>>> sentence.split(" ")
['This', 'will', 'be', 'the', 'start', 'of', 'a', 'beautiful', 'friendship.']

>>> sentence.split(" ", maxsplit = 3)
['This', 'will', 'be', 'the start of a beautiful friendship.']

>>> *firstOnes, last = sentence.split(" ", 3)

>>> firstOnes
['This', 'will', 'be']

>>> last
'the start of a beautiful friendship.'


#####


# But ...
# note that when '*a' or '**d' appears in a parameter list, it means something different. 
# This is somewhat similar to the case of '*p' in 'Student F( Student *p ) ;' in C. 
#    Here, '*p' no longer means "the Student struct pointed at by 'p' ". 
#    Instead, it means "p is a pointer that (can) point to a Student struct"
# When '*a' appears in a parameter list, it means " 'a' is a list of the corresponding caller (unkeyworded) arguments."
# When '**d' appears in a parameter list, it means " 'd' is a dictionary of the corresponding caller keyworded arguments."

>>> def function( *arg ) :
...   print( type(arg) )
...   for i in arg :
...     print (i)
>>> function(1,2,3)
<class 'tuple'>
1
2
3

>>> def my_func(man, *para, opt = 'default', **kwpara):
...   print()
...   
...   print( man )
...   print( para )
...   print( opt )
...   print( kwpara )
>>> 
>>> my_func('mandatory value', 'a', 'b', 'c', name='Chris', age=33)

mandatory value
('a', 'b', 'c')
default
{'name': 'Chris', 'age': 33}
```

-------


# A little bit more practices

```sh
# *c : arbitrary number of arguments (wrapped in a tuple named 'c')
# def F1( a, b, *c )  # starting with the third argument, '*c' packs all remaining non-keyword arguments into a tuple named 'c'

def Print( *args )    # suppose we use >>Print(1, 2, 3)<< to call this routine
  print( args )       # prints the tuple ; we get >>(1, 2, 3)<<
  print( *args )      # prints the "unpacked result of the tuple" ; we get >>1 2 3<<

print( *(1, 2, 3) )   # >>1 2 3<<

def Print( a, *args, b ) :  # 'args' is a tuple ; when called, 'b' must be specified using a keyword argument
  print( b, *args, a )      # 'args' is being unpacked here

Print( 3, 4, 5, 6, b = 7 ) # we get >>7 4 5 6 3<<
```

--------------------------------

Discuss why this design of parameter-passing is easy to learn.

Should there be syntax restrictions for different levels of software developments?

--------------------------------

######################## How to meorize - THE FINAL COUNT - written on 2023-11-01, revised on 2023-11-21 ########################

Arguments of a function call

  positional
  keyword

  Rule : Keyworded arguments can only go behind positional arguments (no exception)

Parameters of a function definition

  no-default
  with default

  /                       # meaning : if there is an argument corresponding to a parameter preceding '/', that argument must be positional
  *                       # meaning : if there is an argument corresponding to a parameter behind '*', that argument must be keyworded

  *aTuple                 # recall the game PacMan ('aTuple' will "eat up" all the remaining positional arguments)
  **aDict                 # recall the game PacMan ('aDict' will "eat up" all the remaining keyworded argumebts)

  Rule : A defaulted parameter can only go behind parameters without defaults UNLESS this parameter is behind '*'

  Rule : '**aDict' can only be the last one in the parameter list (of the being defined function)

```sh
>>> def F( a=10, b=20, *Tuple, c=30, d ) :
...   print( a, b, aTuple, c, d )
... 
>>> 
>>> F( 100, 200, 300, 400, 500, 600, d = 700 )
100 200 (300, 400, 500, 600) 30 700
```

######################## END - How to meorize - THE FINAL COUNT - written on 2023-11-01, revised on 2023-11-21 ########################




