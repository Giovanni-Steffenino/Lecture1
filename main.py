#Scriviamo un codice che modelli un semplice gestionale aziendale. Dovremmo prevedere la possibilità di
#definire entità che modellano i prodotti , i clienti, offrire interfacce per calciolare i prezzi eventualmente
#scontati, ...
from platform import processor

class Prodotto:

    aliquota_iva = 0.22 #è la stessa per tutte le istanze che verranno create

    def __init__(self, name: str, price: float, quantity: int, supplier:str):
        self.name = name
        self._price = None #underscore davanti diventa privata: non ti fa andare avanti perché non lo vede
        self.price=price
        self.quantity = quantity #doppio underscore non bisogna accedere a quella variabile
        self.supplier = supplier

    def valore(self):
        return self.price*self.quantity

    def valore_lordo(self):
        netto = self.price*self.quantity
        lordo = netto * (1+self.aliquota_iva)
        return lordo

    @classmethod #decoratore che viene messo prima di un metodo e sta ad indicare che è un metodo di classe
    def costruttore_con_quantita_uno(cls, name:str, price: float, supplier: str): #non prendono il self, ma cls
        return cls(name, price, 1, supplier)

    @staticmethod #informazione generale.
    def applica_sconto(prezzo, percentuale):
        return prezzo*(1-percentuale)

    @property #GETTER
    def price(self):
        return self._price
    @price.setter #SETTER posso farlo solo dopo aver fatto un getter
    def price(self, valore):
        if valore < 0:
            raise ValueError("Attenzione il prezzo non può essere negativo")
        self._price = valore

    def __str__(self):
        return f"{self.name} - disponibili {self.quantity} pezzi a {self.price}€"

    def __repr__(self):
        return f"Prodotto(nome = {self.name}, price = {self.price}, quantity = {self.quantity}, supplier = {self.supplier}"

    def __eq__(self, other: object ):
        if not isinstance(other, Prodotto):
            return NotImplemented
        return self.name == other.name and self.price == other.price and self.quantity==other.quantity and self.supplier == other.supplier

    def __lt__(self, other: "Prodotto") -> bool:
        return self.price < other.price


class Cliente:
    def __init__(self, name:str, mail, category ):
        self.name = name
        self.mail = mail
        self._category = None
        self.category=category

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, categoria):
        categorie_valide = {"Gold", "Silver", "Bronze"}
        if categoria not in categorie_valide:
            raise ValueError("Categoria non valida, Scegliere tra Gold, Silver e Bronze")
        else:
            self._category = categoria #CIAO BELLO


    def descrizione(self):
        return f"Cliente {self.name} ({self.category}) - {self.mail}"

myproduct1 = Prodotto("Laptop", 1200, 12, supplier="ABC")
print(f"Nome Prodotto: {myproduct1.name}")
print(f"Prezzo Prodotto: {myproduct1.price}")

myproduct2 = Prodotto("Mouse", 10, 25, "CDE")
print(f"Nome Prodotto: {myproduct2.name}")
print(f"Prezzo Prodotto: {myproduct2.price}")
print (f"Il totale lordo di myproduct1 è {myproduct1.valore_lordo()}")
p3 = Prodotto.costruttore_con_quantita_uno("Auricolari", 200, "ABC")
p_a = Prodotto("Laptop", 1200, 12, "ABC")
p_b = Prodotto("Mouse", 10, 14, "ABC")

print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price, 0.50)}")

print(p3)
print("myproduct == p_a", myproduct1==p_a) #va a chiamare il metoto __eq__ appena implementato #ASPETTO TRUE
print("p_b == p_a", p_b==p_a) #ASPETTO FALSE
mylist = [p_a,p_b, myproduct1]
mylist.sort()
print ("Lista di prodotti ordinata")
for p in mylist:
    print(f" - {p}") #rende la lista ordinata in base al prezzo --> __lt__


c1= Cliente("Mario Bianchi", "mario.bianchi@polito.it", "Gold" )
print(c1.descrizione())
c2 = Cliente("Carlo Masone", "carlo.masone@polito.it", "Silver" )






