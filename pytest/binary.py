# python program Swap
# two nibbles in a byte

def swap_nibbles(num):
    return (num & 0x0F) << 4 | (num & 0xF0) >> 4


if __name__ == '__main__':
    number = 100
    print(swap_nibbles(number))
else:
    pass
