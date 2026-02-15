class Cashier:
    def __init__(self):
        self.money = 0.0

    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickels = int(input("how many nickels?: "))
        pennies = int(input("how many pennies?: "))

        total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        return round(total, 2)

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False

        change = round(coins - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")

        self.money = round(self.money + cost, 2)
        return True
