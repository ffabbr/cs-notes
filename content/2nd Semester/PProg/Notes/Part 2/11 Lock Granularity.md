
Beispiel linked list
## Coarse grained locking

synchronized add, remove, contains methods

## Fine grained locking

- jedes listenelement hat ein eigenes lock
- handover lock when traversing, always only lock 2 nodes at ta time
- lock both read and write node, so for f.ex. `remove(c)` we need to lock b and c, as we move the pointer from b to d instead of b to c

![[Bildschirmfoto 2026-05-04 um 11.38.30.png]]

Problems: 
- many lock/unlock because of traversal
- locks can't overtake

## Optimistic synchronization locking

get to node without locking, check all is okay (to make sure in the meantime another thread hasn't changed something), then lock only affected notes

- lock
- validate: rescan, traverse from the start to check if the connection up to the element after b is still reachable (connected)

```java
private Boolean validate(Node pred, Node curr) {
    Node node = head;
    while (node.key <= pred.key) { // reachable?
        if (node == pred)
            return pred.next == curr; // connected?
        node = node.next;
    }
    return false;
}
```

Problems: 
- need to traverse list multiple times
- not starvation free

## Lazy synchronization locking

- like optimistic, but
- add deleted flag 
- lazy delete nodes flagged as to be deleted when f.ex. traversing

delete c
- lock b and c
- check if b or c marked
- if not marked, mark c (flag) and then delete c (update pointer)

contains
- iterate linked list while current key < destination key
- return yes if both 
	- current key = destination key
	- current key is not marked

![[Bildschirmfoto 2026-05-05 um 10.38.33.png]]


## Skip lists

las vegas 

- probability on height n = $0.5^n$, we start at height 0
- left $- \infty$, right is $\infty$, in between are values (list items)
- higher level lists are contained in lower lists, so level 0 contains everything
- logarithmic search 
	- we traverse from left to right on the same level and go down when we are at a place where we are smaller than destination and next element is bigger than destination
	- we adapt the limits to narrow down on elements that are bigger or smaller than the destination
	- Example of finding 8: 
	  ![[Bildschirmfoto 2026-05-05 um 10.50.29.png]]

- add
	- find predecessors lock free
	- lock predecessors
	- validate
- remove
	- find predecessofs
	- change poitners to point to next value (next col in same row), OR mark as removed per lazy delete 
		- lock predecessors, validate, physically remove, unlock