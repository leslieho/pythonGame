''' 
print "Welcome to Chapter 2: The Forest of Love!" 
print " "
print "You have successfully escaped from your cell! But you are being chased by the palace guards. You run for your life and end up crashing into a lovely maiden."
print " "
print "You give her a cut across her knee.  She is tearing up from the pain.  Will you " + "\"heal her cut magical 			quill\"" + ' or '+ "\"give her an angry look\""+'?'
pain_response = raw_input()
if 'heal her cut with your magical quill' in pain_response:
	print " "
	print "She says thank you and asks why you, the palace scribe, is running through the forest. You reply and say 		that you   are running from the palace guards because you defied the king.  She then provides refuge for you 	in return for you healing her.  As you begin conversing to better know your savior, she tells you of the beast that has 	been tormenting her village.  She looks at you with a desperate look. Will you " + "\"choose to ignore story\"" + 	' or '+ "\"do something about the beast\""+'?'
	beast_response = raw_input()
	if 'choose to ignore story' in beast_response:
		print "You ignore her desperate look and change the topic with an embarassed look.  She gives you an 				understanding look and proceeds to give you blankets and bids you good night. The next morning, you 		wake before your savior does.   
	if 'do something about the beast' in beast_response:
		print "You proceed to tell her you will do everything you can to protect her and the village.  She exclaims with appreciation and gives you a hug and a kiss.  She embarassingly thanks you and leads you to the blacksmith to help you fight the beast.  You greet the blacksmith.  The blacksmith grunts, looks you over, and laughs.  He asks you what you would prefer, " + "\"suit of armor\"" + " or " + "\"simple sword\""+"?"
		blacksmith_response = raw_input()
		if 'suit of armor' in blacksmith_response:
			print "The blacksmith laughs, creates a suit of armor for you, and you can barely walk.  The 					blacksmith laughs as you fall to the ground.  He bids you good luck and you slowly leave the blacksmith.  You travel to the cave where the beast is located.  Do you "\"enter the cave\"" or"

else:
	print " "
	print "She says " +"\"HMPH\""+" and runs away crying." 
'''	
