# Geometric Lib — документация

## Общее описание решения

`geometric_lib` — небольшая Python-библиотека для расчёта площади и периметра простых геометрических фигур.  
Сейчас реализованы модули для **круга** (`circle.py`) и **квадрата** (`square.py`). Каждый модуль предоставляет две функции: `area` и `perimeter`.

## Описание функций

### `circle.area(r)`

Принимает радиус круга `r`, возвращает площадь: \(S = \pi r^2\).

```python
from circle import area
print(area(5))  # 78.53981633974483
```

### `circle.perimeter(r)`

Принимает радиус круга `r`, возвращает длину окружности, то есть периметр: \(P = 2\pi r\).

```python
from circle import perimeter
print(perimeter(5))  # 31.41592653589793
```

### `square.area(a)`

Принимает сторону квадрата `a`, возвращает площадь: \(S = a^2\).

```python
from square import area
print(area(4))  # 16
```

### `square.perimeter(a)`

Принимает сторону квадрата `a`, возвращает периметр: \(P = 4a\).

```python
from square import perimeter
print(perimeter(4))  # 16
```

## История изменений

| Хеш | Описание |
|-----|----------|
| `8ba9aeb3cea847b63a91ac378a2a6db758682460` | L-03: Circle and square added |
| `d078c8d9ee6155f3cb0e577d28d337b791de28e2` | L-03: Docs added |
| `5d78d814a2a60c667c73595ce1fd1d4699d901fe` | add circle fuction notation |
| `39b2f2f843564c8996bae8f6dfa564684d8fad18` | add square fuction notation |
| — | update documentation |
