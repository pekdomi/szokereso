import random

#abc and its lenght
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n" ,"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lenght_abc = len(abc)

#create random board
board = [[],[],[]]
for i in range(3):
    for j in range(3):
        letter = abc[random.randint(0,lenght_abc-1)]
        board[i].append(letter)
        abc.remove(letter)
        lenght_abc -= 1
print("\nTo end game tpye 'end'\n")
for i in board:
    print(i)

#get letter's position in board
def getLetterPosInBoard(board, letter):
    for i in board:
        for j in i:
            if j == letter:
                return [board.index(i), i.index(j)]
    return False

#decide whether word is valid or not
def getWordValidity(board, word):
    if word == "end":
        return("end")
    board = board.copy()
    walk = []
    used_pos = []
    for i in word:
        letter_pos = getLetterPosInBoard(board, i)
        if not letter_pos:
            return(f"Letter not in board: {i}")
        if letter_pos in used_pos:
            return(f"Letter already used: {i}")
        walk.append(letter_pos)
        used_pos.append(letter_pos)
    for i in range(len(walk)):
        if i == 0: continue
    if abs(walk[i][0] - walk[i-1][0]) > 1 or abs(walk[i][1] - walk[i-1][1]) > 1:
        return("Letters not in order")
    return("In board")

#main loop
while True:
    input_word = input("\nWord: ")
    valid = getWordValidity(board, input_word)
    if valid == "end": break
    print(valid)