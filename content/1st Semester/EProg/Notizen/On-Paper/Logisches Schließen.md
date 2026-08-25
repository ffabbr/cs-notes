## Hoare-Logik

Hoare-Logik dient zur formalen Verifikation von Programmen.  Sie beschreibt, **welche Bedingungen vor und nach einer Anweisung gelten müssen**, um Korrektheit zu garantieren.

{P} X = E {Q}

1. Bilden von Q' durch Ersetzen aller X in Q durch E
2. Zeigen, dass P ⇒ Q' gilt

Für die weakest precondition, basically die Post-Condition nehmen, von unten nach oben überall einsetzen und schauen was rauskommt.  Ich habe ein Video dazu aufgenommen, siehe Media > Videos.

### Beispiel 

![[Hoare-Logik Beispiel.png]]

### if-else Precondition finden

![[06_Logisches_Schliessen.pdf#page=49]]
![[06_Logisches_Schliessen.pdf#page=47]]
![[06_Logisches_Schliessen.pdf#page=46]]
![[06_Logisches_Schliessen.pdf#page=52]]


---

## Loop Invariante (Loop Counting)

### Slides

![[06_Logisches_Schliessen.pdf#page=66]]

![[06_Logisches_Schliessen.pdf#page=67]]

### Muster erkennen durch Tabellen

![[Loop Invariante 1.png]]![[Loop Invariante 2.png]]
![[Loop Invariante 3.png]]

Siehe [Lecture](https://video.ethz.ch/lectures/d-infk/2025/autumn/252-0027-00L/v/Pt2Oh56tbGa?t=08m04s), [[Loop Invariant.mp4]], [[Hoare Triples.mp4]]

### Beispielaufgabe zur Invariante (Prüfungsaufgabe)

![[Nützliche schwächste Invariante-1.png]]
![[Nützliche schwächste Invariante-2.png]]