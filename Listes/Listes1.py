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
elif choix == ma_liste[3]:
  print("Non! Ressayez-vous!")

print("combien de temps a tu de devoirs par semaine?")
liste = [2, 4, 6]
for i in range (2,4,6):
    print (liste)
    choix2 = int(input())
    if choix2 == 2:
        print("Sa ces normale!")

    if choix2 == 4:
        print("Suffisament de travaille!")
      
    if choix2 == 6:
        print("Give yourself a break please!")


print("Merci de participer a mon questionnaire!")