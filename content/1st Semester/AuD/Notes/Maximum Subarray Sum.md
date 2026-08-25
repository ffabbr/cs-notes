**Beispiel:**  

`A = [−2, 1, −3, 4, −1, 2, 1, −5, 4]`  
→ optimales Teilarray: `[4, −1, 2, 1]` mit Summe **6**

---

## Naiver Ansatz (Brute Force)

**Idee:**  
Berechne einfach alle möglichen Teilarrays und vergleiche ihre Summen.

**Wie er funktioniert:**  
Man startet bei jedem Index `i`, summiert bis zu jedem möglichen Ende `j` und merkt sich die größte Summe.

**Algorithmus:**

```text
maxSum ← -∞
for i ← 1 to n:
    for j ← i to n:
        s ← 0
        for k ← i to j:
            s ← s + A[k]
        maxSum ← max(maxSum, s)
```

**Laufzeit:** Θ(n³)

---

## Brute Force mit Merken

**Idee:**  
Verwende Teilsummen, um wiederholte Berechnungen zu vermeiden.

**Wie er funktioniert:**  
Anstatt jede Teilfeldsumme von Grund auf neu zu berechnen, merkt man sich laufend die Summe und addiert einfach das nächste Element dazu.

**Algorithmus:**

```text
maxSum ← -∞
for i ← 1 to n:
    s ← 0
    for j ← i to n:
        s ← s + A[j]
        maxSum ← max(maxSum, s)
```

**Laufzeit:** Θ(n²)

---

## Divide-and-Conquer-Ansatz

**Idee:**  
Teile das Problem in zwei Hälften und kombiniere die Ergebnisse.

**Wie er funktioniert:**  
Das Maximum liegt entweder komplett in der linken Hälfte, in der rechten Hälfte oder überlappt die Mitte.  
Man löst beide Seiten rekursiv und kombiniert die Resultate durch den größten mittleren Übergang.

**Komplexität:**  

$$T(n) = 2T(n/2) + O(n) = O(n \log n)$$

---

## Dynamisch

**Idee:**  
Entscheide bei jedem Element, ob du die bisherige Summe fortsetzt oder neu beginnst.

**Wie er funktioniert:**  
Man läuft einmal durch das Array und speichert die beste Teilfeldsumme, die an der aktuellen Stelle enden kann. Wenn die Summe negativ wird, beginnt man neu.

**Algorithmus:**

```text
maxSum ← A[1]
current ← A[1]
for i ← 2 to n:
    current ← max(A[i], current + A[i])
    maxSum ← max(maxSum, current)
```

**Laufzeit:** Θ(n)  
**Speicher:** O(1)
