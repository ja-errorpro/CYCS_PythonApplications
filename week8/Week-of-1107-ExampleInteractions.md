Week-of-1107-ExampleInteractions.txt

#########################################################################################

> cat ~/bin/StartUpScript.py
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

#########################################################################################

# 對正在執行中的function而言
locals()  # a dict that is the current local name space (of the being executed function) ; unsorted  
globals() # a dict that is the current name space of所屬module ; unsorted
# 如果不幸不是在一個正在執行中的function之中呼叫，那我們就是在the module level，而locals()就只好等同globals()

# 對一個object而言(Remember! Everything is an object, including a module or a function)
# Once created, an object (supposedly an instance of some class), 
#   until it is being explicitly deleted or implicitly garbage collected, 
#   is a permanent entity.
dir( <obj> )   # = 這個object的所有屬性(所有data members與member functions)的names ; sorted 
vars( <obj> )  # = <obj>.__dict__ ; unsorted

--- 如果希望dict print整齊一點、而且也有排序(!!!) ---

pprint( locals() )
pprint( globals() )
pprint( vars( <obj> ) )

--- 如果希望只看names、而且要求有排序 ---

# 對正在執行中的function而言
sorted( locals() )  # sorted keys of locals() # should be the same as dir()
sorted( globals() ) # sorted keys of globals()

# 對一個object而言(Remember! Everything is an object, including a module or a function)
sorted( vars( <obj> ) ) 

--- 如果呼叫dir()或vars()但居然不給必要的argument (an object)，只好當作是對目前正在執行的function而言 ---
--- 如果甚至並不是在function執行時呼叫、就只能當globals()看了，不然還能怎樣？說它是error嗎？？？ ---
dir()    # sorted keys of locals()
vars()   # = locals()  
# sorted( vars() ) = sorted( locals() ) = dir()

#########################################################################################

```sh
> python3.9 -i ~/bin/StartUpScript.py

>>> print('\nPython %s on %s' % (sys.version, sys.platform))

Python 3.9.13 (main, Aug 25 2022, 18:29:29) 
[Clang 12.0.0 ] on darwin

>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fdb0008ccd0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'os': <module 'os' from '/Users/wang/opt/anaconda3/lib/python3.9/os.py'>, 'subprocess': <module 'subprocess' from '/Users/wang/opt/anaconda3/lib/python3.9/subprocess.py'>, 'sys': <module 'sys' (built-in)>, 'pprint': <function pprint at 0x7fdb00264700>, 'S': <function S at 0x7fdb000e8040>, 'B': <function B at 0x7fdb00272670>}

>>> sorted( globals() )
['B', 'S', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']
 
>>> pprint( globals() )
{'B': <function B at 0x7fdb00272670>,
 'S': <function S at 0x7fdb000e8040>,
 '__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fdb0008ccd0>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'os': <module 'os' from '/Users/wang/opt/anaconda3/lib/python3.9/os.py'>,
 'pprint': <function pprint at 0x7fdb00264700>,
 'subprocess': <module 'subprocess' from '/Users/wang/opt/anaconda3/lib/python3.9/subprocess.py'>,
 'sys': <module 'sys' (built-in)>}

>>> sorted( globals() )
['B', 'S', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']
>>> sorted( locals() )
['B', 'S', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']
>>> sorted( dir() )
['B', 'S', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']
>>> sorted( vars() )
['B', 'S', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']

>>> sorted( vars( sys ) )
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework', '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'ps1', 'ps2', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions']

>>> sorted( dir( sys ) )
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework', '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'ps1', 'ps2', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions']

>>> sorted( vars( os ) )
['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_KILLED', 'CLD_STOPPED', 'CLD_TRAPPED', 'DirEntry', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 'F_LOCK', 'F_OK', 'F_TEST', 'F_TLOCK', 'F_ULOCK', 'GenericAlias', 'Mapping', 'MutableMapping', 'NGROUPS_MAX', 'O_ACCMODE', 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_EXLOCK', 'O_NDELAY', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O_RDONLY', 'O_RDWR', 'O_SHLOCK', 'O_SYNC', 'O_TRUNC', 'O_WRONLY', 'POSIX_SPAWN_CLOSE', 'POSIX_SPAWN_DUP2', 'POSIX_SPAWN_OPEN', 'PRIO_PGRP', 'PRIO_PROCESS', 'PRIO_USER', 'P_ALL', 'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_WAIT', 'PathLike', 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD', 'RTLD_NOW', 'R_OK', 'SCHED_FIFO', 'SCHED_OTHER', 'SCHED_RR', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'ST_NOSUID', 'ST_RDONLY', 'TMP_MAX', 'WCONTINUED', 'WCOREDUMP', 'WEXITED', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_fwalk', '_get_exports_list', '_spawnvef', '_walk', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chflags', 'chmod', 'chown', 'chroot', 'close', 'closerange', 'confstr', 'confstr_names', 'cpu_count', 'ctermid', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'environb', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 'fchmod', 'fchown', 'fdopen', 'fork', 'forkpty', 'fpathconf', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'fwalk', 'get_blocking', 'get_exec_path', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 'getgrouplist', 'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid', 'getppid', 'getpriority', 'getsid', 'getuid', 'initgroups', 'isatty', 'kill', 'killpg', 'lchflags', 'lchmod', 'lchown', 'linesep', 'link', 'listdir', 'lockf', 'lseek', 'lstat', 'major', 'makedev', 'makedirs', 'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty', 'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'popen', 'posix_spawn', 'posix_spawnp', 'pread', 'putenv', 'pwrite', 'read', 'readlink', 'readv', 'register_at_fork', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sched_get_priority_max', 'sched_get_priority_min', 'sched_yield', 'sendfile', 'sep', 'set_blocking', 'set_inheritable', 'setegid', 'seteuid', 'setgid', 'setgroups', 'setpgid', 'setpgrp', 'setpriority', 'setregid', 'setreuid', 'setsid', 'setuid', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe', 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'st', 'stat', 'stat_result', 'statvfs', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names', 'system', 'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 'truncate', 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write', 'writev']

>>> help( os.getenv )
Help on function getenv in module os:

getenv(key, default=None)
    Get an environment variable, return None if it doesn't exist.
    The optional second argument can specify an alternate default.
    key, default and the result are str.
(END)

>>> os.getenv( 'PATH' )
'/Users/wang/opt/anaconda3/bin:/Users/wang/opt/anaconda3/condabin:/Library/Frameworks/Python.framework/Versions/3.10/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/Applications/VMware Fusion.app/Contents/Public:/Users/wang/bin'

>>> B( 'echo $PATH' )
/Users/wang/opt/anaconda3/bin:/Users/wang/opt/anaconda3/condabin:/Library/Frameworks/Python.framework/Versions/3.10/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/Applications/VMware Fusion.app/Contents/Public:/Users/wang/bin

>>> sys.path
['/Users/wang/bin', '/Users/wang/bin', '/Users/wang', '/Users/wang/opt/anaconda3/lib/python39.zip', '/Users/wang/opt/anaconda3/lib/python3.9', '/Users/wang/opt/anaconda3/lib/python3.9/lib-dynload', '/Users/wang/opt/anaconda3/lib/python3.9/site-packages', '/Users/wang/opt/anaconda3/lib/python3.9/site-packages/aeosa']

### 以下三個指令是"插隊"(從舊的class notes copy過來)，所以working directory不一樣
### 只是要show how we can use 'os' to access and change the external Linux environment

>>> B( 'pwd' )
/Users/wang/Documents/PythonProj/Testing

>>> os.chdir( '..' )

>>> B( 'pwd' )
/Users/wang/Documents/PythonProj

### END - "插隊"指令 ###

>>> B( 'date > non' )
>>> exit()

> ls
Applications			Library				StartUpScript-canBeDeleted.py	__pycache__
C_Practices			Movies				StartUpScript-canBeDeleted.pyc	bin
Desktop				Music				Temp				date
Documents			MyMyDate			Test				java_error_in_pycharm.hprof
Downloads			Pictures			Untitled.ipynb			non
Final				Public				VSCode				opt
FinalPrepare			PycharmProjects			Virtual Machines.localized	vmware-share

> rm -f non


> python3.9 -i ~/bin/StartUpScript.py
```

############ What will happen to a 'nonlocal'? ############

```sh
>>> def Test0() :
...   def Test01() :
...     
...     nonlocal a      # 'a' may or may not have been assigned
...     
...     print( "\n----- Test01() -----" )
...     print( "locals() : " ) ; pprint( locals() )
...     print( "globals() : " ) ; print( sorted( globals() ) )
...     print( "----- END - Test01() -----\n" )
...     
...   # END - Test01()
...   
...   print( "----- Test0() -----" )
...   print( "locals() : " ) ; pprint( locals() )
...   print( "globals() : " ) ; print( sorted( globals() ) )
...   
...   Test01()
...   
...   a = 10   # 'a' assigned here
...   
...   print( "locals() : " ) ; pprint( locals() )
...   print( "globals() : " ) ; print( sorted( globals() ) )
...   
...   Test01()
...   
...   # END - Test0()
... 
>>> 

>>> Test0()
----- Test0() -----
locals() : 
{'Test01': <function Test0.<locals>.Test01 at 0x7fcc901bb280>}
globals() : 
['B', 'S', 'Test0', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']

----- Test01() -----
locals() : 
{}
globals() : 
['B', 'S', 'Test0', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']
----- END - Test01() -----

locals() : 
{'Test01': <function Test0.<locals>.Test01 at 0x7fcc901bb280>, 'a': 10}
globals() : 
['B', 'S', 'Test0', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']

----- Test01() -----
locals() : 
{'a': 10}
globals() : 
['B', 'S', 'Test0', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']
----- END - Test01() -----
```

############ When a 'nonlocal' starts to exist in a descendent function ... ############

```sh
>>> def Test1() :
...   def Test11() :
...     
...     nonlocal a   # 'a' may or may not have been assigned
...     
...     print( "\n----- Test11() -----" )
...     print( "locals() : " ) ; pprint( locals() )
...     print( "globals() : " ) ; print( sorted( globals() ) )
...     print( "----- END - Test11() -----\n" )
...     
...     a = 55   # 'a' assigned here
...     
...   # END - Test11()
...   
...   print( "----- Test1() -----" )
...   print( "locals() : " ) ; pprint( locals() )
...   print( "globals() : " ) ; print( sorted( globals() ) )
...   
...   Test11()
...   
...   print( "locals() : " ) ; pprint( locals() )
...   print( "globals() : " ) ; print( sorted( globals() ) )
...   
...   Test11()
...   
...   a = 10   # just to make 'a' a local var. of Test1(), so that Test11() can make it 'nonlocal'
...   
...   # END - Test1()
... 
>>> 

>>> Test1()
----- Test1() -----
locals() : 
{'Test11': <function Test1.<locals>.Test11 at 0x7fcc901bb280>}
globals() : 
['B', 'S', 'Test0', 'Test1', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']

----- Test11() -----
locals() : 
{}
globals() : 
['B', 'S', 'Test0', 'Test1', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']
----- END - Test11() -----

locals() : 
{'Test11': <function Test1.<locals>.Test11 at 0x7fcc901bb280>, 'a': 55}
globals() : 
['B', 'S', 'Test0', 'Test1', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']

----- Test11() -----
locals() : 
{'a': 55}
globals() : 
['B', 'S', 'Test0', 'Test1', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']
----- END - Test11() -----

>>> sorted( globals() )
['B', 'S', 'Test0', 'Test1', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']
```

############ So, what about 'global gA' ? ############

```sh
>>> def Test3() :
...   def Test31() :
...     
...     nonlocal a   # 'a' may or may not have been assigned
...     global gA    # <--------------------- 'global' declared here
...     
...     print( "\n----- Test31() -----" )
...     print( "locals() : " ) ; pprint( locals() )
...     print( "globals() : " ) ; print( sorted( globals() ) )
...     
...     gA = 100     # <--------------------- the global starts to exist here
...     
...     print( "----- END - Test31() -----\n" )
...     
...   # END - Test31()
...   
...   print( "----- Test3() -----" )
...   print( "locals() : " ) ; pprint( locals() )
...   print( "globals() : " ) ; print( sorted( globals() ) )
...   
...   Test31()
...   
...   a = 10   # 'a' assigned here
...   
...   print( "locals() : " ) ; pprint( locals() )
...   print( "globals() : " ) ; print( sorted( globals() ) )
...   
...   Test31()
...   
...   # END - Test3()
... 
>>> 

>>> Test3()
----- Test3() -----
locals() : 
{'Test31': <function Test3.<locals>.Test31 at 0x7fcc901bb430>}
globals() : 
['B', 'S', 'Test0', 'Test1', 'Test3', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']

----- Test31() -----
locals() : 
{}
globals() : 
['B', 'S', 'Test0', 'Test1', 'Test3', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'pprint', 'subprocess', 'sys']
----- END - Test31() -----

locals() : 
{'Test31': <function Test3.<locals>.Test31 at 0x7fcc901bb430>, 'a': 10}
globals() : 
['B', 'S', 'Test0', 'Test1', 'Test3', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']

----- Test31() -----
locals() : 
{'a': 10}
globals() : 
['B', 'S', 'Test0', 'Test1', 'Test3', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']
----- END - Test31() -----

>>> 

>>> sorted( globals() )
['B', 'S', 'Test0', 'Test1', 'Test3', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']

>>> dir()
['B', 'S', 'Test0', 'Test1', 'Test3', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']
```


#########################################################################################

The "variable search process" :

  from the enclosing function (its local names), to the nearest enclosing function (its local names), to the next enclosing function (its local names), etc., to the current module's global names, and finally to the namespace containing the built-in names of the Python interpreter

  # Note : there is always a "current module" !

#########################################################################################

dir( <object> ) 與 vars( <object> ) 的同與異

  vars( anObject ) returns something equivalent to anObject.__dict__   
    # the namespace of the given object ( the dict object pointed at by the attribute '__dict__' of anObject )

  dir( anObject ) returns the following:

    for a module object: the module's attributes.

    for a class object:  its attributes, and recursively the attributes
      of its bases.

    for any other object: its attributes, its class's attributes, and
      recursively the attributes of its class's base classes.

    # dir( anObject) just calls anObject.__dir__() ; If the object does not provide __dir__(), dir() will try to gather information first from the object’s __dict__ attribute, if defined, and then from its type object.  

#########################################################################################

```sh
>>> dir()
['B', 'S', 'Test0', 'Test1', 'Test3', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']

>>> gA = "Hi"

>>> vars( gA )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: vars() argument must have __dict__ attribute

>>> type( gA )
<class 'str'>

>>> dir( gA )
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>> dir( str )   # 80個屬性
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>> sorted( vars( str ) )   # 70個屬性
['__add__', '__contains__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__repr__', '__rmod__', '__rmul__', '__sizeof__', '__str__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>> gA.__class__
<class 'str'>

>>> gA.__doc__
"str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."

>>> print( gA.__doc__ )
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
>>> 

>>> help( str )   # Press 'q' to exit interaction with help()
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
...

>>> help( str.__add__ )
Help on wrapper_descriptor:

__add__(self, value, /)
    Return self+value.
(END)
>>> # the '!!!' comment at the beginning of a function definition
```

#########################################################################################

# 舉凡function名稱是'__'開頭與結尾者、Python稱之為"special functions"，Special functions supposedly都有其既定功能、隨時可能被系統implicitly呼叫( 比如說、dir(<某object>)就是designed to呼叫<某object>的__dir__() )。

# Python的「assign即(重新)宣告」、與一般使用這種做法(如Visual Basic)「只是純粹提供寫程式的"方便"而已」(a functionality that is very strongly opposed by wang)有一個很大的差異 : 

#  以special function為例，由於"everything is an object！"，再加上Python是個interpreted language，所以任何function都可以呼叫任何object的'__XYZFunction__()'、而不須管這個任何object的型別是否真有提供'__XYZFunction__()'這個member function。

#  就以dir()與__dir__()而言，Programmers在定義任何class時、只要想「在被dir()呼叫時提供呼叫者想得到的結果(或者呼叫者也許只是想試試看是否會得到那個結果)」、就提供一個'__dir()__'

#  這種做法有個基本要件：dir(a)----不能----檢查'a'的型別、因為這牽涉到使用者有可能會定義到的----任何----型別。

#  dir(a)的程式碼基本上應該是'return a.__dir__()'，如果'a'沒有'__dir__()'，Python的run-time system就會raise相關exception。

#  通常這種undefined類的exception一發生、要麼是使用者的程式自己(攔截並)處理、要麼是回到(正在interacting with Python的)user-prompt level、讓run code的人決定要怎麼樣。

#  不過dir()對於此undefined類的exception的處理方式顯然不一樣；如果'a'沒有'__dir__()'，dir()會攔截exception，然後try to gather information first from the object’s __dict__ attribute, if defined, and then from (the __dict__ attribute of) its type object。

  • If the object is a module object, the resulting list contains (just) the names of the module’s attributes.

  • If the object is a type or class object, the resulting list contains the names of its attributes, and recursively of the attributes of its bases.

  • Otherwise, the object is an instance of a class or type, and the resulting list contains the object’s attributes’ names, the names of its class’s attributes, and recursively of the attributes of its class’s base classes.

#########################################################################################

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

                           Everything is an object

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

# A 「function definition」 (≠ the execution of this function) is an object

```sh
>>> dir()
['B', 'S', 'Test0', 'Test1', 'Test3', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']

>>> vars( Test0 )
{}

>>> dir( Test0 )
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

>>> Test0.__dict__
{}

>>> Test0.__call__()
----- Test0() -----
locals() : 
{'Test01': <function Test0.<locals>.Test01 at 0x7fcc803104c0>}
globals() : 
['B', 'S', 'Test0', 'Test1', 'Test3', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']

----- Test01() -----
locals() : 
{}
globals() : 
['B', 'S', 'Test0', 'Test1', 'Test3', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']
----- END - Test01() -----

locals() : 
{'Test01': <function Test0.<locals>.Test01 at 0x7fcc803104c0>, 'a': 10}
globals() : 
['B', 'S', 'Test0', 'Test1', 'Test3', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']

----- Test01() -----
locals() : 
{'a': 10}
globals() : 
['B', 'S', 'Test0', 'Test1', 'Test3', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']
----- END - Test01() -----
```

###########

# Does the system store the local namespace (of an execution instance) in the __dict__ of a function definition? Probably not！

```
>>> def Test4() :   # Modified from Test1()
...   def Test41() :
...     
...     nonlocal a   # 'a' may or may not have been assigned
...     
...     print( "\n----- Test41() -----" )
...     print( "locals() : " ) ; pprint( locals() )
...     print( "Test41.__dict__" ) ; pprint( Test41.__dict__ ) ;  # <----- just added this
...     print( "globals() : " ) ; print( sorted( globals() ) )
...     print( "----- END - Test41() -----\n" )
...     
...     a = 55   # 'a' assigned here
...     
...   # END - Test41()
...   
...   print( "----- Test4() -----" )
...   print( "locals() : " ) ; pprint( locals() )
...   print( "Test4.__dict__" ) ; pprint( Test4.__dict__ ) ;   # <----- and this
...   print( "globals() : " ) ; print( sorted( globals() ) )
...   
...   Test41()
...   
...   print( "locals() : " ) ; pprint( locals() )
...   print( "Test4.__dict__" ) ; pprint( Test4.__dict__ ) ;   # <----- and this
...   print( "globals() : " ) ; print( sorted( globals() ) )
...   
...   Test41()
...   
...   a = 10   # just to make 'a' a local var. of Test1(), so that Test11() can make it 'nonlocal'
...   
...   # END - Test4()
... 
>>> 

>>> Test4()
----- Test4() -----
locals() : 
{'Test41': <function Test4.<locals>.Test41 at 0x7fcc901bb430>}
Test4.__dict__
{}
globals() : 
['B', 'S', 'Test0', 'Test1', 'Test3', 'Test4', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']

----- Test41() -----
locals() : 
{'Test41': <function Test4.<locals>.Test41 at 0x7fcc901bb430>}
Test41.__dict__
{}
globals() : 
['B', 'S', 'Test0', 'Test1', 'Test3', 'Test4', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']
----- END - Test41() -----

locals() : 
{'Test41': <function Test4.<locals>.Test41 at 0x7fcc901bb430>, 'a': 55}
Test4.__dict__
{}
globals() : 
['B', 'S', 'Test0', 'Test1', 'Test3', 'Test4', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']

----- Test41() -----
locals() : 
{'Test41': <function Test4.<locals>.Test41 at 0x7fcc901bb430>, 'a': 55}
Test41.__dict__
{}
globals() : 
['B', 'S', 'Test0', 'Test1', 'Test3', 'Test4', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']
----- END - Test41() -----

>>> 

############

>>> dir( Test0 )
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

>>> Test0.__module__
'__main__'

>>> dir()
['B', 'S', 'Test0', 'Test1', 'Test3', 'Test4', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']
 
>>> __name__
'__main__'

############

# An imported module is an object.


>>> import random


>>> dir()
['B', 'BBB', 'C', 'F', 'F0402_1435', 'F1', 'F2023_0728_1241', 'F2023_0728_1243', 'F3', 'G1', 'GetSecondOf', 'S', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'a0402_1435', 'a2023_0728_1241', 'abcde', 'c', 'd', 'inputStr', 'keys', 'len', 'more_players', 'my_dict', 'new_dict', 'os', 'players', 'pprint', 'random', 'sos', 'subprocess', 'sys', 'team', 'view_of_my_dict', 'x']


>>> dir( random )
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_inst', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']


>>> help( random.random )
random() method of random.Random instance
    random() -> x in the interval [0, 1).

>>> help( random.randint )
randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

>>> help( random.seed )
seed(a=None, version=2) method of random.Random instance
    Initialize internal state from a seed.
    
    The only supported seed types are None, int, float,
    str, bytes, and bytearray.
    
    None or no argument seeds from current time or from an operating
    system specific randomness source if available.
    
    If *a* is an int, all bits are used.
    
    For version 2 (the default), all of the bits are used if *a* is a str,
    bytes, or bytearray.  For version 1 (provided for reproducing random
    sequences from older versions of Python), the algorithm for str and
    bytes generates a narrower range of seeds.
```

############

# The 「Class object」

```sh
>>> class Class123 :
...   
...   classDataMember123 = 10          #
...   
...   def __init__( self ) :
...     
...     Class123.classDataMember123 += 1
...     
...     self.myOwn123 = 1000
...     
...   def InstanceMethod123( self ) :
...     pass
...   
...   def ClassMethod123() :
...     pass
... 
>>> 

>>> dir()
['B', 'Class123', 'S', 'Test0', 'Test1', 'Test3', 'Test4', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'os', 'pprint', 'subprocess', 'sys']

>>> pprint( vars( Class123 ) )
mappingproxy({'ClassMethod123': <function Class123.ClassMethod123 at 0x7fcc8032c700>,
              'InstanceMethod123': <function Class123.InstanceMethod123 at 0x7fcc8032cd30>,
              '__dict__': <attribute '__dict__' of 'Class123' objects>,
              '__doc__': None,
              '__init__': <function Class123.__init__ at 0x7fcc8033a310>,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'Class123' objects>,
              'classDataMember123': 10})

>>> pprint( dict( vars( Class123 ) ) )
{'ClassMethod123': <function Class123.ClassMethod123 at 0x7fcc8032c700>,
 'InstanceMethod123': <function Class123.InstanceMethod123 at 0x7fcc8032cd30>,
 '__dict__': <attribute '__dict__' of 'Class123' objects>,
 '__doc__': None,
 '__init__': <function Class123.__init__ at 0x7fcc8033a310>,
 '__module__': '__main__',
 '__weakref__': <attribute '__weakref__' of 'Class123' objects>,
 'classDataMember123': 10}

>>> sorted( dict( vars( Class123 ) ) )
['ClassMethod123', 'InstanceMethod123', '__dict__', '__doc__', '__init__', '__module__', '__weakref__', 'classDataMember123']

>>> dir( Class123 )
['ClassMethod123', 'InstanceMethod123', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'classDataMember123']

# Note that a class-object (e.g., 'Class123') has a '__dict__' attribute

>>> Class123.__dict__
mappingproxy({'__module__': '__main__', 'classDataMember123': 10, '__init__': <function Class123.__init__ at 0x7fcc8033a310>, 'InstanceMethod123': <function Class123.InstanceMethod123 at 0x7fcc8032cd30>, 'ClassMethod123': <function Class123.ClassMethod123 at 0x7fcc8032c700>, '__dict__': <attribute '__dict__' of 'Class123' objects>, '__weakref__': <attribute '__weakref__' of 'Class123' objects>, '__doc__': None})

>>> pprint( dict( Class123.__dict__ ) )
{'ClassMethod123': <function Class123.ClassMethod123 at 0x7fcc8032c700>,
 'InstanceMethod123': <function Class123.InstanceMethod123 at 0x7fcc8032cd30>,
 '__dict__': <attribute '__dict__' of 'Class123' objects>,
 '__doc__': None,
 '__init__': <function Class123.__init__ at 0x7fcc8033a310>,
 '__module__': '__main__',
 '__weakref__': <attribute '__weakref__' of 'Class123' objects>,
 'classDataMember123': 10}

# vars( anObject ) = anObject.__dict__

>>> pprint( dict( vars( Class123 ) ) )
{'ClassMethod123': <function Class123.ClassMethod123 at 0x7fcc8032c700>,
 'InstanceMethod123': <function Class123.InstanceMethod123 at 0x7fcc8032cd30>,
 '__dict__': <attribute '__dict__' of 'Class123' objects>,
 '__doc__': None,
 '__init__': <function Class123.__init__ at 0x7fcc8033a310>,
 '__module__': '__main__',
 '__weakref__': <attribute '__weakref__' of 'Class123' objects>,
 'classDataMember123': 10}

############

# The 「instance-of-a-class object」

>>> obj123 = Class123()
 
>>> dir()
['B', 'Class123', 'S', 'Test0', 'Test1', 'Test3', 'Test4', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'obj123', 'os', 'pprint', 'subprocess', 'sys']
 
>>> vars( obj123 )
{'myOwn123': 1000}

# Note that the object 'obj123' actually has a '__dict__' attribute (since 'vars( obj123 )' is defined) (and this is actually very important) ; however, the fact that 'obj123' has the attribute '__dict__' is not shown in vars( obj123 )

>>> obj123.__dict__
{'myOwn123': 1000}

>>> obj123.hi = 5    # Assign = 宣告

>>> obj123.__dict__
{'myOwn123': 1000, 'hi': 5}

>>> vars( obj123 )
{'myOwn123': 1000, 'hi': 5}

>>> obj123.__dict__["Hello"] = 20

>>> obj123.__dict__
{'myOwn123': 1000, 'hi': 5, 'Hello': 20}

>>> vars( obj123 )
{'myOwn123': 1000, 'hi': 5, 'Hello': 20}

>>> dir( obj123 )
['ClassMethod123', 'Hello', 'InstanceMethod123', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'classDataMember123', 'hi', 'myOwn123']

# How about the __dict__ of a Class object ???

>>> Class123.__dict__['classDataMember123'] = 200
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'mappingproxy' object does not support item assignment

# So, this is why class attributes are not directly stored in a dictionary ...

############

# All "values" are objects too.
# ！！！ Much like how we implement values as "atoms" in OurScheme ！！！

>>> type( 5 )
<class 'int'>

>>> type( 'x' )
<class 'str'>

>>> dir( 5 )     # same as 'dir( int )'
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

>>> dir( 'x' )   # same as 'dir( str )'
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>> help( 'x'.join )
join(iterable, /) method of builtins.str instance
    Concatenate any number of strings.
    
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    
    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

>>> (5).__abs__()
5

>>> 'x'.join('y')
'y'

>>> 'x'.isalpha()
True

>>> 'xyz'.replace('y','a')
'xaz'

>>> (5).bit_count
<built-in method bit_count of int object at 0x103a52648>

>>> (5).bit_count()
2
```

#########################################################################################

---

                          if __name__ == "__main__"

---

# Why do we often see something like the following (usually located at the end of (the top-level of) a module)
#   if __name__ == "__main__"
#     main( 100, 200 )

# Do you remember that every Java class can have a 'main()' ( 'public static void main( String argStr ) throws Throwable { ... }' ) ？

#########################################################################################

```sh
>>> sys.path
['/Users/wang/bin', '/Users/wang/bin', '/Users/wang', '/Users/wang/opt/anaconda3/lib/python39.zip', '/Users/wang/opt/anaconda3/lib/python3.9', '/Users/wang/opt/anaconda3/lib/python3.9/lib-dynload', '/Users/wang/opt/anaconda3/lib/python3.9/site-packages', '/Users/wang/opt/anaconda3/lib/python3.9/site-packages/aeosa']

>>> B( 'cat ~/bin/PyTestOfFandC_02.py' )
#!/Users/wang/opt/anaconda3/bin/python3.9
# To use a coding scheme other than UTF-8, put, e.g., '# -*- coding: cp1252 -*-' on this line, where 'cp1252' (Windows-1252) must be a valid codecs supported by Python.
# File name : PyTestOfFandC.py

aOfFandC     = 10
bOfFandC_    = 20
_cOfFandC    = 30
_dOfFandC_   = 40
__eOfFandC   = 50
__fOfFandC_  = 60
__gOfFandC__ = 70

def F() :
  print( "__name__ printed from the module named 'PyTestOfFandC' :" )
  print( __name__ )

class C :
  def F( self ) :
    print( "__name__ printed from the module named 'PyTestOfFandC' :" )
    print( __name__ )
  
  def G() :
    print( "__name__ printed from the module named 'PyTestOfFandC' :" )
    print( __name__ )

def PrintModuleVar() :
  print( "Value of aOfFandC :",     aOfFandC )
  print( "Value of bOfFandC :",     bOfFandC_ )
  print( "Value of _cOfFandC :",    _cOfFandC )
  print( "Value of _dOfFandC_ :",   _dOfFandC_ )
  print( "Value of __eOfFandC :",   __eOfFandC )
  print( "Value of __fOfFandC_ :",  __fOfFandC_ )
  print( "Value of __gOfFandC__ :", __gOfFandC__ )

print( "(Module path : ~/bin/PyTestOfFandC_02.py) Value of '__name__' :", __name__ )

if __name__ == "__main__" :
  aOfFandC     += 10000
else :
  aOfFandC     += 20000

print( "Value of aOfFandC : ", aOfFandC )
 
>>> dir()
['B', 'Class123', 'S', 'Test0', 'Test1', 'Test3', 'Test4', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'obj123', 'os', 'pprint', 'subprocess', 'sys']
 
>>> import PyTestOfFandC_02
(Module path : ~/bin/PyTestOfFandC_02.py) Value of '__name__' : PyTestOfFandC_02
Value of aOfFandC :  20010
 
>>> PyTestOfFandC_02.__name__  # the name of this imported module 'PyTestOfFandC_02' is 'PyTestOfFandC_02' (and not '__main__')
'PyTestOfFandC_02'

>>> __name__   # it is this fictitious "main" module (this interative session with Python) that has '__main__' as the value of '__name__'
'__main__'

>>> PyTestOfFandC_02.aOfFandC  # just to double check
20010

# Just when will the value of '__name__' - the one that appears in 'PyTestOfFandC_02' - be '__main__'?

##### Two alternative ways of running 'PyTestOfFandC_02' #####

# if we run 'PyTestOfFandC_02.py' (directly) as a Linux command

> PyTestOfFandC_02.py 
(Module path : ~/bin/PyTestOfFandC_02.py) Value of '__name__' : __main__
Value of aOfFandC :  10010

# or, if we run 'PyTestOfFandC_02.py' as the starting code fragment of the fictitious "main" module

> python3.9 -i ~/bin/PyTestOfFandC_02.py  
(Module path : ~/bin/PyTestOfFandC_02.py) Value of '__name__' : __main__
Value of aOfFandC :  10010

>>> exit()

> 

# Do you remember that every Java class can have a 'main()' ( 'public static void main( String argStr ) throws Throwable { ... }' ) ？

##### END - Two alternative ways of running 'PyTestOfFandC_02' #####

# Now that we have imported the module named 'PyTestOfFandC_02'

>>> dir()   # what are the attributes (the so-called "globals") of the fictitious "main" module-object as of now?

['B', 'Class123', 'PyTestOfFandC_02', 'S', 'Test0', 'Test1', 'Test3', 'Test4', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'gA', 'obj123', 'os', 'pprint', 'subprocess', 'sys']

# So, we now have a global, a name 'PyTestOfFandC_02', that is a pointer to a newly created module-object 

# A module-object is an object too.  

# Therefore, this module-object also has its attributes, just like other module-objects such as the ones named by 'os' and 'sys'.

>>> pprint( vars( PyTestOfFandC_02 ) )  # a sorted listing of its attribute-object pairs

# Since Python is an interpreter (it "interprets code-texts"), all Python-variables are really just "names" (strings) and not memory-addresses. It (Python) makes use of this feature REALLY well.

{'C': <class 'PyTestOfFandC_02.C'>,
 'F': <function F at 0x7fcc8032cdc0>,
 'PrintModuleVar': <function PrintModuleVar at 0x7fcc8032c9d0>,
 '__builtins__': {'ArithmeticError': <class 'ArithmeticError'>,   # Note : these are the builtins of the system
                  'AssertionError': <class 'AssertionError'>,
                  'AttributeError': <class 'AttributeError'>,
                  'BaseException': <class 'BaseException'>,
                  'BlockingIOError': <class 'BlockingIOError'>,
                  'BrokenPipeError': <class 'BrokenPipeError'>,
                  'BufferError': <class 'BufferError'>,
                  'BytesWarning': <class 'BytesWarning'>,
                  'ChildProcessError': <class 'ChildProcessError'>,
                  'ConnectionAbortedError': <class 'ConnectionAbortedError'>,
                  'ConnectionError': <class 'ConnectionError'>,
                  'ConnectionRefusedError': <class 'ConnectionRefusedError'>,
                  'ConnectionResetError': <class 'ConnectionResetError'>,
                  'DeprecationWarning': <class 'DeprecationWarning'>,
                  'EOFError': <class 'EOFError'>,
                  'Ellipsis': Ellipsis,
                  'EnvironmentError': <class 'OSError'>,
                  'Exception': <class 'Exception'>,
                  'False': False,
                  'FileExistsError': <class 'FileExistsError'>,
                  'FileNotFoundError': <class 'FileNotFoundError'>,
                  'FloatingPointError': <class 'FloatingPointError'>,
                  'FutureWarning': <class 'FutureWarning'>,
                  'GeneratorExit': <class 'GeneratorExit'>,
                  'IOError': <class 'OSError'>,
                  'ImportError': <class 'ImportError'>,
                  'ImportWarning': <class 'ImportWarning'>,
                  'IndentationError': <class 'IndentationError'>,
                  'IndexError': <class 'IndexError'>,
                  'InterruptedError': <class 'InterruptedError'>,
                  'IsADirectoryError': <class 'IsADirectoryError'>,
                  'KeyError': <class 'KeyError'>,
                  'KeyboardInterrupt': <class 'KeyboardInterrupt'>,
                  'LookupError': <class 'LookupError'>,
                  'MemoryError': <class 'MemoryError'>,
                  'ModuleNotFoundError': <class 'ModuleNotFoundError'>,
                  'NameError': <class 'NameError'>,
                  'None': None,
                  'NotADirectoryError': <class 'NotADirectoryError'>,
                  'NotImplemented': NotImplemented,
                  'NotImplementedError': <class 'NotImplementedError'>,
                  'OSError': <class 'OSError'>,
                  'OverflowError': <class 'OverflowError'>,
                  'PendingDeprecationWarning': <class 'PendingDeprecationWarning'>,
                  'PermissionError': <class 'PermissionError'>,
                  'ProcessLookupError': <class 'ProcessLookupError'>,
                  'RecursionError': <class 'RecursionError'>,
                  'ReferenceError': <class 'ReferenceError'>,
                  'ResourceWarning': <class 'ResourceWarning'>,
                  'RuntimeError': <class 'RuntimeError'>,
                  'RuntimeWarning': <class 'RuntimeWarning'>,
                  'StopAsyncIteration': <class 'StopAsyncIteration'>,
                  'StopIteration': <class 'StopIteration'>,
                  'SyntaxError': <class 'SyntaxError'>,
                  'SyntaxWarning': <class 'SyntaxWarning'>,
                  'SystemError': <class 'SystemError'>,
                  'SystemExit': <class 'SystemExit'>,
                  'TabError': <class 'TabError'>,
                  'TimeoutError': <class 'TimeoutError'>,
                  'True': True,
                  'TypeError': <class 'TypeError'>,
                  'UnboundLocalError': <class 'UnboundLocalError'>,
                  'UnicodeDecodeError': <class 'UnicodeDecodeError'>,
                  'UnicodeEncodeError': <class 'UnicodeEncodeError'>,
                  'UnicodeError': <class 'UnicodeError'>,
                  'UnicodeTranslateError': <class 'UnicodeTranslateError'>,
                  'UnicodeWarning': <class 'UnicodeWarning'>,
                  'UserWarning': <class 'UserWarning'>,
                  'ValueError': <class 'ValueError'>,
                  'Warning': <class 'Warning'>,
                  'ZeroDivisionError': <class 'ZeroDivisionError'>,
                  '_': ['B',                                    # Result of the last (Python) command
                        'Class123',
                        'PyTestOfFandC_02',
                        'S',
                        'Test0',
                        'Test1',
                        'Test3',
                        'Test4',
                        '__annotations__',
                        '__builtins__',
                        '__doc__',
                        '__loader__',
                        '__name__',
                        '__package__',
                        '__spec__',
                        'gA',
                        'obj123',
                        'os',
                        'pprint',
                        'subprocess',
                        'sys'],
                  '__build_class__': <built-in function __build_class__>,
                  '__debug__': True,
                  '__doc__': 'Built-in functions, exceptions, and other '
                             'objects.\n'
                             '\n'
                             "Noteworthy: None is the `nil' object; Ellipsis "
                             "represents `...' in slices.",
                  '__import__': <built-in function __import__>,
                  '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
                  '__name__': 'builtins',
                  '__package__': '',
                  '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in'),
                  'abs': <built-in function abs>,
                  'all': <built-in function all>,
                  'any': <built-in function any>,
                  'ascii': <built-in function ascii>,
                  'bin': <built-in function bin>,
                  'bool': <class 'bool'>,
                  'breakpoint': <built-in function breakpoint>,
                  'bytearray': <class 'bytearray'>,
                  'bytes': <class 'bytes'>,
                  'callable': <built-in function callable>,
                  'chr': <built-in function chr>,
                  'classmethod': <class 'classmethod'>,
                  'compile': <built-in function compile>,
                  'complex': <class 'complex'>,
                  'copyright': Copyright (c) 2001-2022 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.,
                  'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.,
                  'delattr': <built-in function delattr>,
                  'dict': <class 'dict'>,
                  'dir': <built-in function dir>,
                  'divmod': <built-in function divmod>,
                  'enumerate': <class 'enumerate'>,
                  'eval': <built-in function eval>,
                  'exec': <built-in function exec>,
                  'exit': Use exit() or Ctrl-D (i.e. EOF) to exit,
                  'filter': <class 'filter'>,
                  'float': <class 'float'>,
                  'format': <built-in function format>,
                  'frozenset': <class 'frozenset'>,
                  'getattr': <built-in function getattr>,
                  'globals': <built-in function globals>,
                  'hasattr': <built-in function hasattr>,
                  'hash': <built-in function hash>,
                  'help': Type help() for interactive help, or help(object) for help about object.,
                  'hex': <built-in function hex>,
                  'id': <built-in function id>,
                  'input': <built-in function input>,
                  'int': <class 'int'>,
                  'isinstance': <built-in function isinstance>,
                  'issubclass': <built-in function issubclass>,
                  'iter': <built-in function iter>,
                  'len': <built-in function len>,
                  'license': Type license() to see the full license text,
                  'list': <class 'list'>,
                  'locals': <built-in function locals>,
                  'map': <class 'map'>,
                  'max': <built-in function max>,
                  'memoryview': <class 'memoryview'>,
                  'min': <built-in function min>,
                  'next': <built-in function next>,
                  'object': <class 'object'>,
                  'oct': <built-in function oct>,
                  'open': <built-in function open>,
                  'ord': <built-in function ord>,
                  'pow': <built-in function pow>,
                  'print': <built-in function print>,
                  'property': <class 'property'>,
                  'quit': Use quit() or Ctrl-D (i.e. EOF) to exit,
                  'range': <class 'range'>,
                  'repr': <built-in function repr>,
                  'reversed': <class 'reversed'>,
                  'round': <built-in function round>,
                  'set': <class 'set'>,
                  'setattr': <built-in function setattr>,
                  'slice': <class 'slice'>,
                  'sorted': <built-in function sorted>,
                  'staticmethod': <class 'staticmethod'>,
                  'str': <class 'str'>,
                  'sum': <built-in function sum>,
                  'super': <class 'super'>,
                  'tuple': <class 'tuple'>,
                  'type': <class 'type'>,
                  'vars': <built-in function vars>,
                  'zip': <class 'zip'>},                 # Note : Here is where the listing of the builtins (of the system) ends
 '__cached__': '/Users/wang/bin/__pycache__/PyTestOfFandC_02.cpython-39.pyc',
 '__doc__': None,
 '__eOfFandC': 50,
 '__fOfFandC_': 60,
 '__file__': '/Users/wang/bin/PyTestOfFandC_02.py',
 '__gOfFandC__': 70,
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fcc90262a60>,
 '__name__': 'PyTestOfFandC_02',
 '__package__': '',
 '__spec__': ModuleSpec(name='PyTestOfFandC_02', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7fcc90262a60>, origin='/Users/wang/bin/PyTestOfFandC_02.py'),
 '_cOfFandC': 30,
 '_dOfFandC_': 40,
 'aOfFandC': 20010,
 'bOfFandC_': 20}

>>> pprint( sorted( vars( PyTestOfFandC_02 ) ) )    # a sorted list of just names (of the attributes of the object named 'PyTestOfFandC_02')
['C',
 'F',
 'PrintModuleVar',
 '__builtins__',  # all builtins of the system
 '__cached__',
 '__doc__',
 '__eOfFandC',
 '__fOfFandC_',
 '__file__',
 '__gOfFandC__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '_cOfFandC',
 '_dOfFandC_',
 'aOfFandC',
 'bOfFandC_']
 ```

#########################################################################################

                           ### Class and object in Python ###

```sh
>>> class Class123 :
...   
...   classDataMember123 = 10          
...   
...   def __init__( self ) :
...     
...     Class123.classDataMember123 += 1
...     
...     self.myOwn123 = 1000
...     
...   def InstanceMethod123( self ) :
...     
...     Class123.classDataMember123 += 7
...     print( "Value of Class123.classDataMember123 : ", Class123.classDataMember123 )
...     print( "Value of self.classDataMember123 : ", self.classDataMember123 )
...     
...     self.myOwn123 += 5
...     print( "Value of self.myOwn123 : ", self.myOwn123 )
...     
...     myOwn123 += 50
...     print( "Value of self.myOwn123 : ", self.myOwn123 )
...     
...   def ClassMethod123() :
...     
...     Class123.classDataMember123 += 10
...     print( "Value of classDataMember123 : ", Class123.classDataMember123 )
... 
>>> 

>>> obj123 = Class123()

>>> dir( obj123 )
['ClassMethod123', 'InstanceMethod123', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'classDataMember123', 'myOwn123']

>>> dir( Class123 )
['ClassMethod123', 'InstanceMethod123', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'classDataMember123']

>>> obj123.myOwn123
1000

>>> obj123.classDataMember123
11

>>> Class123.classDataMember123
11

>>> Class123.ClassMethod123()
Value of classDataMember123 :  21

>>> obj123.ClassMethod123()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ClassMethod123() takes 0 positional arguments but 1 was given

### Why the above error ?

>>> obj123.InstanceMethod123()
Value of Class123.classDataMember123 :  28
Value of self.classDataMember123 :  28
Value of self.myOwn123 :  1005
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 20, in InstanceMethod123
UnboundLocalError: local variable 'myOwn123' referenced before assignment

### Why the above error ?

###############

>>> class Class123 :
...   
...   classDataMember123 = 10          
...   
...   def __init__( self ) :
...     
...     Class123.classDataMember123 += 1
...     
...     self.myOwn123 = 1000
...     
...   def InstanceMethod123( self ) :
...     
...     Class123.classDataMember123 += 7
...     print( "Value of Class123.classDataMember123 : ", Class123.classDataMember123 )
...     print( "Value of self.classDataMember123 : ", self.classDataMember123 )
...     
...     self.myOwn123 += 5
...     print( "Value of self.myOwn123 : ", self.myOwn123 )
...     
...     myOwn123 = 50
...     print( "Value of myOwn123 : ", myOwn123 )
...     
...   def ClassMethod123() :
...     
...     Class123.classDataMember123 += 10
...     print( "Value of classDataMember123 : ", Class123.classDataMember123 )
... 
>>> 

>>> obj123 = Class123()

>>> dir( obj123 )
['ClassMethod123', 'InstanceMethod123', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'classDataMember123', 'myOwn123']

>>> obj123.myOwn123
1000

>>> obj123.InstanceMethod123()
Value of Class123.classDataMember123 :  18
Value of self.classDataMember123 :  18
Value of self.myOwn123 :  1005
Value of myOwn123 :  50

>>> obj123.InstanceMethod123()
Value of Class123.classDataMember123 :  25
Value of self.classDataMember123 :  25
Value of self.myOwn123 :  1010
Value of myOwn123 :  50

### Please explain the distinction between instance-var and local var.

##############

# the concept of "growing instance" and "growing class"

>>> class Class123 :
...   
...   classDataMember123 = 10          
...   
...   def __init__( self ) :
...     
...     Class123.classDataMember123 += 1
...     
...     self.myOwn123 = 1000
...     
...   def InstanceMethod123( self ) :
...     
...     Class123.classDataMember123 += 7
...     print( "Value of Class123.classDataMember123 : ", Class123.classDataMember123 )
...     print( "Value of self.classDataMember123 : ", self.classDataMember123 )
...     
...     self.myOwn123 += 5
...     print( "Value of self.myOwn123 : ", self.myOwn123 )
...     
...     myOwn123 = 50
...     print( "Value of myOwn123 : ", myOwn123 )
...     
...   def InstanceMethod456( self ) :
...     
...     self.myOwn456 = 5
...     print( "Value of self.myOwn456 : ", self.myOwn456 )
...     
...   def InstanceMethod789( self ) :
...     
...     self.myOwn456 += 5
...     print( "Value of self.myOwn456 : ", self.myOwn456 )
...     
...   def ClassMethod123() :
...     
...     Class123.classDataMember123 += 10
...     print( "Value of classDataMember123 : ", Class123.classDataMember123 )
...     
...   def ClassMethod456() :
...     
...     Class123.classDataMember456 = 10
...     print( "Value of classDataMember123 : ", Class123.classDataMember123 )
...     
...   def ClassMethod789() :
...     
...     Class123.classDataMember456 += 10
...     print( "Value of classDataMember456 : ", Class123.classDataMember456 )
... 
>>> 

>>> obj123 = Class123()

>>> obj456 = Class123()

>>> dir( obj123 )
['ClassMethod123', 'ClassMethod456', 'ClassMethod789', 'InstanceMethod123', 'InstanceMethod456', 'InstanceMethod789', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'classDataMember123', 'myOwn123']

>>> dir( obj456 )
['ClassMethod123', 'ClassMethod456', 'ClassMethod789', 'InstanceMethod123', 'InstanceMethod456', 'InstanceMethod789', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'classDataMember123', 'myOwn123']

>>> obj123.InstanceMethod456()
Value of self.myOwn456 :  5

>>> obj123.InstanceMethod789()
Value of self.myOwn456 :  10

>>> obj456.InstanceMethod789()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 30, in InstanceMethod789
AttributeError: 'Class123' object has no attribute 'myOwn456'

# Why the above error?

>>> dir( obj123 )
['ClassMethod123', 'ClassMethod456', 'ClassMethod789', 'InstanceMethod123', 'InstanceMethod456', 'InstanceMethod789', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'classDataMember123', 'myOwn123', 'myOwn456']

>>> dir( obj456 )
['ClassMethod123', 'ClassMethod456', 'ClassMethod789', 'InstanceMethod123', 'InstanceMethod456', 'InstanceMethod789', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'classDataMember123', 'myOwn123']

>>> obj123.ClassMethod456()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ClassMethod456() takes 0 positional arguments but 1 was given

>>> obj123.ClassMethod456( "anything here" )   # a little bit of confusion on my own part
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ClassMethod456() takes 0 positional arguments but 2 were given

>>> Class123.ClassMethod456()
Value of classDataMember123 :  12

>>> Class123.ClassMethod789()
Value of classDataMember456 :  20

>>> dir( obj123 )
['ClassMethod123', 'ClassMethod456', 'ClassMethod789', 'InstanceMethod123', 'InstanceMethod456', 'InstanceMethod789', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'classDataMember123', 'classDataMember456', 'myOwn123', 'myOwn456']

>>> dir( obj456 )
['ClassMethod123', 'ClassMethod456', 'ClassMethod789', 'InstanceMethod123', 'InstanceMethod456', 'InstanceMethod789', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'classDataMember123', 'classDataMember456', 'myOwn123']

>>> dir( Class123 )
['ClassMethod123', 'ClassMethod456', 'ClassMethod789', 'InstanceMethod123', 'InstanceMethod456', 'InstanceMethod789', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'classDataMember123', 'classDataMember456']

>>> Class123.InstanceMethod123( "anything here" )
Value of Class123.classDataMember123 :  19
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 15, in InstanceMethod123
AttributeError: 'str' object has no attribute 'classDataMember123'

# The execution of Class123.InstanceMethod123( "anything here" ) was partially successful.
# WHY?
# The system eventually raised an error-exception. What happened?
```

#########################################################################################

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

           public/private/protected/'_'/'__' ; static/non-static

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

###################################################################################################################

1. Python只有public的概念, 沒有private 或 protected的概念 ＃ wang: 可能是與沒有explicit declaration有關

# 完全要靠naming convention 與 自我約束 來做到  private、protected、public  與  static、non-static (如果有此方面的考量的話)

# 問：private、protected、public  與  static、non-static 各是什麼樣的概念？

2. module (=file) 之中的 '_varName'（底線開頭。至於varName本身是否有底線開頭與底線結尾已與右方所述之module import規矩不相關）當 from module123 import * 時、不會被import進來。However, we can can always use 'Module123._varName' to access such variables/module-attributes。 只是說、我們在一般程式碼中不該去存或取這些變數或呼叫這些functions.   # 因為這是module-static的概念！

3. class之中的 '_dataMember123'（單底線開頭者）是「希望能比照」一般OOP的'protected'的概念，與系統運作無關。這只是在提醒"外人"(＝非descendent-class者)不要去動它。系統並不強制控管此事。

4. 同樣的，class之中的 '__dataMember456'或'＿dataMember789_'（雙底線開頭，頂多一個底線結尾）是「希望能比照」一般OOP的'private'的概念，programmers自己應當要注意不要去動它。系統雖然也是一樣不強制控管此事，但有作name mangling (！！！)。

"Name mangling" 是什麼意思?

e.g., >> from SomeModule import SomeClass ; anObject = SomeClass() <<  之後， 原先應是
         anObject.__dataMember456
         或anObject.__dataMember789_
         或anObject.__memberFunction789()
         或anObject.__memberFunction999_()的，
         現在改名為
         anObject._SomeClass__dataMember456
         或anObject._SomeClass__dataMember789_
         或anObject._SomeClass__memberFunction789()
         或anObject._SomeClass__memberFunction999_()。

5. 至於'__dataMember999__'與'__memberFunction888__()'（既雙底線開頭又雙底線結尾的名字-不管是變數名稱還是function/method名稱）這種名字是系統在用的，通常是「可能與系統的運作有關」(e.g., __le__()是系統在執行'<='時會呼叫者)。我們在一般程式碼中  不該使用  這樣的名字。 (但系統並沒有阻止我們用)

6. 至於另外兩種static：(a) static local variables (of a function/method) (b) class static (used for declaring class methods/data-members)

6(a) For class static, Python已用其獨特要求移除大部分障礙：

       一個method在呼叫「自己或自己家的function」或是access「自己或自己家的變數(data member)」時一定要説   是ClassName.Func123()、還是self.Func123()、還是ClassName.var456、還是self.var456。(不像一般的OOP語言，可以不寫'ClassName'或'this'(='self'))

       唯一的問題是： self.var456有可能是個class data member(如果instance不曾assign過任何值給self.var456的話)，而這是OOP的老問題。

       self.fun456()也有可能是個class member function(Python不接受function overload，所以instance自己不能有同名的function)，這同樣是OOP的老問題，不過可以因為"the implicit handling of 'self'"而略微得到緩解。

       類似的狀況也可能會在instance method呼叫「自己的function或自己家的function」時發生，但此部分已因「Python不接受function overload、而又要求必須在呼叫時寫清楚是ClassName.Func123()還是self.Func123()」而自動獲得解決。

  (一) Class method (class member function)，只要在define method時  不放  'self' 這個parameter  即可
       同樣的，instance method (instance member function)，只要在define method時  放  'self' 這個parameter  即可
       Python不接受function overload(即不同的functions使用同一名字)，所以也不會有Class1.Func123()「既有可能是class method、也有可能是instance method」的問題。

  (二) 若是class data member，必須保證所有的instance method都不會自行宣告(=assign)一個同名稱的變數才行！此時一個比較好的作法是
            將此class data member宣告(=assign)為__dataMember123___(雙底線開頭三底線結尾)  # 不過這只是夏氏公司的建議寫法。

6(b) For static local variables (of a function/method), 我們可在module或class中宣告(=assign)一個變數，其名稱或為_funcName_varName(如果是module的話)、或為__methodName_varName___(如果是class的話)

#############################

如何在寫Python script時 實作 private、protected、public  與  static、non-static (如果有此方面的考量的話)  -  該怎麼做？？？

### 一切要靠naming convention 與 寫程式人的良心 ！！！ 系統只提供了聊勝於無的小小幫助(不import '_'開頭者 與 do name mangling for '__'開頭者) ### 

### 既然一切要靠「寫程式的規矩」與「寫程式的人的自我約束」，那「規矩」到底是什麼？ 必須講清楚、說明白。 ###

# Below shows why syntax-restrictions in Python are necessary for different levels of software development.
  
Module (=file) 之中不想被別人動的變數或functions   # module-static

  '_varName' 或 '_FuncName()' 或 '__varName' 或 '__FuncName()', etc.（底線開頭） 

Class之中不想被「非我族類」(＝非descendent-class者)動的變數或functions   # class-protected

  '_dataMember123' 或 '_FuncName()'（單底線開頭）

Class之中不想被任何「非我家人」(＝非本class者)動的變數或functions   # class-private

  '__dataMember123' 或 '__FuncName()'（雙底線開頭）
  但注意頂多只能一個底線結尾。

除非是自己的"自製系統"要用到，否則不准使用雙底線開頭又雙底線結尾的變數名稱或function/method名稱(e.g., __var123__ 與 __Func567__() )。

Static local variables (of a function/method)

  名稱必須是 __funcName_varName(如果是module的話) 或 __methodName_varName___(如果是class的話)
  +
  此 __funcName_varName(如果是module的話) 或 __methodName_varName___(如果是class的話) 必須 事先 有在module/class中宣告(= assign)

Class static method (即class member function)

  在define method時  不放  'self'這個parameter # Python系統有支援此做法

Class static data member (即class data member) ： 

  將此class data member宣告(=assign)為  __dataMember123___  (雙底線開頭、三底線結尾)
  +
  Never write something like 'self.__varName___ = ...' (in an instance method)

剩下的就只能靠禱告了：祈求寫程式的人能尊重這些不成文的規矩(否則一切完矣...)。  

##### 能不reference最好！能不看更好！！但最最起碼也千萬不要update！！！ #####

#############################

      A comprehensive example for private/protected/public and static/non-static 

#############################

```sh
# Note by wang : The following was copied from a previous class note, followed by doing some modifications in the system-output-part.
#                Therefore, there may be some discrepancy between the system output shown here and the real system output.

>>> B( 'cat ~/bin/PyTestOfFandC.py' )
# File name : PyTestOfFandC.py

aOfFandC     = 10
bOfFandC_    = 20
_cOfFandC    = 30
_dOfFandC_   = 40
__eOfFandC   = 50
__fOfFandC_  = 60
__gOfFandC__ = 70

def F() :
  print( "__name__ printed from the module named 'PyTestOfFandC' :" )
  print( __name__ )

class C :
  def F( self ) :
    print( "__name__ printed from the module named 'PyTestOfFandC' :" )
    print( __name__ )
  
  def G() :
    print( "__name__ printed from the module named 'PyTestOfFandC' :" )
    print( __name__ )

def PrintModuleVar() :
  print( "Value of aOfFandC :",     aOfFandC )
  print( "Value of bOfFandC :",     bOfFandC_ )
  print( "Value of _cOfFandC :",    _cOfFandC )
  print( "Value of _dOfFandC_ :",   _dOfFandC_ )
  print( "Value of __eOfFandC :",   __eOfFandC )
  print( "Value of __fOfFandC_ :",  __fOfFandC_ )
  print( "Value of __gOfFandC__ :", __gOfFandC__ )


>>> import PyTestOfFandC as testFC

>>> dir( testFC )
['C', 'F', 'PrintModuleVar', '__builtins__', '__cached__', '__doc__', '__eOfFandC', '__fOfFandC_', '__file__', '__gOfFandC__', '__loader__', '__name__', '__package__', '__spec__', '_cOfFandC', '_dOfFandC_', 'aOfFandC', 'bOfFandC_']

>>> testFC.F()
__name__ printed from the module named 'PyTestOfFandC' :
PyTestOfFandC

# this is not surprising
# but how about this ???

>>> from PyTestOfFandC import *    ### <---------------------------------------- (watch out!)

>>> dir()
['B', 'C', 'Class123', 'F', 'PrintModuleVar', 'PyTestOfFandC_02', 'S', 'Test0', 'Test1', 'Test3', 'Test4', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'aOfFandC', 'bOfFandC_', 'gA', 'obj123', 'obj456', 'os', 'pprint', 'subprocess', 'sys', 'testFC']

# we see that module-vars with names starting with '_' are not imported (thereby becoming names of the current "namespace")

# therefore,
>>> __name__
'__main__'

>>> F()
__name__ printed from the module named 'PyTestOfFandC' :
PyTestOfFandC

# Good! the '__name__' referenced by this F() (which is actually PyTestOfFandC.F() and not our original, locally defined F()) is still 'PyTestOfFandC.__name__' and not the local '__name__' here

# Lesson learned : imported functions and classes and "globals" 會蓋掉原有的 functions and classes and globals！ 但其運作方式依舊是依照其"來處"的運作方式！(wang : 應只是name qualification的問題 - 我們所使用的names與系統真正使用的names不一樣。 More comments from wang : It's only a matter of "誰是誰"、亦即系統必須由我們所使用的名字搞清楚我們指的到底是誰、一旦搞清楚我們指的是誰、就依照那個「誰」該有的運作方式運作(該怎麼做就怎麼做)！)

# But is 'module-static' protection (module-static variables cannot be accessed from the outside) honored in Python??? 

>>> testFC.__name__ = testFC.__name__ + '_okay'

>>> F()
__name__ printed from the module named 'PyTestOfFandC' :
PyTestOfFandC_okay

# Nope! (i.e., the concept of module-static is not really honored in Python)

# How about "globals" in the general sense (and not just those with names starting with two '_' and ending with two '_')?

>>> PrintModuleVar()
Value of aOfFandC : 10
Value of bOfFandC : 20
Value of _cOfFandC : 30
Value of _dOfFandC_ : 40
Value of __eOfFandC : 50
Value of __fOfFandC_ : 60
Value of __gOfFandC__ : 70

# Obviously, PrintModuleVar() (which is actually testFC.PrintModuleVar() ; 'PrintModuleVar' is just a kind of "alias" if you will) still works in its original "namespace" environment (and not in the current "namespace" environment (there is no '_cOfFandC', for example, in the current "namespace" environment))

>>> aOfFandC += 5
>>> bOfFandC_ += 5
>>> _cOfFandC += 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_cOfFandC' is not defined. Did you mean: 'aOfFandC'?

# that is, there is no '_cOfFandC' in the current "namespace"

>>> testFC._cOfFandC += 5
>>> testFC._dOfFandC_ += 5
>>> testFC.__eOfFandC += 5
>>> testFC.__fOfFandC_ += 5
>>> testFC.__gOfFandC__ += 5

>>> sorted( vars())
['B', 'C', 'Class123', 'F', 'PrintModuleVar', 'PyTestOfFandC_02', 'S', 'Test0', 'Test1', 'Test3', 'Test4', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'aOfFandC', 'bOfFandC_', 'gA', 'obj123', 'obj456', 'os', 'pprint', 'subprocess', 'sys', 'testFC']

# 'PrintModuleVar', 'aOfFandC', and 'bOfFandC_' are said to be "declared in the current namespace". But actually, they are not.

# We do have these names in the current "namespace". However, it is not guaranteed that they are declared here!

>>> PrintModuleVar()
Value of aOfFandC : 10
Value of bOfFandC : 20
Value of _cOfFandC : 35
Value of _dOfFandC_ : 45
Value of __eOfFandC : 55
Value of __fOfFandC_ : 65
Value of __gOfFandC__ : 75

# On one hand, this is outrageous (an imported name is not really the original one ...)！
# On the other hand, it means that the system does not allow us to DIRECTLY change the module-vars of imported modules (i.e., we can only reference them, but we cannot update them), a restriction that is understandable.

# now, 'aOfFandC', and 'bOfFandC_' are really declared in the current "namespace". (But is there an easy way to tell which case it is ???)

# Quick recap : Python has module-static (a module can have its own "globals"), but it does not offer module-static-protection. 

#               Furthermore, after we have SUCCESSFULLY imported other module's "globals", we can only reference these imported globals ; if we change them, these "globals" of other modules become our own globals (this, however, does not mean that we cannot change other module's global though).

# Q : Suppose we only reference aOfFandC and bOfFandC_ in the current namespace (and do not do things like 'aOfFandC += 5', i.e., do not change their values directly). If we first do 'tesfFC.aOfFandC += 5' and then reference 'aOfFandC' again, will we find the value of 'aOfFandC' changed?  You'll be surprised. (at least I am surprised...)

# Q : What will happen if we first 'testFC.aOfFandC += 100' and then 'from PyTestOfFandC import *' again???

# A new recap : (about F() and PrintModuleVar() and aOfFandC and bOfFandC_ ...)

# 說起來也蠻好笑的...，既然一旦import *進來就完全變成另外一個人，又何必在乎名稱是否是以'_'作為開頭(反正也改不到原來的那個)？

# 那個重複import *所得的結果又要如何在abstract-level解釋清楚？？？
```

#############################

# Let us now turn our attention to a different question - does Python support the notion of private or protected or "class/function static"?

```sh
>>> class Class1 :
...   
...   # class data members (three underlines following the name) declared (= assigned) here
...   __a123___ = 10          # intended to be sprivate
...   _b123___ = 20           # intended to be protected
...   c123___ = 30            # intended to be public
...   
...   __d123__ = 40           # special class data members (only two underlines following the name)
...   
...   __e123_  = 50           # just want to see what will happen
...   __f123   = 60           # just want to see what will happen
...   
...   def __init__( self ) :
...     
...     Class1.__a123___ += 1
...     
...     # instance data members (no more than two underlines following the name) declared (= assigned) here
...     self.myOwn = 1000      # intended to be public
...     self._myOwn = 2000     # intended to be protected
...     self.__myOwn = 3000    # intended to be private
...     self.__myOwn_ = 4000   # just want to see the effects of '__' plus '_'
...     
...     self.__myOwn__ = 5000  # special instance data member
...     
...     self.__myOwn___ = 6000 # just want to see the effects of '__' plus '___'
...   
...   def PrintClassVar() :
...     
...     ## NameError: name '__a123___' is not defined
...     # print( "Value of __a123___ :", __a123___ )
...     
...     print( "Value of __a123___ :", Class1.__a123___ )
...     print( "Value of _b123___ :",  Class1._b123___ )
...     print( "Value of c123___ :",   Class1.c123___ )
...     print( "Value of __d123__ :",  Class1.__d123__ )
...     print( "Value of __e123_ :",   Class1.__e123_ )
...     print( "Value of __f123 :",    Class1.__f123 )
...   
...   def PrintInstanceVar( self ) :
...     print( "Value of self.myOwn :",      self.myOwn )
...     print( "Value of self._myOwn :",     self._myOwn )
...     print( "Value of self.__myOwn :",    self.__myOwn )
...     print( "Value of self.__myOwn_ :",   self.__myOwn_ )
...     print( "Value of self.__myOwn__ :",  self.__myOwn__ )
...     print( "Value of self.__myOwn___ :", self.__myOwn___ )
...     
...     print( "Value of __a123___ :", Class1.__a123___ )
...     print( "Value of _b123___ :",  Class1._b123___ )
...     print( "Value of c123___ :",   Class1.c123___ )
...     print( "Value of __d123__ :",  Class1.__d123__ )
...     print( "Value of __e123_ :",   Class1.__e123_ )
...     print( "Value of __f123 :",    Class1.__f123 )
... 
>>> # END-Class1

>>> aClass1 = Class1()

>>> dir( Class1 )
['PrintClassVar', 'PrintInstanceVar', '_Class1__e123_', '_Class1__f123', '__a123___', '__class__', '__d123__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_b123___', 'c123___']

>>> sorted( vars( Class1 ))
['PrintClassVar', 'PrintInstanceVar', '_Class1__e123_', '_Class1__f123', '__a123___', '__d123__', '__dict__', '__doc__', '__init__', '__module__', '__weakref__', '_b123___', 'c123___']

>>> # Apparently, name mangling only occurs for data members (class or instance) that have names with two '_' before and at most one '_' behind.

>>> Class1.PrintClassVar()
Value of __a123___ : 11
Value of _b123___ : 20
Value of c123___ : 30
Value of __d123__ : 40
Value of __e123_ : 50
Value of __f123 : 60

>>> Class1.__a123___ += 5
>>> Class1._b123___ += 5
>>> Class1.c123___ += 5
>>> Class1.__d123__ += 5
>>> Class1._Class1__e123_ += 5
>>> Class1._Class1__f123 += 5

>>> Class1.PrintClassVar()
Value of __a123___ : 16
Value of _b123___ : 25
Value of c123___ : 35
Value of __d123__ : 45
Value of __e123_ : 55
Value of __f123 : 65

>>> dir( aClass1 )
['PrintClassVar', 'PrintInstanceVar', '_Class1__e123_', '_Class1__f123', '_Class1__myOwn', '_Class1__myOwn_', '__a123___', '__class__', '__d123__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__myOwn__', '__myOwn___', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_b123___', '_myOwn', 'c123___', 'myOwn']

>>> sorted( vars( aClass1 ))
['_Class1__myOwn', '_Class1__myOwn_', '__myOwn__', '__myOwn___', '_myOwn', 'myOwn']

>>> aClass1.PrintInstanceVar()
Value of self.myOwn : 1000
Value of self._myOwn : 2000
Value of self.__myOwn : 3000
Value of self.__myOwn_ : 4000
Value of self.__myOwn__ : 5000
Value of self.__myOwn___ : 6000
Value of __a123___ : 16
Value of _b123___ : 25
Value of c123___ : 35
Value of __d123__ : 45
Value of __e123_ : 55
Value of __f123 : 65

>>> aClass1._Class1__myOwn += 5
>>> aClass1._Class1__myOwn_ += 5
>>> aClass1.__myOwn__ += 5
>>> aClass1.__myOwn___ += 5
>>> aClass1._myOwn += 5
>>> aClass1.myOwn += 5

>>> aClass1.PrintInstanceVar()
Value of self.myOwn : 1005
Value of self._myOwn : 2005
Value of self.__myOwn : 3005
Value of self.__myOwn_ : 4005
Value of self.__myOwn__ : 5005
Value of self.__myOwn___ : 6005
Value of __a123___ : 16
Value of _b123___ : 25
Value of c123___ : 35
Value of __d123__ : 45
Value of __e123_ : 55
Value of __f123 : 65

>>> # The above should serve to show that Python does not offer 'private' or 'protected' protection for 'class-static' data and instance data.
>>> # Python does offer name mangling for data members with names starting with two '_' and ending with at most one '_' (be it class-data or instance-data)

# Quick recap : Python does have class-static, but it does not offer private/protected-like protection for class/instance data members.
# I believe the same is true for class/instance member functions (= methods)
```

Q : 為何module-static的data不比照instance-data或class-data的作法、以name mangling的方式來多少使user感到不方便、從而discourage user對這些data(即名字是雙底線開頭至多單底線結尾的data)的access？  或者反過來說，為何instance-data或class-data不比照module-static data的作法、乾脆讓user"看不到"(因此就無法access)？

#############################

# END - A comprehensive example for private/protected/public and static/non-static

####### reflection time #######

https://towardsdatascience.com/private-protected-attributes-in-python-demystified-once-and-for-all-9456d4e56414

Critics suggest that to prevent attribute clobbering it’s enough to simply stick to the convention of prepending the attribute with a single underscore. Here’s the full quote from Ian Bicking I cited at the beginning of the article;

  Never, ever use two leading underscores. This is annoyingly private. If name clashes are a concern, use explicit name mangling instead (e.g., _MyThing_balabla). This is essentially the same thing as double-underscore, only it’s transparent where double underscore obscures.

I must note that an attribute with a single leading underscore _ does not mean anything special to the python interpreter. But, it’s one of those strong conventions in the world of Pythonistas. If you see one, it means that you should not access such attributes from outside the class. You can even observe that even in some corners of the official Python documentation, attributes with a single leading underscore _ are called “protected.”

Even though the practice of “protecting” an attribute using a single leading underscore is common, it is not as often to hear them being called “protected” attributes. Some even call them “private.”

#############################

Function分三種：

  Module functions   - 即傳統的functions 
                      (除非所屬module有被'from ModuleName import *'或是所屬module是本module或是所屬module是top-level，否則稱呼時必須指名所屬module，e.g., os.system(); 如果有作'from os import *'、則system()即可 )

  Class functions    - Module之中被分門別類(稱呼時必須冠上其"姓氏")的傳統functions
                      (呼叫原則與module functions相同，只是要加上其"姓氏"而已，e.g., MyModule1.Class10.G123(); 如果有作'from MyModule1 import *'、則Class10.G123()即可 )

  Instance functions - instances "自有" 的functions (e.g., a = ClassName() ; a.F() )
                       (note : 可經由instance呼叫其所屬class的class functions，也可經由instance access其所屬class的class data (前提是instance本身並沒有define (= assign)同名的data) 。 instance本身若要(在其 "自有" 的function裡面)assign to class variables、必須'ClassName.var1 = ...'而不能'self.var1 = ...'！)

如果module-variable (module-data)不希望被存取，就在此module-variable名稱的最前面加'_'(隨便幾個'_'皆可，一個就夠)。如此一來，使用者就不能在'from ModuleName import *'之後直接以名稱來access此module-variable。不過使用者依舊可以使用'ModuleName._varName'這個名稱來access (包括update) '_varName'(不管varName的名稱之中還有幾個'_')這個「ModuleName的作者不希望被存取的」module-data; 同時，我們一般也不鼓勵使用'from ModuleName import *'這種寫法。所以再怎麼說、module-variables (module-data)都無系統保護可言。

如果class data或instance data不希望被存取，就在這些data名稱的最前面加雙底線、而名稱的最後--頂多--只能有一個底線。如此一來，使用者就不能直接以此data的名稱來access此data。不過不過不過、這只是個小小的不方便措施而已，使用者依舊可以使用'_ClassName__dataName'(或'_ClassName__dataName_')這個名稱來access (包括update) '__dataName'(或'__dataName_')這個--不希望被存取的--class-data或instance-data。

# 讀者(of this article)可以compare what-is-said-here with what is said in the Python reference manual (e.g., p. 9, p. 45, and p. 64 of reference.pdf, version 3.7.4) about the meaning of the use of underscores ('_') at the beginning (and possibly at the end too) of variable names. I think what-is-said-here is clearer.


～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

低中高階層programmers的風格要求

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

Discussions.

############################# Final Summary written on 2023-11-10, revised on 2023-11-20 #############################

Python認為：

  Function就是function，不該有"module function", "class function"與"instance function"的區別！

  同理，data (or name)就是data (or name)，不該有"module data", "class data"與"instance data"的區別！

  F()、module1.F()、class1.F()、class1_instance.F()都是同一"種類"的functions，而且Python的functions就那麼一個種類而已、沒有不同的種類。我們只是有不同的「命名規矩」而已，而「命名規矩的不同」並不意味著這些「使用不同命名方式取名字的functions」事實上是不同種類的functions。

  任何function都有一個「所屬module」、此「所屬module」就是「內中有列出此function之定義」的那個檔案。(請注意：「the fictitious top-level」也視同一個"檔案")。
    --
    (請注意：「from ModuleABC import *」的意義分兩部分，對ModuleABC的屬性data而言，「from ModuleABC import *」是在run完ModuleABC之中的程式碼之後、先是在目前所屬module之中重新create同名字的屬性data、然後再將「ModuleABC之中的x之值」copy成為「『目前所屬module』之中的x之值」，而這是個pointer assignmenbt。 那ModuleABC的屬性function怎麼辦？對ModuleABC的屬性function而言，「from ModuleABC import *」只是create aliases而已；也就是說、以ModuleABC之中的function F()為例、雖然看似「目前所屬module」來了這麼一個function F()，但事實上這F()依舊是ModuleABC.F()、而並不真的是「『目前所屬module』的(新的)『屬性function』F()」，只是說、我們在呼叫ModuleABC.F()之時只要寫「F()」就可以了；重點：在「from ModuleABC import *」或「from ModuleABC import F」之後，ModuleABC原有的F()並沒有真的成為「目前所屬module」的屬性function，它(F())依舊是ModuleABC的屬性function；但屬性data的部分就不一樣了，在「from ModuleABC import *」之後，ModuleABC原有的屬性data x (which is a pointer variable)的值會copy成為「新產生的、同名字的、『目前所屬module』的屬性data x」的值)
    --
    (一般的建議是「不要寫『from ModuleABC import *』(除非有很好的理由要這樣做)！ 寫『from ModuleABC import F』 或 『import ModuleABC』就好！」。原因有三，一是「覆蓋」、「目前所屬module」原有的屬性function會被同名字的外來aliases所覆蓋掉(這與C/C++/Java的規矩完全相反)，二是若想"update ModuleABC的屬性data"可能會產生confusion、請見下文的(9)，三是「pointer assignment」所導致的後果也是很容易產生confusion（"「新產生的、同名字的、『目前所屬module』的屬性data x」與ModuleABC原有的屬性data x的關係到底是什麼？"）)
    --
    (Quiz : 在執行「aOfFandC = 55 ; testFC.newF = lambda : print( aOfFandC )」之後，testFC.newF()所印出的aOfFandC是testFC.aOfFandC還是aOfFandC？)
    --
  任何function在執行時都有globals，而這些globals就是「此function之『所屬module』」的「屬性data」(與「屬性functions」) # 「global宣告」對二者都適用

    # 純好奇：根據本人對Python的哲學的了解，應該會...

    ```sh
    >>> def F123() :
    ...   print( 123 )
    ... 
    >>> def F456() :
    ...   global F123
    ...   F123 = lambda : print( 456 )   # recall the 'lambda' of OurScheme ...
    ... 
    >>> F123()
    123
    >>> F456()
    >>> F123()
    456
    # "Yes！" (我們這種人都是很無聊的！Don't you think so？)
    ```

  倒是object的概念要尊重！

    有些objects是primitive objects (primitive objects事實上是其他語言中的values)。

    除了primitive-objects之外，每個object都可以有它「自有的data」(即所謂的「屬性data」)與「屬性function」。
    # Primitive objects沒有「屬性data」，不過它們有「屬性function」。

    屬性又分作「genuine屬性」與「衍伸屬性」兩種。「genuine屬性」是object「自有」者，「衍伸屬性」則來自其他地方、只是可透過此object reference之而已。

    原則上，只要呼叫 vars( anObj ) 就可知道 anObj有哪些generic屬性(包括「generic屬性data」與「generic屬性function」)。
    
    「屬性data」是(任何人都)可以reference的，「屬性function」則是(任何人都)可以呼叫的。    # i.e., "public", as it is called in other languages

    而且「一個object有哪些屬性」這件事是可以調整的。 Just do : anObj.b = ... 或 del anObj.b 
     # 任何object都是如此 (不管是instance-obj還是class-obj還是module-obj還是func-obj)

    如果一個object是經由a = Some()被創造出來的，那它在被創造出來的時候就會(依據Some這個class的定義)具有某些屬性。
    凡是經由a = Some()被創造出來的objects，我們統稱之為instance-objects。

    instance-objects的屬性分作「genuine屬性」與「衍伸屬性」兩種： # 有點類似function在執行時的local var有「genuine local var」與「fake local var」兩種

      在instance-obj剛被創造出來的時候(也就是 anObj = Some() 剛執行完的時候)、

        相對應的class-object（即Some這個class-object）的「屬性function」就自動成為此instance-obj的 「衍伸屬性function」，

        而所有的「相對應的class-object的『屬性data』」(也就是Some這個class-object的所有「屬性data」)也自動成為instance-obj的「衍伸屬性data」、

          除非在創造此instance-obj時(也就是Some.__init__( anObj, ...)在執行時)有對同名字的屬性作assign的動作(從而使該屬性成為anObj的「genuine屬性」)

    Module也是一種object，不過它不是經由a = Some()創造出來的，Class-objects也不是經由a = Some()創造出來的。

    Function-objects、class-objects、與module-objects這三"種"objects都是經由「定義」的方式而implicitly創造出來的、
    而不是經由a = Some()這種方式explicitly創造出來的。

    換言之，總共有五種objects : instance-objects, module-objects, class-objects, function-objects, 與primitive-objects。
           其中instance-objects有呼叫「屬性function」時的特殊待遇( a.F(...) 會被轉換成 Some.F(a, ...) )，
               而primitive-objects則沒有「屬性data」(但有「屬性function」)

Class-objects的「(default)屬性data」是由其定義決定之，

  e.g.,
```py
  class Class1 :
    data1 = 10
    data2 = 20
    def __init__( self ) :
      ...
    def F() :
      ...
    ...
```
  就決定

  'Class1'所name的class-object有'data1'與'data2'這兩個屬性data

a = Class1() 除了產生一個 ('a'所name的) instance-object (an instance of Class1) 之外、也有implicitly呼叫 Class1.__init__( a )。

以上就是幾乎所有「Python有關OOP的設計」。  # 也許再加上繼承的概念與一些'from ModuleABC import *'的限制與name-mangling的特殊設計。  That's all！

# 不過還是要談一下「如何(正確的)定義一個class以及其衍伸class」

```sh
>>> class Test :
...   x = 10                         # class-object (即Test) 的(default)屬性data是寫在這裡
...   def __init__( self ) :         # 在此constructor產生self(supposedly是個此class的instance-object)的(default)屬性data
...     self.x1 = 10                 #   例如x1與下面這一行的y1
...     self.y1 = self.x1 + self.x   # x(只要是reference而非update) 事實上是 self的「衍伸屬性data」(Test的屬性data)
...     z1 = 100                     # z1只是__init__()的區域變數
...   def F( whatever ) :
...     print( whatever.x )
...   def G() :
...     print( Test.x )
... 
>>> test = Test()

>>> sorted( vars( Test ) )   # Test的generic屬性(包括generic屬性functions)
['F', 'G', '__dict__', '__doc__', '__init__', '__module__', '__weakref__', 'x']

>>> sorted( Test.__dict__ )  # 只是要證明'vars( Test )'事實上是直接return Test.__dict__
['F', 'G', '__dict__', '__doc__', '__init__', '__module__', '__weakref__', 'x']

>>> sorted( vars( test ) )  # test這個instance-obj的generic屬性(注意沒有generic屬性function)
['x1', 'y1']

>>> dir( test )             # test這個instance-obj的衍伸屬性(包括衍伸屬性functions)
['F', 'G', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'x', 'x1', 'y1']

>>> dir( Test )             # 只是要show「test這個instance-obj的所有衍伸屬性都是來自Test(的衍伸屬性)」
['F', 'G', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'x']


>>> class RefinedTest( Test ) : # RefinedTest是Test的衍伸class (它也可以是 Test1, Test2, Test3 三者共同的衍伸class ; 只要三者都有出現於參數區即可)
...   refined_x = 10            # 「class-object的『屬性』的繼承」是自動的(亦即：RefinedTest這個class-object不用做任何事就會有Test的所有屬性)
...   def __init__( self ) :    
...                             # 「instance-object的『屬性data』的繼承」則必須要靠「呼叫上一層的constructor」才行
...     super().__init__()      # For any call to this __init__() such as a.__init__(), execute a.__init__() here ;
...                             #   however, the __init__() being called this time is the one defined in the parent class
...                             # This way of doing things is to mimic the use of 'super()' in a Java constructor
...     # 也就是 Test.__init__( self ) ； 事實上左邊這個寫法較好(不用硬加一些如上的ad hoc觀念)、也比較general
...     
...     self.refined_x1 = 10
...     self.refined_y1 = self.x1 + self.x   # x是個自動有的衍伸屬性data(它是RefinedTest的衍伸屬性data)； x1則要靠呼叫Test.__init__( self )才會有
...     z1 = 100
...   def Refined_F( whatever ) :
...     print( whatever.refined_x )
...   def Refined_G() :
...     print( Test.refined_x )
...   def G() :
...     pass
... 
>>> 
>>> refined_test = RefinedTest()

>>> sorted( vars( RefinedTest ) )  # generic屬性
['G', 'Refined_F', 'Refined_G', '__doc__', '__init__', '__module__', 'refined_x']

>>> dir( RefinedTest )             # generic屬性 + 衍伸屬性
['F', 'G', 'Refined_F', 'Refined_G', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'refined_x', 'x']

>>> vars( refined_test )           # generic屬性(注意沒有generic屬性functions)
{'x1': 10, 'y1': 20, 'refined_x1': 10, 'refined_y1': 20}

>>> dir( refined_test )            # generic屬性 + 衍伸屬性
['F', 'G', 'Refined_F', 'Refined_G', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'refined_x', 'refined_x1', 'refined_y1', 'x', 'x1', 'y1']

>>> RefinedTest.G()   # G() has been overridden in RefinedTest  # 「覆蓋」這件事、在Python倒是蠻自然的(Python根本就是以「覆蓋」為業，到處都可以覆蓋！)
>>> 
```

請注意：

在  任何function  的  執行過程之中...

1. 你不可能經由 self.class_x = ... (或 obj.class_x = ...) 的方式  來  更改(update)  self(或obj)所屬class的class-obj  的  class_x屬性 
   唯有使用  Class1.class_x = ...  的方式  才能  更改(update)到  self(或obj)所屬class的class-obj(即Class1)  的  class_x屬性

2. 本來 ancestor function的local var. 與 所屬module的屬性data(即所謂的global data) 也是一樣的狀況、甚至更糟(因為根本無法update這些local var與global var)
   而這就是Python提供'nonlocal'與'global'宣告的原因！(讓我們能在一個function執行的過程之中  更改  ancestor function的local var. 與  所屬module的屬性data)

   (Quiz : 可以透過'nonlocal'宣告 來 更改 ancestor function的local function的定義 嗎？)

---------------------------

1. 再一次強調：Assign(一個東西給一個name)即宣告(這個name於「目前的namespace」之中)、除非有在此assignment上方作'nonlocal'或'global'宣告。
             而且只要function中有這麼一個statement(不管出現在function的哪一部分)就算數，Python並沒有要求一定要執行到這個assignment stmt才算數。

             注意Python並沒有把「宣告」與「存在」視為同一回事。
             前者是個「文法檢查的概念」，後者則是個「執行環境的概念」。
             此二者有可能同時發生、也可能不同時發生。

     # Python所謂的namespace，就只是一個「a set of names」(而已)

     # A Python-namespace可能是module(-object)的屬性 (其中的「屬性data」、對屬於這個module的functions而言是global var.)、
       也可能包括function()在執行時的local var.與para.、 # Python的conditionals與loops沒有自己的local vars ; local var.只有function才有
       也可能是某個instance-obj的屬性(包括「屬性data」與「屬性function」)、
       也可能是某個class-object的屬性(包括「屬性data」與「屬性function」)、
       也可能是某個function-object的「屬性data」 (看不出有什麼用就是了)

2. vars( anObj ) 可以 show anObj 的 namespace                     # 即anObj的屬性 目前有哪些、以及其值為何
   locals() 可以 show 「目前正在執行的這個function」 可 reference的"local names" (≠ local vars)  # 目前有哪些、以及其值為何
   # 請注意以上兩個是完全不一樣的概念。一個是function在執行時的temporary data，一個是permanent data (只要object存在就有、而objects一經產生就理論上永遠存在)
   # 後者有包括到前者，前者不可能牽涉到後者

3. def vars( anObj ) :        # 事實上是
     return anObj.__dict__    # That's all, folks!

4. 也就是說、如果我們能更動 anObj 的 __dict__ 這個"屬性"的內容，我們就能改變 anObj的屬性

   e.g., anObj.__dict__['x'] = 100

5. "primitive objects"(Python版的"values")  沒有  __dict__ 這個"屬性"； 

   # 每一個「執行中的functions」(即call-stack上的每一個activation records)應該都有一個類似 __dict__ 的東西，但system不show它 (for very good reasons)
   
6. 有些objects (如class objects) 的 __dict__ 、系統不讓我們(輕易？)改。

7. 'x = x + 1'有可能會導致error，因為尚未宣告x就要取其值。但如果ancestor function已有設定x這個local就可以。
   但此時'x = x + 1'並不是改變ancestor function的x (假設並沒有作'nonlocal'的宣告)，而是宣告一個local x。

8. 同理，'self.x = self.x + 1'有可能會導致error，因為尚未宣告self的x就要取其值。但如果所屬class已有設定x這個data就可以。
   但此時'self.x = self.x + 1'並不是改變所屬class的x，而是宣告一個self的instance data x。

9. 同理，假設ModuleABC之中有moduleABC_x這個屬性data，'from ModuleABC import * ; moduleABC_x = moduleABC_x + 1'
   並不會改變ModuleABC的moduleABC_x，而是宣告一個「目前所屬module」的屬性data moduleABC_x。

10. 在任何地方、只要系統允許我們改anObj的__dict__ (e.g., anObj.__dict__['x'] = 100)，我們就可以 anObj.x = 100 ；
    二者的效果是一樣的。

    而且系統並「不」要求「anObj必須已經有x這個instnace data」才能這樣改其值。

    也就是說，我們事實上可以任意增加一個object (be it a module or a class or an instance of a class) 的屬性。Just do : anObj.x = ...
    也可以任意去掉一個object (be it a module or a class or an instance of a class) 的屬性。 Just do : del anObj.x    

    # 當然， we can also delete a local var (or 某object的屬性) inside any function
    # Just do : del x (or del self.x, or del os.happy)

############################# END - Final Summary written on 2023-11-10, revised on 2023-11-20 #############################


#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

def Test0() :
  def Test01() :
    
    nonlocal a   # 'a' may or may not have been assigned
    
    print( "\n----- Test01() -----" )
    print( "locals() : " ) ; pprint( locals() )
    print( "globals() : " ) ; print( sorted( globals() ) )
    print( "----- END - Test01() -----\n" )
    
  # END - Test01()
  
  print( "----- Test0() -----" )
  print( "locals() : " ) ; pprint( locals() )
  print( "globals() : " ) ; print( sorted( globals() ) )
  
  Test01()
  
  a = 10   # 'a' assigned here
  
  print( "locals() : " ) ; pprint( locals() )
  print( "globals() : " ) ; print( sorted( globals() ) )
  
  Test01()
  
  # END - Test0()

#########################################################################################

def Test1() :
  def Test11() :
    
    nonlocal a   # 'a' may or may not have been assigned
    
    print( "\n----- Test11() -----" )
    print( "locals() : " ) ; pprint( locals() )
    print( "globals() : " ) ; print( sorted( globals() ) )
    print( "----- END - Test11() -----\n" )
    
    a = 55   # 'a' assigned here
    
  # END - Test11()
  
  print( "----- Test1() -----" )
  print( "locals() : " ) ; pprint( locals() )
  print( "globals() : " ) ; print( sorted( globals() ) )
  
  Test11()
  
  print( "locals() : " ) ; pprint( locals() )
  print( "globals() : " ) ; print( sorted( globals() ) )
  
  Test11()
  
  a = 10   # just to make 'a' a local var. of Test1(), so that Test11() can make it 'nonlocal'
  
  # END - Test1()

#########################################################################################

def Test3() :
  def Test31() :
    
    nonlocal a   # 'a' may or may not have been assigned
    global gA    # <--------------------- 'global' declared here
    
    print( "\n----- Test31() -----" )
    print( "locals() : " ) ; pprint( locals() )
    print( "globals() : " ) ; print( sorted( globals() ) )
    
    gA = 100     # the global starts to exist here
    
    print( "----- END - Test31() -----\n" )
    
  # END - Test31()
  
  print( "----- Test3() -----" )
  print( "locals() : " ) ; pprint( locals() )
  print( "globals() : " ) ; print( sorted( globals() ) )
  
  Test31()
  
  a = 10   # 'a' assigned here
  
  print( "locals() : " ) ; pprint( locals() )
  print( "globals() : " ) ; print( sorted( globals() ) )
  
  Test31()
  
  # END - Test3()


#########################################################################################

# Does the system store the local namespace (of an execution instance) in the __dict__ of a function definition? Probably not.

def Test4() :      # Modified from Test1()
  def Test41() :
    
    nonlocal a   # 'a' may or may not have been assigned
    
    print( "\n----- Test41() -----" )
    print( "locals() : " ) ; pprint( locals() )
    print( "Test41.__dict__" ) ; pprint( Test41.__dict__ ) ;  # <----- just added this
    print( "globals() : " ) ; print( sorted( globals() ) )
    print( "----- END - Test41() -----\n" )
    
    a = 55   # 'a' assigned here
    
  # END - Test41()
  
  print( "----- Test4() -----" )
  print( "locals() : " ) ; pprint( locals() )
  print( "Test4.__dict__" ) ; pprint( Test4.__dict__ ) ;   # <----- and this
  print( "globals() : " ) ; print( sorted( globals() ) )
  
  Test41()
  
  print( "locals() : " ) ; pprint( locals() )
  print( "Test4.__dict__" ) ; pprint( Test4.__dict__ ) ;   # <----- and this
  print( "globals() : " ) ; print( sorted( globals() ) )
  
  Test41()
  
  a = 10   # just to make 'a' a local var. of Test1(), so that Test11() can make it 'nonlocal'
  
  # END - Test4()


#########################################################################################

# Just for showing what is a class-object

class Class123 :
  
  classDataMember123 = 10        
  
  def __init__( self ) :
    
    Class123.classDataMember123 += 1
    
    self.myOwn123 = 1000
    
  def InstanceMethod123( self ) :
    pass
  
  def ClassMethod123() :
    pass

#########################################################################################

# for demonstrating the distinction between local var. and instance var.

class Class123 :
  
  classDataMember123 = 10          
  
  def __init__( self ) :
    
    Class123.classDataMember123 += 1
    
    self.myOwn123 = 1000
    
  def InstanceMethod123( self ) :
    
    Class123.classDataMember123 += 7
    print( "Value of Class123.classDataMember123 : ", Class123.classDataMember123 )
    print( "Value of self.classDataMember123 : ", self.classDataMember123 )
    
    self.myOwn123 += 5
    print( "Value of self.myOwn123 : ", self.myOwn123 )
    
    myOwn123 += 50
    print( "Value of self.myOwn123 : ", self.myOwn123 )
    
  def ClassMethod123() :
    
    Class123.classDataMember123 += 10
    print( "Value of classDataMember123 : ", Class123.classDataMember123 )

#########################################################################################

# for demonstrating the distinction between local var. and instance var.

class Class123 :
  
  classDataMember123 = 10          
  
  def __init__( self ) :
    
    Class123.classDataMember123 += 1
    
    self.myOwn123 = 1000
    
  def InstanceMethod123( self ) :
    
    Class123.classDataMember123 += 7
    print( "Value of Class123.classDataMember123 : ", Class123.classDataMember123 )
    print( "Value of self.classDataMember123 : ", self.classDataMember123 )
    
    self.myOwn123 += 5
    print( "Value of self.myOwn123 : ", self.myOwn123 )
    
    myOwn123 = 50
    print( "Value of myOwn123 : ", myOwn123 )
    
  def ClassMethod123() :
    
    Class123.classDataMember123 += 10
    print( "Value of classDataMember123 : ", Class123.classDataMember123 )

#########################################################################################

# The concept of "growing instance" and "growing class"

class Class123 :
  
  classDataMember123 = 10          
  
  def __init__( self ) :
    
    Class123.classDataMember123 += 1
    
    self.myOwn123 = 1000
    
  def InstanceMethod123( self ) :
    
    Class123.classDataMember123 += 7
    print( "Value of Class123.classDataMember123 : ", Class123.classDataMember123 )
    print( "Value of self.classDataMember123 : ", self.classDataMember123 )
    
    self.myOwn123 += 5
    print( "Value of self.myOwn123 : ", self.myOwn123 )
    
    myOwn123 = 50
    print( "Value of myOwn123 : ", myOwn123 )
    
  def InstanceMethod456( self ) :
    
    self.myOwn456 = 5
    print( "Value of self.myOwn456 : ", self.myOwn456 )
    
  def InstanceMethod789( self ) :
    
    self.myOwn456 += 5
    print( "Value of self.myOwn456 : ", self.myOwn456 )
    
  def ClassMethod123() :
    
    Class123.classDataMember123 += 10
    print( "Value of classDataMember123 : ", Class123.classDataMember123 )
    
  def ClassMethod456() :
    
    Class123.classDataMember456 = 10
    print( "Value of classDataMember123 : ", Class123.classDataMember123 )
    
  def ClassMethod789() :
    
    Class123.classDataMember456 += 10
    print( "Value of classDataMember456 : ", Class123.classDataMember456 )
    
#########################################################################################

class Class1 :
  
  # class data members (three underlines following the name) declared (= assigned) here
  __a123___ = 10          # intended to be sprivate
  _b123___ = 20           # intended to be protected
  c123___ = 30            # intended to be public
  
  __d123__ = 40           # special class data members (only two underlines following the name)
  
  __e123_  = 50           # just want to see what will happen
  __f123   = 60           # just want to see what will happen
  
  def __init__( self ) :
    
    Class1.__a123___ += 1
    
    # instance data members (no more than two underlines following the name) declared (= assigned) here
    self.myOwn = 1000      # intended to be public
    self._myOwn = 2000     # intended to be protected
    self.__myOwn = 3000    # intended to be private
    self.__myOwn_ = 4000   # just want to see the effects of '__' plus '_'
    
    self.__myOwn__ = 5000  # special instance data member
    
    self.__myOwn___ = 6000 # just want to see the effects of '__' plus '___'
  
  def PrintClassVar() :
    
    ## NameError: name '__a123___' is not defined
    # print( "Value of __a123___ :", __a123___ )
    
    print( "Value of __a123___ :", Class1.__a123___ )
    print( "Value of _b123___ :",  Class1._b123___ )
    print( "Value of c123___ :",   Class1.c123___ )
    print( "Value of __d123__ :",  Class1.__d123__ )
    print( "Value of __e123_ :",   Class1.__e123_ )
    print( "Value of __f123 :",    Class1.__f123 )
  
  def PrintInstanceVar( self ) :
    print( "Value of self.myOwn :",      self.myOwn )
    print( "Value of self._myOwn :",     self._myOwn )
    print( "Value of self.__myOwn :",    self.__myOwn )
    print( "Value of self.__myOwn_ :",   self.__myOwn_ )
    print( "Value of self.__myOwn__ :",  self.__myOwn__ )
    print( "Value of self.__myOwn___ :", self.__myOwn___ )
    
    print( "Value of __a123___ :", Class1.__a123___ )
    print( "Value of _b123___ :",  Class1._b123___ )
    print( "Value of c123___ :",   Class1.c123___ )
    print( "Value of __d123__ :",  Class1.__d123__ )
    print( "Value of __e123_ :",   Class1.__e123_ )
    print( "Value of __f123 :",    Class1.__f123 )

#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################


