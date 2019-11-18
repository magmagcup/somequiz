# Food in KU
## 1st task
Create a **food** object to store each food
from **food.txt**.

Each **food** object must contain 3 attributes

1. Food name
2. Price
3. Place

~~~
food = Food("Potato", 40, "IUPbar")
>>> print(food.name)
Potato
>>> print(food.price)
40
>>> print(food.place)
IUPbar
~~~


## 2nd task

Create **Store** class that store every **Food** object from **Food.txt**, then add **find food quantity_from_name** method in 
**Store** object

~~~
def find_food_quantity_from_name(self, food_name: str) -> int:
    """
    Return food quantity.
    """
~~~




# Optional
Write what you brought in **bill.txt** and calculate the price at the end of the food list.