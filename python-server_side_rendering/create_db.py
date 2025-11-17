import sqlite3


def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Créer la table Products si elle n'existe pas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insérer les produits
    cursor.execute('DELETE FROM Products')  # optionnel : vider la table si existante
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
