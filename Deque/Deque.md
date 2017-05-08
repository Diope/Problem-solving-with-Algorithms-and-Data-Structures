# Deques

Also known as a double ended queue, is an ordered collection of items similar to the queue. it has two ends, front and rear and items remained positioned in the collection. Unlike normal queues, new items can be added and removed at either the front or the rear of a deque.

It does not require the LIFO and FIFO ordering that are enforced by stacks and queues, it is up to the programmer to make consistent use of the addition and removal operations

## Deque Abstract Data Types
* `Deque()` creates a new deque that is empty. It needs no parameters and returns an empty deque.
* `add_front(item)` adds a new item to the front of the deque. It needs the item and returns nothing
* `add_rear(item)` adds a new item to the rear of the deque. it needs no parameters and returns nothing.
* `remove_front()` removes the front item from the deque. Needs no parameters and returns the item. The deque is modified
* `remove_rear()` removes the rear item from the deque. Needs no parameters and returns the item. The deque is modified.
* `is_empty()` tests to see whether the deque is empty. Needs no parameters and returns a boolean value
* `size()` returns the number of items in the deque. Needs no parameters and returns an integer.
