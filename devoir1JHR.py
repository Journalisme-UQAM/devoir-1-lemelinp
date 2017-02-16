data1 = list(range(30000,100000))
data2 = list(range(00000,18000))
print(data1+data2)

# Tu as bien créé deux listes de nombres correspondant aux numéros de permis possibles du Collège des médecins, liste qui s'affichent successivement.
# Sauf pour la torpinouche de décennie 2000 à 2009 où il manque les zéros précédant les numéros qu'on cherche.

# Une des façons d'y arriver est de faire une liste qui va de 2000 à 2017.
# En fait, tant qu'à y être, pourquoi ne pas immédiatement couvrir toutes les années qui nous intéressent:

annees = list(range(1930,2018))

# On peut ensuite faire une boucle afin de convertir chaque année en chaîne de caractères.
# Cela permet de ne conserver que les deux derniers caractères (avec 2002, par exemple, on obtient ainsi 02):

for annee in annees:
	codeDeDeuxChiffres = str(annee)[2:]

# Après, on utilise la même technique pour les trois derniers chiffres des numéros de permis avec, une façon parmi d'autres, une liste qui va de 1000 à 1999:

num = list(range(1000,2000))

# Puis, à l'aide d'une deuxième boucle, on peut convertir chacun des nombres qu'elle contient en chaîne de caractères et de ne conserver que les 3 derniers caractères, transformant ainsi 1001 en 001, par exemple, un peu comme on l'a fait avec les années.

for n in num:
	codeDeTroisChiffres = str(n)[1:]

# Pour coller les deux ensemble, on peut imbriquer la 2e boucle dans la première, ainsi:

for annee in annees:
	codeDeDeuxChiffres = str(annee)[2:]
	for n in num:
		codeDeTroisChiffres = str(n)[1:]
		numeroDePermis = codeDeDeuxChiffres + codeDeTroisChiffres
		print(numeroDePermis)

		# Magie! :)