# Python Design Patterns

 - [Pattern Builder](#pattern-builder-строитель-на-python)
 - [Factory Method](#factory-method-фабричный-метод-в-python)
 - [Prototype in Python](#prototype-in-python-прототип-в-python)
 - [Singleton в Python](#singleton-в-python-одиночка)


# Pattern Builder (Строитель на Python)
![image](https://github.com/dan9Protasenia/Python_Design_Patterns/assets/100715839/b2d21fe9-20ab-476b-aa36-23fc53125b02)

Шаблонный метод (Pattern Builder) - это порождающий шаблон проектирования, который позволяет создавать объекты различных конфигураций, используя один и тот же процесс строительства. Этот шаблон отделяет конструирование сложного объекта от его представления, что позволяет одному и тому же процессу конструирования создавать различные представления объекта.

<details>
<summary>🔍 Признаки применения паттерна</summary>
 
```
Строителя можно узнать в классе, который имеет один создающий метод и
несколько методов настройки создаваемого продукта. Обычно, методы настройки
вызывают для удобства цепочкой (например, someBuilder.setValueA(1).setValueB(2).create()).
 ```
</details>

### Схема
![изображение](https://github.com/dan9Protasenia/Python_Design_Patterns/assets/100715839/e965f39b-b45a-46dd-a674-7cf51b39cc95)

### Пример на Python

Допустим, у нас есть класс `House`, который мы хотим строить. У дома может быть различное количество этажей, окон и дверей. Давайте создадим классы для строительства дома и конкретные реализации строителей:


<details>
<summary>код</summary>
 
```python
class House:
    def __init__(self):
        self.floor = None
        self.windows = None
        self.doors = None

    def __str__(self):
        return f"Дом с {self.floor} этажами, {self.windows} окнами и {self.doors} дверьми"


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_floor(self):
        pass

    def build_windows(self):
        pass

    def build_doors(self):
        pass

    def get_house(self):
        return self.house


class OneFloorHouseBuilder(HouseBuilder):
    def build_floor(self):
        self.house.floor = 1

    def build_windows(self):
        self.house.windows = 2

    def build_doors(self):
        self.house.doors = 1


class TwoFloorHouseBuilder(HouseBuilder):
    def build_floor(self):
        self.house.floor = 2

    def build_windows(self):
        self.house.windows = 4

    def build_doors(self):
        self.house.doors = 2
```

Теперь создадим класс `HouseDirector`, который будет использовать строителей для построения дома:

```python
class HouseDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_floor()
        self.builder.build_windows()
        self.builder.build_doors()

    def get_house(self):
        return self.builder.get_house()
```

Теперь можем создать различные типы домов, используя разные строителей:

```python
builder = OneFloorHouseBuilder()
director = HouseDirector(builder)
director.construct_house()
house = director.get_house()
print(house)

builder = TwoFloorHouseBuilder()
director = HouseDirector(builder)
director.construct_house()
house = director.get_house()
print(house)
```

Этот код создаст два разных дома: один с одним этажом и другой с двумя этажами.

</details>


## Заключение

Шаблон Builder позволяет нам создавать сложные объекты с различными конфигурациями, не загромождая конструкторы классов множеством параметров. Он способствует более чистому и управляемому коду.


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
 
 ```
Фабричный метод можно определить по создающим методам, которые возвращают объекты
продуктов через абстрактные типы или интерфейсы. Это позволяет переопределять типы
создаваемых продуктов в подклассах.
```
</details>

## Схема
![изображение](https://github.com/dan9Protasenia/Python_Design_Patterns/assets/100715839/6114ae54-8f3e-41de-93cc-e414975c4ef1)

<details>
<summary>Пример Кода</summary>

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
</details>

---
Фабричный метод задаёт метод, который следует использовать вместо вызова оператора new для создания объектов-продуктов. Подклассы могут переопределить этот метод, чтобы изменять тип создаваемых продуктов.

# Prototype in Python (Прототип в Python)
![image](https://github.com/dan9Protasenia/Python_Design_Patterns/assets/100715839/c3efdfe3-de01-405a-8bce-1647d992e438)

Прототип - это порождающий шаблон проектирования, который позволяет копировать объекты, не вдаваясь в подробности их реализации.

## Основные Понятия

1. **Прототип (`Prototype`)**: Определяет интерфейс для клонирования самого себя.
2. **Конкретный Прототип (`Concrete Prototype`)**: Реализует операцию клонирования.
3. **Клиент (`Client`)**: Создаёт новый объект, обращаясь к прототипу с запросом на клонирование.

<details>
<summary>🔍 Признаки применения паттерна</summary>

 ```
Прототип реализован в базовой библиотеке Python посредством модуля copy.
  
Прототип легко определяется в коде по наличию методов "clone, copy" и прочих.
```
</details>


### Схема
![изображение](https://github.com/dan9Protasenia/Python_Design_Patterns/assets/100715839/afd55179-5138-45c9-9556-3b33cd2dda4c)

<details>
<summary>Пример Кода</summary>

```python
import copy

class Prototype:
    def clone(self):
        pass

class ConcretePrototype(Prototype):
    def __init__(self, field):
        self.field = field

    def clone(self):
        return copy.deepcopy(self)

# Использование
original = ConcretePrototype("ABC")
clone = original.clone()
```
</details>

## Заключение
Все классы—Прототипы имеют общий интерфейс. Поэтому вы можете копировать объекты, не обращая внимания на их конкретные типы и всегда быть уверены, что получите точную копию. Клонирование совершается самим объектом-прототипом, что позволяет ему скопировать значения всех полей, даже приватных.

# Singleton в Python (Одиночка) 
![image](https://github.com/dan9Protasenia/Python_Design_Patterns/assets/100715839/a0f57bf6-8800-45a1-8c70-119eee19811a)

Singleton - это порождающий шаблон проектирования, который гарантирует, что класс имеет только один экземпляр, и предоставляет глобальную точку доступа к этому экземпляру.

## 

Одиночка имеет такие же преимущества и недостатки, что и глобальные переменные. Его невероятно удобно использовать, но он нарушает модульность вашего кода.

Вы не сможете просто взять и использовать класс, зависящий от одиночки в другой программе. Для этого придётся эмулировать присутствие одиночки и там. Чаще всего эта проблема проявляется при написании юнит-тестов.

## Ключевые Концепции

- **Одиночный экземпляр**: Гарантирует наличие только одного экземпляра класса.
- **Глобальная точка доступа**: Удобный способ доступа к единственному экземпляру.


<details>
<summary>🔍 Признаки применения паттерна</summary>

 ```
Многие программисты считают Одиночку антипаттерном, поэтому его всё реже и реже можно встретить в Python-коде.

Одиночку можно определить по статическому создающему методу, который возвращает один и тот же объект.
```
</details>

### Схема
![изображение](https://github.com/dan9Protasenia/Python_Design_Patterns/assets/100715839/31c3c2b9-20e3-441d-9e9b-52c68743e91e)

<details>
<summary>Пример Кода</summary>

```python
class SingletonMeta(type):
    """
    В Python класс Одиночка можно реализовать по-разному. Возможные способы
    включают себя базовый класс, декоратор, метакласс. Мы воспользуемся
    метаклассом, поскольку он лучше всего подходит для этой цели.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Данная реализация не учитывает возможное изменение передаваемых
        аргументов в `__init__`.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Наконец, любой одиночка должен содержать некоторую бизнес-логику,
        которая может быть выполнена на его экземпляре.
        """

        # ...


if __name__ == "__main__":
    # Клиентский код.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
```
</details>

## Применение

Используется для управления доступом к ресурсу, который должен быть представлен в единственном экземпляре, например, к базе данных или файловой системе.
