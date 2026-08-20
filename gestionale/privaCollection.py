from gestionale.core.prodotto import ProdottoRecord

p1 = ProdottoRecord("Laptop", 1200.0)
p2= ProdottoRecord("Mouse", 20.0)
p3= ProdottoRecord("Auricolari", 250.0)

carrello = [p1, p2, p3, ProdottoRecord("Tablet", 700.0)]

#Aggiungere a una lista
carrello.append(ProdottoRecord("Monitor", 150.0))

carrello.sort(key=lambda x: x.prezzo_unitario, reverse=True)

print("Prodotti nel carrello")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale carrello: {tot}")

#append, aggiunge un solo elemento in coda
#estend più di uno.
#insert (index: 2, ....) inserire dove vuoi

#remove(p1) rimuove p1, elimina il primo che trova
#pop --> rimuove l'ultimo pop(2) rimuove l'elemento in posizione due
#clear() rimuove tutto

#carrello.sort() ---> ordinamento naturlale         ammette reverse=True
#carrello.sort(key=fuction)
#sorted(carrello) --> crea una nuova lista ordinata
#carrello.reverse() --> inverte l'ordine
#carrello.copy --> copia di carrello
#carrello.copy().deepcopy(carrello)

#tuple()
sede_principale = (45, 8) #non si possono modificare
sede_milano = (45,9)
print (f"sede lat {sede_principale[0]} long {sede_principale[1]}")

AliquotaIva = (("Standard", 0.22), #tupla di tuple
               ("Ridotta", 0.10),
               ("Alimentari", 0.04),
               ("Esente", 0)
               )
for descrizione, valore in AliquotaIva:
    print (f"{descrizione}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    #restituisce prezzo totale, medio, massimo e minimo
    prezzi = [p.prezzo_unitario for p in carrello]
    return sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi)

tot, media, max, min = calcola_statistiche_carrello(carrello)

print(tot)

#set
categorie = {"Gold", "Silver", "Bronze","Gold"}
#non stampa il secondo Gold, con un set possiamo calcolare la dimensione
categorie_2 = {"Platinum", "Elite"}
categorie_all = categorie.union(categorie_2) #anche con |, con # & solo elementi comuni

categorie_comuni = categorie_all & categorie_2

categorie_esclusive = categorie - categorie_2
print(categorie_esclusive)

prodotti_codice_A = {ProdottoRecord("Laptop", 1200.0) , ProdottoRecord("Mouse", 20.0), ProdottoRecord("Auricolari", 250.0)}
prodotti_codice_B = {ProdottoRecord("Tablet", 700.0)}

s = set()
#Aggiungere
s.add(ProdottoRecord("Laptop", 1200.0))
s.update([ProdottoRecord("s", 4.0)])
#Togliere
s.remove(ProdottoRecord("s", 4.0)) #anche discard e pop (rimuove e restituisce un elemento)

s1 = set()
s.union(s1) #set che unisce i due set di partenza
s.intersection(s1) #AND solo elementi in comune

s1.issubset(s) #True solo se gli elementi di s1 sono contenuti in s
s1.isdisjoint(s) #True se gli elementi di s e s1 sono diverse















