

> [!success] Download
> Ladet das Projekt [[Checksum-Projekt.zip]] herunter, entpackt es, öffnet in IntelliJ, und implementiert die `checksum` Methode rekursiv.

## Arrays

Arrays haben eine **feste Länge**, jeder Eintrag hat speichert einen Wert des deklarierten Datentyps. 

```java
int[] arr1 = {1, 2, 3}; // deklarieren mit Werten
int[] arr2 = new int[3]; // array mit 3 int elementen
arr2[2] = 10; // wert festlegen 
```

Eine Matrix kann als zweidimensionales Array dargestellt werden. Dabei enthält jeder Eintrag des Arrays wiederum ein Array. Die einzelnen Arrays können unterschiedlicher Länge sein (oder sogar `null`). ==Macht keine Annahmen über die Längen==.

![[Bildschirmfoto 2026-10-14 um 13.41.12.png]]

## Referenzen

Deklarieren wir `int[] numbers = {1, 2, 3, 4, 5};`,  so speichert `numbers` die Referenz zu den eigentlichen Werten. Übergeben wir `numbers` als Parameter an eine Methode, wird nur die Referenz übergeben. Ändern wir Werte in diesem Array, sind diese Änderungen auch anderswo sichtbar (nicht so wie bei primitiven Typen wie `ints`). Ändern wir in der Methode jedoch die Referenz auf ein anderes Array, so sind diese Änderungen nicht mehr sichtbar. 

(Beispiele folgen)

## Method-Overloading

Die Signatur einer Methode besteht aus 

- dem Namen der Methode
- den Parametern

Somit können wir unterschiedliche Methoden mit gleichem Namen, aber unterschiedlichen Parametern deklarieren. 

![[Bildschirmfoto 2026-10-14 um 13.47.40.png]]

Method-Overloading beschreibt, mehrere Methoden mit gleichem Namen für unterschiedliche Parameter für unterschiedliche Einsatzzwecke aufzustellen.

![[Bildschirmfoto 2026-10-14 um 13.47.53.png]]

## Rekursion

Wir lösen Aufgaben, indem wir innerhalb einer Methode dieselbe Methode erneut aufrufen. 

Wir schauen uns verschiedene Beispiele in der Übungsstunde an. 

## Java Debugger

→ siehe Slides. 

Versucht den Java Debugger aus, ich persönlich habe auch in der Prüfung viele print-Statements genutzt, statt dem debugger, das funktioniert natürlich weiterhin. 

