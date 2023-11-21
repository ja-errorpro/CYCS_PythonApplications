Week-of-1031(Week07Materials).txt

---

Variables (or rather, names) : Part I

* What does "pointer and struct" have to do with the "name-object" paradigm
* Variables (or rather, names) can come into existence when ...
* Restricted re-declaration of "system variables"
* Regarding import
* Global var. and local var. VS the use of 'global' and 'nonlocal'

---


---

1. What does "pointer and struct" have to do with the "name-object" paradigm

---

   Come to class！！！

---

2. Variables (or rather, names) can come into existence when ...

---

# Variables (or rather, names) can come into existence as a result of executing 
# the THEN (or ELSE) part of a statement

```sh
>>> a = c = 4

>>> print( b )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined

>>> if c == 4 :
...     a = 10
...     b = 20 # 'b' declared here
... 
>>> 
>>> print( "a :", a, "b :", b)  # 'b' exists only because 'c' was 4 (and 'if' entered)
a : 10 b : 20                   # If the 'if' was not entered, 'b' would not have existed

# Variables can also come into existence as a result of making a function call

>>> print( a )
10

>>> def F1() :      # globals have to be declarewd to be 'global' in a function definition
...     global x    # By default, variables appearing in the definition of a function are
...                 # assumed to be locals
...     x = 250
...     if x > 100 :
...         y = 30
...     # print(x, a, y) # 'a' unresolved reference
...     a = 1000         # local 'a' now comes into existence
...     print( "x :", x, "a :", a, "y :", y) # 'y' exists only because 'x' bigger than 100
...                                          # (and 'if' entered)
... 
>>> 
>>> print( "x : ", x )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined

>>> F1()
x : 250 a : 1000 y : 30

>>> print( a )    # still 10 ; not 1000
10

>>> print( x )    # 'x' has come into existence
250

>>> print( y )    # why?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined

# Currently existed names can also be deleted by using the 'del' command

>>> del a

>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined

>>> del F1

>>> F1()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'F1' is not defined

# Supposed we do ("elaborate" to be more precise) 'Student * p = new Student ;' in a C function. 
# What will happen to the "newly created Student node" when the function call returns (say to 'main()')? (For sure, 'p' no longer exists when we are back to main().)

```

---

3. Restricted re-declaration of "system variables"

---

```sh
>>> len( (1,2,3) )
3

>>> len = 4          # 'len' can be made a variable name

>>> len( (1,2,3) )   # now 'len' is no longer a function name ; it is an integer (object) now
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable

# sum = 5 # but 'sum' cannot be made a variable name
print( sum( [5, 6, 7] ) )

# print = 3 # nor can 'print' be made a variable name

# Q : Just what basic functions can be overridden???

# How about keywords? Can they be overridden?

# To get a listing of Python keywords : help() | keywords | q

>>> help()

Welcome to Python 3.9's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               break               for                 not
None                class               from                or
True                continue            global              pass
__peg_parser__      def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield

help> q

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>>

```

---

4. Regarding import

---

                                有關Python import

1. 我們可以在(the fictitious) top level (module) 'import'，我們也可以在任何(real) module (之中) 'import'。

2. 執行'import Module1'會導致(among other things)'Module1'裏的code(e.g., creating classes and functions、宣告names、and 建立bindings)被執行

3. 系統在執行'import'時、必須要能找到「我們所要import的東西」，否則就是error (of course)。

4. Default是try out所有'sys.path'所説的絕對路徑(absolute path)

   e.g., 'import dir1.dir2.moduleXYZ' (或 'from dir1.dir2.moduleXYZ import *')
         # recall Java-styled import ; e.g., import java.util.*
         就是要系統依序try out 'sys.path'所説的絕對路徑(absolute path)
         看哪一個絕對路徑之下有dir1這個目錄、而dir1之下又有dir2、而dir2之下有moduleXYZ這個檔案
         一找到就import該模組(import the first one found)
         找不到就是error

5. 換言之，如果有任何module系統說它無法找到、而我們知道那個module在哪裏，理論上、只要把那個module所在的directory的絕對路徑加入sys.path即可import該module
   (自己要注意系統是否能真正執行或正確執行該module裏面的東西)

```sh
>>> pprint( sys.path )
['/Users/myUserID/bin',
 '/Users/myUserID/bin',
 <SomeDir>,                 # the directory in which we invoked this version of Python (Python 3.9)
 '/Users/myUserID/opt/anaconda3/lib/python39.zip',
 '/Users/myUserID/opt/anaconda3/lib/python3.9',
 '/Users/myUserID/opt/anaconda3/lib/python3.9/lib-dynload',
 '/Users/myUserID/opt/anaconda3/lib/python3.9/site-packages',
 '/Users/myUserID/opt/anaconda3/lib/python3.9/site-packages/aeosa']

>>> type( sys.path )
<class 'list'>

>>> help( list )    # to exit the interaction with help(), press 'q'
 ...
 |  ...
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  ... 
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  ...

>>> sys.path.append( '/Users/myUserID/magicDir' )

>>> sys.path.insert( 0, '/Users/myUserID/OneMoreMagicDir' )

>>> pprint( sys.path )
['/Users/myUserID/OneMoreMagicDir',
 '/Users/myUserID/bin',
 '/Users/myUserID/bin',
 <SomeDir>,
 '/Users/myUserID/opt/anaconda3/lib/python39.zip',
 '/Users/myUserID/opt/anaconda3/lib/python3.9',
 '/Users/myUserID/opt/anaconda3/lib/python3.9/lib-dynload',
 '/Users/myUserID/opt/anaconda3/lib/python3.9/site-packages',
 '/Users/myUserID/opt/anaconda3/lib/python3.9/site-packages/aeosa',
 '/Users/myUserID/magicDir']

# Now we should be able to import the modules under the two newly added directories

# 先這樣 (還有一些較囉唆的東西以後再談)

###
```

The 4 ways to import a module (https://www.pythonmorsels.com/4-ways-import-module-python/)

Import the whole module using its original name: 

  import random

Import specific things from the module: 

  from random import choice, randint

Import the whole module and rename it, usually using a shorter variable name: 

  import pandas as pd

Import specific things from the module and rename them as you're importing them: 

  from os.path import join as join_path

That last one is usually done to avoid a name collision or sometimes to make a more descriptive name (though that's not very common).

###

另： 雖然可以這樣做，但強烈建議不要這樣做(除非有很好的理由)： 

  from module123 import *      # 這樣就可以不要 module123.F() 或 module123.name1，直接 F() 或 name1 即可。

---
5. Global var. and local var. VS the use of 'global' and 'nonlocal'

---

             A thorough understanding of 'global' and 'nonlocal' declarations

Bear in mind !!!
 
  assign = (re-)declare 

  Default : we are always declaring a variable in "the current namespace" (the "namespace" of the current module, function, or object) ！！！

----- A quick review of 'global' and 'local' in C/C++ -----

global df= in a file and outside of all functions (without a 'static' prefix)

file-scope df= in a file and outside of all functions, with a 'static' prefix

local df= inside a function

nested locals df= locals declared within blocks

scope of global vs. scope of file-scope vs. scope of nested local

C/C++/Java uses static scoping (scope of a variable is determined by program layout) for determining the scope of a variable (= where the variable can be accessed in the program)

----- Similarities and differences between 'import' of Python and 'include' of C/C++ and 'import' of Java -----

Python
  You must 'import' a module in order to use anything belonging to that module.
  You can 'from module123 import *' or 'import module123 as m' (and then either m.F(), m.abc, or directly F(), abc)
  If you 'from module123 import *' AFTER you have defined (= assigned something to) your 'abc', then 'abc' is in fact 'module123.abc' at this point.  # Why?

C/C++
  Once you have included stdio.h (or cstdio), the compiler will accept your calls to printf(), and prinft() is considered the same as any other function.
  If you define a printf() of your own, the compiler will use your printf() for any call to printf(), even if you have included stdio.h (or cstdio).  # Why？
  For variables such as 'stdin' (and 'stdout' and 'stderr'), the situation is the same.

Java
  Once you have imported java.util.ArrayList, you can use 'ArrayList' to create new array-list objects. E.g., 'a = new ArrayList<String>() ;'
  However, even if you have not imported java.util.ArrayList (or java.util.* for that matter), you can still use 'java.util.ArrayList' to create new array-list objects. (e.g., 'a = new java.util.ArrayList<String>() ;' ) # Why?

----- Some Python basics -----

# Terminology :
#   to reference a variable df= to get the value of the variable
#   to update a variable df= to change the value of the variable
#   to access a variable df= to reference and/or update the variable
#
# There is a distinction among these three terms, especially in the case of Python.

Basically, 

Python uses 'global' to refer to variables (names) that are declared (= assigned a value) on the top-level (inside of a module, outside of all functions)

Python functions can have "local functions."

'Globals' of a module can be referenced by all functions within the module.

Python uses 'local' to refer to variables (names) that are declared (= assigned a value) inside of a function

Python does not have the notion of "nested locals."

---

An example of nested local functions 
# One other reason why Python is "genuinely high level" : 以下的function code還真的syntactically correct and executable！

```py
def F() :
  def F1() :
    def F12() :
      def F123() :
        def F1234() :
          
          ...
        # END - F1234()
        
        ...
      # END - F123()
      
      ...
    # END - F12()
    
    ...
  # END - F1()
  
  def F2() :
    def F22() :
      def F223() :
        def F2234() :
          
          ...
        # END - F2234()
        
        ...
      # END - F223()
      
      ...
    # END - F22()
    
    ...
  # END - F2()
  
  F1()
  F2()
# END - F()

>>> F()

```
---

"Namespaces in Python are implemented as Python dictionaries, that is, they are defined by a mapping of names, i.e. the keys of the dictionary, to objects, i.e. the values." https://python-course.eu/python-tutorial/namespaces.php

---

The "variable search process" :

  from the enclosing function (its local names), to the nearest enclosing function (its local names), to the next enclosing function (its local names), etc., to the current module's global names, and finally to the namespace containing the built-in names of the Python interpreter

---

Should there be syntax restrictions (for the use of variables) for different levels of software developments？？？ - Just a question for you to think about

---

What is a local function for? (Why do we need local functions?)

Local functions? Local variables? Local (inner?) classes? What are the rationale for these things?  - Always a question to ponder upon

--- END - Some Pythonb basics ---

----- Prelude (序曲) -----

```sh
>>> def F() :
...   print( s )      # note that 's' is not defined in F()
...
>>>

>>> s = "Kaohsiung"   # this makes 's' a global variable (or name) of the (fictitious) "top level module"

>>> F()               # F() can reference a global variable (name) such as 's'
Kaohsiung

>>> def F() :
...   s = "Taipei"
...   print( s )
...
>>>

>>> F()
Taipei                 # of course

>>> print( s )
Kaohsiung              # ？？？

>>> def F() :          # Rewrite F()
...   print( s )
...   s = "Taipei"
...   print( s )
...
>>>

>>> print( s )         # just to show that 's' is (still) a legitimate global variable (name)
Kaohsiung

>>> F()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in F
UnboundLocalError: local variable 's' referenced before assignment     # This error msg is refering to the first 'print(s)' of F()

# What is going on here???
```

----- END - Prelude (序曲) -----


# 正戲開演！

# Note : 
#   The following descriptioon of 'global' and 'nonlocal' is now outdated; it is deliberately left here to show how things in Python could be so easily misunderstood. (Almost all of what is said here is true, and there is a very high chance that you won't even notice the small misleading part of it.)
#   The updated description of 'global' and 'nonlocal' is located at the end of this section (below all examples).
#   However, it is strongly suggested that you don't look at the updated version now. Because we want to "find things out" by examining several examples.
#   If you look at the updated description now, you will miss the fun.

'global' :

1. global-var df= a variable that was/will-be delared(=assigned) on the top level (= outside of the definition of any function or class)

2. A global-var (if it already exists) can be refrenced by any function (whatever its level is) without having to be declared to be 'global' by that function (IF the function does not have a local var. with the same name).

3. To change the value of a global-var in a function (whatever its level is), we must use 'global' to declare that the var is global.

4. To declare a var as 'global' (in a function), the var does not have to exist when the system accepts the definition of that function.

'nonlocal' :

1. non-loca-var df= a variable that is declared (whether by using an assignment or a 'nonlocal' declaration) in the IMMEDIATE enclosing function (of the current function).

2. If a var. is only referenced and not declared (whether by using an assignment or a 'nonlocal' declaration) in a function, that var must be either a global variable (second priority) or a variable that is declared (whether by using an assignment or a 'nonlocal' declaration) in the immediate enclosing function (first priority).

3. To declare a var as 'nonlocal', it has to be the case that there is a declaration (whether by using an assignment or a 'nonlocal' declaration) of that var in the immediate enclosing function.

---

The "game" now is to verify what is just said in the above (about the use of 'global' and 'nonlocal' and the meaning of global and local in Python). 

---





```
    ～～ break ～～
```





# Below, we will go through several examples. Each example first shows a definition of the function F1(), with nested functions in it, and then calls F1(). 

# Function calling sequence : F1() -> F12() -> F123() -> F1234(), with F1234() attempting to reference (and print) one, maybe two, non-local variables.

# One of the focuses of these examples is to find out about the answer to the following question :
#
#   If a function has a local var. (a local name), can this local var. (or local name) be referenced by ALL its "descendant functions"?
#
#   (On first thought, the answer seems to be YES, since a global var. can be referenced by any function.)
# 
#   e.g.,
#

```sh
>>> def G1() :
...   def G12() :
...     def G123() :
...       
...       print( abcde ) ;    # 'abcde' is not defined in G123() (or any enclosing function for that matter)
...     
...     G123()
...   
...   G12()
... 
>>> 
>>> abcde = 12345 ;           # defining 'abcde' on the top level (the fictitious "top level module")

>>> G1()                      # Calling G1() ;   G1() -> G12() -> G123() -> 'print( abcde )'
12345
```

#############################

# Example 1 :

# Below shows that even when a local variable named a0319_1348 IS defined in F12() before F12() calls F123(), F1234() still cannot "see"
# a0319_1348 when there is NO local variable named a0319_1348 defined in F123().

# But as long as there IS a local var. named a0319_1348 defined in F123() when F123() calls F1234(), F1234() will always "see" 
# a0319_1348.

```sh
>>> def F1() :
...   
...   def F12( b12 ) :      # b12  df= whether to define 'a0319_1348' before calling F123()
...     
...     def F123( b123 ) :  # b123 df= whether to define 'a0319_1348' before calling F1234()
...       
...       def F1234() :     # just to REFERENCE the value of 'a0319_1348' (and print its value) # 'a0319_1348' is non-local (= not a local var.)
...         
...         print( "Printing the value of a0319_1348 in F1234() :", a0319_1348 )
...         
...       # END - F1234()
...       
...       # we are now properly within F123()
...       
...       if b123 : # i.e., I am asked to define 'a0319_1348' before calling F1234()
...         
...         print( "F123() now defines a0319_1348." )
...         a0319_1348 = 'Defined in F123()'
...         
...       else :    # I am asked not to define a0319_1348 before calling F1234()
...         print( "F123() does not define a0319_1348." )
...       
...       print( "F123() now calls F1234()." )
...       F1234()  # calling F1234() disregarding whether I have defined a local var. named a0319_1348
...       
...     # END - F123()
...     
...     # we are now properly within F12()
...     
...     if b12 :  # i.e., we are asked to define 'a0319_1348' before calling F123( )
...       
...       print( "F12() now defines a0319_1348." )
...       a0319_1348 = 'Defined in F12()'
...       
...       print( "F12() now calls F123() with a 'True' argument" )
...       F123( True )   # True : "Please also define 'a0319_1348' before calling F1234()"
...       
...       print( "F12() calls F123() again ; this time with a 'False' argument" )
...       F123( False )  # False : "Please do not define 'a0319_1348' before calling F1234()"
...       
...     else :    # we are not asked to define 'a0319_1348' before calling F123( )
...      print( "F12() does not define a0319_1348." )
...      print( "F12() now calls F123() with a 'True' argument" )
...      F123( True ) # Please define 'a0319_1348' before calling F1234()
...     
...   # END - F12()
...   
...   # we are now properly within F1()
...   
...   print( "F1() now calls F12() with a 'False' argument " )
...   F12( False )  # Do not define 'a0319_1348' ; Let F123() defines it (before it calls F1234())
...   
...   print( "F1() calls F12() again ; this time with a 'True' argument " )
...   F12( True )   # Define 'a0319_1348' ; But see what will happen if F123() defines it (or not defines it) before it calls F1234()
...   
... # END - F1()
... 
>>> 

>>> F1()
F1() now calls F12() with a 'False' argument 
F12() does not define a0319_1348.
F12() now calls F123() with a 'True' argument
F123() now defines a0319_1348.
F123() now calls F1234().
Printing the value of a0319_1348 in F1234() : Defined in F123()      # F1234() can "see" (well, REFERENCE) the local var. of its parent-function
F1() calls F12() again ; this time with a 'True' argument 
F12() now defines a0319_1348.
F12() now calls F123() with a 'True' argument
F123() now defines a0319_1348.
F123() now calls F1234().
Printing the value of a0319_1348 in F1234() : Defined in F123()      # when the grand-parent also has such a local var., F1234() "sees" the one of its parent
F12() calls F123() again ; this time with a 'False' argument
F123() does not define a0319_1348.
F123() now calls F1234().
Traceback (most recent call last):                                   # F1234() cannot "see" the loval var. of its grand-parent-function
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 54, in F1
  File "<stdin>", line 39, in F12
  File "<stdin>", line 24, in F123
  File "<stdin>", line 9, in F1234
NameError: free variable 'a0319_1348' referenced before assignment in enclosing scope

# Interesting... 上一次呼叫F1()(只是print-msg有差異)時的error message是
#   NameError: cannot access free variable 'a0319_1348' where it is not associated with a value in enclosing scope

# Example 1 seems to mean : A function can only REFERENCE the local variables of its parent-function (and NOT the local variables of its other ancestor functions).
```

#############################

But wait！！！ There is also this short example.

Example 1-1

```
def F3() :
  
  def F31() :
    
    def F312() :
      
      def F3123() :
        print( a333 )    # F3123() references a non-local var 'a333'
      # END - F3123()
      
      print( a333 )      # F312() references a non-loval var 'a333'
      F3123()            # F312() calls F3123()
    # END - F312()
    
    a333 = 333           # F31() defines its local var. 'a333'
    F312()               # F31() then calls F312()
  # END-F31()
  
  F31()                  # F3() calls F31()
# END - F3()

>>> F3()
333
333                      # <--------------------- The REFERECing of 'a333' (a local var. of F31()) in F3123() was successful！
                         #                        # F31() is the grand-parent of F3123(), not its parent.

```
#############################

# On the one hand, Example 1 shows that a function can only REFERENCE the local variables of its parent-function (and NOT the local variables of its grand parent function).

# On the other hand, Example 1-1 shows that a function CAN REFERENCE the local variables of its grand parent function.

# What is going on here？？？

# Let us add just one extra print-statement to Example 1 and see what will happen ...

Example 3-2 (= Example 1 with an extra print statement)

```sh
>>> def F1() :
...   
...   def F12( b12 ) :      # b12  df= whether to define 'a0319_1348' before calling F123()
...     
...     def F123( b123 ) :  # b123 df= whether to define 'a0319_1348' before calling F1234()
...       
...       def F1234() :     # just to REFERENCE the value of 'a0319_1348' (and print its value) # 'a0319_1348' is non-local (= not a local var.)
...         
...         print( "Printing the value of a0319_1348 in F1234() :", a0319_1348 )
...         
...       # END - F1234()
...       
...       # we are now properly within F123()
...       
...       if b123 : # i.e., I am asked to define 'a0319_1348' before calling F1234()
...         
...         print( "F123() now defines a0319_1348." )
...         a0319_1348 = 'Defined in F123()'
...         
...       else :    # I am asked not to define a0319_1348 before calling F1234()
...         print( "Printing the value of a0319_1348 in F123() :", a0319_1348 )    # <---------------- the extra print-statement that we add to Example 1
...         print( "F123() does not define a0319_1348." )
...       
...       print( "F123() now calls F1234()." )
...       F1234()  # calling F1234() disregarding whether I have defined a local var. named a0319_1348
...       
...     # END - F123()
...     
...     # we are now properly within F12()
...     
...     if b12 :  # i.e., we are asked to define 'a0319_1348' before calling F123( )
...       
...       print( "F12() now defines a0319_1348." )
...       a0319_1348 = 'Defined in F12()'
...       
...       print( "F12() now calls F123() with a 'True' argument" )
...       F123( True )   # True : "Please also define 'a0319_1348' before calling F1234()"
...       
...       print( "F12() calls F123() again ; this time with a 'False' argument" )
...       F123( False )  # False : "Please do not define 'a0319_1348' before calling F1234()"
...       
...     else :    # we are not asked to define 'a0319_1348' before calling F123( )
...      print( "F12() does not define a0319_1348." )
...      print( "F12() now calls F123() with a 'True' argument" )
...      F123( True ) # Please define 'a0319_1348' before calling F1234()
...     
...   # END - F12()
...   
...   # we are now properly within F1()
...   
...   print( "F1() now calls F12() with a 'False' argument " )
...   F12( False )  # Do not define 'a0319_1348' ; Let F123() defines it (before it calls F1234())
...   
...   print( "F1() calls F12() again ; this time with a 'True' argument " )
...   F12( True )   # Define 'a0319_1348' ; But see what will happen if F123() defines it (or not defines it) before it calls F1234()
...   
... # END - F1()
... 
>>> F1()
F1() now calls F12() with a 'False' argument 
F12() does not define a0319_1348.
F12() now calls F123() with a 'True' argument
F123() now defines a0319_1348.
F123() now calls F1234().
Printing the value of a0319_1348 in F1234() : Defined in F123()
F1() calls F12() again ; this time with a 'True' argument 
F12() now defines a0319_1348. # <--------------------------------------------------
F12() now calls F123() with a 'True' argument
F123() now defines a0319_1348.
F123() now calls F1234().
Printing the value of a0319_1348 in F1234() : Defined in F123()
F12() calls F123() again ; this time with a 'False' argument # <------------------- this time, F123() does not define 'a0319_1348' as its local var.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 55, in F1
  File "<stdin>", line 40, in F12
  File "<stdin>", line 21, in F123                      # <--- F123() cannot reference 'a0319_1348' (a local var of its parent function F12()) either
UnboundLocalError: local variable 'a0319_1348' referenced before assignment

# Come to think of it. This error message seems to be saying that 'a0319_1348' is a local var. (of F123()).
# To be more precise, this error message is saying that "the local var. 'a0319_1348' has not been assigned a value."
# How in the world can a variable that has not been assigned (= declared or defined) become a local var. (of the current function)？？？
```

#############################

There is only one logical explanation for the results of running Example 1, Example 1-1, and Example 1-2, which is the following.

Whenever the system sees that a function contains the code of an assignment to some var. (and that var. does not have a corresponding 'global' or 'nonlocal' declaration in this function ... 不過那是後話), the system will just pragmatically consider this var. as a (true) local var. of the function.

This decision of "who is a local var." is based solely on program layout. It is a syntactical decision and not a decision that is based on execution semantics (i.e., the decision is made even if the execution of the function does not involve any assignment to the alleged local var.).

# Given the above explanation of how the system determines whether a var. is a (true) local var. (of the current function), you still need to explain the results of Example 1, Example 1-1, and Example 1-2. (Why were there such results?)

# And YES, a function CAN REFERENCE the local var. of its ancestor-function IF the other ancestor-functions "in between" do not have a local-var-with-the-same-name.

#############################

# Example 2 : # An exploration of the meaning of 'global'

# A variable CAN BE declared to be 'global' even when there are no such global variables.

```sh
>>> a2023_0728_1241                                 # There is no global name 'a2023_0728_1241' on the top level
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a2023_0728_1241' is not defined

>>> def F2023_0728_1241() :
...   global a2023_0728_1241
...   print( "Hi" )
... 
>>>                                                  # Nevertheless, defining a function with a 'global' declaration of 'a2023_0728_1241' is okay

>>> F2023_0728_1241()
Hi

>>> a2023_0728_1241
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a2023_0728_1241' is not defined

>>> def F2023_0728_1243() :
...   global a2023_0728_1241
...   a2023_0728_1241 = 10
...   print( "Hello" )
... 
>>> 

>>> F2023_0728_1243()
Hello

>>> a2023_0728_1241  # If a function with a 'global' declaration of some variable xyz that does not exist defines xyz
10                   #   then after the execution of this function, xyz starts to exist on the top level
```

#############################

What about 'nonlocal' declarations？

#############################

############################# Final Summary written on 2023-10-31, revised on 2023-11-17 #############################

Note : 
  Below, when we write 'local var.', we mean either a genuine var or a fake local var.

genuine var. x 
  df= there is an assignment stmt in F() that assigns to x and there is no corresponding 'global'/'nonlocal' declaration of x in F()

fake local var. x 
  df= there is a legal 'nonlocal' declaration of x in F()

A 'nonlocal' declaration of x (in a function F()) is legal
  if
  x is a local var. of some nearest ancestor function of F()

Parent function and child function :

  If the definition of F() includes the definition of G(), 
    then F() is the parent function of G() and G() is a child function of F().

Ancestor function and descendent function :

  If F() is the parent function of G(), 
    then F() is an ancestor function of G() and G() is a descendent function of F().

  If F() is an ancestor function of G() and G() is an ancestor function of H(),
    then F() is an ancestor function of H() and H() is a descendent function of F().

Rule : a 'global'/'nonlocal' declaration of x in F() must appear ABOVE any statement/expression of F() in which x appears.

Implicit rule : a variable cannot be declared to be both 'global' and 'nonlocal' in the same function.

-----------

Global var, nonlocal var, 'global', and 'nonlocal'

1. A global var. x can be referenced (including x.F()) anywhere.  # referenced df= appears without being assigned ('=')
   # Case in point : no 'global x' is needed in order for a function to reference a global variable x (assuming that the object named by 'x' already exists in the execution environment when this object is to be referenced by the system via 'x').

2. A function F() can always reference a local var. x of some NEAREST ancestor function (note : the concept of referencing includes x.F()).
   # Case in point : no 'nonlocal x' is needed in order for a function to reference a local variable x of its nearest ancestor function (assuming that the object named by 'x' already exists in the execution environment when this object is to be referenced by the system via 'x').

3. Whenever there is an assignment to a variable x in F(), then

   case I : there is no corresponding 'nonlocal'/'global' declaration of x in F() (ABOVE this assignment)
            
     x is a (re-)declaration of a ("true") local variable of F().

   case II : there is a corresponding 'global' delaration of x in F() (ABOVE this assignment)

     x is a (re-)declaration of a global variable.
     # Case in point : the object named by 'x' does not have to exist in the execution environment before this assignment to x is executed.

   case III : there is a corresponding 'nonlocal' delaration of x in F() (ABOVE this assignment)

     x is a (re-)declaration of a local variable of the nearest ancestor function.
     # Case in point : the object named by 'x' does not have to exist in the execution environment before this assignment to x is executed.

Here is a recap of how the system determines whether a var. x is a local var. of F() :

A variable x is considered a local var. of F() 

```
IFF
     there is an assignment to x ANYWHERE within F() (disregarding whether this assignment is within nested conditionals/loops)
     AND
     there is no 'global'/'nonlocal' declaration of x ABOVE all references/updates to x (within F()).
  OR
     there is a legal 'nonlocal' declaration of x within F() 
```

！！！ It is possible that 「a local var. (of a function F) does not already exist at some point when F() is being executed」 ！！！

      (i.e., 有可能「在F()的執行過程之中、起碼到某一點為止、F()的某個區域變數x並不存在」，此狀況即使是fake local var. of F()也一樣成立)

「x is a local var. of F()」 是個文法上的概念(a syntactical concept) (亦即、這是用「文法檢查」所決定的)  # 「x 是不是 F() 的區域變數」 是個 「文法上的概念」

「whether the local var. x of F() exists or not」is a run-time concept   # 「系統在run的時候到底有沒有x這個東西存在於系統之中」 是個 「執行上的概念」 
 # (在F()執行的過程之中)執行print( locals() )就知道「目前whether the local var. x of F() exists or not」 # 「existence of x」is a run-time concept

BTW :

  每次我們要reference一個x的值時、系統怎麼知道"x unbound"？ 

  The "variable search process" :
  
    from the enclosing function (its local names), to the nearest enclosing function (its local names), to the next enclosing function (its   local names), etc., to the current module's global names, and finally to the namespace containing the built-in names of the Python   interpreter

  亦即：系統先看(目前這function)的local vars，如果沒有、就看目前這function的parent function的local vars、一層一層找上去、一直找到globals()為止，找到就取其值(嚴格來說應該是「retrieve所name的object」才對)，找不到就"x unbound".

  # 看起來、locals()所return的、是「先列(目前這function)的local vars，然後列目前這function的parent function的local vars、一層一層上去、一直到列出最外層function的local vars為止」。所以，每次當我們要取x的值時，系統的作法是(起碼在理論上是同等於)：先呼叫locals()、看所得到的dict之中有沒有x，如果沒有、就再呼叫globals()、看所得到的dict之中有沒有x，如果沒有、就"x unbound"。

  # 請注意以下的documentation可能會誤導人：
  ```sh
  >>> help( locals )
  Help on built-in function locals in module builtins:
  
  locals()
      Return a dictionary containing the current scope's local variables.
      
      NOTE: Whether or not updates to this dictionary will affect name lookups in
      the local scope and vice-versa is *implementation dependent* and not
      covered by any backwards compatibility guarantees.

  >>> def F() :                # F()的程式碼之中有'x = ...'、而且也沒相關的'global'/'nonlocal'宣告，所以「x是F()的local var」無誤
  ...   def F1() :
  ...     nonlocal x
  ...     print( locals() )    # 第一次被呼叫時locals()所return的dict應該什麼都沒有，因為連F()的x也還都不存在
  ...     y = 10               # F1()自己的local var y是從現在開始(才)存在
  ...     print( locals() )    # locals()所return的dict之中有加入y
  ...   # END - F1()
  ...   
  ...   F1()                   # 此時(F()的)x還不存在
  ...   x = 100                # (F()的)x是從現在才開始存在
  ...   F1()
  ...   
  ...   # END - F()
  ... 
  >>> F()
  {}
  {'y': 10}
  {'x': 100}
  {'x': 100, 'y': 10}
  >>> 
  
  >>> def F() :                # F()的程式碼之中有'x = ...'、而且也沒相關的'global'/'nonlocal'宣告，所以「x是F()的local var」無誤
  ...   def F1() :
  ...     nonlocal x, count            # 所以，F1()之中出現的x是某個ancestor function(碰巧是F())的local var
  ...     count += 1
  ...     print( 'F1() :', locals() )
  ...     y = 10
  ...     print( 'F1() :', locals() )
  ...     x = 50                       # 請注意F()的local var x是從現在開始(才)存在
  ...     print( 'F1() :', locals() )
  ...     if count > 1 :
  ...       print( 'Printing z in F1() : ', z )  # 可reference到(但不可能update到、除非有作nonlocal宣告) ancestor function的local var
  ...   # END - F1()
  ...   
  ...   count = 0
  ...   print( 'F() :', locals() )     # 此時count有存在、但x還不存在
  ...   F1()                           
  ...   print( 'F() :', locals() )     # x開始存在(但不可能有y這個東西)
  ...   x = 100
  ...   print( 'F() :', locals() )
  ...   z = 200                        # 來一個正宗的(F()的)local var
  ...   F1()
  ...   print( 'F() :', locals() )
  ... 
  >>> # F() has 3 locals : count, x, and z ; 
  >>> # F1() has 1 local y and 2 nonlocals : count, x  
  >>> # z is referenced by F1() but z is neither a local of F1() nor a nonlocal of F1()
  >>> 
  >>> F()
  F() : {'F1': <function F.<locals>.F1 at 0x7ff6f829ef70>, 'count': 0} # 'count' assigned, therefore exists ; note that there is no 'x'
  F1() : {'count': 1}
  F1() : {'count': 1, 'y': 10}                    # 'y' assigned, therefore exists
  F1() : {'count': 1, 'y': 10, 'x': 50}           # 'x' assigned in F1() ; now it exists
  F() : {'F1': <function F.<locals>.F1 at 0x7ff6f829ef70>, 'count': 1, 'x': 50}   # Back to F(), 'x' now exists
  F() : {'F1': <function F.<locals>.F1 at 0x7ff6f829ef70>, 'count': 1, 'x': 100}
  F1() : {'count': 2, 'x': 100, 'z': 200}   # Note that 'z' is neither a local of F1() nor a nonlocal of F1() ; but is in locals() of F1()
  F1() : {'count': 2, 'x': 100, 'z': 200, 'y': 10}
  F1() : {'count': 2, 'x': 50, 'z': 200, 'y': 10}
  Printing z in F1() :  200                 # Just to show that 'z' of F() can be referenced in F1() ; also note that it is in locals() here
  F() : {'F1': <function F.<locals>.F1 at 0x7ff6f829ef70>, 'count': 2, 'x': 50, 'z': 200}
  >>> 
  ```

############################# END - Final Summary written on 2023-10-31, revised on 2023-11-17 #############################


# Example 3 # An exploration of the meaning of 'nonlocal'

# non-verbose version

```sh
>>> def F() :
...   def F1( b1 ) :          # b1  df= whether to re-define 'a2023_0728_F'
...     def F12( b12 ) :      # b12 df= whether to re-define both 'a2023_0728_F' and 'a2023_0728_F1'
...       def F123() :
...         def F1234() :
...                                                                      # <------------------- there are no 'nonlocal' declarations in this function
...           print( "Printing the value of a2023_0728_F in F1234() : ", a2023_0728_F )
...           print( "Printing the value of a2023_0728_F1 in F1234() : ", a2023_0728_F1 )
...           
...         # END - F1234()
...                                                                      # <------------------- there are no 'nonlocal' declarations in this function
...         F1234()
...       # END - F123()
...       
...       nonlocal a2023_0728_F, a2023_0728_F1                           # <-------------------
...       
...       if b12 : # I am asked to re-define both 'a2023_0728_F' and 'a2023_0728_F1'
...         a2023_0728_F  = "Re-defined in F12()"                        # <------------------- normally, system would consider it a (true) local var.
...         a2023_0728_F1 = "Re-defined in F12()"                        # <------------------- normally, system would consider it a (true) local var.
...       
...       F123()
...     # END - F12()
...     
...     nonlocal a2023_0728_F                                            # <-------------------
...     
...     if ( b1 ) : # I am asked to re-define 'a2023_0728_F'
...       a2023_0728_F = "Re-defined in F1()"                            # <------------------- normally, system would consider it a (true) local var.
...     
...     a2023_0728_F1 = "Defined in F1()"                                # <------------------- 'a2023_0728_F1' is a (true) local var. of F1()
...     F12( True )   # True  : please re-define both 'a2023_0728_F' and 'a2023_0728_F1'
...     
...     if ( b1 ) : # I am asked to re-define 'a2023_0728_F'
...       a2023_0728_F = "Re-defined in F1()"
...     
...     a2023_0728_F1 = "Defined in F1()"
...     F12( False )  # False : please do not re-define any of  'a2023_0728_F' and 'a2023_0728_F1'
...   # END - F1()
...   
...   a2023_0728_F = "Defined in F()"                                    # <------------------- 'a2023_0728_F' is a (true) local var. of F()
...   F1( True )  # True  : please re-define 'a2023_0728_F'
...   
...   a2023_0728_F = "Defined in F()"
...   F1( False ) # False : please do not re-define 'a2023_0728_F'
...   
... # END - F()
... 
>>> F()
Printing the value of a2023_0728_F in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F1 in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F in F1234() :  Re-defined in F1()
Printing the value of a2023_0728_F1 in F1234() :  Defined in F1()
Printing the value of a2023_0728_F in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F1 in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F in F1234() :  Re-defined in F12()      # Shouldn't this be 'Defined in F()' ？？？
Printing the value of a2023_0728_F1 in F1234() :  Defined in F1()



# not-so-verbose version

>>> def F() :
...   def F1( b1 ) :          # b1  df= whether to re-define 'a2023_0728_F'
...     def F12( b12 ) :      # b12 df= whether to re-define both 'a2023_0728_F' and 'a2023_0728_F1'
...       def F123() :
...         def F1234() :
...           
...           print( "Printing the value of a2023_0728_F in F1234() : ", a2023_0728_F )
...           print( "Printing the value of a2023_0728_F1 in F1234() : ", a2023_0728_F1 )
...           
...         # END - F1234()
...         
...         print( "F123() now calls F1234()." )
...         F1234()
...       # END - F123()
...       
...       nonlocal a2023_0728_F, a2023_0728_F1
...       
...       if b12 : # I am asked to re-define both 'a2023_0728_F' and 'a2023_0728_F1'
...         a2023_0728_F  = "Re-defined in F12()"
...         a2023_0728_F1 = "Re-defined in F12()"
...       
...       print( "F12() now calls F123()." )
...       F123()
...     # END - F12()
...     
...     nonlocal a2023_0728_F
...     
...     if ( b1 ) : # I am asked to re-define 'a2023_0728_F'
...       a2023_0728_F = "Re-defined in F1()"
...     
...     a2023_0728_F1 = "Defined in F1()"
...     print( "F1() now calls F12() with a True argument." )
...     F12( True )   # True  : please re-define both 'a2023_0728_F' and 'a2023_0728_F1'
...     
...     if ( b1 ) : # I am asked to re-define 'a2023_0728_F'
...       a2023_0728_F = "Re-defined in F1()"
...     
...     a2023_0728_F1 = "Defined in F1()"
...     print( "F1() calls F12() again ; this time with a False argument." )
...     F12( False )  # False : please do not re-define any of  'a2023_0728_F' and 'a2023_0728_F1'
...   # END - F1()
...   
...   a2023_0728_F = "Defined in F()"
...   print( "F() now calls F1() with a True argument." )
...   F1( True )  # True  : please re-define 'a2023_0728_F'
...   
...   a2023_0728_F = "Defined in F()"
...   print( "F() calls F1() again ; this time with a False argument." )
...   F1( False ) # False : please do not re-define 'a2023_0728_F'
...   
... # END - F()
... 
>>> F()
F() now calls F1() with a True argument.
F1() now calls F12() with a True argument.
F12() now calls F123().
F123() now calls F1234().
Printing the value of a2023_0728_F in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F1 in F1234() :  Re-defined in F12()
F1() calls F12() again ; this time with a False argument.
F12() now calls F123().
F123() now calls F1234().
Printing the value of a2023_0728_F in F1234() :  Re-defined in F1()
Printing the value of a2023_0728_F1 in F1234() :  Defined in F1()
F() calls F1() again ; this time with a False argument.
F1() now calls F12() with a True argument.
F12() now calls F123().
F123() now calls F1234().
Printing the value of a2023_0728_F in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F1 in F1234() :  Re-defined in F12()
F1() calls F12() again ; this time with a False argument.
F12() now calls F123().
F123() now calls F1234().
Printing the value of a2023_0728_F in F1234() :  Re-defined in F12()      # Shouldn't this be 'Defined in F()' ？？？
Printing the value of a2023_0728_F1 in F1234() :  Defined in F1()




# verbose version

>>> def F() :
...   def F1( b1 ) :          # b1  df= whether to re-define 'a2023_0728_F'
...     def F12( b12 ) :      # b12 df= whether to re-define both 'a2023_0728_F' and 'a2023_0728_F1'
...       def F123() :
...         def F1234() :
...           
...           print( "Printing the value of a2023_0728_F in F1234() : ", a2023_0728_F )
...           print( "Printing the value of a2023_0728_F1 in F1234() : ", a2023_0728_F1 )
...           
...         # END - F1234()
...         
...         print( "F123() now calls F1234()." )
...         F1234()
...       # END - F123()
...       
...       print( "F12() declares both a2023_0728_F and a2023_0728_F1 to be 'nonlocal'." )
...       nonlocal a2023_0728_F, a2023_0728_F1
...       
...       if b12 : # I am asked to re-define both 'a2023_0728_F' and 'a2023_0728_F1'
...         print( "F12() re-defines both 'a2023_0728_F' and 'a2023_0728_F1'." )
...         a2023_0728_F  = "Re-defined in F12()"
...         a2023_0728_F1 = "Re-defined in F12()"
...       
...       print( "F12() now calls F123()." )
...       F123()
...     # END - F12()
...     
...     print( "F1() declares a2023_0728_F to be 'nonlocal'." )
...     nonlocal a2023_0728_F
...     
...     if ( b1 ) : # I am asked to re-define 'a2023_0728_F'
...       print( "F1() re-defines a2023_0728_F." )
...       a2023_0728_F = "Re-defined in F1()"
...     
...     print( "Initializing a2023_0728_F1 as 'Defined in F1()' in F1()" )
...     a2023_0728_F1 = "Defined in F1()"
...     print( "F1() now calls F12() with a True argument." )
...     F12( True )   # True  : please re-define both 'a2023_0728_F' and 'a2023_0728_F1'
...     
...     if ( b1 ) : # I am asked to re-define 'a2023_0728_F'
...       print( "F1() re-defines a2023_0728_F." )
...       a2023_0728_F = "Re-defined in F1()"
...     
...     print( "Again initializing a2023_0728_F1 as 'Defined in F1()' in F1()" )
...     a2023_0728_F1 = "Defined in F1()"
...     print( "F1() calls F12() again ; this time with a False argument." )
...     F12( False )  # False : please do not re-define any of  'a2023_0728_F' and 'a2023_0728_F1'
...   # END - F1()
...   
...   print( "Initializing a2023_0728_F as 'Defined in F()' in F()" )
...   a2023_0728_F = "Defined in F()"
...   print( "F() now calls F1() with a True argument." )
...   F1( True )  # True  : please re-define 'a2023_0728_F'
...   
...   print( "Again initializing a2023_0728_F as 'Defined in F()' in F()" )
...   a2023_0728_F = "Defined in F()"
...   print( "F() calls F1() again ; this time with a False argument." )
...   F1( False ) # False : please do not re-define 'a2023_0728_F'
...   
... # END - F()
... 
>>> F()
Initializing a2023_0728_F as 'Defined in F()' in F()
F() now calls F1() with a True argument.
F1() declares a2023_0728_F to be 'nonlocal'.
F1() re-defines a2023_0728_F.
Initializing a2023_0728_F1 as 'Defined in F1()' in F1()
F1() now calls F12() with a True argument.
F12() declares both a2023_0728_F and a2023_0728_F1 to be 'nonlocal'.
F12() re-defines both 'a2023_0728_F' and 'a2023_0728_F1'.
F12() now calls F123().
F123() now calls F1234().
Printing the value of a2023_0728_F in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F1 in F1234() :  Re-defined in F12()
F1() re-defines a2023_0728_F.
Again initializing a2023_0728_F1 as 'Defined in F1()' in F1()
F1() calls F12() again ; this time with a False argument.
F12() declares both a2023_0728_F and a2023_0728_F1 to be 'nonlocal'.
F12() now calls F123().
F123() now calls F1234().
Printing the value of a2023_0728_F in F1234() :  Re-defined in F1()
Printing the value of a2023_0728_F1 in F1234() :  Defined in F1()
Again initializing a2023_0728_F as 'Defined in F()' in F()
F() calls F1() again ; this time with a False argument.
F1() declares a2023_0728_F to be 'nonlocal'.
Initializing a2023_0728_F1 as 'Defined in F1()' in F1()
F1() now calls F12() with a True argument.
F12() declares both a2023_0728_F and a2023_0728_F1 to be 'nonlocal'.
F12() re-defines both 'a2023_0728_F' and 'a2023_0728_F1'.
F12() now calls F123().
F123() now calls F1234().
Printing the value of a2023_0728_F in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F1 in F1234() :  Re-defined in F12()
Again initializing a2023_0728_F1 as 'Defined in F1()' in F1()
F1() calls F12() again ; this time with a False argument.
F12() declares both a2023_0728_F and a2023_0728_F1 to be 'nonlocal'.
F12() now calls F123().
F123() now calls F1234().
Printing the value of a2023_0728_F in F1234() :  Re-defined in F12()      # Shouldn't this be 'Defined in F()' ？？？
Printing the value of a2023_0728_F1 in F1234() :  Defined in F1()



# a slightly modified non-verbose version (we comment out five lines of code in F12() so that 'a2023_0728_F' does not appear in the code of F12())

>>> def F() :
...   def F1( b1 ) :          # b1  df= whether to re-define 'a2023_0728_F'
...     def F12( b12 ) :      # b12 df= whether to re-define both 'a2023_0728_F' and 'a2023_0728_F1'
...       def F123() :
...         def F1234() :
...                                                                      # <------------------- there are no 'nonlocal' declarations in this function
...           print( "Printing the value of a2023_0728_F in F1234() : ", a2023_0728_F )
...           print( "Printing the value of a2023_0728_F1 in F1234() : ", a2023_0728_F1 )
...           
...         # END - F1234()
...                                                                      # <------------------- there are no 'nonlocal' declarations in this function
...         F1234()
...       # END - F123()
...       
...       nonlocal a2023_0728_F, a2023_0728_F1                           # <-------------------
...       
...       if b12 : # I am asked to re-define both 'a2023_0728_F' and 'a2023_0728_F1'
...         a2023_0728_F  = "Re-defined in F12()"                        # <------------------- normally, system would consider it a (true) local var.
...         a2023_0728_F1 = "Re-defined in F12()"                        # <------------------- normally, system would consider it a (true) local var.
...       
...       F123()
...     # END - F12()
...     
...     # nonlocal a2023_0728_F                                            # commented <-------------------
...     
...     # if ( b1 ) : # I am asked to re-define 'a2023_0728_F'             # commented
...     #   a2023_0728_F = "Re-defined in F1()"                            # commented <------------------- normally, system would consider it a (true) local var.
...     
...     a2023_0728_F1 = "Defined in F1()"                                # <------------------- 'a2023_0728_F1' is a (true) local var. of F1()
...     F12( True )   # True  : please re-define both 'a2023_0728_F' and 'a2023_0728_F1'
...     
...     # if ( b1 ) : # I am asked to re-define 'a2023_0728_F'             # commented
...     #   a2023_0728_F = "Re-defined in F1()"                            # commented
...     
...     a2023_0728_F1 = "Defined in F1()"
...     F12( False )  # False : please do not re-define any of  'a2023_0728_F' and 'a2023_0728_F1'
...   # END - F1()
...   
...   a2023_0728_F = "Defined in F()"                                    # <------------------- 'a2023_0728_F' is a (true) local var. of F()
...   F1( True )  # True  : please re-define 'a2023_0728_F'
...   
...   a2023_0728_F = "Defined in F()"
...   F1( False ) # False : please do not re-define 'a2023_0728_F'
...   
... # END - F()
... 
>>> F()
Printing the value of a2023_0728_F in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F1 in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F1 in F1234() :  Defined in F1()
Printing the value of a2023_0728_F in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F1 in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F in F1234() :  Re-defined in F12()
Printing the value of a2023_0728_F1 in F1234() :  Defined in F1()
```

#############################

The meaning of 'nonlocal' in conclusion :

  For any non-local XYZ that a function CAN reference, this function can declare xyz as 'nonlocal'.  Once xyz has been declared to be 'nonlocal' in a function, any assignment to xyz just amounts to an assignment to the (true) local var. xyz that belongs to its "host function" (= the nearest ancestor function that has a (true) local var named 'xyz')

Below is a simple example showing that "not any var. can be declared to be 'nonlocal'" ...

```sg
>>> def F() :
...   def F1() :
...     nonlocal xyz0728
...     xyz0728 = 10
...   print( xyz0728 )
... # there is no space at line-start, signifying that this is the end of the definition of F()
  File "<stdin>", line 3
SyntaxError: no binding for nonlocal 'xyz0728' found

# Only when a function CAN reference a local var. can this function declare the local var. in question as 'nonlocal'.

>>> def F( b ) :
...   def F1() :
...     nonlocal xyz0728
...     xyz0728 = 10
...   
...   xyz0728 = 100
...   F1()
...   print( xyz0728 )
... 
>>> # the appearance of '>>>' means that the system has accepted this definition of F() (and that the code of F() is syntatically correct)
```

#############################

# Example 4  # An attempt to verify the validity of the above conclusion regarding the meaning of 'nonlocal'

  For any non-local XYZ that a function CAN reference, this function can declare xyz as 'nonlocal'.  Once xyz has been declared to be 'nonlocal' in a function, any assignment to xyz just amounts to an assignment to the (true) local var. xyz that belongs to its "host function" (= the nearest ancestor function that has a (true) local var named 'xyz')

# Below, F() defines a2023_0729_F, F2234() references a2023_0729_F, and F1234() redefines a2023_0729_F.
# To successfully UPDATE, F1234() needs to declare a2023_0729_F as 'nonlocal'. (F2234() needs not do so, because it only needs to REFERENCE a2023_0729_F.)
# F() first calls F2(), then F1(), and then F2() again.

# Purpose of the example : to show that for the two inner functions F1234() and F2234(), the a2023_0729_F of F() is a kind of "global variable" to them. 

```sh
>>> def F() :
...   def F1() :
...     def F12() :
...       def F123() :
...         def F1234() :
...           
...           nonlocal a2023_0729_F                      # <--------------------------------
...           a2023_0729_F = "Re-defined in F1234()"     # a2023_0729_F re-defined in F1234()
...         # END - F1234()
...         
...         F1234()
...       # END - F123()
...       
...       F123()
...     # END - F12()
...     
...     F12()
...   # END - F1()
...   
...   def F2() :
...     def F22() :
...       def F223() :
...         def F2234() :
...           
...           print( "Printing the value of a2023_0729_F in F2234() :", a2023_0729_F )
...         # END - F2234()
...         
...         F2234()
...       # END - F223()
...       
...       F223()
...     # END - F22()
...     
...     F22()
...   # END - F2()
...   
...   a2023_0729_F = "Defined in F()"         # a2023_0729_F defined in F()
...   F2()                                    # <---------------------------
...   F1()                                    # <---------------------------
...   F2()                                    # <---------------------------
...   
... # END - F()
... 
>>> F()
Printing the value of a2023_0729_F in F2234() : Defined in F()
Printing the value of a2023_0729_F in F2234() : Re-defined in F1234()
>>> 
```

#############################

Code template No. 1  # One other reason why Python is "genuinely high level" : 以下的function code還真的syntactically correct and executable！

```sh
def F() :
  def F1() :
    def F12() :
      def F123() :
        def F1234() :
          
          ...
        # END - F1234()
        
        ...
      # END - F123()
      
      ...
    # END - F12()
    
    ...
  # END - F1()
  
  ...
# END - F()
```

#########

Code template No. 2  # One other reason why Python is "genuinely high level" : 以下的function code還真的syntactically correct and executable！

```sh
def F() :
  def F1() :
    def F12() :
      def F123() :
        def F1234() :
          
          ...
        # END - F1234()
        
        ...
      # END - F123()
      
      ...
    # END - F12()
    
    ...
  # END - F1()
  
  def F2() :
    def F22() :
      def F223() :
        def F2234() :
          
          ...
        # END - F2234()
        
        ...
      # END - F223()
      
      ...
    # END - F22()
    
    ...
  # END - F2()
  
  ...
# END - F()
```

#############################

# Example 5 :  # Some more understanding about (the syntactical aspects of) 'nonlocal'

# You need only notice Lines 15 and 18 ; together, these two lines cause an error message when the definition of F1() is entered.

# Below shows that a 'nonlocal' declaration of a variable should not appear UNDER the first assignment to a same-name-variable.
# This is a restriction that is enforced by the syntax checker (of the Python interpreter).

# Meaning : 
#   To declare a var. as being 'nonlocal' and also to assign something to it, the 'nonlocal' declaration must appear ABOVE the assignment (= re-declare).
#   Again, this is a judgment of whether there is a syntax error that is based solely on program layout and not on the semantics of running the program.

```sh
>>> def F1() :
...   
...   def F12( b12 ) :      # b12  df= whether to define 'a0319_1348' before calling F123()
...     
...     def F123( b123 ) :  # b123 df= whether to define 'a0319_1348' before calling F1234()
...       
...       def F1234() :     # just to print the value of 'a0319_1348'
...         nonlocal a0319_1348  # 'a0319_1348' is the-local-with-this-name of the IMMEDIATE enclosing function
...         print( a0319_1348 )  # so, which one is it
...       # END - F1234()
...       
...       # we are now properly within F123()
...       
...       if b123 : # I am asked to define 'a0319_1348' before calling F1234()
...         a0319_1348 = 'Defined in F123()'    ##### Line 15 (an assignment to 'a0319_1348')
...       
...       else :    # I am asked NOT to define 'a0319_1348' before calling F1234()
...         nonlocal a0319_1348                 ##### Line 18 (a 'nonlocal' declaration associated with 'a0319_1348')
...      
...       F1234()  # calling F1234() no matter what
...       
...     # END - F123()
...     
...     # we are now properly within F12()
...     
...     if b12 :  # I am asked to define 'a0319_1348' before calling F123( )
...       a0319_1348 = 'Defined in F12()'
...       print( "F12() now calls F123() with a 'True' argument" )
...       F123( True )   # True : "Please also define 'a0319_1348' before calling F1234()"
...       
...       print( "F12() now calls F123() again with a 'False' argument" )
...       F123( False )  # False : "This time, please do not define 'a0319_1348' before calling F1234()"
...       
...     else :    # I am asked NOT to define 'a0319_1348' before calling F123( )
...      print( "F12() now calls F123() with a 'True' argument" )
...      F123( True ) # True : Please define 'a0319_1348' before calling F1234()
...     
...   # END - F12()
...   
...   # we are now properly within F1()
...   
...   print( "Calling F12( False ) " )
...   F12( False )  # False : Do not define 'a0319_1348' ; Let F123() defines it (before it calls F1234())
...   
...   print( "Calling F12( True ) " )
...   F12( True )   # True : Define 'a0319_1348' ; But see what will happen if F123() defines it (or not defining it) before it calls F1234()
...   
... # END - F1()
... 
  File "<stdin>", line 18
SyntaxError: name 'a0319_1348' is assigned to before nonlocal declaration
```

###################################################################################################################

某些Python有關syntax的基本立場現在應該很清楚了...

1. 要先宣告(= assign)才能使用(尤指REFERENCE)    # 這事實上任何語言都是如此。因為「有宣告才有型別，有型別才能根據型別資訊來interpret儲存於記憶體中相關的bits (相關的"bit string")」

2. 什麼叫做「先」，「先」就是「出現於相關程式碼的上方」。也就是說：系統在"讀"程式碼時、必須先"讀"到宣告的部分(不管是不是出現於if-clause or then-clause or ...)，然後才"讀"到使用的部分(不管是不是出現於if-clause or then-clause or ...)。

3. 也就是說：這裡所謂的「先」或「後」的決定純粹是由program layout所決定、而不是由execution of the program code所決定。 It is purely a syntactical decision and not a semantical descision (whicn is based on, e.g., the results of program execution).

4. 只要一個name有被assign、不管此assignment是出現於程式碼的哪裏(不管是不是出現於if-clause or then-clause or ...)，此name、by default、就被視為此function的(true) local var。

5. 什麼時候才不是「by default」？  就是「當有出現相關的'global'或'nonlocal' declaration (i.e., 'global <name>' or 'nonlocal <name>')之時」。

6. 至於'global'或'nonlocal' declaration的「正確使用方式」，也是同樣的道理。那就是：the 'global'或'nonlocal' declaration of a name (in a function) must appear ABOVE any use of this name in the code body of this function。而這裡所謂的「ABOVE」也是一樣、純粹是由program layout所決定、而不是由execution of the program code所決定。It is purely a syntactical decision and not a semantical descision (whicn is based on, e.g., the results of program execution).

7. When a name has been (correctly) declared to be 'nonlocal', we (i.e., hsia's Python class) say that the name is a "false local variable" of this function (in which the 'nonlocal' declaration appears).

###################################################################################################################

Final summary about 'global' :

1. global-var df= a variable that was/will-be delared(=assigned) on the top level (= outside of the definition of any function or class)

2. A global-var (if it already exists) can be referenced by any function (whatever its level is) without having to be declared to be 'global' by that function (IF the function does not have a local var. with the same name).

3. To change the value of a global-var in a function (whatever its level is), there must be a 'global' declaration to declare the var as a global variable.

4. To declare a var as 'global' (in a function), the var does not have to exist when the system accepts the definition of that function. 

5. If the var is declared as 'global' in a function F() and the var. does not exist before F() is called, then after F() defines (= assigns some something to) the presumed gloval var, the var starts to exist as a module-var on the top level.

Final summary about 'nonlocal' :

1. non-loca-var df= EITHER the variable has been declared to be 'global' or 'nonlocal' OR there is no assignment statement for this var. in the current function

   local-var df= There are no 'global' or 'nonlocal' declaration for this variable AND there is an assignment statement for this var. in the current function.
   # "true local var."

2. By saying that a variable is a "non-local-var.", it just means that "this variable is not a true local var. (of this function)". However, for reason of easier understanding, a variable that has been declared to be 'nonlocal' is STILL CONSIDERED A LOCAL VAR. of this function. (It is just that this variable is a "false loval var." and not a "true local var.")    # Note that this rule is for this class (hsia's Python class) only.

3. Meaning of a 'nonlocal' declaration : 'nonlocal aVar' means that 'aVar' is a local var. (be it a true local var. or a false local var.) of 「the nearest ancestor function」 (= the nearest ancestor function that has 'aVar' as a local var.). 

# 'nonlocal aVar' also means that 'aVar' is a "false local var." of the current function.

4. If a local var. of some ancestor function has been (correctly) declared to be 'nonlocal' in the current function, then that var. can be UPDATEd in the current function.

5. Suppose F() is the nearest ancestor function that has 'xyz' as its local var. (be it a true local var. or a false local var.). Also suppose that 'xyz' is not declared to be 'nonlocal' in the current function.  The current function CAN REFERENCE this 'xyz' of F().

6. A 'nonlocal' declaration (of 'xyz', say) must appear ABOVE any use of the name in question (i.e., 'xyz') in the current function.

7. It is possible that 'xyz' has been declared to be 'nonlocal' in the current function and yet 'xyz' has not come into existence in its host function (= the nearest ancestor function that has 'xyz' as its true local var.) when the program control reaches this function. When this is the case and the current function makes its first assignment to 'xyz', then 'xyz' starts to exist (as a true local var.) in its host function.

# hsia : 比起"天書"(see p. 93, reference.pdf (version 3.7.4))對'global'與'nonlocal'的描述，此處的說明應該容易了解多了！





