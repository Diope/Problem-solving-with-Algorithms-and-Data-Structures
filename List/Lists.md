# Unordered List Abstraction Data Type
The structure of an unordered list, is a collection of items where each item holds a relative position with respect to the others. Some possible list operations are as follows:

* `List()` creates a new list that is empty. It needs no parameters and returns an empty list.
* `add(item)` adds a new item to the list. It needs the items and returns nothing. Assume the item is not already in the list.
* `remove(item)` removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
* `search(item)` searches for the item in the list, it needs the items and returns a boolean value
* `size()` returns the number of items in the list. it needs no parameters and returns an integer.
* `append(item)` adds a new item to the end of the list makign it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.
* `insert(pos,item)` adds a new item to the list at the given position, needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have postiion pos.
* `pop()` removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.
* `pop(0)` Removes and returns the item at position pos. it needs the position and returns the item. Assume the item is in the list.

# Ordered List Data Abstract Types
* `OrderedList()` creates a new ordered list that is empty. Needs no parameters and returns an empty list
* `add(item)` adds a new item to the list making sure that the order is preserved. It needs the item and returns nothing. Assume the item is not already in the list.
* `remove(item)` removes the item from the list. it needs the item and modifies the list. Assume the item is present in the list.
* `search(item)` searches for the item in the list. Needs the item and returns a boolean.
* `is_empty()`tests to see whether the list is empty. Needs no parameters and returns a boolean value.
* `size()` returns the number of items in the list. Needs no parameters and returns an integer.
* `pop()` removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.
* `pop(pos)` removes and returns the item at the position 'pos'. Needs position, and returns the item. Assume the item is in the list.

In order to implement the ordered list, rememeber that the relative positions of the items are based on some underlying characteristic. The ordered list can be represented bya linked structure. Node and link structure is ideal for representing the relative positioning of items.
