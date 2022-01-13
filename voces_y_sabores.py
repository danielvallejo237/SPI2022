import PyPDF2

def recette2(text_page, text):
    """pour les pages avec 2 recettes dessus

    Args:
        text_page (str): le text de la page
        text (list): la liste des recettes

    Returns:
        list: la liste des recettes mise à jour
    """
    recette1 = {}
    recette2 = {}

    # on va découper le texte en fonction des ingredients
    a = text_page.split(mot_cle[0])

    a[1] = a[1].replace(mot_cle[2],"")
    a[2] = a[2].replace(mot_cle[2],"")

    # on va découper le texte en fonction des étapes de la recette
    a[1] = a[1].split(mot_cle[1])
    a[2] = a[2].split(mot_cle[1])

    # on va découper le texte en fonction des étapes de la recette (NTHOKI)
    a[1][1] = a[1][1].split(mot_cle[3])
    a[2][1] = a[2][1].split(mot_cle[3])

    # on récupère le nom de la première recette
    a[0] = a[0].split('\n')
    for i in range(10):
        a[0][0] = a[0][0].replace(str(i),"")

    try:
        # on récupère le nom de la deuxième recette
        # s'il n'y avait pas de NTHOKI pour la première recette on aura une erreur
        a[1][1][1] = a[1][1][1].split('.')
        nom = (a[1][1][1].pop()).split('\n')

    except:
        # on récupère le nom de la deuxième recette
        a[1][1][0] = a[1][1][0].split('.')
        nom = a[1][1][0].pop()

        a[1][1][0] = '.'.join(a[1][1][0])

        nom = nom.split('\n')

    # on essaie de trouver le bon nom
    nom2 = nom[0]
    if len(nom) > 1:
        if nom2 == '':
            nom2 = nom[1]
            if len(nom) > 2:
                if nom[2]!='' and nom[2][0] == ' ':
                    nom2+=nom[2]
        elif nom[1]!='' and nom[1][0] == ' ':
            nom2+=nom[1]
            if len(nom) > 2:
                if nom[2]!='' and nom[2][0] == ' ':
                    nom2+=nom[2]
    if nom2 == '':
        print(a,nom,'1')

    recette1['nom'] = a[0][0]
    recette1['ingredient'] = a[1][0]
    recette1['recette'] = a[1][1][0]
    text.append(recette1)

    recette2['nom'] = nom2
    recette2['ingredient'] = a[2][0]
    recette2['recette'] = a[2][1][0]
    text.append(recette2)

    return text

def recette2_ingredient1(text_page, text):
    """Pour les pages avec 2 recettes, dont une seul à des ingrédients

    Args:
        text_page (str): le text de la page
        text (list): la liste des recettes

    Returns:
        list: la liste des recettes mise à jour
    """
    recette1 = {}
    recette2 = {}

    # on va découper le texte en fonction des ingredients
    a = text_page.split(mot_cle[0])
    a[1] = a[1].replace(mot_cle[2],"")

    if text_page.index(mot_cle[0]) < text_page.index(mot_cle[1]): # si les ingrédients sont pour la première recette


        # on va découper le texte en fonction des étapes
        a[1] = a[1].split(mot_cle[1])

        # on va découper le texte en fonction des étapes de la recette (NTHOKI)
        a[1][1] = a[1][1].split(mot_cle[3])
        a[1][2] = a[1][2].split(mot_cle[3])

        # on récupère le nom de la première recette
        a[0] = a[0].split('\n')
        for i in range(10):
            a[0][0] = a[0][0].replace(str(i),"")

        try:
            # on récupère le nom de la deuxième recette
            # s'il n'y avait pas de NTHOKI pour la première recette on aura une erreur
            a[1][1][1] = a[1][1][1].split('.')
            nom = (a[1][1][1].pop()).split('\n')

        except:
            # on récupère le nom de la deuxième recette
            a[1][1][0] = a[1][1][0].split('.')
            nom = a[1][1][0].pop()

            a[1][1][0] = '.'.join(a[1][1][0])

            nom = nom.split('\n')

        # on essaie de trouver le bon nom
        nom2 = nom[0]
        if len(nom) > 1:
            if nom2 == '':
                nom2 = nom[1]
                if len(nom) > 2:
                    if nom[2]!='' and nom[2][0] == ' ':
                        nom2+=nom[2]
            elif nom[1]!='' and nom[1][0] == ' ':
                nom2+=nom[1]
                if len(nom) > 2:
                    if nom[2]!='' and nom[2][0] == ' ':
                        nom2+=nom[2]
        if nom2 == '':
            print(a,nom,'2')

        recette1['nom'] = a[0][0]
        recette1['ingredient'] = a[1][0]
        recette1['recette'] = a[1][1][0]
        text.append(recette1)

        recette2['nom'] = nom2
        recette2['ingredient'] = ""
        recette2['recette'] = a[1][2][0]
        text.append(recette2)

        return text
    else: # si les ingrédients sont pour la deuxième recette

        # on va découper le texte en fonction des étapes
        a[0] = a[0].split(mot_cle[1])
        a[1] = a[1].split(mot_cle[1])

        # on va découper le texte en fonction des étapes de la recette (NTHOKI)
        a[0][1] = a[0][1].split(mot_cle[3])
        a[1][1] = a[1][1].split(mot_cle[3])

        # on récupère le nom de la première recette
        a[0][0] = a[0][0].split('\n')
        for i in range(10):
            a[0][0][0] = a[0][0][0].replace(str(i),"")

        try:
            # on récupère le nom de la deuxième recette
            # s'il n'y avait pas de NTHOKI pour la première recette on aura une erreur
            a[0][1][1] = a[0][1][1].split('.')
            nom = (a[0][1][1].pop()).split('\n')
        except:
            # on récupère le nom de la deuxième recette
            a[0][1][0] = a[0][1][0].split('.')
            nom = a[0][1][0].pop()

            a[0][1][0] = '.'.join(a[0][1][0])

            nom = nom.split('\n')

        # on essaie de trouver le bon nom
        nom2 = nom[0]
        if len(nom) > 1:
            if nom2 == '':
                nom2 = nom[1]
                if len(nom) > 2:
                    if nom[2]!='' and nom[2][0] == ' ':
                        nom2+=nom[2]
            elif nom[1]!='' and nom[1][0] == ' ':
                nom2+=nom[1]
                if len(nom) > 2:
                    if nom[2]!='' and nom[2]!='' and nom[2][0] == ' ':
                        nom2+=nom[2]
        if nom2 == '':
            print(a,nom,'3')

        recette1['nom'] = a[0][0][0]
        recette1['ingredient'] = ""
        recette1['recette'] = a[0][1][0]
        text.append(recette1)

        recette2['nom'] = nom2
        recette2['ingredient'] = a[1][0]
        recette2['recette'] = a[1][1][0]
        text.append(recette2)

        return text

def recette2_ingredient0(text_page, text):
    """Pour les pages avec 2 recettes, dont aucune n'a d'ingrédient

    Args:
        text_page (str): le text de la page
        text (list): la liste des recettes

    Returns:
        list: la liste des recettes mise à jour
    """
    recette1 = {}
    recette2 = {}

    a = text_page.split(mot_cle[1])

    a[1] = a[1].split(mot_cle[3])
    a[2] = a[2].split(mot_cle[3])

    a[0] = a[0].split('\n')

    for i in range(10):
        a[0][0] = a[0][0].replace(str(i),"")

    try:
        a[1][1] = a[1][1].split('.')
        nom = (a[1][1].pop()).split('\n')
    except:
        a[1][0] = a[1][0].split('.')
        nom = a[1][0].pop()
        nom = nom.split('\n')

        a[1][0] = '.'.join(a[1][0])

    # on essaie de trouver le bon nom
    nom2 = nom[0]
    if len(nom) > 1:
        if nom2 == '':
            nom2 = nom[1]
            if len(nom) > 2:
                if nom[2]!='' and nom[2][0] == ' ':
                    nom2+=nom[2]
        elif nom[1]!='' and nom[1][0] == ' ':
            nom2+=nom[1]
            if len(nom) > 2:
                if nom[2]!='' and nom[2][0] == ' ':
                    nom2+=nom[2]
    if nom2 == '':
        print(a,nom,'4')

    recette1['nom'] = a[0][0]
    recette1['ingredient'] = ""
    recette1['recette'] = a[1][0]
    text.append(recette1)

    recette2['nom'] = nom2
    recette2['ingredient'] = ""
    recette2['recette'] = a[2][0]
    text.append(recette2)

    return text



text = []
mot_cle = ['INGREDIENTES:', 'ELABORACIÓN:', ' MPËUI:', 'NTHOKI:']
lieu='./voces_y_sabores.pdf'

with open(lieu, 'rb') as pdf_file:
    # on ouvre le pdf
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    for i in range(23,82):
        # on lit la page du pdf et on récupère le texte
        pdf_page = pdf_reader.getPage(i)
        text_page = pdf_page.extractText()

        # on compte combien de fois arrive les mots cle
        a=[0,0,0,0]
        for i in range(4):
            a[i]=text_page.count(mot_cle[i])

        # on récupère les recettes (ne marche que s'il y a 2 recettes sur la pages)
        if a[1] == 2 and a[0] == 2:
            text=recette2(text_page, text)
        elif a[1] == 2 and a[0] == 1:
            text=recette2_ingredient1(text_page, text)
        elif a[1] == 2 and a[0] == 0:
            text=recette2_ingredient0(text_page, text)

print(text)