import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True

    while is_on:
        choice = input("What would you like? (small/medium/large): ").lower().strip()

        if choice == "off":
            is_on = False

        elif choice == "report":
            print("\n--- REPORT ---")
            for item, amount in resources.items():
                print(f"{item}: {amount}")
            print(f"Money: ${cashier_instance.money}")
            print("-------------\n")

        elif choice in recipes:
            order = recipes[choice]
            ingredients = order["ingredients"]
            cost = order["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)

        else:
            print("Invalid option. Type small, medium, large, report, or off.")


if __name__ == "__main__":
    main()
