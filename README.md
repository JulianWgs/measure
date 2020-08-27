# Measure

> Benchmarking just got easier

Measure the execution time together with information about the input and output arguments just by wrapping the function definition.

```python
import time

import measure

@measure.measure(
    # process input and output args
    input_map={"numbers": len},  
    output_map={"type": lambda item: type(item)}
)
def add(numbers, b, c=0):
    time.sleep(1.2)
    return [number + b * c for number in numbers]

result = add(range(5), 2, c=5)
print(result)  # [10, 11, 12, 13, 14]
```

Logging data:
```python
{
    'function': 'add',
    'module': '__main__',
    'version': None,
    'input': {'numbers': 5, 'b': 2, 'c': 5},
    'output': {'type': <class 'list'>},
    'duration': 1.2014620304107666
}
```