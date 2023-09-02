Week-of-0919(Week02Materials)

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

1. On the side : how the problem of "installed but not found" may be solved
2. Python as a "programming-language like" shell-scripting language - back to the original ideal : Part II

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

1. On the side : how the problem of "installed but not found" may be solved

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

How to AVOID the problem of「pipED the correct package but python gives a ModuleNotFoundError and says there is no such module」

1. There may be many versions of Python installed on our computer.

   Just >>python[TAB][TAB]<< and we will see what versions of python are installed on our computer

   e.g.,
```sh
   > python   # 'python[TAB][TAB]'
   python              python2             python3             python3.10          python3.11          python3.9-config
   python-config       python2.7           python3-config      python3.10-config   python3.11-config   pythonw
   python.app          python2.7-config    python3-intel64     python3.10-intel64  python3.9           pythonw2.7
```
2. Each version of python comes (in theory at least) with a version of 'pip', which is located under the same 'bin/' as what that particular version of python is located. (If there is no 'pip' under the same 'bin/' as the pythonX.Y we are using, then perhaps try >>pythonX.Y -m ensurepip --upgrade<< to get that corresponding 'pip' first.) (>>pythonX.Y -m pip install --upgrade pip setuptools wheel<< ???)

3. Either we use this "right" version of 'pip' to do 'pip install ...' (so that the things we install are indeed put in the "right" places),

   or we do something like 'pythonX.Y -m pip install <packageName>' (or 'pythonX.Y -m pip install -user <packageName>', if there is a 'sudo' requirement), so that pythonX.Y itself chooses the right 'pip' to run, where pythonX.Y is the particular version of python we intend to use for running the being-installed-package.

4. To find where the "right" version of 'pip' is located :

   (a) Run the particular version of python we want to use
       e.g.,
       > python3.11

   (b) >>> import os

   (c) >>> os.__file__
       '/opt/homebrew/Cellar/python@3.11/3.11.1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/os.py'

   (d) 'os.py' is located under some 'lib' ;
       under the same parent directory of this 'lib/' is a corresponding 'bin/' ;
       in theory, pythonX.Y is located under this 'bin/' ;
       under this 'bin/', there should be a version of 'pip' ; this 'pip' is the "right" version of 'pip' to use.

    e.g.,
```sh
       >>> sos.B( 'ls -al /opt/homebrew/Cellar/python@3.11/3.11.1/Frameworks/Python.framework/Versions/3.11/bin' )
       total 184
       drwxr-xr-x   9 USER  GROUP    288  2  4 14:50 .
       drwxr-xr-x  10 USER  GROUP    320  1 22 14:52 ..
       -rwxr-xr-x   1 USER  GROUP    173  1 22 14:52 2to3-3.11
       -rwxr-xr-x   1 USER  GROUP    171  1 22 14:52 idle3.11
       -rwxr-xr-x   1 USER  GROUP    249  2  4 14:50 pip3
       -rwxr-xr-x   1 USER  GROUP    249  2  4 14:50 pip3.11
       -rwxr-xr-x   1 USER  GROUP    156  1 22 14:52 pydoc3.11
       -rwxr-xr-x   1 USER  GROUP  69168  1 22 14:52 python3.11
       -rwxr-xr-x   1 USER  GROUP   2115  1 22 14:52 python3.11-config
```
5. Go to the directory where this "right" version of 'pip' is located, and then do './pip install ...' in that directory.

e.g.,
```sh
   > cd /opt/homebrew/Cellar/python@3.11/3.11.1/Frameworks/Python.framework/Versions/3.11/bi
   > ./pip3 install ...
```

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

2. Python as a "programming-language like" shell-scripting language - back to the original ideal : Part II

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

To be able to import a Python-script in an interaction session with Python ...
```sh
> ls ~/bin     # just to show that we have StartUpScript.py under <HOME-DIR>/bin/
... StartUpScript.py ...

> export PYTHONPATH=$PYTHONPATH:~/bin       # Must have the word 'export' !!!      # where do we specify PYTHONPATH in PyCharm???
```
# Put whatever extra path we want the-python-we-run to search in $PYTHONPATH (and 'export' it)

# 注意： # Seems that below is true only if we have defined (and also exported) PYTHONPATH ... Not clear why.
#   不管我們在run python時要import什麼module，必須要make sure我們在invoke python interpreter時所在的working directory之下  不能  有同名的py檔。
#
#   例：假設現在我們的working directory是/home/wang/，而我們現在要run python3.9，且我們在啟動python3.9之後也打算import StartUpScript，
#      而相關的StartUpScript.py事實上是位於/home/wang/bin/之下。那麼current working directory (即/home/wang/)之下就不能有StartUpScript.py檔。
#      因為python interpreter的設計是在一啟動之後就把目前所在的working directory放入sys.path之中作為第一個，導致它所找到的StartUpScript.py是啟動
#      python interpreter時所在的working directory之下的StartUpScript.py、而不是我們希望它找到的/home/wang/bin/StartUpScript.py。
#      ($PYTHONPATH的內容是會放進sys.path之中，不過將會是放在current working directory的緊後面)

Now you should be able to run, e.g., 'python3.9' and successfully 'import StartUpScript' in the Python environment.

----------------------------------------------

How to make a script file directly executable (just like, e.g., 'date')

(1) Content of the script file (named 'fileName') # assume that the path of 'python3.9' is within $PATH

#!/usr/bin/env python3.9
...  # python code

### Alternative content of the script file (named 'fileName') ###

#!<full path of python3.9>
... # python code

(2) chmod u+x fileName

(3) ./fileName

### An alternative for executing fileName ###

```sh
> cp fileName ~/bin
> fileName   # assuming that '~/bin/' is "a part of" $PATH
```

----------------------------------------------

To compile python script into byte code :   # said to be so, but never tried ...

```sh
python3.11 -m py_compile python_shell.py
```

# Q : what is the file name that we get, and how do we run the file?

--------------------------------------------------------------------------------------------------------------------------------------

```sh
> echo $PYTHONPATH      # just to make sure that 'PythonPath' is properly set
:<HOME-DIR>/bin

> cat argParseProg03Out    # Content of the script file 'argParseProgO3Out'
#!/usr/bin/env python3.9
# #!/Users/myUserID/opt/anaconda3/bin/python3.9
```

```py
from StartUpScript import *

import argparse
from pprint import pprint

parser = argparse.ArgumentParser()

# parser.add_argument( "echo", help = "to echo the parameter here" ) # this is for positional argument

parser.add_argument( '-of', '--outfile', type = str, help = 'the file to print to' ) # for keyword argument (options)
parser.add_argument( '-ov', '--outputVar', type = str, help = 'name of the variable to assign to in the output file' )

args = parser.parse_args()

a = ( (10, 20), 30, 40, ((50,), 60), 70)

if args.outfile != None :

  print( '\n' + 'outfile : ' + args.outfile )

  if args.outputVar != None :
    print( 'outputVar : ' + args.outputVar )

  outfile = open( args.outfile, mode = 'w' )

  if args.outputVar != None :
    print( '\n' + args.outputVar + ' = \\' + '\n\\', file = outfile ) # can have no '\n' at the end ; 'print' will print one
  else :
    print( file = outfile )

  pprint( a, stream = outfile, width = 10, indent = 2 )
  print( file = outfile )

  B( 'echo Testing of executing shell command \'ls\' : ' )
  B( 'ls' )

if args.outputVar != None :
  print( '\n' + args.outputVar + ' = ' + '\n' )
else :
  print()

pprint( a, width = 10, indent = 2 )
print()
```
```sh
> ./argParseProg03Out      # Three ways to run the "command" './argParseProgO3Out' : First one

( ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)

> ./argParseProg03Out -of Result357.py      # Three ways to run the "command" './argParseProgO3Out' : Second one

outfile : Result357.py
Testing of executing shell command ls :
AnyScript		Result357.py		argParseProg		argParseProg03Out	pyCommand-02
Result123.py		Result456.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result135.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py
Result246.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py

( ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)

> cat Result357.py

( ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)

> ./argParseProg03Out -of Result357.py -ov list357      # Three ways to run the "command" './argParseProgO3Out' : Third one

outfile : Result357.py
outputVar : list357
Testing of executing shell command ls :
AnyScript		Result357.py		argParseProg		argParseProg03Out	pyCommand-02
Result123.py		Result456.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result135.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py
Result246.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py

list357 =

( ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)

> cat Result357.py

list357 = \
\
( ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)

```

--------------------------------------------------------------------------------------------------------------------------------------

```sh
> cat argParseProg03In          # Content of the script file 'argParseProgO3In'
#!/usr/bin/env python3.9
# #!/Users/myUserID/opt/anaconda3/bin/python3.9
```

```py
from StartUpScript import *

import argparse
from pprint import pprint

parser = argparse.ArgumentParser()

# parser.add_argument( "echo", help = "to echo the parameter here" ) # this is for positional argument

parser.add_argument( '-if', '--infile', type = str, help = 'the file to input from' ) # for keyword argument (options)
parser.add_argument( '-iv', '--inputVar', type = str, help = 'name of the variable that is assigned a value in the input file' )

args = parser.parse_args()

if args.infile != None :                       # <------------------ note here
  print( '\n' + 'infile : ' + args.infile )

if args.inputVar != None :                     # <------------------ note here
  print( 'inputVar : ' + args.inputVar )

if args.infile != None :

  infile = open( args.infile, mode = 'r' )

  # either
  # from Result246 import *
  # or
  inputStr = infile.read()                     # <------------------ either read it (content of the entire file) in here (as ONE string)

else :

  inputStr = sys.stdin.read()                  # <------------------ or read it (content of the entire file) in here (as ONE string)

a = eval( inputStr )                           # <------------------ ！！！
a = a[0:2] + a                                 # <----- just to show that we did read in that list and were also able to make changes to it
pprint( a, width = 10, indent = 2 )            #        note that the value of a[0:2] is >>((10, 20), 30)<<
pprint( inputStr, width = 10, indent = 2 )

B( 'echo Testing of executing shell command \'ls\' : ' )
B( 'ls' )

```



～～～～～～～～～～～～～～～～～～ break ～～～～～～～～～～～～～～～～～～




```sh

> rm -f Result357.py

> ls
AnyScript		Result456.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result123.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py
Result135.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py
Result246.py		argParseProg		argParseProg03Out	pyCommand-02

> echo $PYTHONPATH
:/Users/myUserID/bin

> ./argParseProg03Out

( ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)

> ls
AnyScript		Result456.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result123.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py
Result135.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py
Result246.py		argParseProg		argParseProg03Out	pyCommand-02

# Three ways to run './argParseProgO3Out' and './argParseProgO3In' : First one

> ./argParseProg03Out | ./argParseProg03In         # "list piping"
( ( 10,         # value of 'a' ; note that it is different from the original 'a' value (since we made some changes to it)
    20),
  30,
  ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)
('\n'           # value of inputStr (printed by pprint()) # see the explanation below to understand why the the string is printed this way
 '( ( '
 '10,\n'
 '    '
 '20),\n'
 '  30,\n'
 '  40,\n'
 '  ( '
 '(50,),\n'
 '    '
 '60),\n'
 '  70)\n'
 '\n')
Testing of executing shell command ls :
AnyScript		Result456.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result123.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py
Result135.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py
Result246.py		argParseProg		argParseProg03Out	pyCommand-02

```

--------------------------------------------------------------------------------------------------------------------------------------
一個unexpected小插曲 - the working of pprint() - 當你給它的是含有'\n'的字串時... 

```sh

>>> inputStr = '''
... 
... ( ( 10,
...     20),
...   30,
...   ( 10,
...     20),
...   30,
...   40,
...   ( (50,),
...     60),
...   70)
... 
... '''
>>> inputStr
'\n\n( ( 10,\n    20),\n  30,\n  ( 10,\n    20),\n  30,\n  40,\n  ( (50,),\n    60),\n  70)\n\n'

>>> print( inputStr )        # print()


( ( 10,
    20),
  30,
  ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)


>>> pprint( inputStr )       # pprint()     # apparently, pprint() is viewing each '\n' char as a string-terminator
('\n'             
 '\n'
 '( ( 10,\n'
 '    20),\n'
 '  30,\n'
 '  ( 10,\n'
 '    20),\n'
 '  30,\n'
 '  40,\n'
 '  ( (50,),\n'
 '    60),\n'
 '  70)\n'
 '\n')

### Why so? (why enclosing all-these-(internal)-strings within '(' and ')'?) It is all due to a special "Python way" of expressing strings.

>>> ( 
...    'This will'
... ' be the '
... 
... 'beginning'    ' of'
...         ' a beautiful'      ' friendship.')           # a special way of writing Python strings ; note that there is no ',' ！！！
'This will be the beginning of a beautiful friendship.'

# therefore,

>>> ('\n'             
...  '\n'
...  '( ( 10,\n'
...  '    20),\n'
...  '  30,\n'
...  '  ( 10,\n'
...  '    20),\n'
...  '  30,\n'
...  '  40,\n'
...  '  ( (50,),\n'
...  '    60),\n'
...  '  70)\n'
...  '\n')         # is just a way of expressing the string on the next line
'\n\n( ( 10,\n    20),\n  30,\n  ( 10,\n    20),\n  30,\n  40,\n  ( (50,),\n    60),\n  70)\n\n'

>>> inputStr = ('\n'             
...  '\n'
...  '( ( 10,\n'
...  '    20),\n'
...  '  30,\n'
...  '  ( 10,\n'
...  '    20),\n'
...  '  30,\n'
...  '  40,\n'
...  '  ( (50,),\n'
...  '    60),\n'
...  '  70)\n'
...  '\n')

>>> inputStr
'\n\n( ( 10,\n    20),\n  30,\n  ( 10,\n    20),\n  30,\n  40,\n  ( (50,),\n    60),\n  70)\n\n'

>>> a = eval( inputStr )

>>> a
((10, 20), 30, (10, 20), 30, 40, ((50,), 60), 70)


--------

>>> pprint( '''
... 
... ( 1200, (2000, 3000),
... whatdoyoumeanbythat)
... 
... '''
... , width = 10, indent = 2)
('\n'
 '\n'
 '( '
 '1200, '
 '(2000, '
 '3000),\n'
 'whatdoyoumeanbythat)\n'
 '\n')

>>> inputStr
'\n\n( ( 10,\n    20),\n  30,\n  ( 10,\n    20),\n  30,\n  40,\n  ( (50,),\n    60),\n  70)\n\n'

>>> pprint( inputStr )
('\n'
 '\n'
 '( ( 10,\n'
 '    20),\n'
 '  30,\n'
 '  ( 10,\n'
 '    20),\n'
 '  30,\n'
 '  40,\n'
 '  ( (50,),\n'
 '    60),\n'
 '  70)\n'
 '\n')

# One of the essential ingredients of being "genuinely high level" is that the user must be able to try out things and see what will come out in no time.

```

--------------------------------------------------------------------------------------------------------------------------------------

> ls
AnyScript		Result456.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result123.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py
Result135.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py
Result246.py		argParseProg		argParseProg03Out	pyCommand-02

> ./argParseProg03Out -of Result357.py

outfile : Result357.py
Testing of executing shell command ls :
AnyScript		Result357.py		argParseProg		argParseProg03Out	pyCommand-02
Result123.py		Result456.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result135.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py
Result246.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py

( ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)

> cat Result357.py

( ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)

> rm -f Result357.py

> ls
AnyScript		Result456.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result123.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py
Result135.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py
Result246.py		argParseProg		argParseProg03Out	pyCommand-02

# Three ways to run './argParseProgO3Out' and './argParseProgO3In' : Second one

> ./argParseProg03Out -of Result357.py && ./argParseProg03In -if Result357.py

outfile : Result357.py
Testing of executing shell command ls :
AnyScript		Result357.py		argParseProg		argParseProg03Out	pyCommand-02
Result123.py		Result456.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result135.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py
Result246.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py

( ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)


infile : Result357.py
( ( 10,
    20),
  30,
  ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)
('\n'
 '( ( '
 '10,\n'
 '    '
 '20),\n'
 '  30,\n'
 '  40,\n'
 '  ( '
 '(50,),\n'
 '    '
 '60),\n'
 '  70)\n'
 '\n')
Testing of executing shell command ls :
AnyScript		Result357.py		argParseProg		argParseProg03Out	pyCommand-02
Result123.py		Result456.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result135.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py
Result246.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py

-------------------------------------------------------------------------------------------------------------------------

#################### Once we have made them Linux commands ...

> cp argParseProg03Out ~/bin/

> cp argParseProg03In ~/bin/

> ls ~/bin/
PyCharmCommon.py	PyTest01.py		StartUpScript.py	__pycache__		argParseProg03In	argParseProg03Out

# Three ways to run './argParseProgO3Out' and './argParseProgO3In' ; Third one

> argParseProg03Out -of Result579.py && argParseProg03In -if Result579.py      #################### Just treat them as genuine Linux commands

outfile : Result579.py
Testing of executing shell command ls :
AnyScript		Result357.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py
Result123.py		Result456.py		argParseProg		argParseProg03Out	pyCommand-02
Result135.py		Result579.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result246.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py

( ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)


infile : Result579.py
( ( 10,
    20),
  30,
  ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)
('\n'
 '( ( '
 '10,\n'
 '    '
 '20),\n'
 '  30,\n'
 '  40,\n'
 '  ( '
 '(50,),\n'
 '    '
 '60),\n'
 '  70)\n'
 '\n')
Testing of executing shell command ls :
AnyScript		Result357.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py
Result123.py		Result456.py		argParseProg		argParseProg03Out	pyCommand-02
Result135.py		Result579.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result246.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py

> ls
AnyScript		Result357.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py
Result123.py		Result456.py		argParseProg		argParseProg03Out	pyCommand-02
Result135.py		Result579.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result246.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py

-------------------------------------------------------------------------------------------------------------------------

> echo $PYTHONPATH
:<HOME-DIR>/bin

> pwd
<CURRENT WD>

> python3.9 -i ~/bin/StartUpScript.py
>>> pprint( sys.path )
['<HOME-DIR>/bin',              # <----- due to "-i ~/bin/StartUpScript.py"
 '<CURRENT WD>',                # <----- due to invoking pathon3.9 at <CURRENT WD> (with PYTHONPATH defined and exported)
 '<HOME-DIR>/bin',              # <----- due to $PYTHONPATH (exported)
 '<HOME-DIR>/opt/anaconda3/lib/python39.zip',
 '<HOME-DIR>/opt/anaconda3/lib/python3.9',
 '<HOME-DIR>/opt/anaconda3/lib/python3.9/lib-dynload',
 '<HOME-DIR>/opt/anaconda3/lib/python3.9/site-packages',
 '<HOME-DIR>/opt/anaconda3/lib/python3.9/site-packages/aeosa']

# Now we have Python shell + Unix/Linux shell + Unix/Linux commands (including commands that are Pythons scripts)

>>> B( 'pwd' )
<CURRENT WD>

>>> B( 'ls' )
AnyScript		Result357.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py
Result123.py		Result456.py		argParseProg		argParseProg03Out	pyCommand-02
Result135.py		Result579.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result246.py		Result789.py		argParseProg02In	prog.py			pyScript-02.py

>>> B( 'argParseProg03Out -of Result999.py && argParseProg03In -if Result999.py' )   #################

outfile : Result999.py
Testing of executing shell command ls :
AnyScript		Result357.py		Result999.py		argParseProg02In	prog.py			pyScript-02.py
Result123.py		Result456.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py
Result135.py		Result579.py		argParseProg		argParseProg03Out	pyCommand-02
Result246.py		Result789.py		argParseProg02		bashScript-01.sh	pyScript-01.py

( ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)


infile : Result999.py
( ( 10,
    20),
  30,
  ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)
('\n'
 '( ( '
 '10,\n'
 '    '
 '20),\n'
 '  30,\n'
 '  40,\n'
 '  ( '
 '(50,),\n'
 '    '
 '60),\n'
 '  70)\n'
 '\n')
Testing of executing shell command ls :
AnyScript		Result357.py		Result999.py		argParseProg02In	prog.py			pyScript-02.py
Result123.py		Result456.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py
Result135.py		Result579.py		argParseProg		argParseProg03Out	pyCommand-02
Result246.py		Result789.py		argParseProg02		bashScript-01.sh	pyScript-01.py

>>> B( 'ls' )
AnyScript		Result357.py		Result999.py		argParseProg02In	prog.py			pyScript-02.py
Result123.py		Result456.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py
Result135.py		Result579.py		argParseProg		argParseProg03Out	pyCommand-02
Result246.py		Result789.py		argParseProg02		bashScript-01.sh	pyScript-01.py

>>> infile = open( 'Result999.py', mode = 'r' ) ; a = eval( infile.read() )

>>> a
((10, 20), 30, 40, ((50,), 60), 70)

--------------------------------------------------------------------------------------------------------------------------

>>> # Actually, what we really need to do may be something like the following ...
>>> #       B( 'argParseProg03Out -of Result999.py && argParseProg03In -if Result999.py -of Result100.py -ov list100' )
>>> # Since I want to leave it to you regarding how argParseProg03In should be modified to do things like this,
>>> # let me just use argParseProg03Out to demonstrate what I mean.

>>> B( 'argParseProg03Out -of Result100.py -ov list100' )   ################# (OR : without '-ov list100' and do what we just shown in the above)

outfile : Result100.py
outputVar : list100
Testing of executing shell command ls :
AnyScript		Result246.py		Result789.py		argParseProg02		bashScript-01.sh	pyScript-01.py
Result100.py		Result357.py		Result999.py		argParseProg02In	prog.py			pyScript-02.py
Result123.py		Result456.py		__pycache__		argParseProg03In	pyCommand-01		typeChecking.py
Result135.py		Result579.py		argParseProg		argParseProg03Out	pyCommand-02

list100 =

( ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)

>>> from Result100 import *                  #################

>>> list100
((10, 20), 30, 40, ((50,), 60), 70)

>>> B( 'cat Result100.py' )

list100 = \
\
( ( 10,
    20),
  30,
  40,
  ( (50,),
    60),
  70)

>>> # Why do we need to put the backslash ('\') in Result100.py ???

-------------------------------------------------------------
-------------------------------------------------------------

Python as a "programming-language like" shell-scripting language

                    --- Summary ---

-------------------------------------------------------------

＊＊＊ A suggested way of making a Python script a Linux command ＊＊＊

1. Content of the script file : 

# assume that the path of 'python3.9' is within $PATH

> cat PythonScript.py
#!/usr/bin/env python3
print( "hi" )

2. Alternative content of the script file (this does not requre that the path of 'python3.9' is within $PATH)

#!<full path of python3.9>
... # python code

3. chmod u+x PythonScript.py

4. ./PythonScript.py

5. 

> cp PythonScript.py ~/bin/PythonCmd
> PythonCmd   # if $PATH contains this path (/home/userID/bin)
   
-------------------------------------------------------------

＊＊＊ A suggested way of doing "list piping" ＊＊＊

(the first script prints the value of a list ; the second script reads in the list)

1. Content of the python script (call it 'argParseProg03Out' for the moment) that does the output :

(a) output to a file (print the value of the list named 'a' to the file)

Content of Python script file START ---

outfile = open( outfileName, mode = 'w' )
pprint( a, stream = outfile, width = 10, indent = 2 )

Content of Python script file END ---

(b) output to stdout :

Content of Python script file START ---

pprint( a, width = 10, indent = 2 )

Content of Python script file END ---

(2) Content of the Python script (call it 'argParseProg03In' for the moment) that does the input :

(a) read from a file

Content of Python script file START ---

infile = open( args.infile, mode = 'r' )
inputStr = infile.read()
a = eval( inputStr )

Content of Python script file END ---

(b) read from stdin 

Content of Python script file START ---

inputStr = sys.stdin.read()
a = eval( inputStr )

Content of Python script file END ---

3. Ways of doing "list piping"

(a) > ./argParseProg03Out | ./argParseProg03In
    # or, if the two are already made Linux commands, ##### > argParseProg03Out | argParseProg03In #####

(b) > ./argParseProg03Out -of Result357.py && ./argParseProg03In -if Result357.py    # '-of' and '-if' are options for the scripts
    # or, if the two are already mad Linux commands, 
    #    > argParseProg03Out -of Result357.py && argParseProg03In -if Result357.p

-------------------------------------------------------------

＊＊＊ Ways of handling command-line options in a Python script ＊＊＊

### Below is an example (for 'argParseProg03In') ###

import argparse

parser = argparse.ArgumentParser()

parser.add_argument( '-if', '--infile', type = str, help = 'the file to input from' ) # for keyword argument (options)

args = parser.parse_args()

# now 'args.infile' contains the value of the command-line option '-if' 

if args.infile != None :
  print( '\n' + 'infile : ' + args.infile )

if args.infile != None :

  infile = open( args.infile, mode = 'r' )

  inputStr = infile.read()

else :

  inputStr = sys.stdin.read()

a = eval( inputStr )

### Above is an example (for 'argParseProg03In') ###

-------------------------------------------------------------

＊＊＊ Suggested ways of invoking the Python interpreter ＊＊＊

1. Assume that this line ##### export PYTHONPATH=~/bin:$PYTHONPATH ##### is in ~/.bash_profile

python3.11  # or your favorite Python interpreter

# once we are within "the Python environment"

import os, sys

import StartUpScript as sos    # so that we can run Linux commands (e.g., 'ls ~/bin') as, say, sos.B( 'ls ~/bin' )
# OR just 'from StartUpScript import *', so that we can directly use 'pprint' and 'B' without giving them the prefix 'sos.'

2. If the line ##### export PYTHONPATH=~/bin:$PYTHONPATH ##### is not in ~/.bash_profile or the above does not work for whatever reason ...

python3.11 -i ~/bin/StartUpScript.py

# once we are within the Python environment, we can use 'B' and 'pprint' directly ...

--------------------------------------------------------------------------------------

＊＊＊ Content of StartUpScript.py ＊＊＊

```py
#!/usr/bin/env python3.9
# To use a coding scheme other than UTF-8, put, e.g., '# -*- coding: cp1252 -*-' on this line, where 'cp1252' (Windows-1252) must be a valid codecs supported by Python.

import os
import subprocess
import sys
from pprint import pprint  

## Since we now have B(), L() should not be needed.
## One "drawback" with L() is that it runs 'cmd' in the background,
## causing '>>>' to be displayed before the output of 'cmd' is displayed,
## making it look like the user is not prompted after the output of 'cmd' appears.

# def L( cmd ) :
#   subprocess.Popen( cmd, shell=True, executable='/bin/bash' )

# 'S' means 'sh' (the shell that is used to run the 'cmd'

def S( cmd ) :
  os.system( cmd )

# 'B' means 'bash' ;
#
# Remember to always use >>' ... '<< to specify a bash-command (i.e., use single-quotes for specifying the cmd-string).
# In specifying the command itself (i.e., the >>...<< of >>'...'<<), use >>"<< as much as possible.
# e.g.,
# B( 'LANG=zh_TW.UTF-8 ; var123="The dollar expression \$(( 3 + 5 )) will give us $((3+5)), while \`date\` will give us `date`" ; echo $var123 ' )
#
# If the use of >>'<< is absolutely necessary for specifying the bash-command to execute, see if >>\'<< will work.
# However, there is no guarantee (that >>\'<< will work).
#
# Of course, we can also run >>B( './BashTestScript.sh' )<< to simplify typing.
# But to try to prevent from potential hacking, the file permission bits of this shell script (e.g., BashTestScript.sh)
# should be such that the 'setuid' and 'setgid' bits are both set (i.e., do >>chmod 7755 BashTestScript.sh<< in advance)

def B( cmd ) :
  os.system( "bash -c '" + cmd + "'" )

# # Better not print below, so as not to distort the output
# print('\nPython %s on %s' % (sys.version, sys.platform))
# print( "\n--- StartUpScript.py loaded ---\n" )
```
＊＊＊ END - Content of StartUpScript.py ＊＊＊

--------------------------------------------------------------------------------------------------------------------------

So much for the idea of "king of kings" ...

--------------------------------------------------------------------------------------------------------------------------

