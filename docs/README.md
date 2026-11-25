# Geometric Lib — документация

## Общее описание

Библиотека на Python для площади и периметра фигур:  
круг, квадрат, прямоугольник, треугольник.

## Функции

### Круг (`circle.py`)

- `area(r)` — площадь, `πr²`
- `perimeter(r)` — длина окружности, `2πr`

```python
from circle import area, perimeter
area(5)
perimeter(5)
```

### Квадрат (`square.py`)

- `area(a)` — `a²`
- `perimeter(a)` — `4a`

```python
from square import area, perimeter
area(4)
perimeter(4)
```

### Прямоугольник (`rectangle.py`)

- `area(a, b)` — `a * b`
- `perimeter(a, b)` — ожидаем `2*(a+b)`

```python
from rectangle import area, perimeter
area(10, 5)
perimeter(10, 5)
```

### Треугольник (`triangle.py`)

- `area(a, b, c)` — площадь по трём сторонам (Герону)
- `perimeter(a, b, c)` — `a+b+c`

```python
from triangle import area, perimeter
area(3, 4, 5)
perimeter(3, 4, 5)
```

## Тесты (ЛР №4)

Файлы в папке `tests/`: `test_circle.py`, `test_square.py`, `test_rectangle.py`, `test_triangle.py`  
План тестирования: `docs/TEST_PLAN.md`

Запуск из корня `geometric_lib`:

```bash
python -m unittest discover tests -v
```

## История изменений

| Хеш | Описание |
|-----|----------|
| `8ba9aeb3cea847b63a91ac378a2a6db758682460` | L-03: Circle and square added |
| `d078c8d9ee6155f3cb0e577d28d337b791de28e2` | L-03: Docs added |
| `5d78d814a2a60c667c73595ce1fd1d4699d901fe` | add circle fuction notation |
| `39b2f2f843564c8996bae8f6dfa564684d8fad18` | add square fuction notation |
| `673ca00614d31b8030fe3b82b4b0718da37a8658` | update documentation |
| — | added lab work 4 |
