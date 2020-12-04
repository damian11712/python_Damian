print("Bonjour, est bienvenue a mon petit quiz de soccer!")

print("Qui a les plus de buts dans l'histoire de soccer?" )

#question1
print("ronaldo nazario, pele, cristiano ronaldo ou lionel messi?")
choix = input().lower()

if choix == "ronaldo nazario":
  print("Non! ronaldo nazario a 414.")
elif choix == "pele":
  print("WOW! pele a une énorme 767 buts! C'est une bon depart! Continuer")
elif choix == "cristiano ronaldo":
  print("Non, mais tes proches! cristiano ronaldo à 750 buts. Il peut briser le record de pele.")
elif choix == "lionel messi":
  print("lionel messi est juste en arriére de cristiano ronaldo avec 711, comme cristiano, tous les deux peuves passer pele.")
else:
  print("ce n'était pas une choix valid")
  
#question2
print("Quelle equipe de soccer a le plus de trophée de champions league?")

print("real madrid, ac milan, manchester utd ou liverpool")
choix = input().lower()

if choix == "real madrid":
  print("correct! real madrid sont encore en haut avec 13 trophées")
if choix == "ac milan":
  print("non!ac milan sont assis en arriére de real madrid avec 7 trophées")
if choix == "manchester utd":
  print("non! manchester utd a seulement gagnée le fameux trophées 3 fois")
if choix == "liverpool":
  print("non! liverpool a 3 de plus de trophées que manchester utd mais pas le plus!")
else:
  print("ce n'était pas une valid choix")