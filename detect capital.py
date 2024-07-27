def detectCapitalUse(word):
    return word.isupper() or word.islower() or word.istitle()

word1 = "USA"
print(detectCapitalUse(word1))


