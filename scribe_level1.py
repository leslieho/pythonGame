# -*- coding: utf-8 -*-
print "Chapter 1: Breakin' Bad Habits" #the title of the level prints 

print "As a result of your actions, you’re sent to the dungeon to think about what you've done.\n" #this is an intro sentence for the Scribe's version of the game, level 1

action = raw_input("What will you do in this dank and lonely cell? Break out or stay dank and lonely?\n") #Input asking the user if he/she wants to break out of the cell (and thus play the game) or not 
if 'Stay dank and lonely' in action: #If the user says this...
  print "If you wish..." #Then this is the response that will print
  import scribe_level1.py #And as a result, the user will be forced to the start of the scribe's version of level 1

if 'Break out' in action: #If the user wants to break out...
  print "Excellent! You take out your handy dandy quill and begin lockpicking the door.\n" #Then the user has the ability   to lockpick the door 
  lockpick = raw_input("Do you turn your quill to the right or the left first?\n") #Input asking which way the user wants   to turn the quill to lockpick
  if 'Left' in lockpick: #If the user turns it to the left...
      print "The lock breaks free and your cell door swings open!" #Then the user is able to break free from the cell 
  if 'Right' in lockpick: #If the user turns it to the right...
      print "The lock does not budge. Try again.\n" #Then the user is not able to open the door
      lockpick = raw_input("Do you turn your quill to the right or the left first?\n") #Input prompting the user to choose       which way to turn the quill to lockpick again
      if 'Right' in lockpick: #If the user turns it to the right...
      	print "The lock does not budge. Try again.\n" #Then the user is not able to open the door
      if 'Left' in lockpick: #If the user turns it to the left...
      	print "The lock breaks free and your cell door swings open!\n" #Then the user is able to break free from the cell
  door = raw_input("Which door do you choose to leave from? Door one or door two?\n") #Input asking the user which door to   leave from
  if 'Door one' in door: #If the user chooses door one...
        print "Guards find you! You are manhandled and forced back into your cell.\n" #The user is forced back into his/her cell
        import scribe_level1.py #Then the user is forced to start the Scribe's version of level 1 over again
  if 'Door two' in door: #If the user chooses door two...
        print "Fresh, clean air! You are free, Palace Scribe!"#The user is free
        import scribe_level2.py #And the user continues on to the Scribe's version of level 2

        
  

