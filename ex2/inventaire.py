from article import Article


a1 = Article("A001", "Stylo bleu", 1.20, 150)
a2 = Article("A002", "Cahier A4", 2.50, 80)
a3 = Article("A003", "Classeur", 3.75, 40)
articles=[a1,a2,a3]
for a in articles :
    print (a)


total = sum(a.valeur_stock() for a in articles)
print(f"Valeur d’inventaire : {total:.2f} €")   