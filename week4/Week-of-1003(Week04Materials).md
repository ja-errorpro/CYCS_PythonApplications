Week-of-1003(Week04Materials).txt

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

1. Some resemblance in constructs and style between CAL (and hsia-idea) and Python
2. How can a language be "genuinely high-level" (again) - Python as the very first and the only example
3. Function annotation and variable annotation - Introduction and discussion

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

1. Some resemblance in constructs and style between CAL (and hsia-idea) and Python

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

-----

Compared with hsia-styled constructs

-----

conditional :
  if - elif - elif - else    # if - else if - else if - else
  no 'switch'

-----

縮排                         # however, Python does not require the existence of an end-marker

-----

Tabs are replaced (from left to right) by one to eight spaces ... it is unwise to use a
mixture of spaces and tabs for the indentation in a single source file. (p. 7)

------

Too bad there is (still) no 'repeat until'

-----

# 'The Python Language Reference' uses BNF (actually a combination of BNF and RE) and the presentation style is lexical + syntactical (with a complete grammar of course)

ref. : reference.pdf

-----

The assert statement (reference.pdf, 7.3)

  Assert statements are a convenient way to insert debugging assertions into a program:
    assert_stmt ::= "assert" expression ["," expression]

  The simple form, assert expression, is equivalent to
    if __debug__:
      if not expression: raise AssertionError

  The extended form, assert expression1, expression2, is equivalent to
    if __debug__:
      if not expression1: raise AssertionError(expression2)

// note : in C, there is a utility assert( expr ) ; however, it leads to program dump if the given expr fails to be true ;

-----

// hsia-styled constructs in constrast

package CYICE;

/**
 * Debug : A class providing two debugging utilities : Trace() and Assert().
 */
public class Debug {

  /**
   * <pre>
   * A trace-print utility.
   * Print &ltstr> when the given &ltcondition> holds.
   * Example usage : Debug.Trace( debugTrace12, "value of abc : " + abc);
   * </pre>
   */
  public static void Trace(boolean condition, String str) throws Throwable
  {
    if ( condition )
      System.out.println(str);
  } // Trace()

  /**
   * <pre>
   * Assert() checks whether the said &ltcondition> holds.
   * If &ltcondition> does not hold,
   *   then an exception will be thrown, along with &ltstr>.
   * &ltstr> should be something that describes what the "unacceptable error" is.
   * Example Usage : Debug.Assert( numOfPersons >= 0,
   *                               "Wrong value of numOfPersons : " + numOfPersons);
   * </pre>
   */
  public static void Assert(boolean condition, String str) throws Throwable
  {
    if ( ! condition )
      throw new Exception(str);
  } // Assert()

} // class Debug

-----

>>> import pprint    # the 'PrettyPrint' package

>>> t = (((( 'black', 'cyan' ), 'white', (  'green', 'red' )), (( 'magenta', 'yellow' ), 'blue' )))

>>> t   # Notice how a Python printout uses SPACEs
((('black', 'cyan'), 'white', ('green', 'red')), (('magenta', 'yellow'), 'blue'))

>>> pprint.pprint( t, width = 30, indent = 2 )
( ( ('black', 'cyan'),
    'white',
    ('green', 'red')),
  ( ('magenta', 'yellow'),
    'blue'))

# vs.

( ( ( ( 'black',
        'cyan'
      ),
      'white',
      ( 'green',
        'red'
      )
    ),
    ( ( 'magenta',
        'yellow'
      ),
      'blue'
    )
  )
)

# vs.

( ( ( ( 'black', 'cyan' ),
      'white',
      ( 'green', 'red' )
    ),
    ( ( 'magenta', 'yellow' ),
      'blue'
    )
  )
)

# ---------------

>>> t = (((( 'black', 'cyan' ), 'white', (  'green', 'red' )), (( 'magenta', 'yellow' ), 'blue' )),)

>>> pprint.pprint( t, width = 30, indent = 2 )

( ( ( ('black', 'cyan'),
      'white',
      ('green', 'red')),
    ( ('magenta', 'yellow'),
      'blue')),)

# vs.

( ( ( ( 'black', 'cyan' ),
      'white',
      ( 'green', 'red' )
    ),
    ( ( 'magenta', 'yellow' ),
      'blue'
    )
  )
  ,
)

# vs.

( ( ( ( 'black' 'cyan' )
      'white'
      ( 'green' 'red' )
    )
    ( ( 'magenta' 'yellow' )
      'blue'
    )
  )
)

>>class<< and >>type<< are synonymous     # type = class  ## an open secret (= known but very few dare to say it ; reason? well, there are a few.)
# Python goes one step further in making >>int<< a class and >>5<< the name of an object (with attributes of course)
# thus solving the problem of >>value vs. object<< in, e.g., Java

was : value vs. object (C++ and Java)

Python :

  A value (including strings) is considered an (immutable) object

  There are only objects. Some are mutable (list, dictionary, file, user-defined types). Some are not ("values" including tuples)

  And variables are just (temporary) names of objects, and each literal is a name for some object (a string literal may be the name for two or more distinct objects though)

  a = 5 ; a = a + 1    # 'a' is a name for a differenbt object
  b.x = 10             # the object for which 'b' is a name has just changed

There may be two different objects that are exactly the same (but they cannot be numbers) :

>>> a = 'hi there'
>>> id(a)
4382224304
>>> b = 'hi '
>>> c = 'there'
>>> d = b + c
>>> id(d)
4382807856
>>> a
'hi there'
>>> d
'hi there'
>>> id(a)
4382224304
>>> id(d)
4382807856

>>> a==d
True
>>> a!=d
False

>>> a = 50
>>> id(a)
4377986832
>>> b = 3 * 20 - 10
>>> id(b)
4377986832
>>> id(50)
4377986832
>

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

2. How can a language be "genuinely high-level" (again) - Python as the very first and the only example

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

Other aspects of why Python is "genuinely high level"

# The problem of 「你只要...」 (一個害人不淺的觀念)

true is 'True'   (and not "非0")
false is 'False' (and not 0)
not is 'not' (and not '!')
and is 'and' (and not '&&')
or is 'or'   (and not '||')

a = (1,2,3)
if a == 5 :    # ??? Should the system treat it as an error ???
  ...

3+(a:=10)*5

a=(b:=10)

a=b=c
# assignment_stmt ::= (target_list "=")+ (starred_expression | yield_expression)
# An assignment statement evaluates the expression list (remember that this can be a single expression or a comma-separated list, the latter yielding a tuple) and assigns the single resulting object to each of the target lists, from left to right.

a>b>10         # ??? a op1 b op2 c df= a op1 b and b op2 c  # "operator chaining"

# (5,) vs. (5)     # the four (?) meanings of '( ... )'

a[3:]

a[-1]

'string here' "string with 'inner string' here"

print()

use ';' (and not ',') to separate same-line-statements (and not to pretend to be expressions)

no declaration before use (??? if you are willing to think of an assignment as a declaration, then there is still the requirement of declaration before use)

ENTER and not ';'

# "You should know what I mean."  # hsia : well, yes and no ; it is complicated ; guessing is always possible, but to what extent???

the idea of 'in' + the many faces of 'in' ( "ch in <str>", "elt in <tuple>", "elt in <list>", "elt in <set>", "elt in range( from, toButNotInclude, step)" )

>>3 not in list1<< vs. >>not (3 in list1)<<

# IF it CAN BE done to be more user-oriented (i.e., more oriented toward the user), then do it ;

Principle 1 : 更改文法以利使用者   Example : a > b > c  ( or even : a > b < c )    # 都是「本位主義」在作祟...

Principle 2 : "偷偷替換"   Example : 3/5 ;

                          Example : [ (x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2 ]

                          >>> ( (x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2 )
                          <generator object <genexpr> at 0x7fc5702f1660>

                          # 顯然有用到(Python所謂的)generator，問題只在「怎麼做」

                          # What does the first '(' ( and the last ')' ) mean ???






～～～～～～～～～～～～～～～～～～ break ～～～～～～～～～～～～～～～～～～







「 The problem of 【你只要...】」 re-visited：  # 必須要補充一句: 除非你沒有對手！

interpreted  # "trying and exploration" is the norm of today
# [knowing + learning + understanding] by exploration + the use of a system such as PyCharm (for displaying attributes)
# which greatly improves the learning curve
# e.g.,
# >>> a = [10, 20, 30, 40]
# >>> a
# >>> a.insert( 2, 70 )
# >>> a
# >>> a.remove( 3 )
# >>> a
# >>> del a[3]
# >>> a
# >>> a.remove( 70 )
# >>> a
# e.g.,
syntax check (when possible) when you ENTER
# e.g.,
# >>> 5.
# >>> 5.3.
# >>> (5).      # since it is said that >>5<< is an object (>>id(5)<< exists too)
#
# >>> dict1 = { 10 : 'Taipei', 'Hi' : ( 1,2,3 ), 25.8 : [ 3, [ 4, 5 ] ] }
# >>> dict1[10]
# 'Taipei'
# >>> dict1['Hi']
# (1, 2, 3)
# >>> dict1[25.8]
# [3, [4, 5]]
# >>> print( dict1.items() )
# dict_items([(10, 'Taipei'), ('Hi', (1, 2, 3)), (25.8, [3, [4, 5]])])
# >>> print( list( dict1.items() ) )
# [(10, 'Taipei'), ('Hi', (1, 2, 3)), (25.8, [3, [4, 5]])]
# >>> print( list( dict1.keys() ) )
# [10, 'Hi', 25.8]
# >>> print( list( dict1.values() ) )
# ['Taipei', (1, 2, 3), [3, [4, 5]]]
#
>>> a = [ 10, 20 ]
>>> a[0]
10
>>> a[1]
20
>>> a[2]
IndexError: list index out of range

>>> a[5] = 100
IndexError: list assignment index out of range

>>> a[3] = 100
IndexError: list assignment index out of range

>>> a.insert( 5, 100 )
>>> a
[10, 20, 100]

>>> a[3]
IndexError: list index out of range
>>> a[2]
100
>>> len(a)
3

>>> "hi there"[3]
't'
>>> (10, 20, 30, 40)[2]
30

>>> {10, 20, 30, 40}[2]
<stdin>:1: SyntaxWarning: 'set' object is not subscriptable; perhaps you missed a comma?
...
TypeError: 'set' object is not subscriptable

>>> {10:'a', 20:'b', 30:'c', 40:'d'}[2]
...
KeyError: 2

>>> {10:'a', 20:'b', 30:'c', 40:'d'}[20]
'b'

if ( a > b )   vs.    if a > b

# if you require 'if ( a > b )', then '(' and ')' are a MUST ;
# but if it only needs to be 'if a > b', then 'if ( a > b )' is okay too ;

if can-be 直覺，then do so :    # "直覺 is king"
  if ( a > b > c ) ...
  if ( str1 == str2 ) ...
  int1/int2
  str1 + str2
  list1 + list2

Generalization of "small rule-breaking things" :
  'void'  --->  'None'
  "0 is false" "nil is false"  --->   a whole bunch

>>[]<<, >>()<<, and >>set()<< instead of >>NULL<< or >>null<<

Make implicit ones explicit whenever it can help :
  the case of 'self'

"no pointer" (and auto. storage allocation/deallocation)

auto. detection of array index out of range

'=' is assign
'==' is equal
':=' is '=' of C/C++/Java  # the "walrus" operator # difficult for Pascal/Modula people to swallow ...

a lot of convenience tools (but note that Java also has a lot of classes to start with ...)

# last, but not least # to prevent from 縮排errors
>>> def F1( ... ) :
...   <code>
...   <code>
...
>>> # next command here

>>> def A(a) :
...   ...            # Python is even willing to go to an extent that may be considered ridiculous (the use of '... ' to help with indentation)
...   return a + 5
...
>>> A(10)
15

# Even blank lines must have the right indentation (in order that the previous block(s) is/are still "in effect")！！！
# Basic rationality : Indentations tells the system "where we are" in the current block structure of the program (but it may discourage the use of blank lines！)

# There is a small defect in the current indentation requirement of Python ...
>>> for i in range( 3 ) :
...   print( i )
... # what next ?
...   print( i * 2 )
...
0
0
1
2
2
4


# Suppose the following code fragment is in a file ; also suppose that we 'import' this file ; what will happen???
def F2() :
  print( "Within F2() for sure." )

# last line has no indentation (no space) on purpose
  print( "Still within F2()???" )
# END OF the code fragment

# from '011' of Python2 to '0o11' of Python3 (and '011' is error in Python3)

# from '3/4 returns 0' in Python2 to '3/4 returns 0.75' in Python3

# type-casts are considered to be function-calls   ???????????? should it be so ????????????
# well, "creation of new objects"!!!

>>> list( (1,2,3) )
[1, 2, 3]
>>> tuple( [1,2,3] )
(1, 2, 3)
>>> list( { 1:'a', 2:'b', 3:'c' } )
[1, 2, 3]
>>> tuple( { 1:'a', 2:'b', 3:'c' } )
(1, 2, 3)


～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

3. Function annotation and variable annotation - Introduction and discussions

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

             Function annotation (just a way of doing commenting, with no semantics)

An annotation of a function parameter or return value. Function annotations are usually used for type hints.

def sum_two_numbers( a : int, b : int ) -> int :
  return a + b

>>> def f( ham : str, eggs : str = 'eggs' ) -> str :
... print("Annotations :", f.__annotations__)
... print("Arguments :", ham, eggs)
... return ham + ' and ' + eggs
...

>>> def f( ham : str, eggs : str = 'eggs' ) -> str :
...   return ham + eggs
...
>>> f(10, 20)
30

----------------------------------

              Variable annotation (just a way of doing commenting, with no semantics)

count : int = 0

>>> count : int = 0
>>> count = 'Hi! Hello!'
>>> print(count)
Hi! Hello!

----------------------------------

# Use 'mypy' to do type-checking for a script file before running that script
# i.e., assuming that we are now under .../site-packages/
# > ./mypy pythonScript.py
# > ./pythonScript.py

###################################################################################################################

Discussion time ...

###################################################################################################################

                                    Some concluding remarks for the moment

Python = shell-scripting + Lisp-styled list data structure + (a little bit of) hsia-styled constructs + "high level" + what-else-?

The issue of "king of kings" vs. technology integration (considering shell scripts can arrange events)
# Python has the potential of being a programming language that effectively achieves the original "king of kings" intention of shell scripts.
# How should it be done?

Python has brought in non-programming-oriented programmers. It makes "integration of technology of diverse domains" a reality.

Now, what we, as professional programmers, should do?





