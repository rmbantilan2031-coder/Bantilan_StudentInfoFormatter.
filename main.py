e = (input("Enter First Name:    "))

f = (input("Enter Last Name:    "))

g = (input("Enter Section:    "))

h = (input("Enter favorite subject:    "))

first_name = e.strip()
Last_name = f.strip()
section = g.strip()
h = h.strip()

full_name = (e + " " + f).title()
namecode = full_name.upper()
g = g.upper()
h = h.title()

print("\nFormatted output:")
print("Name: ", full_name)
print("Name Code: ", namecode)
print("Section: ", g)
print("Favorite Subject: ", h)
print("Chracter Count: ", len(full_name))

