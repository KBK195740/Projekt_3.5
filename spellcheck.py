# !/usr/bin/python
# coding=utf-8
# První dva řádky odstranily případný problém s kódováním (např. tagem komentáře)

dictionary = set()

def read():
    # Projde slovník (databázi k posouzení správnosti vstupního textu).
    global dictionary
    if dictionary:
        return

    with open("database.txt", "r") as f:
        contents = f.read()

    dictionary = set(
        word.lower()
        for word in contents.splitlines()
    )

def correct(word):
    # Vrací hodnotu True u slov vyhodnocených jako správně napsané, hodnotu False u ostatních.
    word = word.lower()
    read()
    return word in dictionary

def didyoumean(word):
    # Funkce k nalezení podobného slova pomocí knihovny.
    word.lower()
    read()

    misspelled = spell.unknown(word)

    for word in misspelled:
        print(spell.correction(word))
        print(spell.candidates(word))

    for word in words:
        print(spell.correction(word))