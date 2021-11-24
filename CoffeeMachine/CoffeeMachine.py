# Этап 1. Общие сообщения.
print("Starting to make a coffe\nGrinfing coffe beans\nBoiling water\nMixing boiled water with crushed coffee beans\nPouring coffee into the cup\nCoffee is ready!")

# Этап 2. Ввод данных и расчет количества ингредиентов.
water = 200
milk = 50
coffee_beans = 15
amount_of_coffee = input("Write how may cups of coffe you will need:")
print("For", amount_of_coffee, "cups of coffe you will need:\n", int(amount_of_coffee) * water, "ml of water\n", int(amount_of_coffee) * milk, "ml of milk\n", int(amount_of_coffee) * coffee_beans, "g of coffee beans" )

# Этап 3. Проверка доступности воды, молока и кофейных зерен.
num_of_water = int(input("Write how many ml of water the coffee machine has: > "))
num_of_milk = int(input("Write how many ml of milk the coffee machine has: > "))
num_of_coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has: > "))
amount_of_coffee = int(input("Write how many cups of coffee you will need: > "))
amount_of_water = amount_of_coffee * water
amount_of_milk = amount_of_coffee * milk
amount_of_beans = amount_of_coffee * coffee_beans
if num_of_water >= amount_of_water and num_of_milk >= amount_of_milk and num_of_coffee_beans >= amount_of_beans:
    print("Yes, I can make that amount of coffee")
n = (num_of_water + num_of_milk + num_of_coffee_beans) // (amount_of_water + amount_of_milk + amount_of_beans)
if n > amount_of_coffee:
    print("Yes, I can make that amount of coffee (and even", n - amount_of_coffee, "more than that)")
if num_of_water < amount_of_water and num_of_milk < amount_of_milk and num_of_coffee_beans < amount_of_beans:
    n = (num_of_water + num_of_milk + num_of_coffee_beans) // (water + milk + coffee_beans)
    print("No, I can make only", n, "cups of coffee")

# Этап 4. Ограничение запасов ресурсов кофемашины и расчёт выручки за продажу, включая различные виды кофе.
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550
coffee_list = [1, 2, 3]
action_list = ["buy", "fill", "take"]
print("The coffee machine has:\n", water, "of water\n", milk, "of milk\n", coffee_beans, "of coffee beans")
print(disposable_cups, "of disposable cups\n", money, "of money")
action = input("Write action (buy, fill, take):\n > ")
if action == action_list[0]:
    coffee_class = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n > "))
    if coffee_class == coffee_list[0]:
        water1 = 250
        coffee_beans1 = 16
        disposable_cups1 = 1
        money1 = 4
        print("The coffee machine has:\n", water - water1, "of water")
        print(coffee_beans - coffee_beans1, "of coffee beans")
        print(disposable_cups - disposable_cups1, "of disposable cups\n", money - money1, "of money")
    if coffee_class == coffee_list[1]:
        water2 = 350
        milk2 = 75
        coffee_beans2 = 20
        disposable_cups2 = 1
        money2 = 7
        print("The coffee machine has:\n", water - water2, "of water\n", milk - milk2, "of milk")
        print(coffee_beans - coffee_beans2, "of coffee beans")
        print(disposable_cups - disposable_cups2, "of disposable cups\n", money - money2, "of money")
    if coffee_class == coffee_list[2]:
        water3 = 200
        milk3 = 100
        coffee_beans3 = 12
        disposable_cups3 = 1
        money3 = 6
        print("The coffee machine has:\n", water - water3, "of water\n", milk - milk3, "of milk")
        print(coffee_beans - coffee_beans3, "of coffee beans")
        print(disposable_cups - disposable_cups3, "of disposable cups\n", money - money3, "of money")
if action == action_list[1]:
    water_add = int(input("Write how many ml of water you want to add:\n > "))
    milk_add = int(input("Write how many ml of milk you want to add:\n > "))
    coffee_beans_add = int(input("Write how many grams of coffee beans you want to add:\n > "))
    disposable_cups_add = int(input("Write how many disposable coffee cups you want to add:\n > "))
    print("The coffee machine has:\n", water + water_add, "of water\n", milk + milk_add, "of milk")
    print(coffee_beans + coffee_beans_add, "of coffee beans")
    print(disposable_cups + disposable_cups_add, "of disposable cups\n", money, "of money")
if action == action_list[2]:
    print("I gave you", money)
    print("The coffee machine has:\n", water, "of water\n", milk, "of milk")
    print(coffee_beans, "of coffee beans\n",disposable_cups, "of disposable cups\n", money - money, "of money")