# Budget App
# This program is a budget app that allows users to create categories, deposit and withdraw funds from those categories, transfer funds between categories, and display a bar chart of the percentage of funds spent in each category.

class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.first_deposit = True

    def deposit(self, amount, description =''):
        if self.first_deposit and not description:
            description = 'initial deposit'
            self.first_deposit = False
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description =''):
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
    
    def get_withdrawals(self):
        return abs(sum(item['amount'] for item in self.ledger if item['amount'] < 0))
    
    def __str__(self):
        title = self.category.center(30, '*') + '\n'
        items = ''
        for entry in self.ledger:
            desc = entry['description'][:23].ljust(23)
            amount = f"{entry['amount']:.2f}".rjust(7)
            items += f"{desc}{amount}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):

    total_spent = sum(category.get_withdrawals() for category in categories)
    percentages = [(category.get_withdrawals() / total_spent) * 100 for category in categories]
    rounded_percentages = [int(p // 10) * 10 for p in percentages]
    chart = "Percentage spent by category\n"
    
    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}| "
        for percent in rounded_percentages:
            chart += 'o' if percent >= i else '  '
        chart += '\n'

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = max(len(category.category) for category in categories)
    category_names = [category.category.ljust(max_length) for category in categories]
   
    for i in range(max_length):
        chart += "     "
        for name in category_names:
            chart += name[i] + "  " if i < len(name) else "   "
        chart += "\n"

    return chart.rstrip("\n")

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

lothing = Category('Clothing')
food.transfer(50, clothing)

auto = Category('Auto')
auto.deposit(1000, 'deposit')
auto.withdraw(100, 'gasoline')

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))
