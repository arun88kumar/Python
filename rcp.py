from random import choice
def rcp():
	win_points = input("How many points you wanna set for a win:")
	play_set = { "R":"Rock","r":"Rock",
				 "P":"Paper","p":"Paper",
				 "S":"Scissors","s":"Scissors",
				 }
	human_pts = 0
	comp_pts = 0
				 
	while(True):
	
		play = input("Choose (R)ock, (P)aper, or (S)cissors?")
		human_play = play_set[play]
		comp_play = choice(["Rock","Paper","Scissors"])
		if human_play == comp_play:
			print "You:{0}, Computer:{1}, Draw".format(human_play,comp_play)
		elif human_play == "Rock":
			if comp_play == "Paper":
				comp_pts += 1
				print "You:{0}, Computer:{1}, Computer Wins".format(human_play,comp_play)
			elif comp_play == "Scissors":
				human_pts += 1
				print "You:{0}, Computer:{1}, You Win".format(human_play,comp_play)
		elif human_play == "Paper":
			if comp_play == "Scissors":
				comp_pts += 1
				print "You:{0}, Computer:{1}, Computer Wins".format(human_play,comp_play)
			elif comp_play == "Rock":
				human_pts += 1
				print "You:{0}, Computer:{1}, You Win".format(human_play,comp_play)
		elif human_play == "Scissors":
			if comp_play == "Rock":
				comp_pts += 1
				print "You:{0}, Computer:{1}, Computer Wins".format(human_play,comp_play)
			elif comp_play == "Paper":
				human_pts += 1
				print "You:{0}, Computer:{1}, You Win".format(human_play,comp_play)
		print "Score You:{0} Computer={1} ".format(human_pts,comp_pts)
		
		if human_pts == win_points:
			print "you win the match"
			break
		elif comp_pts == win_points:
			print "Computer wins the match"
			break

			
rcp()