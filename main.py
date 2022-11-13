import os, time
from getkey import getkey
array = [['-']*7 for i in range(7)] 
column = 0 
row = -1
drop = 0
array[0][0] = '0'
################### print board ###########################################
def printBoard():
  for i in range(7):
    if i == 0: 
      print('  ', end='')
      for i in array[0]:
        print(' ', i, '  ', sep='', end='')
      print('\n')
    else:
      for i in array[i]: 
          print(' | ', i, sep='', end='')
      print(' |\n -----------------------------')
  print('   |                      |\n   _                      _')
########## selection ####################################################
def selection(column):
  choice = getkey()
  choice = choice.lower()
  if choice == 'a':
    column = column - 1
  elif choice == 'd':
    column = column + 1
  if choice == 's':
    drop = 1
  else: d
    drop = 0
  return column, drop
################ main script ##############################################
while True:
  printBoard()
  array[0][column] = '-'
  column, drop = selection(column)
  if column > 6: 
    column = column - 7
  if column < 0: 
    column = column + 7
  if drop == 1:
    print('dropped')
  array[0][column] = '0'
  os.system('clear')
  