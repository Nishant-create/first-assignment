selectedword = "roof"
guess = "o"
letter = enumerate(selectedword)
def findFunction(selectedword, guess):
    list_of_indices = []
    for index,character in letter:
        if (character == guess):
            list_of_indices.append(index)

    return list_of_indices

variable = findFunction(selectedword, guess)
if len(variable) == 0:
    print('empty')
else:
    print(variable)



