from random import randint

play_pts = 0
comp_pts = 0

for i in range(2):
    roll = randint(1, 6)
    print(roll)
    play_pts = play_pts + roll
print("Player's points:", play_pts)

for i in range(2):
    roll = randint(1, 6)
    print(roll)
    comp_pts = comp_pts + roll
print("Computer's points:", comp_pts)

while not play_pts >= 2021 or comp_pts >= 2021:
    input("Continue")
    play_roll = []
    comp_roll = []
    for i in range(2):
        roll = randint(1, 6)
        print(roll)
        play_roll.append(roll)
    if sum(play_roll) == 11:
        play_pts = play_pts * 11
    elif sum(play_roll) == 7:
        play_pts = play_pts // 7
    else:
        play_pts = play_pts + sum(play_roll)
    print("Player's points:", play_pts)

    for i in range(2):
        roll = randint(1, 6)
        print(roll)
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
