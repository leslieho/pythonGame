'''
print "Welcome to Chapter 2: The Forest of Love!" 
print " "
print "You have successfully escaped from your cell! But you are being chased by the palace guards. You run for your life and end up crashing into a lovely maiden."
print " "
pain_response = raw_input("You give her a cut across her knee.  She is tearing up from the pain.  Will you " + "\"heal cut with magical quill\"" + ' or '+ "\"give her an angry look\""+'?')
if 'heal cut with magical quill' in pain_response:
	print " "
	print "She says thank you and asks why you, the palace scribe, is running through the forest. You reply and say that you are running from the palace guards because you defied the king.  She then provides refuge for you in return for you healing her.  As you begin conversing to better know your savior, she tells you of the beast that has been tormenting her village.  She looks at you with a desperate look."
	print " " 
	beast_response = raw_input("Will you " + "\"choose to ignore story\"" + ' or '+ "\"do something about the beast\""+'?')
	if 'choose to ignore story' in beast_response:
		print " "
		print "You ignore her desperate look and change the topic with an embarassed look.  She gives you an understanding look and proceeds to give you blankets and bids you good night. The next morning, you wake before your savior does and you leave her village."
		print "import scribe_level3.py"   
	if 'do something about the beast' in beast_response:
	  print " "
		print "You proceed to tell her you will do everything you can to protect her and the village.  She exclaims with appreciation and gives you a hug and a kiss.  She embarassingly thanks you and leads you to the blacksmith to help you fight the beast.  You greet the blacksmith.  The blacksmith grunts, looks you over, and laughs."
		print " "		
		blacksmith_response = raw_input("He asks you what you would prefer, " + "\"suit of armor\"" + " or " + "\"simple sword\""+"?")
		if 'suit of armor' in blacksmith_response:
			print " "			
			print "The blacksmith laughs, creates a suit of armor for you, and you can barely walk.  The blacksmith laughs as you fall to the ground.  He bids you good luck and you slowly leave the blacksmith.  You travel to the cave where the beast is located."
			print " "			
			cave_response = raw_input("Do you" + "\"enter the cave bravely\"" +" or "+ "\"hesitate\"" +"?")
			if 'enter  the cave bravely' in cave_response:
				print " "				
				print "You walk into the dark cave.  You hear growling and all of a sudden, a fireball rushes your way.  The fireball hits your armor and you get flung backwards.  You get up as fast as you can in the heavy suit of armor.  You ball up your armored fist." 
				print " "				
				swing_response = raw_input("Do you "+'\'swing left\''+' or '+'\'swing right\''+'?')
				if 'swing left' in swing_response:
					print " "					
					swing2_response = raw_input("Yikes, you missed the beast.  Looks like you have to swing again.")
					if 'swing left' in swing2_response:
						print " "
						print "Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving her village.  She says she is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage!"
						print " "
						chapter3_response=raw_input("Would you like to continue to chapter 3," + '\' yes\'' + ' or ' + '\'no\''+'?')
						if 'yes' in chapter3_response:	
							print "import scribe_level3"
								if 'no' in chapter3_response:
							print " "
							print 'You have ended the game! Congratulations hero!'
					if 'swing right' in swing2_response:
						print " "
						print 'Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving her village.  She says she is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage!  Would you like to continue to chapter 3,' + '\' yes\'' + ' or ' + '\'no\''+'?'
						print " "
						chapter3_response=raw_input("Would you like to continue to chapter 3," + '\' yes\'' + ' or ' + '\'no\''+'?')
						if 'yes' in chapter3_response:
							print "import scribe_level3"
						if 'no' in chapter3_response:
							print " "
							print 'You have ended the game! Congratulations hero!'
		if 'simple sword' in blacksmith_response:
			print " "
			print 'The blacksmith smiles, creates a sword of magestic proportions, and gives it to you.  He calls you brave and bids you good luck.  You leave the blacksmith and travel to the cave where the beast is located.'
			print " "
			cave1_response = raw_input("Do you" + "\"enter the cave\"" +" or "+ "\"hesitate\""+"?")
			if 'enter the cave' in cave1_response:
				print " "
				print 'You walk into the dark cave.  You hear growling and all of a sudden, a fireball rushes your way.   You quickly dodge out of the way.  In your action of dodging, you lost your sword!  You decide to use your magical quill and you quickly pull it out.  It is too dark to see where the beast is.' 
				print " "
				wave_response=raw_input('Will you wave your quill'+'\'left\'' +' or '+'\'right\''+'?')
				if 'right' in wave_response:
					print " " 
					wave2_response=raw_input('Yikes, you missed the beast.  Looks like you have to wave again.')
					if 'right' in wave2_response:
					  print " "
						print 'Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving her village.  She says she is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village  and everyone is happy for your marriage!'
						print " "
						chapter3_response=raw_input('Would you like to continue to chapter 3,' + '\' yes\'' + ' or '+ '\'no\''+'?')
						if 'yes' in chapter3_response:
							import scribe_level3
						if 'no' in chapter3_response:
							print " "
							print 'You have ended the game! Congratulations hero!'
					if 'left' in wave_response:
						print " "
						print 'Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving her village.  She says she is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village  and everyone is happy for your marriage!'  
						print " "
						chapter3_response=raw_input('Would you like to continue to chapter 3,' + '\' yes\'' + ' or ' + '\'no\''+'?')
						if 'yes' in chapter3_response:
							import scribe_level3
						if 'no' in chapter3_response:
							print " "
							print 'You have ended the game! Congratulations hero!'
			if 'left' in wave_response:
						print " "
						print 'Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving her village.  She says she is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village  and everyone is happy for your marriage!'  
						print " "
						chapter3_response=raw_input('Would you like to continue to chapter 3,' + '\' yes\'' + ' or ' + '\'no\''+'?')
						if 'yes' in chapter3_response:
							import scribe_level3
						if 'no' in chapter3_response:
							print " "
							print 'You have ended the game! Congratulations hero!'
else:
	print "She says " +"\"HMPH\""+" and runs away crying."
	print " "
	chapter3final_response=raw_input('Would you like to continue to the next chapter?')
	if 'yes' in chapter3final_response:
		import scribe_level3
	if 'no' in chapter3final_response:
		print " "
		print 'You have ended the game!'
'''	
