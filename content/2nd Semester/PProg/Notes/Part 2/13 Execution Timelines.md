
start: invocation
end: return

<iframe src="https://cs.rohlik.net/static/execution.html" style="border-radius: 10px" width="100%" height="500"></iframe>


## Quiescent consistency

1. non-overlapping operations have sequential effect
2. for overlapping operations we cannot say something (could even swap within thread)

## Sequential consistency

*"can we move actions left and right (without swapping) to make it work?"*

aka Threads can interleave anyways, but within Thread order is set; we suppose write operation instantly visible

## Linearizability

*"can we find a point in time where each operation takes effect to make it work?*

Instead of a line where things happen, the change of state happens at a POINT between invocation and return. If there is a point for each action such that everything is correct, we say, it is linearizable. 

- Linearisierbar $\implies$ Sequential consistency
- unlike in sequential consistency, we cannot move the operations (lines), but we decide on the point in time within the operation line

**Describing the line situation formally:** 
- $\to_{G} \subset \to_{S}$: 
	- $\to_{G}$  G ist eine unvollständige Festlegung der absoluten Reihenfolge der Timeline, aber z.B. keine Aussage über overlapping Ops 
	- $\to_{S}$  G schränkt gibt restliche Reihenfolge die auch concurrent Ops eine Reihenfolge zuweist
- H (history) ist linearisierbar, wenn es zu G erweitern kann indem man 
	- appending responses to pending invocations that took effect (even though the program hasn't terminated but we see in other values that it has had effect already, so we set an ending-point)
	- discarding invocations that did not take effect (when no return no effect)

Korrektheits-Beweise mit Linearisierbarkeit, dann darf es nur einen Linearisierungspunkt pro Pfad geben. 


<iframe src="https://cs.rohlik.net/static/consistency.html" style="border-radius: 10px" width="100%" height="500"></iframe>

---

well-formed: per Thread könnte sequentiell sein
equivalent: same per thread projections
complete: no pending responses