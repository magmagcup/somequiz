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

## 3rd task
Add menu interface for easier testing //Ps. it's not the best way to test a program.
~~~
Welcome to storage!

What you want to do? (C: Check food quantity from name): C
Please enter food name: PotatoChip
We have ... PotatoChip in our stock.
~~~

## 4th task
More object! Create **new** class for each place in our data in this case we need 4 class

1. Newbar
2. SevenEleven
3. Scibar
4. IUPbar

Use each place above to store our food data instead of a single **Store** class, data is easier to manage.

```
//This is a template not an actually code don't copy it!
class Store:
    place: list/dict
class Place:
    food: list
    quantity : dict //Ex. {"Chicken": 300}   
```

## 5th task
Create new menu! and make a **find food quantity_from_name** function work with our new structure!
```
Welcome to storage!

What you want to do? (C: Check food quantity from name): C
Place you want to find the food quantity 
(N:Newbar,S:SevenEleven,Sc:Scibar,I:IUPbar or Sk to skip): Sk
Please enter food name or A for all food: A
We have ... food.
```


# Optional
Create **buy** function, write what you brought in **bill.txt** and calculate the price at the end of the file.

```
Welcome to storage!

What you want to do? (C: Check food quantity from name),(B: Buy food): B
Place you want to buy the food ((N:Newbar,S:SevenEleven,Sc:Scibar,I:IUPbar): N
Please enter food name: ChickenFried
You brought ChickenFried from Newbar.
```

bill.txt
```
ChickenFried 50 Newbar

Total price 50
```