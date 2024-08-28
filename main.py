class Store: # инициация класса, где имя и адрес магазина - это хард атрибуты, а ассортимент задается через списоки
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {} # потому что список, создаваемый функциями

    def add_item(self, item_name, price):
        # добавление товара в ассортимент/список
        self.items[item_name] = price

    def remove_item(self, item_name):
        # удаление товара из ассортимента/списка
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар {item_name} не найден в магазинe.")

    def get_price(self, item_name):
        # получение цены товара по его названию. Возвращает None, если товар отсутствует
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        # обновление цены товара
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар {item_name} не найден в магазине.")

# ввод инфо по магазинам
stores = {}

def create_store():
    name = input("Введите название магазина: ")
    address = input("Введите адрес магазина: ")
    stores[name] = Store(name, address)
    print(f"Магазин '{name}' создан.")

def add_item_to_store():
    store_name = input("Введите название магазина: ")
    if store_name in stores:
        item_name = input("Введите название товара: ")
        price = float(input("Введите цену товара: "))
        stores[store_name].add_item(item_name, price)
        print(f"Товар '{item_name}' добавлен в магазин '{store_name}' с ценой {price}.")
    else:
        print(f"Магазин '{store_name}' не найден.")

def update_item_price():
    store_name = input("Введите название магазина: ")
    if store_name in stores:
        item_name = input("Введите название товара: ")
        new_price = float(input("Введите новую цену товара: "))
        stores[store_name].update_price(item_name, new_price)
        print(f"Цена товара '{item_name}' в магазине '{store_name}' обновлена до {new_price}.")
    else:
        print(f"Магазин '{store_name}' не найден.")

def remove_item_from_store():
    store_name = input("Введите название магазина: ")
    if store_name in stores:
        item_name = input("Введите название товара: ")
        stores[store_name].remove_item(item_name)
        print(f"Товар '{item_name}' удалён из магазина '{store_name}'.")
    else:
        print(f"Магазин '{store_name}' не найден.")

def list_store_items():
    store_name = input("Введите название магазина: ")
    if store_name in stores:
        items = stores[store_name].list_items()
        if items:
            for item_name, price in items.items():
                print(f"{item_name}: {price}")
        else:
            print(f"В магазине '{store_name}' нет товаров.")
    else:
        print(f"Магазин '{store_name}' не найден.")

def list_item_prices_across_stores():
    item_name = input("Введите название товара: ")
    found = False
    for store in stores.values():
        price = store.get_price(item_name)
        if price is not None:
            found = True
            print(f"Магазин '{store.name}', адрес: {store.address} — {item_name}: {price}")
    if not found:
        print(f"Товар '{item_name}' не найден ни в одном магазине.")

def menu():
    while True:
        print("\nМеню:")
        print("1. Создать магазин")
        print("2. Добавить товар в магазин")
        print("3. Обновить цену товара в магазине")
        print("4. Удалить товар из магазина")
        print("5. Посмотреть все товары и их цены в магазине")
        print("6. Посмотреть цену товара по всем магазинам")
        print("7. Выйти")

        choice = input("Выберите действие (1-7): ")

        if choice == '1':
            create_store()
        elif choice == '2':
            add_item_to_store()
        elif choice == '3':
            update_item_price()
        elif choice == '4':
            remove_item_from_store()
        elif choice == '5':
            list_store_items()
        elif choice == '6':
            list_item_prices_across_stores()
        elif choice == '7':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 7.")

menu()
