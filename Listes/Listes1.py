print("Bonjour, bienvenue a mon jeu de devinette!")

print("Quelle mot qu'on dit quand on fais des travailles obligatoire aprés l'école?")
print("Tap e pour un indice.")

ma_liste = ['devoir', 'formatif', 'travailler', 'jugler']
choix = input().lower()
if choix == 'e' :
  for lettre in ma_liste:
    print(lettre)
  print("La reponse est parmis ces choix")
if choix == ma_liste[0] :
  print("Exactement! les devoirs sont les travaux qu'on fais aprés l'école!")
elif choix == ma_liste[1]:
  print("Non! Ressayez-vous!")
elif choix == ma_liste[2] : 
  print("Non! Ressayez-vous!")
elif choix == ma_liste :
  print("Non! Ressayez-vous!")

