class MenuItem:
    def __init__(self, name, price, descuento=0):
        self._name = name
        self._price = price
        self._descuento = descuento

    def compute_price(self):
        return self._price - (self._price * self._descuento / 100)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_descuento(self):
        return self._descuento

    def set_descuento(self, descuento):
        self._descuento = descuento

class Beverage(MenuItem):
    def __init__(self, name, price, size, descuento=0):
        super().__init__(name, price, descuento)
        self._size = size

    def get_size(self):
        return self._size

    def set_size(self, size):
        self._size = size

class Appetizer(MenuItem):
    def __init__(self, name, price, vegetarian=False, descuento=0):
        super().__init__(name, price, descuento)
        self._vegetarian = vegetarian

    def get_vegetarian(self):
        return self._vegetarian

    def set_vegetarian(self, vegetarian):
        self._vegetarian = vegetarian

class MainCourse(MenuItem):
    def __init__(self, name, price, country_food, descuento=0):
        super().__init__(name, price, descuento)
        self._country_food = country_food

    def get_country_food(self):
        return self._country_food

    def set_country_food(self, country_food):
        self._country_food = country_food

class Order:
    def __init__(self):
        self.items = []

    def append_item(self, item):
        self.items.append(item)

    def calculate_total_price(self):
        total = sum(item.compute_price() for item in self.items)

        has_main_course = any(isinstance(item, MainCourse) for item in self.items)
        if has_main_course:
            for item in self.items:
                if isinstance(item, Beverage):
                    total -= item.compute_price() * 0.10
        return total

class Payment:
    def __init__(self):
        pass

    def pagar(self, monto):
        raise NotImplementedError("Subclases deben implementar pagar()");

class Tarjeta(Payment):
    def __init__(self, numero, cvv):
        super().__init__()
        self.numero = numero
        self.cvv = cvv

    def pagar(self, monto):
        print(f"Pagando {monto} con tarjeta {self.numero[-4:]}")

class Efectivo(Payment):
    def __init__(self, monto_entregado):
        super().__init__()
        self.monto_entregado = monto_entregado

    def pagar(self, monto):
        if self.monto_entregado >= monto:
            print(f"Pago realizado en efectivo. Cambio: {self.monto_entregado - monto}")
        else:
            print(f"Fondos insuficientes. Faltan {monto - self.monto_entregado} para completar el pago.")

#Ejemplo de uso:
menu = [
    Beverage("Coca Cola", 2.5, "Mediano", descuento=5),
    Beverage("Jugo Natural", 3.0, "Grande", descuento=10),
    MainCourse("Pizza Napolitana", 8.5, "Italiana", descuento=10)
]

pedido = Order()
pedido.append_item(menu[0])
pedido.append_item(menu[1])
pedido.append_item(menu[2])

print(f"Total del pedido con descuentos: ${pedido.calculate_total_price():.2f}")

pago = Tarjeta("1234567890123456", 123)
pago.pagar(pedido.calculate_total_price())