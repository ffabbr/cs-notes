
A [[15 Pipelining|Pipeline]] can stall. 

Lösung: 

[[17 Out of order execution]] versucht, spätere Befehle desselben Threads vorzuziehen. Das ist aber oft schwer wegen der Data Dependencies. 

Bei Fine-Grained Multithreading switchen wir zu einer ganz anderen Aufgabe/Thread (also keine Abhängigkeiten), und führen die aus, während wir auf den Stall warten. CPU holds register state for multiple threads simultaneously. 

Aka wir wechseln in jedem Taktzyklus den Thread. Dadurch Single-thread performance worse (a thread only gets 1 out of N cycles), but overall throughput improves.
