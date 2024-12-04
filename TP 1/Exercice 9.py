def analyse_texte(texte):
    mots = texte.split()
    return {"nombre de mots": len(mots), "nombre de caracteres": len(texte)}


print(analyse_texte("Test Test Test"))  
