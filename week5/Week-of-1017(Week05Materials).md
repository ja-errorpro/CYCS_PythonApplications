Week-of-1017(Week05Materials).txt

---

Review (of what you have been taught) - Q/A

Code tracing (tic-tac-toe)

The use of ChatGPT (and the like) as coding assistants

---

---

                                  Review

---

-------

'=' is assign
'==' is equal
':=' is '=' of C/C++/Java  # the "walrus" operator # difficult for Pascal/Modula people to swallow ...

-------

a = (1,2,3)
if a == 5 :    # ??? Should the system treat it as an error ???
  ...

3+(a:=10)*5    # it is required to have '(' and ')' surrounding an assignment operation (that produces a value)

a=(b:=10)

# use of assignment operation (in an expression) is mainly for efficiency purposes
# ref. python-course.eu | Python Tutorial | Assignment Expressions

a=b=c
# assignment_stmt ::= (target_list "=")+ (starred_expression | yield_expression)
# An assignment statement evaluates the expression list (remember that this can be a single expression or a comma-separated list, the latter yielding a tuple) and assigns the single resulting object to each of the target lists, from left to right.

a>b>10         # ??? a op1 b op2 c df= a op1 b and b op2 c  # "operator chaining"

# (5,) vs. (5)     # the four (?) meanings of '( ... )'

-------

# There is a small defect with the current indentation requirement of Python ...
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

def F2() :
  print( "Within F2() for sure." )

# last line has no indentation (no space)
  print( "Still within F2()." )

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

                             Code tracing practice

～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～

TicTacToe

--------

Original code :  https://code.activestate.com/recipes/578816-the-game-of-tic-tac-toe-in-python/?in=lang-python

def print_board(board):

	print "The board look like this: \n"

	for i in range(3):
		print " ",
		for j in range(3):
			if board[i*3+j] == 1:
				print 'X',
			elif board[i*3+j] == 0:
				print 'O',
			elif board[i*3+j] != -1:
				print board[i*3+j]-1,
			else:
				print ' ',

			if j != 2:
				print " | ",
		print

		if i != 2:
			print "-----------------"
		else:
			print

def print_instruction():
	print "Please use the following cell numbers to make your move"
	print_board([2,3,4,5,6,7,8,9,10])


def get_input(turn):

	valid = False
	while not valid:
		try:
			user = raw_input("Where would you like to place " + turn + " (1-9)? ")
			user = int(user)
			if user >= 1 and user <= 9:
				return user-1
			else:
				print "That is not a valid move! Please try again.\n"
				print_instruction()
		except Exception as e:
			print user + " is not a valid move! Please try again.\n"

def check_win(board):
	win_cond = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
	for each in win_cond:
		try:
			if board[each[0]-1] == board[each[1]-1] and board[each[1]-1] == board[each[2]-1]:
				return board[each[0]-1]
		except:
			pass
	return -1

def quit_game(board,msg):
	print_board(board)
	print msg
	quit()

def main():

	# setup game
	# alternate turns
	# check if win or end
	# quit and show the board

	print_instruction()

	board = []
	for i in range(9):
		board.append(-1)

	win = False
	move = 0
	while not win:

		# print board
		print_board(board)
		print "Turn number " + str(move+1)
		if move % 2 == 0:
			turn = 'X'
		else:
			turn = 'O'

		# get user input
		user = get_input(turn)
		while board[user] != -1:
			print "Invalid move! Cell already taken. Please try again.\n"
			user = get_input(turn)
		board[user] = 1 if turn == 'X' else 0

		# advance move and check for end game
		move += 1
		if move > 4:
			winner = check_win(board)
			if winner != -1:
				out = "The winner is "
				out += "X" if winner == 1 else "O"
				out += " :)"
				quit_game(board,out)
			elif move == 9:
				quit_game(board,"No winner :(")

if __name__ == "__main__":
	main()

---------------------------------------------------------------------------------------------

Modified code (by hsia) :

def print_board( board ) :

  print( "The board looks like this: \n" )

  for i in range(3) :
    print( " ", end = '' )
    for j in range(3):
      if board[ i*3 + j ] == 1 :
        print( 'X', end = '' )
      elif board[ i*3 + j ] == 0 :
        print( 'O', end = '' )
      elif board[ i*3 + j ] != -1 :
        print( board[ i*3 + j ]-1, end = '' )
      else:
        print( ' ', end = '' )

      if j != 2 :
        print( "|", end = '' )
    print( )

    if i != 2 :
      print( "------" )
    else:
      print( )

def print_instruction() :
  print( "Please use the following cell numbers to make your move" )
  print_board( [ 2,3,4,5,6,7,8,9,10 ] )

def get_input( turn ) :

  valid = False
  while not valid :
    try :
      user = input( "Where would you like to place " + turn + " (1-9)? " )   # was 'raw_input'
      user = int( user )
      if user >= 1 and user <= 9 :
        return user - 1
      else :
        print( "That is not a valid move! Please try again." )
        print_instruction()
    except Exception as e :
      print( str( user ) + " is not a valid move! Please try again." )

def check_win( board ) :

  win_cond = ( (1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7) )

  for each in win_cond :
    try :
      if board[ each[0] - 1 ] == board[ each[1] - 1 ] and board[ each[1] - 1 ] == board[ each[2] - 1 ]:
        return board[ each[0] - 1 ]
    except :
      pass

  return -1

def quit_game( board, msg ) :
  print_board( board )
  print( msg )
  quit()

def main():

  # setup game
  # alternate turns
  # check if win or end
  # quit and show the board

  print_instruction()

  board = []
  for i in range(9):
    board.append(-1)

  win = False
  move = 0
  while not win:

    # print board
    print_board( board )
    print( "Turn number " + str( move+1 ) )
    if move % 2 == 0:
      turn = 'X'
    else:
      turn = 'O'

    # get user input
    user = get_input(turn)
    while board[user] != -1 :
      print( "Invalid move! Cell already taken. Please try again." )
      user = get_input( turn )
    board[user] = 1 if turn == 'X' else 0

    # advance move and check for end game
    move += 1
    if move > 4 :
      winner = check_win( board )
      if winner != -1 :
        out = "The winner is "
        out += "X" if winner == 1 else "O"
        out += " :)"
        quit_game(board,out)
      elif move == 9 :
        quit_game(board,"No winner :(")

if __name__ == "__main__" :
  main()

----------------------------------------------------------------------------------------------

Run result : # PyCharm

<HOME-DIR>/PycharmProjects/PythonTheLang/venv/bin/python <HOME-DIR>/PycharmProjects/PythonTheLang/TicTacToe.py
Please use the following cell numbers to make your move
The board looks like this:

 1|2|3
------
 4|5|6
------
 7|8|9

The board looks like this:

  | |
------
  | |
------
  | |

Turn number 1
Where would you like to place X (1-9)? 3
The board looks like this:

  | |X
------
  | |
------
  | |

Turn number 2
Where would you like to place O (1-9)? 5
The board looks like this:

  | |X
------
  |O|
------
  | |

Turn number 3
Where would you like to place X (1-9)? 9
The board looks like this:

  | |X
------
  |O|
------
  | |X

Turn number 4
Where would you like to place O (1-9)? 23
That is not a valid move! Please try again.
Please use the following cell numbers to make your move
The board looks like this:

 1|2|3
------
 4|5|6
------
 7|8|9

Where would you like to place O (1-9)? 5
Invalid move! Cell already taken. Please try again.
Where would you like to place O (1-9)? 2
The board looks like this:

  |O|X
------
  |O|
------
  | |X

Turn number 5
Where would you like to place X (1-9)? 6
The board looks like this:

  |O|X
------
  |O|X
------
  | |X

Turn number 6
Where would you like to place O (1-9)? 8
The board looks like this:

  |O|X
------
  |O|X
------
  |O|X

Turn number 7
Where would you like to place X (1-9)? 1
The board looks like this:

 X|O|X
------
  |O|X
------
  |O|X

The winner is O :)

Process finished with exit code 0

---------------------------------------------------------------------------------------------

Let's debug ...

1. The obvious bug

2. The first char of board printout is extra. How to fix it.

3. After printing "unacceptable move", should show the current board again. How to change the code so that it does it?

---------------------------------------------------------------------------------------------






～～～～～～～～～～～～～～～～～～ break ～～～～～～～～～～～～～～～～～～






Discussion of the use of ChatGPT (and the like) as coding assistants



如果你只想用抄的，那你遲早會被「類ChatGPT」所取代！！！
你必須知道發生什麼事(You must know what the program is doing.)！！！！！
That is, you must UNDERSTAND it and not just MEMORIZE it.

(IF you just want to memorize and repeat what you have been shown to work,
 THEN sooner or later, you will be replaced by ChatGPT or the like.

 But if you know what is actually happening or you can make educated guess about
 what is actually happening, then there is no way that you'll be replaced.)

- 夏延德


根據程式碼管理平台GitHub針對任職於超過1,000名員工大企業的美國程式開發人員的調查，92%的美國工程師表示自己會用AI來編寫程式，70%的受訪者表示AI對大幅提升程式碼品質有幫助。調查也指出，AI工具讓程式開發人員工作成就感提升75%，寫程式的速度也提升超過55%。也因為生成式AI的應用多元且功能驚人，預計將快速滲透至食衣住行育樂的各個層面，而在其功能及介面不斷改善下，百工百業也將有機會進一步採用以提升生產力經濟日報社論／生成式AI對社會的影響與因應

2023-10-03 04:26 經濟日報／ 社論




