import random

# Suppose we need to generate 5 discount codes with length of 6
CODE_COUNT = 5


def codeGen():
    CodeSet = set()

    while len(CodeSet) < CODE_COUNT:
        code = (str(random.randint(100000, 999999)))

        CodeSet.add(code)

    return CodeSet


if __name__ == '__main__':
    print(codeGen())
