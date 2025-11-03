# Інвентаризація продуктів
# Створюємо словник, де ключ — назва продукту, значення — кількість на складі

inventory = {
    "яблука": 10,
    "банани": 3,
    "груші": 7,
    "апельсини": 2,
    "виноград": 12
}

def update_inventory(product, amount):
    """
    Оновлює кількість товарів на складі.
    Якщо товар вже є — додає або віднімає кількість.
    Якщо товару немає — додає новий запис.
    """
    if product in inventory:
        inventory[product] += amount
        if inventory[product] < 0:
            inventory[product] = 0
    else:
        inventory[product] = amount

update_inventory("яблука", -7)   # продали 7 яблук
update_inventory("виноград", 3)    # додали 3 винограда
update_inventory("абрикос", 8)      # додали новий продукт

print("Оновлений склад:")
for product, count in inventory.items():
    print(f"{product}: {count}")

low_stock = [product for product, count in inventory.items() if count < 5]

print("\nПродукти, яких залишилось менше 5:")
print(low_stock)
