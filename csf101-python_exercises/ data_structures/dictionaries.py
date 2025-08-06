name = "Norzin Wangmo"
age = 20
height = 1.56
is_student = True
Person_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}
print(Person_info)
Person_info["Favourite_colour"] = "pink"
print(Person_info)
try:
    print(Person_info["weight"])
except KeyError as e:
    print(f"Error: {e}")
    