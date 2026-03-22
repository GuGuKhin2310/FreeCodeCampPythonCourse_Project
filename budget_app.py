class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })
    
    def withdraw(self,amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
        

    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self,amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
            total = f"Total: {self.get_balance()}"
        return title + items + total

def create_spend_chart(categories):
    spent = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)
    total_spent = sum(spent)

    percentages = []
    for amount in spent:
        percent = int((amount / total_spent) * 100)
        percentages.append(percent - percent % 10)

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(c.name) for c in categories)

    for i in range(max_len):
        chart += "     "
        for c in categories:
            if i < len(c.name):
                chart += c.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")

food = Category('Food')
food.deposit(900, 'deposit')
food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

print(create_spend_chart([food, clothing]))
