pair = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
def caeasar(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char in pair.keys():
            num = pair[char]
            num = (num + key) % 26
            cipher_text += list(pair.keys())[num]
            
        else:
            cipher_text += char
    return cipher_text