class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
        
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
     
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False
        
    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        """ Formatea la salida para imprimir la categoría con su historial de transacciones """
        title = self.category.center(30, '*') + '\n'
        items = ''
        for entry in self.ledger:
            desc = entry['description'][:23].ljust(23)  # Asegura que la descripción no pase de 23 caracteres
            amount = f"{entry['amount']:.2f}".rjust(7)  # Formato de dos decimales alineado a la derecha
            items += f"{desc}{amount}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


# Prueba
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
