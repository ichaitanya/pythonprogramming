customer = {
    "name": "chaitanya trib",
    "age": 30,
    "is_verified": True
}

customer["name"] = "Jack Ma"
print(customer.get("birthdate", "Jan 1 1980"))
print(customer["name"])