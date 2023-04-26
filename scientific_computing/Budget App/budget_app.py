class Category:

    def __init__ (self, name):
        self.name = name
        self.ledger = []

    def __repr__(self):
        title_line = self.name.center(30,'*') + '\n'
        ledger = ''
        for item in self.ledger:
            category_names = f"{item['description']:<23}"
            amounts = f"{item['amount']:>7}"
            ledger += f"{category_names[:23]}{amounts[:7]}\n"
        total = f"Total: {self.get_balance()}"

        return title_line + ledger + total

    def check_funds (self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def deposit (self, amount, description = None):
        if description == None:
            description = ''

        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        current_balance = []
        deposits = []
        withdrawals = []
        for item in self.ledger:
            for key, value in item.items():
                if key == 'amount':
                    current_balance.append(value)

        balance = sum(current_balance)

        return balance

    def withdraw (self, amount, description = None):
        if description == None:
            description = ''

        if self.check_funds(amount) is True:
            #amount = 0 - amount
            self.ledger.append({"amount": - amount, "description": description})
            return True
        else:
            return False


    def transfer (self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, description = f'Transfer to {other_category.name}')
            other_category.deposit(amount, description = f'Transfer from {self.name}')
            return True
        else:
            return False


def create_spend_chart(categories):
    withdrawals = []
    names = []
    for category in categories:
        names.append(category.name)
        withdrawals.append(sum(item['amount'] for item in category.ledger if item['amount'] < 0))

    total_withdrawals = sum(withdrawals)
    percentages = [(withdrawal / total_withdrawals) * 100 for withdrawal in withdrawals]

    chart = ""
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += " " * 4 + "-" * (len(categories) * 3 + 1) + "\n"

    max_name_length = max([len(name) for name in names])
    for i in range(max_name_length):
        chart += " " * 5
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i != max_name_length - 1:
            chart += "\n"

    return "Percentage spent by category\n" + chart





m = Category('Salary')


f = Category('Food')
f.deposit(300, 'salary_april')
f.withdraw(23,'meat')
f.withdraw(6, 'milk')
f.withdraw(3, 'soda')
f.withdraw(5, 'bread')

balance = f.get_balance()

s = Category('Shelter')
s.withdraw(75,'home')

c = Category('Clothing')
c.withdraw(12, 't-shirt')
c.withdraw(20, 'jumper')

#print(balance)
#print(withdrawal)

#s.deposit(40,'home')
#transfer = f.transfer(10,'shelter')
#print(transfer)
balance1 = f.get_balance()
print(balance1)
print(f)
chart = create_spend_chart([f,s])
print(chart)
