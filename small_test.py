# This code is a test to see if I can apply recursion on dictionaries to break the code 100%


import enchant

message = "thisisatest"
encrypted = "abcfcfyavfa"
actual_key = {'a': 'y', 'b': 'g', 'c': 'm', 'd': 'u', 'e': 'v', 'f': 'd', 'g': 'k', 'h': 'b', 'i': 'c', 'j': 'n', 'k': 'i', 'l': 'e',
              'm': 'j', 'n': 'h', 'o': 'o', 'p': 'r', 'q': 'w', 'r': 'l', 's': 'f', 't': 'a', 'u': 'x', 'v': 't', 'w': 'z', 'x': 's', 'y': 'p', 'z': 'q'}


wrong_key = {'v': 'e', 'a': 't', 'h': 'a', 'o': 'o', 'c': 'i', 'f': 'n', 'y': 's', 'l': 'r', 'u': 'h', 'e': 'd', 'b': 'l', 'd': 'u',
             'm': 'c', 'p': 'm', 'j': 'f', 'r': 'y', 'x': 'w', 'k': 'g', 'i': 'p', 't': 'b', 'g': 'v', 'z': 'k', 's': 'x', 'n': 'q', 'q': 'j', 'w': 'z'}
d = enchant.Dict("en_GB")


def check(word):
    return d.check(word)


def similar(word):
    similar = d.suggest(word)
    rhyming = []
    for each in similar:
        if word[1:] == each[1:]:
            rhyming += each[0]

    return rhyming


def fixing_key(wrong_key, decrypted, encrypted):
    each_word = ""
    x = 0
    for i in range(9, -1, -1):
        each_word = decrypted[0: i]
        if check(each_word):
            # decrypted += each_word
            each_word = ""
            break
        else:
            a = similar(each_word)
            for letter in a:
                index_of_first_letter = (list(wrong_key.keys())[
                                         list(wrong_key.values()).index(each_word[0])])
                wrong_key = change(wrong_key, index_of_first_letter, letter)
                decrypt(wrong_key, encrypted)
                print(wrong_key)
    return wrong_key


def decrypt(wrong_key, encrypted):
    decrypted = ""
    for char in encrypted:
        decrypted += wrong_key[char]
    return decrypted


def change(key, l1, l2):
    # I am changing the value of l1 to l2
    index_of_l2 = (list(key.keys())[list(key.values()).index(l2)])
    t = key[l1]
    key[l1] = l2
    key[index_of_l2] = t
    return key


decrypted = decrypt(wrong_key, encrypted)

ans = fixing_key(wrong_key, decrypted, encrypted)
