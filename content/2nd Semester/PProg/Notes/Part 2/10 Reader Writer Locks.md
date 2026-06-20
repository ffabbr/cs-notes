
separate locked for writing from locked for reading

- $0 \le \text{writers} \le 1$
- $0 \le \text{readers}$
- $\text{writers}*\text{readers} == 0$

![[Bildschirmfoto 2026-05-04 um 11.11.54.png]]

This is needed f.ex. in [[08 Producer Consumer|Producer Consumer]], if reader are much faster than writers, and we want the writers also go have a turn. This is ==not== fair. 

To make them fair, use Wait/Notify with synchronized methods `acquire_read`, `acquire_write`, `release_read()`, `release_write`, and an int for writers count and readers count. Also, have int for number of writers that are waiting, and number of readers that are waiting. Also, writersWait int that stores how many readers we're letting to pass after a writer finishes. We set this by counting how many readers try to write (stored in number of writers waiting int). 

