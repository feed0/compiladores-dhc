class SymbolTable:
    def __init__(self):
        # Initialisation de la table des symboles comme un dictionnaire
        self.table = {}

    def add_symbol(self, name, token, lexema, symbol_class, symbol_type, address):
        """
        Ajoute un symbole à la table.
        """
        if name in self.table:
            raise ValueError(f"Le symbole '{name}' existe déjà dans la table.")
        self.table[name] = {
            "TOKEN": token,
            "LEXEMA": lexema,
            "CLASS": symbol_class,
            "TYPE": symbol_type,
            "ADDRESS": address
        }

    def get_symbol(self, name):
        """
        Récupère un symbole par son nom.
        """
        return self.table.get(name, None)

    def remove_symbol(self, name):
        """
        Supprime un symbole de la table.
        """
        if name in self.table:
            del self.table[name]
        else:
            raise KeyError(f"Le symbole '{name}' n'existe pas dans la table.")

    def display_table(self):
        """
        Affiche tous les symboles dans la table.
        """
        print(f"{'NAME':<15}{'TOKEN':<15}{'LEXEMA':<15}{'CLASS':<15}{'TYPE':<15}{'ADDRESS':<15}")
        print("-" * 90)
        for name, attributes in self.table.items():
            print(f"{name:<15}{attributes['TOKEN']:<15}{attributes['LEXEMA']:<15}"
                  f"{attributes['CLASS']:<15}{attributes['TYPE']:<15}{attributes['ADDRESS']:<15}")