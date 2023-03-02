import math
def start_shopping():
    exit = True
    cart = list()
    item_prices = list()
    item_count = list()
    while exit != False:
        print()
        menu = int(input("Please select one of the following by inputting the number: \n0. Quit \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Payment \n"))
        print()
        if menu == 0:
            exit = False
        elif menu == 1:
            while True:
                item = input("Please input an item to add to your cart.\n")
                price = float(input(f"What is the price of {item}? "))
                count = int(input("How many of the item would you like to add? "))
                if count > 0:
                    item_count.append(count)
                cart.append(item)
                item_prices.append(price)
                item_total = count * price
                print(f"{count} {item} added for ${item_total:.2f}\n")
                add_another = int(input("Add another item? \n1. Yes\n2. No\n"))
                if add_another == 1:
                    continue
                else:
                    break
        elif menu == 2:
            print("Your cart contains:")
            for item_index, cart_item in enumerate(cart):
                for price_index, item_price in enumerate(item_prices):
                    for count_index, count in enumerate(item_count):
                        if item_index == price_index == count_index:
                            item_index += 1
                            print(f"{item_index}. {cart_item} ${item_price:.2f} x{count}")
                            item_index -= 1
            print()
        elif menu == 3:
            while True:
                print("Choose an item to remove:")
                print("0. Back to main menu \n")
                for item_index, cart_item in enumerate(cart):
                    item_index += 1
                    print(f"{item_index}. {cart_item}")
                remove = int(input(''))
                if remove == 0:
                    break
                remove -= 1
                if remove > len(cart):
                    print("That number is too big")
                else:
                    del cart[remove]
                    del item_prices[remove]
                    del item_count[remove]
                    remove += 1
                    print(f"Item number {remove} removed")
        elif menu == 4:
            cart_total = float(0)
            item_total = float(0)
            for price_index, item_price in enumerate(item_prices):
                for count_index, count in enumerate(item_count):
                    if count_index == price_index:
                        item_total = item_price * count
                        cart_total += item_total
            print(f"\nThe total of the items in your cart is ${cart_total:.2f}. \n")
        elif menu == 5:
            tax = float(input("What is the sales tax %? "))
            tax2 = tax * 0.01
            subtotal = float(0)
            print("These are the items in your cart:")
            for item_index, cart_item in enumerate(cart):
                for price_index, item_price in enumerate(item_prices):
                    for count_index, count in enumerate(item_count):
                        if item_index == price_index == count_index:
                            item_index += 1
                            print(f"{item_index}. {cart_item} ${item_price:.2f} x{count}")
                            item_index -= 1
            for price_index, item_price in enumerate(item_prices):
                for count_index, count in enumerate(item_count):
                    if count_index == price_index:
                        item_total = item_price * count
                        subtotal += item_total
            print(f"\nYour subtotal is ${subtotal:.2f}\n")
            stax = subtotal * tax2
            print(f"Your sales tax is ${stax:.2f}")
            total = stax + subtotal
            print(f"Your total is ${total:.2f}\n")
            if total == 0:
                exit = False
            while total > 0:
                payment = float(input("How much is the payment amount? "))
                change = payment - total
                print()
                if change < 0:
                    change = abs(change)
                    print(f"Not enough money, ${change:.2f} is still owed.")
                    total -= change
                else:
                    print(f"Your change is ${change:.2f} thank you for shopping with us today.")
                    total -= change
                    exit = False
                    break
        else:
            print("That is not an option, try again. \n")
    while True:
        shop_again = int(input("Would you like to shop again or quit?\n1. Shop Again\n2. Quit\n"))
        if shop_again == 1:
            start_shopping()
        elif shop_again == 2:
            print("Have a nice day, goodbye.")
            break
        else:
            print("That is not an option, try again.\n")
if __name__ == "__main__":
    start_shopping()
