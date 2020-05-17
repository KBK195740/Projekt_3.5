# !/usr/bin/python
# coding=utf-8
# První dva řádky odstranily případný problém s kódováním (např. tagem komentáře)

# PROGRAM PRO ROZPOZNÁNÍ PRAVOPISNÉ CHYBY - na základě porovnání s databází slov

import sys
from spellcheck import correct
from spellchecker import SpellChecker

spell = SpellChecker()

# Načtení databáze slov (slovníku), které je využito k případnému přidání slova do slovníku.
D = open("database.txt", "a+")

# Úprava vstupního textu - odstranění názvu souboru.
values = sys.argv[1:]

# Úprava vstupního textu - odstranění vybraných nežádoucích znaků.
values = [s.replace('.', '') for s in values]
values = [s.replace(',', '') for s in values]
values = [s.replace('?', '') for s in values]
values = [s.replace('!', '') for s in values]

# Procházení jednotlivých slov vstupního textu a vyhodnocení jeho správnosti.
for value in values:

    # Podmínka pro případy, kdy program pomocí funkce vyhodnotil slovo jako nesprávné.
    if not correct(value):
        print(value+ " is not spelled correctly! ")
        # Nabídne podobné slovo.
        print("You maybe mean: " + spell.correction(value))
        # Možnost volby uživatele, zda chce slovo přidat do slovníku (database.txt).
        ATD = raw_input("Type Y to add your word to the dictionary, another letter to continue: ")

        # Pokud uživatel požaduje přidání slova do slovníku.
        if ATD in ['y', 'Y']:
            D.write("\n"+ value)
            print("Added to dictionary! \n")
        else:
            print("Not added to dictionary! \n")

    # Zpětná vazba uživateli v případě, kdy není slovo vyhodnoceno jako nesprávné.
    else:
        print(value+ " is spelled correctly! \n")