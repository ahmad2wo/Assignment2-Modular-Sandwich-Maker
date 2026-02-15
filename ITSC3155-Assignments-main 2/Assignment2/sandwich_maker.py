class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount_needed in ingredients.items():
            amount_have = self.machine_resources.get(item, 0)
            if amount_have < amount_needed:
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the ingredients and make the sandwich."""
        for item, amount_needed in order_ingredients.items():
            self.machine_resources[item] -= amount_needed
        print(f"Here is your {sandwich_size} sandwich. Enjoy!")
