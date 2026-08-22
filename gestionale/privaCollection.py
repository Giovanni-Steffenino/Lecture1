from collections import Counter, deque

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

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
s.update([ProdottoRecord("ciaooo", 4.0)])
#Togliere
#s.remove(ProdottoRecord("ciaooo", 4.0)) #anche discard e pop (rimuove e restituisce un elemento)

s1 = set()
s.union(s1) #set che unisce i due set di partenza
s.intersection(s1) #AND solo elementi in comune

s1.issubset(s) #True solo se gli elementi di s1 sono contenuti in s
s1.isdisjoint(s) #True se gli elementi di s e s1 sono diverse


#dizionari
catalogo = {
    "Lap001" : ProdottoRecord("Laptop", 1200.0),
    "Lap002" : ProdottoRecord("LaptopPRO", 2300.0),
    "MAU001" : ProdottoRecord("Mouse", 20.0),
    "AUR001" : ProdottoRecord("Auricolari", 250.0),
}

cod = "Lap002"
prod = catalogo[cod]
print(f"Il porodotto con codice {cod} è {prod}")

#metodo get del dizionario
prod1 = catalogo.get("Non esiste")
if prod1 is None:
    print("Prodotto non trovato")

prod2 = catalogo.get("Non esiste2", ProdottoRecord("Sconosciuto", 0))
print(prod2)

keys = list(catalogo.keys())
values = list(catalogo.values())

for k in keys:
    print(k)
for v in values:
    print(v)

for keys2, values2 in catalogo.items():
    print(f"Cod {keys2} è associata al val {values2}")

rimosso = catalogo.pop("Lap002")
print(rimosso)

prezzi = {codice : prod.prezzo_unitario for codice, prod in catalogo.items()}
print(prezzi)


#Esercizio LIVE
#Per ciascuno dei seguenti casi decidere cosa usare

#1) Memorizzare un elenco di ordini che dovranno essere processati in ordine di arrivo
ordini_da_processare = []
o1 = Ordine([], ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"))
o2 = Ordine([], ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"))
o3 = Ordine([], ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"))

ordini_da_processare.append((o1, 0))
ordini_da_processare.append((o2, 10))
ordini_da_processare.append((o3, 3))

#2) Memorizzare i codici fiscali dei clienti, univoco
codici_fiscali = {"sgagsgdg", "hahdgfwu", "eduwbd56", "hahdgfwu"}
print(codici_fiscali)

#3) Creare un database di prodotti che posso cercare con un codice univoco
listino_prodotti = {"Lap001", ProdottoRecord("Laptop", 1200.0),
                    "Lap002", ProdottoRecord("LaptopPRO", 2300.0), }

#4) Memorizzare le coordinate gps della nuova sede di Roma
cordinate_Roma = (45, 6)

#5) tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo tempo di ordine temporale
categorie_periodo = set()
categorie_periodo.add("Gold")
categorie_periodo.add("Silver")
print("======================")

#COUNTER
lista_clienti = [
ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"),
ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"),
ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Silver"),
]

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)

print(categorie_counter)
print(categorie_counter.most_common(2))
print(categorie_counter.total())

#DEQUE
coda_ordini = deque()

for i in range(1,10):
    cliente = ClienteRecord(f"Cliente {i}", f"cliente{i}", "Gold")
    prodotto = ProdottoRecord(f"Orodotto{i}", 100*i)

    ordine = Ordine([RigaOrdine(prodotto, 1)], cliente)
    coda_ordini.append(ordine)

print(f"Ordini in coda: {len(coda_ordini)}")

while coda_ordini: #cicla finchè è pieno
    ordine_corrente = coda_ordini.popleft()
    print(f"Sto gestendo l'ordine del cliente:{ordine_corrente.cliente}")

print("Ho gestito tutti gli ordini")











