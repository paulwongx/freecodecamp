class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append({
            "amount": int(amount),
            "description": description
        })

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -int(amount),
                "description": description
            })
            return True
        else:
            return False

    def get_balance(self):
        sum = 0
        for t in self.ledger:
            sum += t["amount"]
        return sum

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -int(amount),
                "description": f"Transfer to {category.category}"
            })
            # To be updated to add to other ledger
            category.ledger.append({
                "amount": int(amount),
                "description": f"Transfer from {self.category}"
            })
            return True
        else:
            return False

    def check_funds(self, amount):
        funds = self.get_balance()
        if funds >= amount:
            return True
        else:
            return False

    def __str__(self):
        output = self.category.center(30,'*') + '\n'

        for t in self.ledger:
            output += f"{t['description']:<15}{t['amount']:>15.2f}" + '\n'

            # desc_len = min(len(t['description']),23)
            # print(f'desc_len: {desc_len}')
            # amount_len = min(len(str(format(t['amount'],'.2f'))),7)
            # print(f'amount_len: {amount_len}')
            # num_spaces = 30-desc_len-amount_len
            # print(f'num_spaces: {num_spaces}')

            # line_item = t['description'][0:23]
            # line_item += ' ' * (30-num_spaces)
            # line_item += format(t['amount'],'.2f')[0:7]
            # output += line_item + '\n'

        output += f"Total: {self.get_balance():.2f}"
        print(output)
        return output

# def create_spend_chart(categories):



# create_spend_chart(["food","entertainment"])



c1 = Category('Food')
print(c1.category)
c1.deposit(100,'income')
c1.withdraw(20,'cash withdrawlaaaaaaaaaa')
print(c1.get_balance())
str(c1)



# food = Category("Food")
# entertainment = Category("Entertainment")
# business = Category("Business")
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)
# print(food.ledger[0:3])
# print(entertainment.ledger[0])

