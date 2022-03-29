price_fruits={'orange':2,'banana':1,'grapes':4,'strawberry':5}
def test(student):
   new={'clementine':3,'apple':4}
   price_fruits.update(new)
   print("Inside the function",price_fruits)
   return
test(price_fruits)
print("outside the function:",price_fruits)