print "Chapter 3: Hung Jury" 

print "You realize that you’re not cut out for a life on the run, 
so you decide to head back to the palace and stand trial. As the judge concludes your charges, you stand
and defiantly plead "Not Guilty"\n"

action = raw_input("What is your argument? Do you claim you were taking notes in such a way to establish a new metadata scheme
and usher in the educational practice of information science OR do you claim your experiences 
in the forest will make you a valuable warrior for the kingdom? Type either 'Information science' or 'Valuable warrior'\n")
if 'Information science' in action:
  print "The king scoffs at your notion. '98% of our kingdom cannot even read. INFORMATION SCIENCE PAH?! I condemn you
  to the guillotine! Ouch, sounds like the king isn't the only one losing his head over this."
  guillotine = raw_input("As you approach the guillotine, the neighboring kingdom suddenly attacks the courtyard.
  You still have your quill in the seat of your pants. Do you 'stay and defend the kingdom', or do you 'take the
  opportunity to run'?\n")
  if 'stay and defend the kingdom' in guillotine:
      print "You withdraw your quill and line up next to the king's guard. 'FOR HONOR' you yell."
      import scribe_level4.py
  if 'take the opportunity to run' in guillotine:
      print "The king catches you running away in the melee and orders a knight after you. You're no match for the horse's
      speed, and the king orders an execution on the spot. Game over. Just kidding, care to try again?"
      import scribe_level3.py
  

if 'Valuable warrior' in action:
  print "The king considers your offer thoroughly. 'Hm' he ponders, 'We have been short a few heroes
  recently.' Suddenly a loud crash is heard outside. 'MILORD' the king's page screams, 'We are besieged by the
  neighboring kingdom!' The king turns to you, 'Alrighty lad, you say you'll be a valuable warrior, now's the time to
  prove it.'\n"
  courtyard = raw_input("Do you 'rush to meet the enemy head on' or 
  do you stay back, nervously observing your surroundings and making a break for the 'back gate' while the king
  is distracted?\n") 
  if 'Meet the enemy head on' in courtyard:
      print "You cautiously but confidently approach the enemy in the company of the king's guard. Quickly, you draw
      your quill (no pun intended), causing the enemy to burst into laughter.\n"
      import scribe_level4.py
  if 'back gate' in courtyard:
      print "The back gate is right behind the dungeon. Unfortunately, the dungeon master is privy to
      your plan and halts you. Your quill barely scratches his imposing armor and thick mask
      'Back in the cell ya go, laddie,' he says, tossing you in the familiarity of your cell. Dammit, not again\n" 
      import scribe_level1.py
