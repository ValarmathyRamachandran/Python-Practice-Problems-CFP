import random


def gambling_game(numberOfBets, goal, money):
    win = 0
    lose = 0
    count = 0

    for i in range(numberOfBets):
        randomNumber = random.random()  # Generate random numbers between 0 to 1
        # print(randomNumber)
        count += 1  # Number of times the namdom number is generating
        if randomNumber > 0.5:  # Win
            money += 1
            win += 1
        # print(self.money)
        else:  # Lose
            money -= 1
            lose += 1
        # print(self.money)

        if money == goal:
            print('You have reached your goal on bet number ' + str(count))
            break
        elif money == 0:
            print('You have exhausted your money')
            break
    print('Number of win : ' + str(win))
    print('Number of lose :' + str(lose))
    print('Percentage of win : ' + str((win * 100) / count))
    print('Percentage of lose : ' + str((lose * 100) / count))


if __name__ == "__main__":
    numberOfBets = int(input('Enter number of times you want to gamble: '))
    goal = int(input('Enter your goal: '))
    money = int(input('Enter amount of money you have: '))
    gambling_game(numberOfBets, goal, money)
