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
