# Created by: Kay Lin
# Created on: 19th Nov 2017
# Created for: ICS3U
# This program displays blackjack game

import ui
from numpy import random
import Image

player_card1_value = 0
player_card2_value = 0
player_card3_value = 0
player_card4_value = 0
player_card5_value = 0
dealer_card1_value = 0
dealer_card2_value = 0
#dealer_card3_value = 0
player_score = 0
dealer_score = 0
game_cards = []

deck_of_cards_image = ['2C.JPG', '2D.JPG', '2H.JPG', '2S.JPG', '3C.JPG', '3D.JPG', '3H.JPG', '3S.JPG', '4C.JPG', '4D,JPG', '4H.JPG', '4S.JPG', '5C.JPG', '5D.JPG', '5H.JPG', '5S.JPG', '6C.JPG', '6D.JPG', '6H.JPG', '6S.JPG', '7C.JPG', '7D.JPG', '7H.JPG', '7S.JPG', '8C.JPG', '8D.JPG', '8H.JPG', '8S.JPG', '9C.JPG', '9D.JPG', '9H.JPG', '9S.JPG', '10C.JPG', '10D.JPG', '10H.JPG', '10S.JPG', 'AC.JPG', 'AD.JPG', 'AH.JPG', 'AS.JPG', 'JC.JPG', 'JD.JPG', 'JH.JPG', 'JS.JPG', 'QC.JPG', 'QD.JPG', 'QH.JPG', 'QS.JPG', 'KC.JPG', 'KD.JPG', 'KH.JPG', 'KS.JPG']

deck_of_cards_value = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

def get_a_card(chosen_cards = []):
    # pick a random number between 1 and 52 from deck without repeating
    
    a_card_index = random.randint(1,52)
    
    repeated_card = True
    while repeated_card == True:
        repeated_card = False
        for a_chosen_card_index in chosen_cards:
            if a_chosen_card_index == a_card_index:
                repeat_card = True
                
    a_card = deck_of_cards_image[a_card_index]
    a_card_value = deck_of_cards_value[a_card_index]
    
    chosen_cards.append(a_card_index)
    #a_card_image = ui.Image.named('card: ')
    a_card_image = ui.Image.named('./Cards/' + a_card)
    
    #print(a_card_image)
    return [a_card_value, a_card_image]
    
def player_card(cards_previously_picked = []):
    # generate player cards
    
    card = get_a_card(cards_previously_picked)
    
    card_value = card[0]
    card_image = card[1]
    
    return [card_value, card_image]
    
def deal_my_cards_touch_up_inside(sender):
    # blackjack start
    
    global dealer_card1_value
    global player_card1_value 
    global player_card2_value 
    global player_card3_value
    global player_card4_value
    global player_card5_value
    global player_cards_value
    global player_score
    global dealer_score
    global game_cards
    
    dealer_card1 = get_a_card(game_cards)
    player_card1 = player_card(game_cards)
    player_card2 = player_card(game_cards)
    
    dealer_card1_value = dealer_card1[0]
    player_card1_value = player_card1[0]
    player_card2_value = player_card2[0]
    
    view['player_card1_imageview'].image = player_card1[1]
    view['player_card2_imageview'].image = player_card2[1]
    view['player_card3_imageview'].image = ui.Image.named('card:BackBlue2')
    view['player_card4_imageview'].image = ui.Image.named('card:BackBlue2')
    view['player_card5_imageview'].image = ui.Image.named('card:BackBlue2')
    
    view['dealer_card1_imageview'].image = dealer_card1[1]
    view['dealer_card2_imageview'].image = ui.Image.named('card:BackBlue2')
    
    # player score
    player_score = player_card1_value + player_card2_value
    view['player_score_label'].text = str(player_score)
    
    # dealer score
    dealer_score = dealer_card1_value
    view['dealer_score_label'].text = str(dealer_score)
    
def ace_touch_up_inside(sender):
    # if player likes ace equal one
    
    global player_score
    if player_card1_value == 11 or player_card2_value == 11 or player_card3_value == 11:
       player_score = player_score - 10
       view['player_score_label'].text = str(player_score)
       view['ace_value_change_button'].enabled = False
    else:
       view['ace_value_change_button'].enabled = False
       
def player_third_cards_touch_up_inside(sender):
    # if player needs additional cards
    
    global player_card3_value
    global game_cards
    global player_score
    
    player_card3 = player_card(game_cards)
    player_card3_value = player_card3[0]
    view['player_card3_imageview'].image = player_card3[1]
    view['player_card4_imageview'].image = ui.Image.named('card:BackBlue2')
    view['player_card5_imageview'].image = ui.Image.named('card:BackBlue2')
    view['player_third_card_button'].enabled = False
    
    # player score
    player_score = player_score + player_card3_value
    view['player_score_label'].text = str(player_score)
    
def player_forth_card_touch_up_inside(sender):
    # give player forth card
    # if player need
    
    global player_card4_value
    global game_cards
    global player_score
    
    player_card4 = player_card(game_cards)
    player_card4_value = player_card4[0]
    view['player_card4_imageview'].image = player_card4[1]
    view['player_card5_imageview'].image = ui.Image.named('card:BackBlue2')
    view['player_forth_card_button'].enabled = False
    
    # player score
    player_score = player_score + player_card4_value
    view['player_score_label'].text = str(player_score)
    
def player_fifth_card_touch_up_inside(sender):
    # give player fifth card
    # if player need
    
    global player_card5_value
    global game_cards
    global player_score
    
    player_card5 = player_card(game_cards)
    player_card5_value = player_card5[0]
    view['player_card5_imageview'].image = player_card5[1]
    view['player_fifth_card_button'].enabled = False
    
    # player score
    player_score = player_score + player_card5_value
    view['player_score_label'].text = str(player_score)
    
def who_is_winner_touch_up_inside(sender):
    # check who is winner
    global player_score
    global dealer_total
    global game_cards
    global dealer_card2_value
    
    dealer_card2 = get_a_card(game_cards)
    dealer_card2_value = dealer_card2[0]
    
    view['dealer_card2_imageview'].image = dealer_card2[1]
    
    # dealer score
    dealer_score = dealer_card1_value + dealer_card2_value
    view['dealer_score_label'].text = str(dealer_score)
    
    # outcome
    if (player_score > dealer_score and player_score <= 21):
      view['winner_label'].text = 'Player wins'
    elif (dealer_score > 21 and player_score <= 21):
      view['winner_label'].text = 'Player wins'
    else:
      view['winner_label'].text = 'Dealer wins'
      
def reset_touch_up_inside(sender):
    # remove the cards
    
    view['winner_label'].text = ' '
    view['player_score_label'].text = ' '
    view['dealer_score_label'].text = ' '
    
    view['player_card1_imageview'].image = ui.Image.named('card:BackBlue2')
    view['player_card2_imageview'].image = ui.Image.named('card:BackBlue2')
    view['player_card3_imageview'].image = ui.Image.named('card:BackBlue2')
    view['player_card4_imageview'].image = ui.Image.named('card:BackBlue2')
    view['player_card5_imageview'].image = ui.Image.named('card:BackBlue2')
    view['dealer_card1_imageview'].image = ui.Image.named('card:BackBlue2')
    view['dealer_card2_imageview'].image = ui.Image.named('card:BackBlue2')
    #view['dealer_card3_imageview'].image = ui.Image.named('card:BackBlue2')
    
    view['player_fifth_card_button'].enabled = True
    view['player_forth_card_button'].enabled = True
    view['player_third_card_button'].enabled = True
    view['ace_value_change_button'].enabled = True
    
view = ui.load_view()
view.present('full_screen')
