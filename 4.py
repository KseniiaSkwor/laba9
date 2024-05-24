# Открываем файл для чтения
with open("93.txt", "r") as file:
    lines = file.readlines()

total_cost = 0
shopping_list = []

# Обработка данных из файла
for line in lines:
    if line.strip():  # Проверяем, что строка не пустая
        product, quantity, price = line.strip().split(",")
        cost = int(quantity) * int(price)
        total_cost += cost
        shopping_list.append(f"{product} - {quantity} шт. за {price} руб.")

# Вывод данных
print("Нужно купить:")
for item in shopping_list:
    print(item)
print(f"Итоговая сумма: {total_cost} руб.")