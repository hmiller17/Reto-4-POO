# Reto 4
Para esta nueva versión del menú de restaurante se implementó el encapsulamiento privado en los atributos **_name, _price, _descuento, _size y _vegetarian**, además
se implementaron **getters** y **setters** para acceder y modificar los atributos encapsulados, tambien se agregó las clases de **payment** y subclases de 
**tarjeta** y **efectivo** para realizar pagos con tarjeta siguiendo el ejemplo en el repositorio de la clase.

## Explicación
Se crea la clase principal **MenuItem** con los atributos encapsulados de **_name, _price y _descuento** por medio de un constructor, luego se creo el método 
**compute_price** que realiza el descuento final a la cuenta, posteriormente se agregaron los **getters y setters** de las clases y asi crear la subclase...
![image](https://github.com/user-attachments/assets/de7c0aa8-25bd-4a92-99d3-574f82c94d1f)

## Beverage 
Esta representa las bebidas, el cual tiene el atributo privado **_size** para determinar el tamaño de la bebida y almacenarlo.
![image](https://github.com/user-attachments/assets/e234748a-31e5-49d8-9a01-34af9696643a)

## Appetizer
Esta subclase fue creada para saber si el aperitivo es vegano, este atributo **__vegetarian** tambien es privado.
![image](https://github.com/user-attachments/assets/10cbb639-9902-49f8-8a15-6d2e58cb8d0e)

## MainCourse
Esta subclase tiene el proposito de identificar el país de procedencia del plato indicado.
![image](https://github.com/user-attachments/assets/3b60a677-ad06-4977-9423-f16eb535239b)

## Order
Esta es una clase extra en la que se realiza el pedido con los platos del menú, contiene un atributo **items** el cual almacena el pedido y metodos como 
**append_item** que se usa para agregar los pedidos a la lista y **calculate_total_price**, el cual realiza el calculo del precio total de los items, aplicando un descuento del 10%
en bebidas si el pedido incluye un plato principal.
![image](https://github.com/user-attachments/assets/556b7a07-5d3a-463d-a0b6-11a89bbdc164)

## Payment
Esta es una clase abstracta que se usa para definir un método de pago generico.
![image](https://github.com/user-attachments/assets/9246d979-db89-4f43-9a30-51410ed6719e)

## Tarjeta
Esta subclase indica que el metodo de pago es con tarjeta e imprime el monto y los ultimos 4 digitos de la tarjeta.
![image](https://github.com/user-attachments/assets/5000a363-b536-4908-b7cb-710987405666)

## Efectivo
En esta se realiza la impresión del valor total y se muestra el cambio en efectivo que se deb devolver a traves del método pagar.
![image](https://github.com/user-attachments/assets/a4aa728b-8941-4c27-8686-6fd720c98c2d)
