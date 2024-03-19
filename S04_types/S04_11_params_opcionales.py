def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hola, {name}!")
    else:
        print("Hello World")

say_hi("Luis")