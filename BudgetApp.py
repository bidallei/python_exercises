'''

Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The 'bars' in the bar chart should be made out of the 'o' character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says 'Percentage spent by category'.

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  s
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g  


'''



class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.first_deposit = True

    def deposit(self, amount, description = ''):
        if self.first_deposit:
            description = 'initial deposit'
            self.first_deposit = False
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
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
        title = self.category.center(30, '*') + '\n'
        items = ''
        for entry in self.ledger:
            desc = entry['description'][:23].ljust(23)
            amount = f"{entry['amount']:.2f}".rjust(7)
            items += f"{desc}{amount}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    pass


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)