class Category:

    def __init__(self, category):
        self.category = category.title()
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append({
            "amount": float(amount),
            "description": description
        })
        print(self.ledger)
        return self.ledger

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -float(amount),
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
                "amount": -float(amount),
                "description": f"Transfer to {category.category}"
            })
            # To be updated to add to other ledger
            category.ledger.append({
                "amount": float(amount),
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
            print(type(t['amount']))
            output += f"{t['description'][0:23]:23}{t['amount']:>7.2f}" + '\n'

        output += f"Total: {self.get_balance():.2f}"
        print(output)
        return output

def create_spend_chart(categories):
    data = []

    for c in categories:
        total_withdrawals = 0
        for t in c.ledger:
            if t['amount'] < 0:
                total_withdrawals += t['amount'] * -1

        data.append({"category": c.category, "amount_spent": total_withdrawals})

    total_spent = 0
    for d in data:
        total_spent += d['amount_spent']

    for d in data:
        print(f"amount spent: {d['amount_spent']}")
        print(f"total spent: {total_spent}")
        pct_spent = d['amount_spent']/total_spent*100
        d["percentage_spent"] = int(pct_spent)

    print(data)

    output = 'Percentage spent by category'+'\n'
    for i in range(100,-1,-10):
        output += f'{i:>3}|'
        for d in data:
            if d['percentage_spent'] >= i:
                output += ' o '
            else:
                output += '   '

        output += ' \n'

    output += '    ' + '-' * len(categories)*3 + '-' + '\n'

    category_names = []
    for c in categories:
        category_names.append(c.category)

    rearr_txt = []
    max_len = len(max(category_names, key=len))

    for i in range(0,max_len):
        for c in category_names:
            rearr_txt.append(list(c)[i]) if len(c) > i else rearr_txt.append(' ')

    row = 1
    num_categories = len(category_names)
    index = 0
    while row <= max_len:
        for i in range(0,num_categories):
            if i==0: output += '   '
            output += '  ' + rearr_txt[index]
            index += 1
            if i == num_categories-1:
                output += '  \n'
        row += 1
    output = output[:-1] # remove the last \n

    print(output)
    return output





food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])


expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "

# print("EXPECTED")
# print(expected)

# file1 = open('chart.txt','w')
# file1.write(repr(actual) + '\n')
# file1.write(repr(expected) + '\n')
# file1.close()

# c1 = Category('Food')
# print(c1.category)
# c1.deposit(123456789,'cash deposit abcdefghijklmnop')
# c1.withdraw(20,'cash withdrawlabcdefghijklmnop')
# print(c1.get_balance())
# str(c1)



# food = Category("Food")
# entertainment = Category("Entertainment")
# business = Category("Business")
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)
# print(food.ledger[0:3])
# print(entertainment.ledger[0])

