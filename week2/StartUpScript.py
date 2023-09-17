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
