def average(students):
  total = 0
  count = 0
  for score in students.values():
    total = total + score
    count = count + 1
  return total / count


class_3B = {"michea": 18, "scooby": 15, "peter": 8, "max": 9}

class_3C = {"mark": 17, "jame": 15, "jean": 8, "chowder": 13}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")