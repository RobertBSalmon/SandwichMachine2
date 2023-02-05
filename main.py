import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier

def main():
    ###  write the rest of the codes ###
    print('test')
    choice = ""
    """Loops until off command is given, wherein program terminates."""
    while choice != 'off':
        choice = input("What would you like? (small/ medium/ large/ off/ report): ")
        choice = choice.lower()  ##Ensures choice can be read no matter how the user typed it
        while choice != "small" and choice != "large" and choice != "medium" and choice != "off" and choice != "report":
            choice = input("Error: Must choose (small/ medium/ large/ off/ report): ")
        if choice == 'off':
            continue
        elif choice == 'report':
            print('Bread:  ' + str(resources['bread']) + ' slice(s)')
            print('Ham:    ' + str(resources['ham']) + ' slice(s)')
            print('Cheese: ' + str(resources['cheese']) + ' ounce(s)')
        elif sandwich_maker_instance.check_resources(data.recipes[choice]['ingredients']):
            print("Please insert $" + str(recipes[choice]['cost']) + " in coins.")
            payment = cashier_instance.process_coins("")
            print("$" + str(payment) + " Entered...")
            if cashier_instance.transaction_result("", payment, recipes[choice]['cost']):
                sandwich_maker_instance.make_sandwich(choice, recipes[choice]["ingredients"])

if __name__=="__main__":
    main()
