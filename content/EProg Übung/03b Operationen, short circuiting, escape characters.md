
## Ordnung der Auswertung

Wir alle kennen "Punkt vor Strich" aus der Mathematik, und ein ähnliches Prinzip gilt auch in Java. Verschiedene Operationen haben verschiedene Rangordnungen (precedence). 

Für's erste genügt es, diese Reihenfolge zu kennen

1. Klammern
2. Multiplikation oder Division
3. Addition oder Subtraktion

Eine genauere Liste findet ihr [[Operatoren.png|hier]]. Lernt das nicht auswendig, aber schaut, dass ihr ein Gefühl dafür bekommt. 
## Assoziativität

Die Assoziativität bestimmt, wie ein Operand verwendet wird. Intuitiv kennen wir auch das aus der Mathematik, `10-5-2` würden wir rechnen als `(10-5)-2`, nicht `(10-(5-2))` (obgleich es in diesem Beispiel keinen Unterschied macht). 

Die [[Operatoren.png|meisten Operatoren]] sind links-assoziativ. Die Zuweisung (`=`) ist rechts-assoziativ. `a = b = c` setzt a und b auf c. 

![[Pasted image 20260928133413.png]]

## Implizites Casting

- int + int = int
- double + double = double
- Bei Ausdrücken, die verschiedene Typen enthalten, „gewinnt“ der genauere Typ falls möglich. `double + int = double`, `String + int = String`

## Addition mit einem String?

Wenn wir `+` auf 2 Zahlen (ints, double) ausführen, bekommen wir das Ergebnis der mathematischen Addition. 

Bei Strings bedeutet `+` jedoch die String-Verkettung, z.B. 

```java
System.out.println("Hello " + "World"); // Hello World
```

Bei

```java
System.out.println("Wir schreiben das Jahr " + 2000 + 24);
```

kombinieren wir `String + int`, und wie oben vermerkt,  `String + int = String`. Sobald wir `"Wir schreiben das Jahr " + 2000` ausgeführt haben, haben wir als Zwischenergebnis `"Wir schreiben das Jahr 2000"` (als String). Jetzt Verketten wir noch 24 und bekommen *Wir schreiben das Jahr 200024*.

---

> [!info]
> Wir üben die Auswertung verschiedener Ausdrücke, siehe Slides (Link unten). Achtet insbesondere auf: 
> - die precedence der Operationen
> - wird gecastet oder nicht?
> - arbeiten wir mit einem String?

---
## Short circuiting

Die Auswertung eines true/false Ausdruckes wird beendet, sobald das Ergebnis feststeht. Oft braucht man dafür nicht den gesamten Ausdruck betrachten. 

Bei `&&` muss **beides true** sein. Ist der linke Ausdruck `false`, kann das Gesamtergebnis nicht mehr `true` sein—die rechte Seite wird daher nicht mehr ausgewertet.

Bei `||` reicht **ein true**. Ist der linke Ausdruck `true`, kann das Gesamtergebnis nicht mehr `false` sein—die rechte Seite wird daher nicht mehr ausgewertet.

Ihr seht im Bild, die Division durch 0 bereitet keinen Fehler, da nie durch 0 dividiert werden muss.

![[Pasted image 20260928133526.png]]
## Escape Characters

Mit \ "escapen" wir. Das bedeutet, wir wollen einen Teil innerhalb von einem String nicht direkt so ausgeben, sondern Java soll den Teil anders interpretieren. Eine Liste findet ihr [[escape.png|hier]]—ihr müsst diese aber keineswegs kennen.

z.B. `\n` steht für einen Zeilenumbruch.

Da `\` escapen bedeutet, müssen wir `\\` machen, um tatsächlich einen Backslash auszugeben.

![[Pasted image 20260928133703.png]]


---

Falls euch bei den Coding-Aufgaben die Knowledge über die Java Syntax fehlt, schaut ev. in [[03 Hi Java]] nach.

> [!success] Slides
> → [[Slides Woche 3.pdf]]