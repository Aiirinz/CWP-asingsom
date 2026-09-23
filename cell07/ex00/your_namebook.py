def array_of_names(namebook):
  result = []
  for first_name, last_name in namebook.items():
    full_name = first_name.capitalize() + " " + last_name.capitalize()
    result.append(full_name)
  return result


persons = {
    "jean": "valjean",
    "Airin": "nnn",
    "nan": "noon",
    "fifi": "fufu",
}

print(array_of_names(persons))