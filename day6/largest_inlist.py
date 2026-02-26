li=[1,5,6,7]
largest=li[0]
for i in li:
    if i>largest:
        largest=i
secound=li[0]
for i in li:
    if i>secound and i<largest:
        secound=i
print("lagest",largest)
print("secound",secound)
