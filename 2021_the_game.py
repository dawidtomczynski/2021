from random import randint

play_pts = 0
comp_pts = 0

for i in range(2):
    roll = randint(1, 6)
    print(roll)
    play_pts = play_pts + roll
print("Player's points: ", play_pts)

for i in range(2):
    roll = randint(1, 6)
    print(roll)
    comp_pts = comp_pts + roll
print("Computer points: ", comp_pts)

while not play_pts >= 2021 or comp_pts >= 2021:
    input("Continue")
    for i in range(2):
        roll = randint(1, 6)
        print(roll)
        play_pts = play_pts + roll
    print("Player's points: ", play_pts)
    for i in range(2):
        roll = randint(1, 6)
        print(roll)
        comp_pts = comp_pts + roll
    print("Computer points: ", comp_pts)
