character2 = {'Name': 'Bar Maid', 'Gender': 'Female', 'Role': 'Serving alcoholic beverages to the king'};

barMaid_level1 = ['dungeon', 'cell', 'window'];

print "Chapter 1: Breakin' Bad Habits"

print "As a result of your actions, you’re sent to the dungeon to think about what you've done.\n"

action = raw_input("What will you do in this dank and lonely cell? Break out or stay dank and lonely?\n")
if 'Stay dank and lonely' in action:
  print "If you wish..."
  import scribe_level1.py

if 'Break out' in action:
  print "Excellent!"
  escape = raw_input("But how will you break out? \n")
  
