from typing import Optional

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f'¡Hola, {name}!')
    else:
        print('Hola... Mundo!')

say_hi('Luis')