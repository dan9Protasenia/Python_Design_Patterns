# Factory Method (Фабричный Метод в Python)
![image](https://github.com/dan9Protasenia/Python_Design_Patterns/assets/100715839/13dd9d73-c4e4-4983-b3da-81a053458030)

Фабричный метод - это порождающий шаблон проектирования, который предоставляет интерфейс для создания объектов в суперклассе, но позволяет подклассам изменять тип создаваемых объектов.

## Структура

1. **Продукт (`Product`)**: Объявляет интерфейс объектов, которые создаются с помощью фабричного метода.
2. **Конкретные Продукты (`Concrete Products`)**: Реализуют интерфейс продукта.
3. **Создатель (`Creator`)**: Объявляет фабричный метод, который возвращает объект типа Product.
4. **Конкретные Создатели (`Concrete Creators`)**: Переопределяют реализацию фабричного метода для создания конкретных продуктов.

<details>
<summary>🔍 Признаки применения паттерна</summary>
Фабричный метод можно определить по создающим методам, которые возвращают объекты продуктов через абстрактные типы или интерфейсы. Это позволяет переопределять типы создаваемых продуктов в подклассах.
</details>

## Схема
![изображение](https://github.com/dan9Protasenia/Python_Design_Patterns/assets/100715839/6114ae54-8f3e-41de-93cc-e414975c4ef1)


## Пример Кода

```python
class Product:
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "Результат операции ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self):
        return "Результат операции ConcreteProductB"

class Creator:
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: тот же код создателя работает с {product.operation()}"
        return result

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()
```

---
Фабричный метод задаёт метод, который следует использовать вместо вызова оператора new для создания объектов-продуктов. Подклассы могут переопределить этот метод, чтобы изменять тип создаваемых продуктов.
