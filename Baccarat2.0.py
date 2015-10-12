import random


#introduction & welcome messages
player_name = "Laura"
print "let's play baccarat,", player_name
player_buyin= 100
print "Here is your buy in money", player_buyin
print "good luck!!!"


#drawing cards
player_1=random.choice(range(1,10))
player_2=random.choice(range(1,10))


banker_1= random.choice(range(1,10))
banker_2= random.choice(range(1,10))




print "hi", player_name, "Your first card is ", player_1

print "the banker's first card is ", banker_1

print player_name, "your next hand is ", player_2
print "the banker's next hand is ", banker_2


def add_cards_together():
	player_total = player_1 + player_2
	banker_total = banker_1 + banker_2
	print "your total is ", player_total
	print "the total is ", banker_total
	return player_total
	return banker_total

def is_nine(player_total, banker_total):
	if player_total == 9:
		print "you win!",player_name
		player_wins = True
		return player_wins
	
	if banker_total == 9 and player_total != 9:
		print "banker wins! Sorry,", player_name
		player_wins = False
		return player_wins

	if banker_total and player_total == 9:
		print player_name, "and banker are tied"
		print "player wins money"
		player_wins = True
		return player_wins


def lessthan_five(player_total, banker_total):
	if player_total < 5 and banker_total < 9:

		print "your total is less than 5, please draw again", player_name
		print "your third card is", player_1
		third_draw = player_1 + player_total
		print "the total of 3 cards is", third_draw	

	if third_draw > 5 and third_draw < banker_total:
		print "banker wins"
		player_wins = False
		return player_wins

	
def greaterthan_nine(player_total, banker_total):
	pass


# if player_total > 9:
# 	player_final = player_total - 10
# 	print player_name, "your total is", player_final

# if banker_total > 9:
# 	banker_final = banker_total - 10
# 	print "the banker's total is", banker_final

# if player_total or player_final == 9:

	
# if banker_total or banker_final == 9:
# 	print "sorry ", player_name, "banker wins!!"

# if player_total or player_final and banker_total or banker_final == 9:
# 	return player_wins = True
# 	print "you win!",player_name	








if __name__ == '__main__':
	main()
	play_bacc()
	add_cards_together()
	is_nine()
	lessthan_five()
	#cash()
	#play_again()




