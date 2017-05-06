# Linear Structures
What distinguishes one linear structure from another is the way in which items are added and removed, in particular the location where these additions and removals occur.

## Stacks
A stack (sometimes called a "push-down stack") is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end. This end is commonly referred to as the "top." The end opposite the top is known as the "base."

The base of the stack is significant because items stored in the stack that are closer to the base represent those that have been in the stack the longest. This is also known as LIFO (last-in first-out). it provides an ordering based on length of time in the collection. Newer items are near the top, while older items are near the base.

 ### Sample Stack Operations
 Stack Operation
 * s.is_empty()     []      True