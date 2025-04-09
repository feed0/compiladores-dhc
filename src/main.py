import pandas as pd
from IPython.display import display

class SymbolTable:
    def __init__(self):
        # Initialisation de la table des symboles comme un DataFrame avec les colonnes spécifiées
        self.columns = ['NAME', 'TOKEN', 'LEXEMA', 'CLASS', 'TYPE', 'ADDRESS']
        self.df = pd.DataFrame(columns=self.columns)

    def add_symbol(self, name, token, lexema, symbol_class, symbol_type, address):
        """
        Ajoute un symbole à la table.
        """
        if name in self.df['NAME'].values:
            raise ValueError(f"Le symbole '{name}' existe déjà dans la table.")
        new_row = {
            'NAME': name,
            'TOKEN': token,
            'LEXEMA': lexema,
            'CLASS': symbol_class,
            'TYPE': symbol_type,
            'ADDRESS': address
        }
        # Utilisation de concat pour ajouter la nouvelle ligne au DataFrame
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)

    def get_symbol(self, name):
        """
        Récupère un symbole par son nom.
        """
        rows = self.df[self.df['NAME'] == name]
        if rows.empty:
            return None
        return rows.iloc[0].to_dict()

# EXISTE NECESSIDADE DE REMOVER
    # def remove_symbol(self, name):
    #     """
    #     Supprime un symbole de la table.
    #     """
    #     if name not in self.df['NAME'].values:
    #         raise KeyError(f"Le symbole '{name}' n'existe pas dans la table.")
    #     self.df = self.df[self.df['NAME'] != name]

    def display_table(self):
        """
        Affiche tous les symboles dans la table.
        """
        display(self.df)


if __name__ == "__main__":
    # Exemple d'utilisation de la table des symboles basée sur un DataFrame
    symbols = SymbolTable()

    # Ajout de symboles
    symbols.add_symbol("x", "IDENTIFIER", "x", "VARIABLE", "INT", "0x001")
    symbols.add_symbol("y", "IDENTIFIER", "y", "VARIABLE", "FLOAT", "0x002")
    symbols.add_symbol("print", "KEYWORD", "print", "FUNCTION", "VOID", "0x100")

    # Affichage de la table
    print("Table des symboles:")
    symbols.display_table()

    # Récupération d'un symbole
    print("\nRécupération du symbole 'x':")
    print(symbols.get_symbol("x"))

    # Suppression d'un symbole
    symbols.remove_symbol("y")
    print("\nTable après suppression de 'y':")
    symbols.display_table()