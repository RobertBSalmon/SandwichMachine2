import data


class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if data.resources["bread"] < ingredients["bread"]:
            print("Sorry there is not enough bread.")
            return False
        elif data.resources["ham"] < ingredients["ham"]:
            print("Sorry there is not enough ham.")
            return False
        elif data.resources["cheese"] < ingredients["cheese"]:
            print("Sorry there is not enough cheese.")
            return False
        else:
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Removes the required ingredients from resources and prints a message when finished."""
        data.resources['bread'] -= order_ingredients["bread"]
        data.resources['ham'] -= order_ingredients["ham"]
        data.resources['cheese'] -= order_ingredients["cheese"]
        print(str(sandwich_size) + " sandwich is ready. Bon appetit!")