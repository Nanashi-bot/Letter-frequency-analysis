from frequency_distribution import monogram, test
import string
import random
import matplotlib.pyplot as plt
import enchant

# text = input("Please enter the text to be encrypted-> ")
text = test
encrypted = ""
decrypted = ""
alphabets = list(string.ascii_lowercase)


# Substitution encryption

# Making text a string of lowercase letters:

def clean_text(text):
    text = text.replace(" ", "").replace(".", "").replace(",", "").lower()
    return text

# For encrypting:

# Creating substitution key


def create_key():
    key = {}
    second_list = []
    for letter in alphabets:
        while len(second_list) < 26:
            alphabet = alphabets[random.randint(0, 25)]
            if alphabet not in second_list:
                second_list.append(alphabet)
                key[letter] = alphabet
                break
    return key


def encrypt(key, text):
    encrypted = ""
    for char in text:
        value = key[char]
        encrypted += value
    return encrypted

# For decrypting:

# Getting the frequency of each letter:


def get_frequency(encrypted):
    total = 0
    encrypted_frequency = {}
    for char in alphabets:
        encrypted_frequency[char] = 0

    for char in encrypted:
        encrypted_frequency[char] += 1
        total += 1

    for char in encrypted_frequency:
        encrypted_frequency[char] = float("{:.2f}".format(
            (encrypted_frequency[char] / total) * 100))

    return encrypted_frequency


# Using python to view the letter frequency:

def show_freq_distribution(monogram, encrypted_frequency):
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title("Letter Frequency Distribution Of Encrypted Text")
    keys = encrypted_frequency.keys()
    values = encrypted_frequency.values()
    plt.bar(keys, values)

    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    keys = monogram.keys()
    values = monogram.values()
    plt.title("Letter Frequency Distribution Of Normal Text")
    plt.bar(keys, values)
    plt.show()


# To test if it is a  word

def check(word):
    d = enchant.Dict("en_GB")
    return d.check(word)


def similar(word):
    d = enchant.Dict("en_GB")
    possible = d.suggest(word)
    other_possible_first_letters = []

    return other_possible_first_letters


def compare(monogram, encrypted_frequency):
    monogram = {k.lower(): v for k, v in monogram.items()}
    decrypted_key = {}
    sorted_monogram = {}
    sorted_encrypted_frequency = {}
    sorted_monogram = dict(
        sorted(monogram.items(), key=lambda item: item[1], reverse=True))
    sorted_encrypted_frequency = dict(
        sorted(encrypted_frequency.items(), key=lambda item: item[1], reverse=True))
    encrypted = list(sorted_encrypted_frequency.keys())
    monogram_list = list(sorted_monogram.keys())
    decrypted_key = {encrypted[i]: monogram_list[i]
                     for i in range(len(encrypted))}

    return decrypted_key


def decrypt(decrypted_key, encrypted):
    decrypted = ""
    for char in encrypted:
        # each_word += decrypted_key[char]
        # decrypted += each_word
        decrypted += decrypted_key[char]
    return decrypted


def percentage_broken(text, decrypted_text):
    percentage_broken = 0
    for i in range(len(text)):
        if text[i] == decrypted_text[i]:
            percentage_broken += 1

    percentage_broken = (percentage_broken/len(text))*100
    return percentage_broken


text = clean_text(text)
print("Text to be encrypted-> " + text)

key = create_key()
print(key)

encrypted = encrypt(key, text)
print("Text after encryption-> " + encrypted)

encrypted_frequency = get_frequency(encrypted)
print(encrypted_frequency)

show_freq_distribution(monogram, encrypted_frequency)

decrypted_key = compare(monogram, encrypted_frequency)
print(decrypted_key)

decrypted = decrypt(decrypted_key, encrypted)
print(decrypted)

percentage_broken = percentage_broken(text, decrypted)
print("Percentage broken-> ", percentage_broken)
