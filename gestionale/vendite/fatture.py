from dataclasses import dataclass
from datetime import date

from gestionale.core.clienti import Cliente
from gestionale.core.prodotto import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


@dataclass
class Fattura:
    ordine: "Ordine"
    numero_fattura: str
    data: date

    def genera_fattura(self):
        linee = [
            f"=" * 60,
            f"data {self.data} numero fattura {self.numero_fattura}",
            f"CLINTE: {self.ordine.cliente.nome}"
            f"=" * 60,
        ]
        for i, riga in enumerate(self.ordine.righe):
            linee.append(
                f"{i+1} "
                f"{riga.prodotto.name} "
                f"Q.tà {riga.quantità} x {riga.prodotto.prezzo_unitario} = "
                f"Tot {riga.totale_riga()}")
        linee.extend([
            f"=" * 60,
            f"Totale netto {self.ordine.totale_netto()}\n"
            f"IVA 22%: {self.ordine.totale_netto()*0.22}\n"
            f"Tot Lordo: {self.ordine.totale_lordo(0.22)}"

        ])

        return "\n".join(linee)

def _test_modulo():
    p1 = ProdottoRecord("laptop", 1200)
    p2 = ProdottoRecord("mouse", 20)
    p3 = ProdottoRecord("ipad", 600)
    cliente = Cliente("Mario Bianchi", "mario.bianchi@polito.it", "Gold")
    ordine=Ordine(righe= [
        RigaOrdine(p1,1)
        ,RigaOrdine(p2,5)
        ,RigaOrdine(p3,2)
    ], cliente=cliente )
    f1 = Fattura (ordine, "2026/01", date.today())
    print(f1.genera_fattura())

if __name__ == "__main__":
    _test_modulo()