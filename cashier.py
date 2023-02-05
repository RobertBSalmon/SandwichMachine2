class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the calculated value of the coins inserted"""
        largedollar = input("How many large dollars?: ")
        halfdollar = input("How many half dollars?: ")
        quarter = input("How many quarters?: ")
        nickles = input("How many nickles?: ")
        return float(largedollar) + (0.5 * float(halfdollar)) + (0.25 * float(quarter)) + (0.05 * float(nickles))

    def transaction_result(self, coins, cost):
        """Checks if the coins given are enough for the cost"""
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False

        print("Payment Accepted.")
        """Only prints out what change is owed if there is any change"""
        if coins > cost:
            print("Here is $" + str(round(coins - cost, 2)) + " in change. ")

        return True
