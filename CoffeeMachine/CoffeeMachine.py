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