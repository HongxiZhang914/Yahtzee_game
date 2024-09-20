import random
from collections import Counter
import pygame
import sys

#initialize pygame program
pygame.init()
screen = pygame.display.set_mode((800,600))
font = pygame.font.SysFont("Arial",32)
roll_button = pygame.Rect(300,450,100,50)

#load dice images
dice_1 = pygame.image.load('1.png')
dice_2 = pygame.image.load('2.png')
dice_3 = pygame.image.load('3.png')
dice_4 = pygame.image.load('4.png')
dice_5 = pygame.image.load('5.png')
dice_6 = pygame.image.load('6.png')
dice_img_list = [dice_1,dice_2,dice_3,dice_4,dice_5,dice_6]

#resize the images
dice_img_list_resized =[]
default_size = (70,70)
for img in dice_img_list:
    img = pygame.transform.scale(img, default_size)
    dice_img_list_resized.append(img)
default_img_x = 150
default_img_y = 300

#simulate rolling dice
def roll_the_dice(number_of_dice):
    dice_list = []
    for i in range(number_of_dice):
        dice_list.append(random.randint(1,6))
    return dice_list

#used for testing    
def display_dice(dice):
    for i in range(5):
        print("Your No." +str(i+1)+" dice roll is "+str(dice[i]))

#Score functions
def score_yahtzee(dice):
    if len(set(dice)) ==1:
        return 50
    return 0

def score_four_of_a_kind(dice):
    counts = Counter(dice)
    for count in counts.values():
        if count >=4:
            return sum(dice)
    return 0

def score_three_of_a_kind(dice):
    counts = Counter(dice)
    for count in counts.values():
        if count >=3:
            return sum(dice)
    return 0

def score_large_straight(dice):
    dice_sorted = sorted(set(dice))
    if dice_sorted == [1,2,3,4,5] or dice_sorted == [2,3,4,5,6]:
        return 40
    return 0

def score_small_straight(dice):
    dice_sorted = sorted(set(dice))
    smaill_straight = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
    large_straight = [[1,2,3,4,5],[2,3,4,5,6]]
    for i in range(3):
        if (dice_sorted[:4] == smaill_straight[i] or dice_sorted[1:] == smaill_straight[i]) and dice_sorted not in large_straight:
            return 30
    return 0

def score_full_house(dice):
    counts = Counter(dice)
    count_list = []
    for count in counts.values():
        count_list.append(count)
    if count_list == [2,3] or count_list == [3,2]:
        return 25
    return 0

def score_upper_section(dice, number):
    return dice.count(number) * number

#draw the dice, called after roll the dice
def draw_dice(dice_img, dice_list):
    img_x = default_img_x
    img_y = default_img_y
    for dice in dice_list:
        screen.blit(dice_img[dice-1],(img_x,img_y))
        img_x+=100

#draw the roll button, called each time empty the screen, so that the button can always show in the screen
def draw_button():
    pygame.draw.rect(screen, (100,100,0),roll_button,5)
    button_text = font.render("ROLL", True,(0,0,0))
    screen.blit(button_text,(roll_button.x+15,roll_button.y+10))

#draw score instructions for the game, called each time empty the screen
def draw_instructions():
    dice_img_list_resized =[]
    default_size = (20,20)
    for img in dice_img_list:
        img = pygame.transform.scale(img, default_size)
        dice_img_list_resized.append(img)
    font = pygame.font.SysFont("Arial",24)
    yahtzee = [1,1,1,1,1,': Yahtzee-> 50 Points']
    four_of_a_kind =[1,1,1,1,2,': four_of_a_kind-> sum of all dices']
    three_of_a_kind = [1,1,1,2,3,': three_of_a_kind-> sum of all dices']
    full_house = [1,1,1,2,2,': full_house-> 25 Points']
    large_straight = [1,2,3,4,5,': large_straight-> 40 Points']
    small_straight = [1,2,3,4,1,': small_straight-> 30 Points']
    img_x, img_y = 10,20
    text_x,text_y = 180,15
    score_rule = [yahtzee,four_of_a_kind,three_of_a_kind,full_house,large_straight,small_straight]
    for item in score_rule:
        for dice in item[:5]:
            screen.blit(dice_img_list_resized[dice-1],(img_x,img_y))
            img_x+=30
        img_x = 10
        img_y+=40
        rule_text = font.render(item[5],True,(0,200,0))
        screen.blit(rule_text,(text_x,text_y))
        text_y+=40
    upper_section_font = pygame.font.SysFont('Arial', 16)
    upper_section_text = upper_section_font.render("**Upper Section: If none of above applied, use the max score of dice number * number of appearance of that number.", True,(0,200,0))
    screen.blit(upper_section_text,(10,250))

#clear the screen after each time the roll button is pressed, so that the screen can display the new dice sets.
def clear_screen():
    screen.fill((255,255,255))
    draw_button()
    draw_instructions()

#Used to calculate how much score the player gets
def judgement(dice):
    score = score_yahtzee(dice)+score_four_of_a_kind(dice)+score_three_of_a_kind(dice)+score_full_house(dice)+score_large_straight(dice)+score_small_straight(dice)
    if score == 0:
        score = max(score_upper_section(dice,1),score_upper_section(dice,2),score_upper_section(dice,3),score_upper_section(dice,4),score_upper_section(dice,5),score_upper_section(dice,6))
    score_str = 'You Score ' + str(score) + ' Points'
    score_text = font.render(score_str,True,(200,0,0))
    screen.blit(score_text,(250,520))

#pygame settings
pygame.display.set_caption("Yahtzee Game")
screen.fill((255,255,255))

#buttons
draw_button()
draw_instructions()

#game loop
while True:
    for event in pygame.event.get():
        #event check for button press
        if event.type == pygame.MOUSEBUTTONDOWN:
            if roll_button.collidepoint(event.pos):
                clear_screen()
                dice_list = roll_the_dice(5)
                draw_dice(dice_img_list_resized,dice_list)
                judgement(dice_list)
        #exit the loop and the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()