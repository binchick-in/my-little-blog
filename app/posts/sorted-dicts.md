---
title: Sorting a List of Dictionaries by Value
path: sorted-dicts
published: 2020-03-14
summary: Sorting a list of dictionaries based on a value in the dictionary is always something I forget. I'll probably not forget it after this post though!
---


You have a list of dictionaries, and you want to sort them by one of the values in each dictionary.


```python
my_list = [
    {'product': 'Laptop', 'price': 1200},
    {'product': 'Bike', 'price': 125},
    {'product': 'Cell Phone', 'price': 700},
    {'product': 'TV', 'price': 320}
]
```

In this case we want to sort this list of products by price.


The main way you will find on places like Stackoverflow is with the `itemgetter` function from the `operator` module.


```python
from operator import itemgetter

sorted(my_list, key=itemgetter('price'))
```

This way works just fine, however, there is a better way in my opinion. One that doesn't require the `itemgetter` import.


```python
sorted(my_list, key=lambda x: x.get('price'))
```

The use of the `lambda` function here removes the need for `itemgetter` altogether.


So far this has only been sorting our list in ascending order. To get the results in descending order, simply add the `reverse=True` flag to the `sorted` arguments.


```python
sorted(my_list, key=lambda x: x.get('price'), reverse=True)
```

And there you have a sorted list of dictionaries in Python3.7