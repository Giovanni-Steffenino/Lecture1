from dataclasses import dataclass

from pydantic_core.core_schema import none_schema

categorie_valide = {"Gold", "Silver" , "Bronze"}

class Cliente:
    def __init__(self, nome, mail, categoria):
        self.nome = nome
        self.mail = mail
        self._categoria = None
        self.categoria = categoria
    @property#GETTER
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        if categoria not in categorie_valide:
            raise ValueError("Attenzione, categoria NON VALIDA!!!")
        self._categoria = categoria

    def descrizione(self):
        return f"Cliente {self.nome} ({self.categoria}) - {self.mail}"

def _test_modulo():
        c1 = Cliente("Mario Bianchi", "mario.bianchi@polito.it","Gold")
        print(c1.descrizione())

if __name__ == "__main__":
    _test_modulo()


@dataclass
class ClienteRecord:
    nome: str
    mail: str
    categoria: str

    def __hash__(self):
        return hash(self.mail)

    def __eq__(self, other):
        self.mail == other.mail

    def __str__(self):
        return f"{self.nome} -- {self.mail} ({self.categoria})"

