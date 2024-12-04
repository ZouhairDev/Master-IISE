def compte_occurences(liste):
    occurences = {}
    for mot in liste:
        occurences[mot] = occurences.get(mot, 0) + 1
    return occurences

print(compte_occurences(["mot1", "mot1", "mot2", "mot2", "mot2", "mot3"]))
