# Pattern Builder (Строитель на Python)
![image](https://github.com/dan9Protasenia/Python_Design_Patterns/assets/100715839/b2d21fe9-20ab-476b-aa36-23fc53125b02)

Шаблонный метод (Pattern Builder) - это порождающий шаблон проектирования, который позволяет создавать объекты различных конфигураций, используя один и тот же процесс строительства. Этот шаблон отделяет конструирование сложного объекта от его представления, что позволяет одному и тому же процессу конструирования создавать различные представления объекта.

<details>
<summary>🔍 Признаки применения паттерна</summary>
Строителя можно узнать в классе, который имеет один создающий метод и несколько методов настройки создаваемого продукта. Обычно, методы настройки вызывают для удобства цепочкой (например, someBuilder.setValueA(1).setValueB(2).create()).
</details>

## Пример на Python

Допустим, у нас есть класс `House`, который мы хотим строить. У дома может быть различное количество этажей, окон и дверей. Давайте создадим классы для строительства дома и конкретные реализации строителей:

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

## Заключение

Шаблон Builder позволяет нам создавать сложные объекты с различными конфигурациями, не загромождая конструкторы классов множеством параметров. Он способствует более чистому и управляемому коду.
```
