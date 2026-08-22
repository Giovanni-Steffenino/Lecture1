#Software gestionale
#1)Supportare larrivo e la gesitione di ordini, quando arriva un nuovo ordine lo aggiungo a una coda
#assicurandomi che sia eseguito solo dopo gli altri
#2) Statistiche sugli ordini
#3) fornire statistiche sulla distribuzione di ordine per categoria di clienti
from collections import deque, Counter, defaultdict

from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine
from gestionale.core.clienti import ClienteRecord

class GestoreOrdini:
    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = []
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list)

    def add_ordine(self, ordine: Ordine):
        self._ordini_da_processare.append(ordine)
        print(f"Arrivato un nuovo ordine da parte di {ordine.cliente}")
        print(f"Ordini ancora da evadere: {len(self._ordini_da_processare)}")

    def processa_prossimo_ordine(self):
        #Questo metodo legge il prossimo ordine in coda e lo gestisce, assicuriamoci che esista
        if not self._ordini_da_processare:
            print("Non ci sono ordini in coda")
            return False

        ordine = self._ordini_da_processare.popleft()

        print(f"Sto processanfo l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita

        #Raggruppare gli orfini per categoria
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        #Archiviamo l'ordine
        self._ordini_processati.append(ordine)

        print("Ordine correttamente processato")
        return True

    def processa_tutti_gli_ordini(self):
        #Proceessa tutti gli ordini in coda
        print(f"Processando {len(self._ordini_da_processare)} ordini")
        while self._ordini_da_processare:
            self.processa_prossimo_ordine()
        print("Tutti gli ordini sono stati processati")

    def get_statistiche_prodotti(self, top_n: int = 5):
        valori=[]
        for prodotto, quantita in self._statistiche_prodotti.most_common(top_n):
            valori.append((prodotto, quantita))
        return valori

    def get_distribuzione_categorie(self):
        valori = []
        for cat in self._ordini_per_categoria.keys():
            ordini = self._ordini_per_categoria[cat]
            totale_fatturato = sum([o.totale_lordo(0.22) for o in ordini])
            valori.append((cat, totale_fatturato))
        return valori

    def stampa_riepilogo(self):
        """Stampa info di massima"""
        print("\n" + "=" * 60)
        print("Stato attuale del business:")
        print(f"Ordini correttamente gestiti: {len(self._ordini_processati)}")
        print(f"Ordini in coda: {len(self._ordini_da_processare)}")

        print("Prodotti più venduti:")
        for prod, quantità in self.get_statistiche_prodotti():
            print(f"{prod}: {quantità}")

        print(f"Fatturato per categoria:")
        for cat, fatturato in self.get_distribuzione_categorie():
            print(f"{cat} : {fatturato}")

def test_modulo():
    sistema = GestoreOrdini()

    ordini = [
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
               ClienteRecord("Mario Rossi", "mario@mail.it", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 2),
                RigaOrdine(ProdottoRecord("Tablet", 500.0), 1),
                RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)],
               ClienteRecord("Fulvio Bianchi", "bianchi@gmail.com", "Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 2),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 2)],
            ClienteRecord("Giuseppe Averta", "giuseppe.averta@polito.it", "Silver")),
        Ordine([
            RigaOrdine(ProdottoRecord("Tablet", 900.0), 1),
            RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)],
            ClienteRecord("Carlo Masone", "carlo@mail.it", "Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
            ClienteRecord("Francesca Pistilli", "francesca@gmail.com", "Bronze"))
    ]
    for o in ordini:
        sistema.add_ordine(o)
    sistema.processa_tutti_gli_ordini()
    print(sistema.stampa_riepilogo())

if __name__ == "__main__":
    test_modulo()














        