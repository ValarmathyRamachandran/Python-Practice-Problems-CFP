def count():
    """

    :return: number of consonants and vowels
    """
    vowels_count = 0
    consonant_count = 0
    str_word = "Welcome to Python program"

    # Converting entire string to lower case to reduce the comparisons
    str_word = str_word.lower()
    for i in range(0, len(str_word)):

        if str_word[i] in ('a', "e", "i", "o", "u"):
            vowels_count = vowels_count + 1
        elif str_word[i] >= 'a' and str_word[i] <= 'z':
            consonant_count = consonant_count + 1
    print("Total number of vowel and consonant are")
    print(vowels_count)
    print(consonant_count)


count()
