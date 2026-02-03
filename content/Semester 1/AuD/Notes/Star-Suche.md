### Grundidee

Stell dir vor, Roger Federer kommt zu einer ETH-Vorlesung.  
Alle erkennen ihn – aber er kennt niemanden im Saal.  
→ Roger ist der „Star“.

**Definition:**  
In einer Gruppe von Personen $P_1, P_2, ..., P_n$ ist eine Person $P_s$ ein **Star**, wenn:

- Alle anderen $P_t$ (für $t \neq s$) **kennen $P_s$**.
    
- Der Star $P_s$ **kennt niemanden** der anderen.
    

---

### Ziel der Star-Suche

Wir wollen herausfinden, ob es in einer Gruppe einen Star gibt – und falls ja, wer das ist.  
Wir dürfen nur Fragen der Form stellen:

> „Kennt Person A die Person B?“

---

## Naiver Ansatz

### Idee:

Wir fragen **alles** ab.

Für jede Person $P_i$ prüfen wir, ob sie jede andere $P_j$ kennt.

Das sind insgesamt $n \cdot (n-1)$ Fragen.

Beispiel: Bei 4 Personen = 12 Fragen.

So wissen wir am Ende genau, wer wen kennt – aber das ist sehr ineffizient.

---

## Rekursiver Ansatz

### Bildliche Vorstellung:

Wir lassen die Personen nacheinander aus dem Raum gehen und behalten nur mögliche Stars zurück.

#### Vorgehen:

1. Finde den Star unter den ersten $n-1$ Personen.  
    (Also wir lassen eine Person raus und suchen dort den Star.)
    
2. Prüfe, ob diese gefundene Person auch in der ganzen Gruppe (mit der letzten Person $P_n$) ein Star ist:
    
    - Kennt der Star die neue Person? (→ dürfte er **nicht**)
        
    - Kennt die neue Person den Star? (→ **muss** sie)
        
3. Falls der Kandidat kein Star ist, teste die neue Person $P_n$.  
    Dazu fragen wir:
    
    - Kennt $P_i$ (alle anderen) $P_n$?
        
    - Kennt $P_n$ (die anderen) $P_i$?
        

Wenn alle $P_i$ $P_n$ kennen und $P_n$ niemanden kennt, ist $P_n$ der Star.

---

## Best Case

Wenn der Star immer sofort gefunden wird (also keine extra Tests nötig sind):

Es werden **2(n – 1)** Fragen gestellt.

Beispiel:  
Bei 5 Personen = $2 \cdot 4 = 8$ Fragen  
(statt 20 beim naiven Ansatz)

---

## Worst Case

Wenn es ganz schlecht läuft – also jedes Mal die falsche Person aus dem Raum geht, und der echte Star erst am Ende erkannt wird –  
dann brauchen wir wieder genauso viele Fragen wie beim naiven Ansatz:

$n \cdot (n – 1)$ Fragen

---

## Verbesserter Algorithmus

Der Trick: **Bevor** wir jemanden aus dem Raum „werfen“, prüfen wir kurz, ob diese Person überhaupt ein Star **sein kann**.

### Neuer Schritt:

Bevor wir rekursiv weitermachen:

> Wenn die zweitletzte Person $P_{n-1}$ die letzte $P_n$ kennt,  
> dann **tauschen wir sie** – und wissen sicher: $P_n$ ist **kein Star**.

Warum?  
Weil ein Star niemanden kennen darf.

So sparen wir unnötige Tests in späteren Schritten.

---

## Ergebnis

Mit dieser Verbesserung brauchen wir im **Worst Case** nur noch:

**3n – 4 Fragen**

Das ist deutlich besser als $n(n – 1)$.

---

## Zusammenfassung

|Algorithmus|Idee|Max. Fragen|
|---|---|---|
|Naiv|Alle fragen alles|$n(n – 1)$|
|Rekursiv|Suche schrittweise mit Ausschluss|bis $n(n – 1)$|
|Verbessert|Schließe Nicht-Stars vorher aus|**3n – 4**|

