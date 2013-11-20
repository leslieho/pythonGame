character1 = {'Name': 'Palace Scribe', 'Gender': 'Male', 'Role': 'Documenting the life of the king'}; 

scribe_level1 = ['dungeon', 'door one', 'door two'];

print "Chapter 1: Breakin' Bad Habits" 

print "As a result of your actions, you’re sent to the dungeon to think about what you've done."

action = raw_input("What will you do in this dank and lonely cell? Break out or stay dank and lonely?")

if 'Stay dank and lonely' in action:
  print "If you wish..."
  import scribe_level1.py
    
if 'Break out' in action:
  print "Excellent! You take out your handy dandy quill and begin lockpicking the door."
  lockpick = raw_input("Do you turn your quill to the right or the left first?") 
    if 'Right' in lockpick:
      print "The lock does not budge. Try again." 
    if 'Left' in lockpick:
      print "The lock breaks free and your cell door swings open!" 
        door = raw_input("Which door do you choose to leave from? Door one or door two?")
          if 'Door one' in door:
            print "Guards find you! You are manhandled and forced back into your cell."
              import scribe_level1.py
          if 'Door two' in door:
            print "Fresh, clean air! You are free, Palace Scribe!" 
        
  

