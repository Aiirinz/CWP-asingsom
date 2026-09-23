def array_of_names(namebook):
  result = []
  for first_name, last_name in namebook.items():
    full_name = first_name.capitalize() + " " + last_name.capitalize()
    result.append(full_name)
  return result


persons = {
    "Micheal": "Jackson",
    "Scooby": "Doo",
    "Peter": "Parker",
    "Max": "Verstappen",
}

print(array_of_names(persons))