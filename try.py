selectedword = "roof"
guess = "f"
letter = enumerate(selectedword)
# print(letter)
# for char in enumerate(selectedword):
    # print(char)
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



