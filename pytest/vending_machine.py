def count_currency(amount):
    """
    :param amount: amount  in rs
    :return: minimum number of notes and number of notes
    """
    notes = [1000, 500, 100, 50, 10, 5, 2, 1]

    noteCounter = [0, 0, 0, 0, 0, 0, 0, 0]

    print("Currency Count -> ")

    totalNotes = 0
    for note, number_of_notes in zip(notes, noteCounter):
        #which is an iterator of tuples where the first item in each passed iterator is paired together,
        # and then the second item in each passed iterator are paired together
        if amount >= note:
            number_of_notes = amount // note
            amount = amount - number_of_notes * note
            print(note, " : ", number_of_notes)
            totalNotes += number_of_notes

    print("minimun number of Notes: ", totalNotes)


if __name__ == "__main__":
    count_currency(2500)



