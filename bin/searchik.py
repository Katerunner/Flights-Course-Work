def searchik(lst, letters):
    """Returns sorted list for similarity by letters"""
    temp = []
    for i in lst:
        if apro_cal(i, letters) != 0.0:
            temp.append(i)
    temp = sorted(temp, key=lambda x: apro_cal(x, letters))
    return temp


def apro_cal(text, letters):
    """Returns the similarity for text by letters"""
    if type(text) != str:
        text = str(text)
    temp = 0
    for i in letters.lower():
        if i in text.lower():
            temp += 1
    if letters.lower() in text.lower():
        temp += 3
    return temp
