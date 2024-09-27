text = input()

trans = {"a": "@", "b": "8", "c": "(", "d": "|)", "e": "3", "f": "#", "g": "6", "h": "[-]", "i": "|", "j": "_|", "k": "|<", "l": "1", "m": "[]\/[]", "n": "[]\[]", "o": "0", "p": "|D", "q": "(,)", "r": "|Z", "s": "$", "t": "']['", "u": "|_|", "v": "\/", "w": "\/\/", "x": "}{", "y": "`/", "z": "2"}

text = text.lower()
text = list(text)



for a in text:
    if not a in trans:
        print(a,end="")
    else:
        print(trans[a],end="")