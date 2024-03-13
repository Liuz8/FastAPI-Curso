def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name

print(get_full_name("Daniel", "paprica"))
# print(get_full_name("Daniel", 12))
print(get_full_name('Juan', 'omar'))