name = "Bob"

print(f"Hello, {name}")

name = "Rolf"

print(f"Hello, {name}")

name = "Bob"

greeting = "Hello, {}"

with_name = greeting.format(name)
with_name_two = greeting.format(name)

print(with_name)

longer_phrase = "Hello, {}. Today is {}"

formatted = longer_phrase.format("Rolf", "Monday")

print(formatted)
