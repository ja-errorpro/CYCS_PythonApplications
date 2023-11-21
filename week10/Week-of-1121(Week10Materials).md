Week-of-1121(Week10Materials).txt

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

Everything is an object (again)
* Regarding "class-objects"
* Regarding "module-objects"
* Regarding "function-objects"

Revisiting Python's insistence on "No values, just objects!" 

How does argparse create new fields of arbitrarily decided names for the objects that it creates?

Python idea of classes and objects are completely unlike that of C/C++/Java

---

          Everything is an object (again) - regarding "class-objects"

---

                            The essence of "Everything is an object" (a Python core concept)

1. Disguishing between the concept of variable-value and the concept of name-binding

   A binding is an association (between two things).

   In Python, it is always the case that "a name may be bound to an object", and it is DEFINITELY NOT the case that "a variable is a place holder for a value".

1a. A reminder of what pointers and values are in C/C++/Java and what a call-stack and a heap mean. (Show drawings.)

    Notice the difference between 『releasing a variable』 and 『releasing the memory occupied by an "object", thereby "releasing" the "object"』！！！

2. The meaning of 'del'

   You 'del' a name. You don't 'del' the object this name is bound to. 

   (i.e., whenever you 'del' something, you are only deleting a name and not the object this name is bound to.)

   You CANNOT 'del' an object (a conceptual entity). You can only 'del' a name.

   Case in point : Is there any way to delete【the conceptual entity that the name 'three' or 'toi' or '三' or '叁' is bound to】？？？

3. Ladies and Gentlemen, allow me to introduce (the concepts of) "class-objects", "module-objects", and "function-objects" in Python.

```sh
>>> sys.version
'3.11.1 (main, Dec 23 2022, 09:25:32) [Clang 13.0.0 (clang-1300.0.29.30)]'


############## 3(a) regarding "class-objects" #############

# what do we have here (on the top level)?

>>> dir()
['C', 'Class1', 'F', 'PrintModuleVar', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'aClass1', 'aClassC', 'aOfFandC', 'anotherClassC', 'bClass1', 'bOfFandC_', 'os', 'sos', 'sys', 'testFC']

# what is the object that the name 'C' is bound to?

>>> C
<class 'PyTestOfFandC.C'>

# what is it that (the object that is bound to (the name)) 'C' has to offer?

>>> dir( C )
['F', 'G', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

# so, if we create an instance of (the object that) 'C' (is bound to) ...

>>> c = C()

>>> dir( c )
['F', 'G', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

>>> c.F()
__name__ printed from the module named 'PyTestOfFandC' :
PyTestOfFandC_okay

>>> c.G()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: C.G() takes 0 positional arguments but 1 was given

>>> C1 = C     # now let (the name) 'C1' be such that it is also bound to the object (a class-object) that 'C' is bound to

>>> del C      # deleting the name 'C'

# what do we have here (on the top level)?

>>> dir()
['C1', 'Class1', 'F', 'PrintModuleVar', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'aClass1', 'aClassC', 'aOfFandC', 'anotherClassC', 'bClass1', 'bOfFandC_', 'c', 'os', 'sos', 'sys', 'testFC']

>>> c1 = C1()

>>> dir( c1 )
['F', 'G', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

>>> c1.G()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: C.G() takes 0 positional arguments but 1 was given

>>> c1.F()
__name__ printed from the module named 'PyTestOfFandC' :
PyTestOfFandC_okay

# the secret ...

>>> C1
<class 'PyTestOfFandC.C'>

# i.e., (the name) 'C1' is still bound to the same object that (the name) 'C' originally was bound to.

### BTW, we use 'class Name : ...' to bind the name 'Name' to a class-object.
### In other words, by executing the code 'class Name : ...', we are doing two things - creating a class-object and binding
### a name to this class object.
```

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

         Everything is an object (again) - regarding "module-objects"

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

```sh
############## 3(b) regarding "module-objects" #############

# what is (the object that is bound to the name) 'testFC'?

>>> testFC
<module 'PyTestOfFandC' from '<HOME-DIR>/bin/PyTestOfFandC.py'>

# what does (this object that is bound to the name) 'testFC' has to offer?

>>> dir( testFC )
['C', 'F', 'PrintModuleVar', '__builtins__', '__cached__', '__doc__', '__eOfFandC', '__fOfFandC_', '__file__', '__gOfFandC__', '__loader__', '__name__', '__package__', '__spec__', '_cOfFandC', '_dOfFandC_', 'aOfFandC', 'bOfFandC_']

# for example ...

>>> testFC.PrintModuleVar()
Value of aOfFandC : 10
Value of bOfFandC : 20
Value of _cOfFandC : 35
Value of _dOfFandC_ : 45
Value of __eOfFandC : 55
Value of __fOfFandC_ : 65
Value of __gOfFandC__ : 75

>>> testFC111 = testFC    # now, the name 'testFC111' also binds to the object that the name 'testFC' is bound to

>>> del testFC            # deleting the name 'testFC'

# what do we have now (on the top level) ?

>>> dir()
['C1', 'Class1', 'F', 'PrintModuleVar', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'aClass1', 'aClassC', 'aOfFandC', 'anotherClassC', 'bClass1', 'bOfFandC_', 'c', 'c1', 'os', 'sos', 'sys', 'testFC111']

>>> dir( testFC111 )
['C', 'F', 'PrintModuleVar', '__builtins__', '__cached__', '__doc__', '__eOfFandC', '__fOfFandC_', '__file__', '__gOfFandC__', '__loader__', '__name__', '__package__', '__spec__', '_cOfFandC', '_dOfFandC_', 'aOfFandC', 'bOfFandC_']

>>> testFC111.PrintModuleVar()
Value of aOfFandC : 10
Value of bOfFandC : 20
Value of _cOfFandC : 35
Value of _dOfFandC_ : 45
Value of __eOfFandC : 55
Value of __fOfFandC_ : 65
Value of __gOfFandC__ : 75

# the secret ...

>>> testFC111
<module 'PyTestOfFandC' from '<HOME-DIR>/bin/PyTestOfFandC.py'>

# i.e., (the name) 'testFC111' is still bound to the same object that (the name) 'testFC' originally was bound to.

### Q: how is the idea of「binding a name to a module-object」implemented in Python???
```

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

        Everything is an object (again) - regarding "function-objects"

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

What does it mean in Python when you think you are calling a function?

```sh
############## 3(c) regarding "function-objects" #############

>>> dir()
['C1', 'Class1', 'F', 'PrintModuleVar', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'aClass1', 'aClassC', 'aOfFandC', 'anotherClassC', 'bClass1', 'bOfFandC_', 'c', 'c1', 'os', 'sos', 'sys', 'testFC111']

>>> F
<function F at 0x100e79800>

>>> F()
__name__ printed from the module named 'PyTestOfFandC' :
PyTestOfFandC_okay

>>> F1 = F

>>> del F

>>> F1()
__name__ printed from the module named 'PyTestOfFandC' :
PyTestOfFandC_okay

>>> F1
<function F at 0x100e79800>

###

>>> def G() :
...   print( "G() is called." )
... 
>>>

>>> G
<function G at 0x100e79c60>

>>> G()
G() is called.

>>> G1 = G

>>> G1
<function G at 0x100e79c60>

>>> del G

>>> G1()
G() is called.

>>> G2 = G1

>>> G2
<function G at 0x100e79c60>

>>> G2()
G() is called.

>>> dir()
['C1', 'Class1', 'F1', 'G1', 'G2', 'PrintModuleVar', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'aClass1', 'aClassC', 'aOfFandC', 'anotherClassC', 'bClass1', 'bOfFandC_', 'c', 'c1', 'os', 'sos', 'sys', 'testFC111']

# 一切盡在不言中 ...

### BTW, we use 'def Name(...) : ...' to bind the name 'Name' to a function-object.
### That is, by executing the code 'def Name(...) : ...', we are doing two things - creating a function object and binding a name to this function object.



# "So, what's the fuss?" You may ask. What you have been shown up til now, you haven't seen anything like these in other languages (with a possible exception of function pointers in C/C++, if your instructor had shown it to you ...).
```

---

          Revisiting Python's insistence on "No values, just objects!" 

---

```sh
############## 3(d) Revisiting Python's insistence of "No values, just objects!" #############

# 其他有關【 '5' 與 '10.3' 與 '[23, "hi", (25, "hello"), [35,]]' 這些names 所bound to的"objects" 】也是一模一樣的道理。
# (只是你以前(很可能)並不是用現在所揭櫫的思考方式來思考的...)

# e.g., (just the examples we already saw before, plus some more ...)

>>> (5).__abs__()
5

>>> 5.5.__ceil__()
6
>>> 5.5.__floor__()
5
>>> 5.5.__round__()
6
>>> 5.5.__trunc__()
5
>>> a = 5.5
>>> a.__round__()
6

# it may be of some interest to note that until Python 3.4.3, it was still the case that only integer-objects had '__ceil__()' and '__floor__()' ( float-objects only had '__round__()' and '__trunc__()' ).
```

--------------------- session with Python 3.4.3 --------------------

```sh
>>> 5.5.__ceil__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'float' object has no attribute '__ceil__'

>>> dir( 5.5 )
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']

>>> dir( float )
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']

>>> sys.version
'3.4.3 (default, Mar 26 2015, 22:03:40) \n[GCC 4.9.2]'
```

--------------------- END - session with Python 3.4.3 --------------------

```sh
# Now back to our current version of Python (at least 3.9)

>>> (5).bit_count
<built-in method bit_count of int object at 0x103a52648>
>>> (5).bit_count()
2

# again, why not '5.bit_count()'?

>>> 'x'.join('y')
'y'

# what exactly does this 'join' do?

>>> 'x'.isalpha()
True

>>> 'xyz'.replace('y','a')
'xaz'

# what is happening below?

>>> [3,].__gt__( [4,] )
False
>>> [3,].__gt__( [2,] )
True
>>> [3,4].__gt__( [4,] )
False
>>> [3,4].__gt__( [3,2,5] )
True
```

---

How does argparse create new fields of arbitrarily decided names for the objects that it creates?

---

This is for you to think about. Obviously, 'argparse' has done it. But how did it do it???




---

  Python idea of classes and objects are completely unlike that of C/C++/Java

---

==========================================

1. Meaning of function definitions and class definitions

Q. : What does 'def F(...) : ...' mean, and what does 'class C[(...)] : ...' mean ?

A. : (the evaluation of) 'def F(...) : ...' creates a function object and binds the name 'F' to this function object.

     Similarly, (the evaluation of) 'class C[(...)] : ...' creates a class object and binds the name 'C' to this class object.

Just try out the following Python code.

```py
def D( bool123 ) :
  global a, b, c, TryF, TryCLS
  if bool123 :
    a = 10
    b = 20
    c = 30
    def TryF() :
      print( "TryF()-if called." )
    class TryCLS :
      a, b = 11, 12
      def __init__( self, bool456 ) :
        if bool456 :
          self.a, self.b = 111, 222
        else :
          self.a, self.b = 1110, 2220
  else :
    a = b = c = 400
    def TryF() :
      print( "TryF()-else called." )
    class TryCLS :
      a, b = 33, 34
      def __init__( self, bool456 ) :
        if bool456 :
          self.a, self.b = 333, 444
        else :
          self.a, self.b = 3330, 4440
```

```
★★★★★ Without 'global' and 'nonlocal', we cannot change the bindings of global-names and nonlocal-names in a function. ★★★★★ 

★★★★★ HOWEVER ★★★★★ 
we can still change the BINDINGS OF THEIR ATTRIBUTES in a function. ★★★★★
★★★★★ 

★★★★★ (In C/C++/Java, when a pointer is passed by value, you cannot change the value of that pointer-variable, but you can still change the content of what-the-pointer-is-pointing-to. It is the same story.)
★★★★★ 

★★★★★ (By the way, just like Java, Python only has call-by-value.)
★★★★★ 

★★★★★ e.g.,
★★★★★ 

★★★★★ # What do we have here (on the top level)?
★★★★★ 

★★★★★ >>> dir()    
★★★★★ ['C', 'Class1', 'F', 'PrintModuleVar', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'aClass1', 'aClassC', 'aOfFandC', 'anotherClassC', 'bClass1', 'bOfFandC_', 'os', 'sos', 'sys', 'testFC']

★★★★★ 
★★★★★ # What's in (the module object named) 'testFC'?
★★★★★ 

★★★★★ >>> dir( testFC )
★★★★★ ['C', 'F', 'PrintModuleVar', '__builtins__', '__cached__', '__doc__', '__eOfFandC', '__fOfFandC_', '__file__', '__gOfFandC__', '__loader__', '__name__', '__package__', '__spec__', '_cOfFandC', '_dOfFandC_', 'aOfFandC', 'bOfFandC_']
★★★★★ 
★★★★★ # What's the class of the instance (named) 'aClass1'?
★★★★★ 
★★★★★ >>> type( aClass1 )
★★★★★ <class '__main__.Class1'>
★★★★★ 
★★★★★ # What are the attributes of (this instance named) 'aClass1'?
★★★★★ 
★★★★★ >>> dir( aClass1 )
★★★★★ ['PrintClassVar', 'PrintInstanceVar', '_Class1__e123_', '_Class1__f123', '_Class1__myOwn', '_Class1__myOwn_', '__a123___', '__class__', '__d123__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__myOwn__', '__myOwn___', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_b123___', '_myOwn', 'c123___', 'myOwn']
★★★★★ 
★★★★★ >>> aClass1.myOwn
★★★★★ 1005
★★★★★ 
★★★★★ >>> testFC.PrintModuleVar()
★★★★★ Value of aOfFandC : 120
★★★★★ Value of bOfFandC : 20     # should be 'bOfFandC_' ...
★★★★★ Value of _cOfFandC : 35
★★★★★ Value of _dOfFandC_ : 45
★★★★★ Value of __eOfFandC : 55
★★★★★ Value of __fOfFandC_ : 65
★★★★★ Value of __gOfFandC__ : 75
★★★★★ 
★★★★★ >>> def TestFunc() :
★★★★★ ...   testFC.bOfFandC_ += 11
★★★★★ ...   aClass1.myOwn += 300
★★★★★ ... 
★★★★★ >>> 
★★★★★ 
★★★★★ # Let's change (the bindings of) the attributes of (the module object named) 'testFC' and (the instance named) 'aClass1'
★★★★★ >>> TestFunc()  
★★★★★ 
★★★★★ >>> aClass1.myOwn
★★★★★ 1305
★★★★★ 
★★★★★ >>> testFC.PrintModuleVar()
★★★★★ Value of aOfFandC : 120
★★★★★ Value of bOfFandC : 31
★★★★★ Value of _cOfFandC : 35
★★★★★ Value of _dOfFandC_ : 45
★★★★★ Value of __eOfFandC : 55
★★★★★ Value of __fOfFandC_ : 65
★★★★★ Value of __gOfFandC__ : 75
```

# Back to our marvelous function 'D()'
# (To be Python-precise, we are executing the following code to create a function-object and name it 'D')

```sh
>>> def D( bool123 ) :
...   global a, b, c, TryF, TryCLS    # Why must we have these? What will happen if we do not have these???
...   if bool123 :
...     a = 10
...     b = 20
...     c = 30
...     def TryF() :
...       print( "TryF()-if called." )
...     class TryCLS :
...       a, b = 11, 12
...       def __init__( self, bool456 ) :
...         if bool456 :
...           self.a, self.b = 111, 222
...         else :
...           self.a, self.b = 1110, 2220
...   else :
...     a = b = c = 400
...     def TryF() :
...       print( "TryF()-else called." )
...     class TryCLS :
...       a, b = 33, 34
...       def __init__( self, bool456 ) :
...         if bool456 :
...           self.a, self.b = 333, 444
...         else :
...           self.a, self.b = 3330, 4440
... 
>>> 
>>> D( True )

>>> c = TryCLS( False )

>>> c.a
1110

>>> TryF()
TryF()-if called.

>>> D( False )

>>> c = TryCLS( False )

>>> c.a
3330

>>> TryF()
TryF()-else called.

>>> a
400
```

This is the very essence of "Now you see it. Now you don't." 

To put it in more precise terms, what you see (what you have) depends on what has been executed before you come to this point (in executing your Python code). You may see (have) something different every time when you come to this point (in executing your Python code).

==========================================

2. 一個衍生出來的程式寫法 - A derivative of the concept that "everything is an object" in programming

```
>>> def CallAll( aModule, aClass, aFunction, anObject, anInt ) :  # case in point : passing (names whose bindings are) modules or classes or functions as parameters
...   
...   aModule.PrintModuleVar()
...   
...   any = aClass()
...   any.F()
...   
...   aFunction()
...   
...   anObject.F()
...   
...   print( anInt )
... 
>>>

# Do you see what the fuss is here (in the above code)???

>>> dir()
['C1', 'CallAll', 'Class1', 'F1', 'G1', 'G2', 'PrintModuleVar', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'aClass1', 'aClassC', 'aOfFandC', 'anotherClassC', 'bClass1', 'bOfFandC_', 'c', 'c1', 'os', 'sos', 'sys', 'testFC111']

>>> testFC111
<module 'PyTestOfFandC' from '/Users/myUserID/bin/PyTestOfFandC.py'>

>>> C1
<class 'PyTestOfFandC.C'>

>>> F1
<function F at 0x100e79800>

>>> c
<PyTestOfFandC.C object at 0x100db4210>    # here, the word 'object' means "an instance of a class"

>>> id(15)
4316784520

>>> CallAll( testFC111, C1, F1, c, 15 )
Value of aOfFandC : 10
Value of bOfFandC : 20
Value of _cOfFandC : 35
Value of _dOfFandC_ : 45
Value of __eOfFandC : 55
Value of __fOfFandC_ : 65
Value of __gOfFandC__ : 75
__name__ printed from the module named 'PyTestOfFandC' :
PyTestOfFandC_okay
__name__ printed from the module named 'PyTestOfFandC' :
PyTestOfFandC_okay
__name__ printed from the module named 'PyTestOfFandC' :
PyTestOfFandC_okay
15
```

#####

```
Function之中可以用的names =  declared (= assigned) local var. + para.
(假設function名為'F')      + 所屬module的namespace裏的所有names (即'dir()'所得之結果，應是與'sorted( dict( F.__globals__ ) )'所得之結果相同) 
                            - 但若要update module-var、就必須要有作'global'宣告(否則同名之var以local var為優先)
                          + 所屬class的(合乎規矩、可呼叫的)function names
                          + 所屬class的class variable names(若與declared local var.同名則以local var為優先)
                          + 所屬class (或所屬module)的IMMEDIATE enclosing function的local variable names (與para. names?)
                            - 但若要update immediate enclosing function中的local variable names (與para. names?)、就必須要有作'nonlocal'宣告(否則同名之var以local var為優先)
                          + if instance method, then 自己(即self)有declare (= assign)過的instance variable names (即：self.xyz)
                          + sorted( dict( F.__builtins__ ) )之中所列出的names (應與'dir(__builtins__)'同。大家應都是一樣)
                          + ModuleName.name, where 'ModuleName' is 所屬module所import的module and 'name' appears in dir( ModuleName )
                            # 強烈建議除非with very good reasons、應該用'import ModuleName as abbreviation'而不要用'from ModuleName import *'
```

#####

對module function與class function與instance function(即所有的function)而言，globals是

  ＊本module的namespace裏的所有names (即'dir()'所show出來的所有names) 
    # 包括所有在本module的top level所define (= assign)者
    #     以及
    #     所有本module的任何function(不管是module function還是class function還是instance function)宣告為'global'且 --有-- define (= assign)者

  ＊所有的ModuleName.name ; 其中  'ModuleName' 是 本module所import者  而  'name' 必須有出現於 dir( ModuleName ) 之中

對class function而言，class variables是

  ＊所有define (= assign)於本class的(任何)function之外(但位於本class之中)的data

  (Class functions不能access instance variables; 因為class functions事實上是傳統的functions，只是有被分類而已)

對instance function而言，instance variables是

  ＊所有define (= assign)於本class的(任何)instance function之內、其名稱是以'self.'作開頭的data  ### 該instance function必須要有被執行過！！！
    # 尤指所有在本class的__init__()之中被define (= assign)、名稱是以'self.'作開頭的data

對instance function而言，class variables是

  ＊所有define (= assign)於本class的(任何)function之外(但位於本class之中)、    且     未被本function所define (= assign)    的data

注意：Instance function所define的variables、其名稱以'self.'作開頭者是instance variables，其名稱不是以'self.'作開頭者是local variables。

     (Java與C++是用naming convention來解決這個"問題"，亦即：instance variable的名字是以'm'作為開頭，local variables則不是)

把class functions與instance functions當傳統functions看就好！(事實上也該如此)

Class functions根本就是傳統functions! Class variables(既然全是public)也根本就是普通的global variables！ 只是二者在被呼叫/access時必須加上其"姓氏"而已。

至於instance function，也根本就只是傳統function＋一個'self' parameter。'self'是一個指向一個「基本上是struct」(既然everything is public)的pointer。
(Instance variables事實上是struct的欄位。一向如此(不管是哪個語言)。)

Python是用list(而不是用array或linked list)來存a bunch of structs (= class instances or dicts)。

Python-list相當於C++與Java的(未宣告其element型別的)vector。

Python-dict相當於C++的struct與Java的「只有data member、且無任何private/protected與static修飾詞的」class instance。
(Python與C/Java的不同之處是Python將此(struct)的概念push到極致、幾乎到了array或linked list或vector或Lisp-styled list的層級)

#####

指令的執行、一定是在「本層次」執行。亦即：我們永遠是在某個「本層次」執行指令。

所謂的「本層次」有三個、也只有三個： 

  本module (包括(the fictitious) top-level)

  本class (即在class之中、但是是在所有class functions與instance functions之外)

  與

  「本function」(不管是傳統functions還是class functions還是instance functions)

當我們在「本層次」assign一個變數時(不管是不是在迴圈或if-then-clause之中、更不管有多少個nesting levels)，我們就是在  宣告  一個「專屬於本層次的變數」

(對module而言，所謂「專屬於本層次的變數」就是本module的global variables)

(對class而言，所謂「專屬於本層次的變數」就是本class的class variables)

(對function而言(不管是傳統functions還是class functions還是instance functions)，所謂「專屬於本層次的變數」就是本function的local variables)

            除非 

此變數  已在本層次被宣告為  'global'或'nonlocal' 
(in which case we are EITHER defining new global/local variables for the-module-we-belong-to/our-immediate-enclosing-function OR updating their existing global/local variables)

            或

此變數的名稱是以 'ModuleName.'或'ClassName.'或'VariableName.'或'ParameterName.'(包括'self.') 作為開頭 
(in which case we are EITHER defining new module-variables/class-variables/instance-variables for this module/class/class-instance OR updating their existing module-variables/class-variables/instance-variables)

#####

至於我們可以在「本層次」reference什麼變數或call什麼functions、這要看「本層次」是module、還是class、還是function。

如果「本層次」是function，所能reference的變數與呼叫的functions已詳述於上(Function之中可以用的names)。
不過要注意：
  如果「現在所reference的module-var或class-data或immediate enclosing function的local var.(或para)」
  「當執行本function之後的code時」"居然"被assign一個值了
  那麼「『原先reference一個module-var或class-data或immediate enclosing function的local var.(或para)』的那行程式碼」現在就變成error了！
  因為此local var. "referenced before assignment"。

如果「本層次」是class (即位於class之內、但又處於class的(任何)function之外)：   # 此處所述未考慮inner class (= class之中的class)
  所屬module的namespace裏的所有names (即'dir()'所得之結果)
  - 但若要update module-var、就必須要有作'global'宣告(否則同名之var以class data為優先)
  + 有宣告(= assign)的class variables與所有first-level class functions
  + dir(__builtins__)之中所列出的names
  + ModuleName.name, where 'ModuleName' is 所屬module所import的module and 'name' appears in dir( ModuleName )
 
如果「本層次」是module (包括 top-level, the fictitious "module" named '__main__')
  namespace裏的所有names (即'dir()'所得之結果)
  + dir(__builtins__)之中所列出的names
  + ModuleName.name, where 'ModuleName' is 所屬module所import的module and 'name' appears in dir( ModuleName )

#############################

# 有關instance data的補充說明：

# 以下程式碼並未放入「StandardStartUpCmds.py」

```sh
>>> class C :
...   a = 10
...   def __init__( self ) :
...     self.b = 20
... 
>>> c = C()
>>> c.b
20

>>> def Hi( self ) :
...   self.x = 30
... 
>>> 

>>> c.__init__ = Hi

>>> c.__init__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Hi() missing 1 required positional argument: 'self'

>>> c.__init__( c )
>>> c.x
30

>>> dir(c)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'b', 'x']

>>> C.__init__ = Hi

>>> d = C()

>>> dir(d)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'x']

>>> d.x
30

# Q : what happened (why does the 'C' instance named 'd' has the attribute (a data of its own) named 'x')? What happened to 'd.b'?

>>> def Hello( hi ) :
...   hi.what = 40
... 
>>> C.__init__ = Hello

>>> e = C()

>>> dir( e )
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'what']

>>> e.what
40

# Q : when we define the class 'C', will the system (the Python interpreter in charge) consider 'def Hello( hi ) : ...' as an instance method???

### furthermore ... ###

# Below is unrelated to StandardStartUpCmds.py (however, the definitions of 'C' and 'aClassC' are taken from StandardStartUpCmds.py)

>>> class C :
...   def F( self ) :
...     print( __annotations__ )
...     print( __name__ )
...   
...   def G() :
...     print( __annotations__ )
...     print( __name__ )
... 
>>> 

>>> aClassC = C()

>>> aClassC.F()
{}
__main__

>>> aClassC.G()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: C.G() takes 0 positional arguments but 1 was given

>>> C.G()
{}
__main__

>>> C.G( aClassC )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: C.G() takes 0 positional arguments but 1 was given

>>> C.F( aClassC )    ### <-------------------------------------- this is how Python "copes with" the OOP methodology
{}                    ###                                         in a sense, Python just makes an "open secret" no longer a secret
__main__

>>> aClassC.F()       ### for you to compare with ###
{}
__main__

# Q : what is happening here???
```

#############################

重要結論：

  我們  --可以--  使用Python來“施行”我們所熟悉的「寫程式方法論」(如structured programming, OOP, and functional programming)。

  但我們必須注意！！！

    Python有它  --自己的--  一套機制與運作邏輯，  --而--  即使是在abstract層面、Python的(虛擬的)程式執行環境的機制與運作邏輯  也與  一般語言如C/C++/C#/Java/Pascal/Modula-3(的程式執行環境)的機制與運作邏輯  -------- 完全不一樣 -------  。

  Python的core concept：  assign就是宣告。 (紅字、字體大兩號)  Never forget！！！

                         # 順便：function是object(是"first class citizen")！可在任何地方specify('def')之，也可被assign與被pass。
                         #      (In Python, objects是可以'obj()'的 (if ItsClass.__call__() is defined ; 此即所謂的"callable")。)
                         #      'def F() : print( "hi" )'是個assignment statement ; 執行它會把'F'這個name的binding設為一個function
                         #      (A function is an abstract concept, just like a number is an abstract concept)

#############################

# Q/A time ...

A recap on (1) "non-local" - the Python way, (2) "module-static" - the Python way, (3) "instance data" - the Python way, (4) the way how Python "copes with" OOP, and (5) the way how Python "copes with" the concept of data protection

Non-local vs. local : once assigned, it is my local and not any body else's local

Non-local without 'nonlocal' : never can tell which local it is     # Why?

about "imported module-static" : once assigned, this data is no longer what we originally thought it was

about "instance data" : once '__init__' gets replaced ... ; plus the story of 'self' - when is it a must? 

the way how Python "copes with" OOP

plus the way how Python "copes with" the concept of data protection (for "module-static" data as well as for instance data)

variable的assign (= 宣告)與function的definition (via the use of 'def')本來就有if-then-else的"問題"(也可能有人會認為這是"正常、本來就該有之現象")

再加上'del'的使用

```sh
>>> # The code below is not in SandardStartUpCmds.py

>>> dir()
['C', 'Hello', 'Hi', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'c', 'd', 'e', 'sys']

>>> dir(c)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'b', 'x']

>>> c.a
10

>>> c.b
20

>>> del c.b

>>> c.a
10

>>> c.b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'C' object has no attribute 'b'

>>> dir(e)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'what']

>>> del e

>>> e
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'e' is not defined

>>> dir(e)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'e' is not defined

>>> h = C()

>>> del C

>>> v = C()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'C' is not defined. Did you mean: 'c'?

>>> dir()
['Hello', 'Hi', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'c', 'd', 'h', 'sys']

>>> dir(h)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'what']

>>> dir(c)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'x']

### furthermore ... ###

>>> def H() :
...   print( "H() called." )
... 
>>> 

>>> H()
H() called.

>>> h = H

>>> del H

>>> H()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'H' is not defined. Did you mean: 'h'?

>>> h()
H() called.

# Please explain the concepts underlying the above statements (concerning 'H' and 'h')！
```

#############################

Time for a past TV commercial.

Google : youtube diet pepsi now you see it, now you don't

#############################

# A very interesting language nevertheless!!!

(中國人：這有什麼用？  朱守禮：Hmmm... This is interesting...)

# You never can tell what one may be able to do with the use of this language!!!

#############################


