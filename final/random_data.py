from random import choice

file = open("food.txt", "w")

food_name = ["Potato", "Soba", "ChickenFried", "PotatoChip", "FriedEgg", "Somtum", "TomyamKung"]
price = [10, 20, 30, 40, 50, 60, 70, 80, 90]
place = ["Newbar", "IUPbar", "SevenEleven", "Scibar"]

file.write("Food Price Place \n")
for each_food in range(99):
    food = choice(food_name)
    food_price = choice(price)
    food_place = choice(place)
    file.write(f"{food} {food_price} {food_place} \n")
file.close()



