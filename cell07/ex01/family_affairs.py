def find_the_redheads(family):
  def is_red(name):
    return family[name] == "red"

  return list(filter(is_red, family.keys()))


dupont_family = {
    "Micheal": "red",
    "Scooby": "blond",
    "Peter": "brunette",
    "Max": "red",
    "Mark": "red",
}

print(find_the_redheads(dupont_family))