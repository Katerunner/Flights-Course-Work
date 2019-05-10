from fuzzywuzzy import fuzz

def searchik(lst, letters):
    temp = []
    for i in lst:
        if apro_cal(i, letters) != 0.0:
            temp.append(i)
    temp = sorted(temp, key = lambda x: apro_cal(x, letters))
    return temp


def apro_cal(text, letters):
    # text = text.lower()
    # letters = letters.lower()
    # ratio = fuzz.ratio(letters, text)
    # partial_ratio = fuzz.partial_ratio(letters, text)
    # token_sort_ratio = fuzz.token_sort_ratio(letters, text)
    # token_set_ratio = fuzz.token_set_ratio(letters, text)
    # temp = (ratio + partial_ratio + token_sort_ratio + token_set_ratio) / 4
    if type(text) != str:
        text = str(text)
    temp = 0
    for i in letters.lower():
        if i in text.lower():
            temp += 1
    if letters.lower() in text.lower():
        temp += 3
    return temp

