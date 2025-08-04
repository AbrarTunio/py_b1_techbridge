cart = {"apple": 2, "banana": 3}

cart.update({"orange": 1})   # add item
cart["apple"] += 1           # update quantity
cart.pop("banana")           # remove item

print(cart)
