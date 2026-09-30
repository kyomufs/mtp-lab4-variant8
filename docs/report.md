# Отчёт по лабораторной работе №4

Самодуров Матвей Николаевич, группа 221341, вариант 8.

Тема: функциональное программирование — `map`/`filter`/`reduce`,
генераторы, декораторы, функции высшего порядка.

## Средняя сложность

- **№4 Факториал через `reduce`** — `lab4/basics.py`:
  `factorial(n)` собирает произведение `1 * 2 * ... * n`
  одним вызовом `functools.reduce(mul, range(1, n + 1), 1)`,
  без единого явного цикла; для `n < 0` поднимается
  `ValueError`. Тест дополнительно проверяет по исходному
  коду, что в функции действительно используется `reduce`.
- **№8 Декоратор замера времени** — `lab4/timing.py`:
  `timer(func)` оборачивает функцию через `functools.wraps`,
  засекает время `time.perf_counter()` до и после вызова и
  сохраняет разницу (в секундах, `float`) в атрибут
  `func.last_duration` обёртки. Атрибут инициализируется
  значением `0.0`, поэтому доступен ещё до первого вызова;
  возвращаемое значение и метаданные (`__name__`, `__doc__`)
  пробрасываются без изменений.
- **№10 Несколько функций к списку через `map`** —
  `lab4/transform.py`: `map_functions(functions, values)`
  для каждой функции строит результат вложенным
  `map(function, values)` и приводит его к `list`;
  явных циклов в теле нет, входные последовательности не
  изменяются (чистая функция). Внешний вид результата —
  список списков, по одному на функцию.

## Повышенная сложность

- **№1 Композиция функций** — `lab4/composition.py`:
  `compose(*functions)` возвращает вызываемый объект,
  применяющий цепочку справа налево:
  `compose(f, g, h)(x) == f(g(h(x)))` — замыкание идёт по
  `reversed(functions)`. `compose()` без аргументов возвращает
  функцию-тождество. Докстринг фиксирует семантику точно;
  тесты проверяют числа, строки и пустую композицию.
- **№8 Фильтрация и преобразование CSV** — `lab4/csvproc.py`:
  `read_rows(path)` читает CSV модулем `csv.DictReader` в
  список `dict[str, str]`; `filter_rows(rows, predicate)`
  отбирает строки через builtin `filter`;
  `average_column(rows, column)` переводит значения через
  `map` и суммирует через `sum`, затем делит на число строк;
  при пустом наборе строк поднимается `ValueError`.
  Реализация демонстративно построена на `map`/`filter`.

## Проверки

Команды выполнялись в корне репозитория; вывод ниже —
реальный stdout команд.

### Демонстрация

```console
$ uv run python -m lab4
Medium tasks
factorial(10) -> 3628800
factorial(-1) -> ValueError: n must be non-negative, got -1
slow_square(7) -> 49
slow_square.last_duration >= 0.01 -> True
map_functions([+1, *2], [1, 2, 3]) -> [[2, 3, 4], [2, 4, 6]]
Advanced tasks
compose(square, inc)(5) -> 36
compose()(42) -> 42
compose(str.upper, str.strip)("  hi  ") -> HI
read_rows -> [{'name': 'alice', 'score': '90'}, {'name': 'bob', 'score': '60'}, {'name': 'carol', 'score': '75'}]
filter(score >= 70) -> ['alice', 'carol']
average_column(score) -> 75.0
```

### Тесты

```console
$ uv run python -m unittest discover -s tests -v
test_base_cases (test_basics.FactorialTests.test_base_cases)
Zero and one factorials are defined as one. ... ok
test_implemented_with_reduce (test_basics.FactorialTests.test_implemented_with_reduce)
The implementation goes through functools.reduce. ... ok
test_negative_value_rejected (test_basics.FactorialTests.test_negative_value_rejected)
A negative argument raises ValueError. ... ok
test_regular_values (test_basics.FactorialTests.test_regular_values)
Factorials of small positive integers are correct. ... ok
test_chain_of_string_functions (test_composition.ComposeTests.test_chain_of_string_functions)
Three-function chain matches the explicit nesting. ... ok
test_identity_for_empty_composition (test_composition.ComposeTests.test_identity_for_empty_composition)
compose() with no arguments is the identity. ... ok
test_numbers_applied_right_to_left (test_composition.ComposeTests.test_numbers_applied_right_to_left)
compose(f, g, h)(x) equals f(g(h(x))) for numbers. ... ok
test_single_function (test_composition.ComposeTests.test_single_function)
A one-function composition is that function. ... ok
test_strings (test_composition.ComposeTests.test_strings)
Composition works on strings as well. ... ok
test_average_column (test_csvproc.CsvProcessingTests.test_average_column)
The mean over score is computed with map and sum. ... ok
test_empty_rows_rejected (test_csvproc.CsvProcessingTests.test_empty_rows_rejected)
An empty row set raises ValueError. ... ok
test_filter_rows_accepts_everything (test_csvproc.CsvProcessingTests.test_filter_rows_accepts_everything)
A predicate that always passes keeps all rows. ... ok
test_filter_rows_keeps_matching_rows (test_csvproc.CsvProcessingTests.test_filter_rows_keeps_matching_rows)
filter_rows applies the predicate via filter. ... ok
test_read_rows_returns_dicts (test_csvproc.CsvProcessingTests.test_read_rows_returns_dicts)
Every CSV line becomes a dictionary of strings. ... ok
test_attribute_exists_before_first_call (test_timing.TimerTests.test_attribute_exists_before_first_call)
The attribute defaults to zero before any call. ... ok
test_duration_covers_sleep (test_timing.TimerTests.test_duration_covers_sleep)
A function sleeping 0.01s reports at least 0.01s. ... ok
test_duration_is_non_negative_float (test_timing.TimerTests.test_duration_is_non_negative_float)
A fast function reports a non-negative float. ... ok
test_metadata_is_preserved (test_timing.TimerTests.test_metadata_is_preserved)
functools.wraps keeps the original name and docstring. ... ok
test_each_function_mapped_over_values (test_transform.MapFunctionsTests.test_each_function_mapped_over_values)
Every function is applied to the whole value list. ... ok
test_empty_function_list (test_transform.MapFunctionsTests.test_empty_function_list)
No functions means no result rows. ... ok
test_empty_value_list (test_transform.MapFunctionsTests.test_empty_value_list)
No values means empty rows for every function. ... ok
test_implemented_with_map (test_transform.MapFunctionsTests.test_implemented_with_map)
The body is built from map calls, not explicit loops. ... ok
test_inputs_are_not_modified (test_transform.MapFunctionsTests.test_inputs_are_not_modified)
The original value list stays intact. ... ok

----------------------------------------------------------------------
Ran 23 tests in 0.012s

OK
```

### Стиль кода

```console
$ uv run --with flake8 flake8 lab4 tests
$ echo $?
0
```

Команда `flake8` (настройка `max-line-length = 79` в
`setup.cfg`) не вывела ни одного замечания: stdout пуст,
код возврата равен 0.

- CI: GitHub Actions workflow `.github/workflows/python-checks.yml`
  с matrix-стратегией по версиям Python `["3.12", "3.13"]`
  запускает `flake8`, `compileall` и юнит-тесты.
