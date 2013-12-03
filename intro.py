name = raw_input("Welcome to our Medieval Python RPG. To get this adventure started, please tell me your name.")
print " So your name is %s." % name

gender = raw_input("Are you going to be a male or female in this game?")

if 'Female' in gender:
    print " Oh, you're a girl! You are a bar maid with an attitude. After recently being homeless on the streets of Karflooglesville, you are now working for the royal family. In particular, your duty is to serve the king his favorite alcoholic beverages. Today, the King has gotten sick of your beer-serving abilities. For some reason, you are off your game and he insists that the beverage is simply too flat, it tastes unbearable, and the smell is too sweet for his senses. In return, you inform the King that his breath is unbearable and you are sent to the dungeon."
    answer = raw_input("Do you speak up or comply?")
	if 'Speak up' in answer:
		print " The King goes into a rage and send you to solitary confinement."
		import barMaid_level1.py   
if 'Male' in gender:
        print " Oh, a boy I see. So you are a palace scribe who has been working for the King of Karflooglesville for a number of years now. As a young boy, your parents sent you to work for the palace in order to pay for their overdue taxes. The King has grown fond of you, but as of late, the King has been displeased with the notes you've taken because you haven't written enough about him to satisfy his arrogance."
	answer = raw_input("Do you speak up or comply?")
	if 'Speak up' in answer:
		print " The King goes into a rage and send you to solitary confinement."
		import scribe_level1.py
if 'Comply' in answer: 
	print "Really? You will let such a defiant moment pass?"
	import intro.py

	
	
	


