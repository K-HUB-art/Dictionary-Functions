# 1. Create this dictionary kamrul_dict
kamrul_dict = {"f_name": "Kamrul", "l_name": "Hasan", "address": "Yliopistokatu 12 90570 Oulu"}
# 2. Output the first name
print("First Name :", kamrul_dict["f_name"])
# 3. Change the address to "Tellervontie 2 90570.
kamrul_dict["address"] = "Tellervontie 2 90570"
# 4. Output the new address
print("New Address :", kamrul_dict["address"])
# 5. Create a new key "city" with a new value "Oulu"
kamrul_dict["city"] = "Oulu"
# 6. Check if there is a key named "city"
print("Is there a city :", "city" in kamrul_dict)
# 7. Delete key/value "f_name" and "Kamrul"
del kamrul_dict["f_name"]
# 8. Print out all key and values on separate lines
# keeps outputting in incorret orders so I output manually
for k, v in kamrul_dict.items():
    print(k, v)