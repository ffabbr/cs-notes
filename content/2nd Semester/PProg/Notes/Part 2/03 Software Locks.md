 
- Um einen Lock für $n$ Prozesse zu bauen, benötigt man im Speicher mindestens $n$ Variablen, Speicherbedarf $O(n)$ 
- Achtung volatile Array doesn't work (only pointer gets atomic)

> [!success]
> Fair + Deadlock-Free = starvation-free

## Decker's Lock

![[Bildschirmfoto 2026-04-21 um 13.09.37.png]]

## Peterson Lock

- We have a flag that indicates we are interested in entering the CS
- I'm the victim, indicate that other thread goes first
- Wait until other thread no longer interested
- CS
- indicate no longer interested

Eigenschaften
- correct
- fair

![[Bildschirmfoto 2026-04-21 um 13.09.51.png]]
![[Bildschirmfoto 2026-04-21 um 13.15.55.png]]
### Proofs

- **Mutual exclusion**: contradiction. Assume both $CS_P$ and $CS_Q$ (critical sections). By chaining the precedence of write ($W$) and read ($R$) events, it shows a logical contradiction where transitivity breaks down, proving that concurrent access is impossible
- **Freedom from Starvation**: contradiction. Assume Process P is stuck forever in its `while` loop. It then evaluates every possible state Process Q could be in (ignoring the lock, constantly acquiring and releasing it, or also stuck). Every single path leads to a mathematical contradiction, proving P cannot be starved indefinitely.

## Filter Lock

Extension of Peterson's lock to n processes

- mutual exclusion
- deadlock free
- starvation free
- not fair (first-come-first-serve)

The filter filters out threads such that only one ends up in the CS. Every thread knows its level in the filter. Each level uses Peterson to filter, there's a victim per levelthat lets other pass when conflict. That happens on each level, so only one ends up.

> [!warning] Fairness
> Filter lock is NOT fair (first come first serve in CS). 

![[Bildschirmfoto 2026-04-21 um 13.19.24.png]]

## Bakery Lock

- Wartezimmer mit gezogenen tickets
- Fair

1. Thread will in CS
2. Schaut auf Nummern von anderen Threads, gibt sich Nummer +1 von max der existierenden threads
3. Thread-ID als backup falls 2 Threads gleiche Nummer

![[Bildschirmfoto 2026-04-21 um 13.27.44.png]]

