

# init
possible_words = []
fivers = open("wordlist.txt", "r")
Lines = fivers.readlines()
for line in Lines:
    possible_words.append(line)

wrong = []
# right = [{"pos": 0, "letter": "c"}, {"pos": 1, "letter": "a"}]
right = []
rightbutwrong = []
bad_words = []


def purge():
    for word in possible_words:
        for w in wrong:
            if w in word and w not in rightbutwrong:
                bad_words.append(word)
                break
        for rw in rightbutwrong:
            if rw[0] not in word or word[int(rw[1])] is rw[0]:
                bad_words.append(word)
                break
        for r in right:
            if not word[r["Position"]] == r["Letter"]:
                bad_words.append(word)
                break


def enter_info():
    print("Enter Right ones")
    right_input = input()
    for index, r in enumerate(right_input):
        if right_input == "":
            break
        if r.isnumeric():
            continue
        if r in rightbutwrong:
            rightbutwrong.remove(r)
        right.append({"Letter": r, "Position": int(right_input[index + 1])})

    print("Enter Right but wrong ones")
    rightbutwrong_input = input()
    for index, rw in enumerate(rightbutwrong_input):
        if rightbutwrong_input == "":
            break
        if rw.isnumeric():
            continue
        rightbutwrong.append(rw + rightbutwrong_input[index + 1])

    print("Enter Wrong ones")
    wrong_input = input()
    for w in wrong_input:
        stop = False
        if wrong_input == "":
            break
        for r in right:
            if r["Letter"] == w:
                stop = True
        if stop is True:
            continue
        wrong.append(w)


letter_score = {"a": 37, "b": 10, "c": 19, "d": 18, "e": 52, "f": 7, "g": 14, "h": 11, "i": 39, "j": 1, "k": 12,
                "l": 25, "m": 13, "n": 34, "o": 29, "p": 13, "q": 1, "r": 35, "s": 41, "t": 32, "u": 16, "v": 5,
                "w": 4, "x": 1, "y": 8, "z": 2}


def best_guess_with_frequency():
    best_guesses = {}
    for word in possible_words:
        score = 0
        used = []
        for w in word:
            if w == "\n":
                continue
            if w not in used:
                score = score + letter_score[w]
            used.append(w)
        best_guesses[word] = score
    best_guesses = {k: v for k, v in sorted(best_guesses.items(), key=lambda item: item[1], reverse=True)}
    print("Best guesses are")
    print(best_guesses)
    print("Possibilities left")
    print(len(best_guesses))


word_occurrences = [{}, {}, {}, {}, {}, {}]


def print_info():
    print(wrong)
    print(rightbutwrong)
    print(right)


while True:
    #fill_occ()
    enter_info()
    purge()
    possible_words = set(possible_words) - set(bad_words)
    print("result is")
    print(possible_words)
    best_guess_with_frequency()
    bad_words = []
    if len(possible_words) is 1:
        break
