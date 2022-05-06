from random import randint, choice

play_pts = 0
comp_pts = 0
dice_list = [3, 4, 6, 8, 10, 12, 20, 100]
n = 0

while not n == 2:
    dice = int(input("Which dice do You want to play? "))
    if dice in dice_list:
        roll = randint(1, dice)
        play_pts = play_pts + roll
        n += 1
    else:
        print("No such dice.")
print("Player's points:", play_pts)

for i in range(2):
    dice = choice(dice_list)
    roll = randint(1, dice)
    comp_pts = comp_pts + roll
print("Computer's points:", comp_pts)

while not play_pts >= 2021 or comp_pts >= 2021:
    play_roll = []
    comp_roll = []
    n = 0
    while not n == 2:
        dice = int(input("Which dice do You want to play? "))
        if dice in dice_list:
            roll = randint(1, dice)
            play_roll.append(roll)
            n += 1
        else:
            print("No such dice.")
    if sum(play_roll) % 11 == 0:
        play_pts = play_pts * 11
    elif sum(play_roll) % 7 == 0:
        play_pts = play_pts // 7
    else:
        play_pts = play_pts + sum(play_roll)
    print("Player's points:", play_pts)

    for i in range(2):
        dice = choice(dice_list)
        roll = randint(1, dice)
        comp_roll.append(roll)
    if sum(comp_roll) == 11:
        comp_pts = comp_pts * 11
    elif sum(comp_roll) == 7:
        comp_pts = comp_pts // 7
    else:
        comp_pts = comp_pts + sum(comp_roll)
    print("Computer points:", comp_pts)


if play_pts >= 2021:
    print("Player won!")
elif comp_pts >= 2021:
    print("Computer won!")
else:
    print("Draw!")
