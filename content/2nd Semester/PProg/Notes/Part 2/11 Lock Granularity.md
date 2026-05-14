
Beispiel linked list
## Coarse grained locking

synchronized add, remove, contains methods

## Fine grained locking

jedes listenelement hat ein eigenes lock
### Starter (Hand over hand locking)

- hand over hand: threads locks können sich nicht überholen, also statt vorzulaufen bis zu vorgänger von delete und dann 2 nodes zu locken (problem ist dass race condition beim lock acquiren, aber davor speichern wir state). hier ist die lösung hand over hand, also wir laufen mit 2 locks die nodes ab und checken jedes mal ob das nächste element schon das gesuchte element ist. so haben wir die locks die wir brauchen safe, und es kann kein anderer thread uns überholen.
- handover lock when traversing, always only lock 2 nodes at the time
- lock both read and write node, so for f.ex. `remove(c)` we need to lock b and c, as we move the pointer from b to d instead of b to c

Problems: 
- many lock/unlock because of traversal
- locks can't overtake in the sense of making changes further to the right

first element make new dummy element in case that we want to insert right at the beginning

![[Bildschirmfoto 2026-05-13 um 16.19.25.png]]

### Optimistic synchronization locking

1. go to node without locking
2. validate all is okay (to make sure in the meantime, so after reading states and before having both locks, another thread hasn't changed something), 
3. lock only needed nodes for method

**validate**: rescan: traverse from the start to check if the connection up to ==the element after b== is still reachable (connected). Element after b is to check that 1) b ist still reachable and hasn't been deleted, and 2) b.next hasn't changed (f.ex. another thread hasn't deleted b.next, this is important for f.ex. adding)

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

![[Bildschirmfoto 2026-05-13 um 16.26.19.png]]

### Lazy synchronization locking

- like optimistic, but
- add deleted flag instead of actually directly deleting 
- lazy delete nodes flagged as to be deleted when f.ex. traversing

delete c
- lock b and c
- check if b or c got marked and if the next pointer still stands (for add(c), this is our new validate instead of iterating from the start)
- if not marked, mark c (flag) and then delete c (update pointer)

contains
- iterate linked list while current key < destination key
- return yes if both 
	- current key = destination key
	- current key is not marked

![[Bildschirmfoto 2026-05-05 um 10.38.33.png]]
![[Bildschirmfoto 2026-05-13 um 16.38.52.png]]


> [!note]- Skip lists (ev. nicht prüfungsrelevant)
> 
> las vegas 
> 
> - probability on height n = $0.5^n$, we start at height 0
> - left $- \infty$, right is $\infty$, in between are values (list items)
> - higher level lists are contained in lower lists, so level 0 contains everything
> - logarithmic search 
> 	- we traverse from left to right on the same level and go down when we are at a place where we are smaller than destination and next element is bigger than destination
> 	- we adapt the limits to narrow down on elements that are bigger or smaller than the destination
> 	- Example of finding 8: 
> 	  ![[Bildschirmfoto 2026-05-05 um 10.50.29.png]]
> 
> - add
> 	- find predecessors lock free
> 	- lock predecessors
> 	- validate
> - remove
> 	- find predecessofs
> 	- change poitners to point to next value (next col in same row), OR mark as removed per lazy delete 
> 		- lock predecessors, validate, physically remove, unlock