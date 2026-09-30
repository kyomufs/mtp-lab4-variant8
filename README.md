# Лабораторная работа №4

Самодуров Матвей Николаевич, группа 221341, вариант 8, лабораторная №4.

## Задания варианта

**Средняя сложность:**

- №4 — факториал через `reduce` (`lab4/basics.py`)
- №8 — декоратор замера времени работы функции (`lab4/timing.py`)
- №10 — применение нескольких функций к списку через `map`
  (`lab4/transform.py`)

**Повышенная сложность:**

- №1 — композиция функций (`lab4/composition.py`)
- №8 — фильтрация и преобразование CSV через `map`/`filter`
  (`lab4/csvproc.py`)

## Клонирование

```bash
git clone https://github.com/kyomufs/mtp-lab4-variant8.git
```

## Запуск

```bash
uv run python -m lab4
```

## Проверки

```bash
uv run python -m unittest discover -s tests -v
uv run --with flake8 flake8 lab4 tests
```

Подробное описание выполнения — в `docs/report.md`.
