class Snack:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability


class CanteenInventory:
    def __init__(self):
        self.snacks = []
        self.sales_records = []

    def add_snack(self, snack):
        self.snacks.append(snack)
        print("Snack added successfully!")

    def remove_snack(self, snack_id):
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                self.snacks.remove(snack)
                print("Snack removed successfully!")
                return
        print("Snack not found!")

    def update_availability(self, snack_id, availability):
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                snack.availability = availability
                print("Snack availability updated successfully!")
                return
        print("Snack not found!")

    def sell_snack(self, snack_id):
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                if snack.availability == "yes":
                    snack.availability = "no"
                    self.sales_records.append(snack)
                    print("Snack sold successfully!")
                    return
                else:
                    print("Snack is already sold!")
                    return
        print("Snack not found!")

    def generate_sales_report(self):
        if len(self.sales_records) == 0:
            print("No snacks have been sold.")
            return

        print("Sales Report:")
        print("Snack ID\tName\tPrice")
        print("---------------------------------")
        for snack in self.sales_records:
            print(f"{snack.snack_id}\t\t{snack.name}\t{snack.price}")

    def run(self):
        while True:
            print("\n==== Canteen Inventory Management ====")
            print("1. Add Snack")
            print("2. Remove Snack")
            print("3. Update Snack Availability")
            print("4. Sell Snack")
            print("5. Generate Sales Report")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                snack_id = input("Enter Snack ID: ")
                name = input("Enter Snack Name: ")
                price = input("Enter Snack Price: ")
                availability = input("Is the Snack available? (yes/no): ")

                snack = Snack(snack_id, name, price, availability)
                self.add_snack(snack)

            elif choice == "2":
                snack_id = input("Enter Snack ID to remove: ")
                self.remove_snack(snack_id)

            elif choice == "3":
                snack_id = input("Enter Snack ID to update availability: ")
                availability = input("Enter new availability (yes/no): ")
                self.update_availability(snack_id, availability)

            elif choice == "4":
                snack_id = input("Enter Snack ID to sell: ")
                self.sell_snack(snack_id)

            elif choice == "5":
                self.generate_sales_report()

            elif choice == "6":
                print("Exiting the application...")
                break

            else:
                print("Invalid choice! Please try again.")


# Create and run the CanteenInventory application
inventory_app = CanteenInventory()
inventory_app.run()