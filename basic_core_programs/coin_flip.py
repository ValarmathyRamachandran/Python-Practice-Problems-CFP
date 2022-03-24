import random


def flip_coin(num_of_flips):
    """

    :param num_of_flips:
    :return: number of flips
    """
    heads = 0
    for i in range(num_of_flips):
        coin = random.randint(1, 2)
        if coin == 1:
            heads += 1

    percent = heads / num_of_flips
    return percent


if __name__ == "__main__":
    flip_coin(5)  # flip coin 5 times
    flip_coin(20)  # flip coin 20 times
