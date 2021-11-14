# Этап 1. Общие сообщения
print("Starting to make a coffe\nGrinfing coffe beans\nBoiling water\nMixing boiled water with crushed coffee beans\nPouring coffee into the cup\nCoffee is ready!")
# Этап 2. Ввод данных и расчет количества ингредиентов
water = 200
milk = 50
coffe_beans = 15
amount_of_coffee = input("Write how may cups of coffe you will need:")
print("For", amount_of_coffee, "cups of coffe you will need:\n", int(amount_of_coffee) * water, "ml of water\n", int(amount_of_coffee) * milk, "ml of milk\n", int(amount_of_coffee) * coffe_beans, "g of coffe beans" )
