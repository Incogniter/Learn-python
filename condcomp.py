menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
 ]

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
# print(meals)
#
# # meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
# meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
# print(meals)

fussy_meals = [meal for meal in menu if "spam" in meal or "eggs" in meal if not
               ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)

fussy_meals = [meal for meal in menu if
               ("spam" in meal or "eggs" in meal) and not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)

# the output should be spam or eggs can be there but bacon and sausage cannot be together
# egg , spam and bacon can be there
# egg , spam and sausage can be there
# eggs and sapm also can be together
# but sausage and bacon cannot be together
