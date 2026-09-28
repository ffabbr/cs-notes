Diese Woche schauen wir uns zum ersten Mal Java an, insbesondere unterschiedliche Operationen. 

## Ordnung der Auswertung

Wir alle kennen "Punkt vor Strich" aus der Mathematik, und ein ähnliches Prinzip gilt auch bei Java. Verschiedene Operationen haben verschiedene Rangordnungen (precedence). 

Für's erste genügt es zu wissen, dass 

1. Klammern
2. Multiplikation oder Division
3. Addition oder Subtraktion

Eine genauere Liste findet ihr [[Precedence.png|hier]]. Lernt das nicht auswendig, aber schaut, dass ihr ein Gefühl dafür bekommt. Manche Operationen aus der Liste haben wir uns noch nicht angeschaut, das folgt noch. 
## Assoziativität

Die Assoziativität bestimmt, wie ein Operand verwendet wird. Intuitiv kennen wir auch das aus der Mathematik, `10-5-2` würden wir alle rechnen als `(10-5)-2`, nicht `(10-(5-2))` (obgleich es in diesem Beispiel keinen Unterschied macht). 

Die Zuweisung (`=`) ist rechts-assoziativ. `a = b = c` setzt a und b auf c. 

![[Pasted image 20260928133413.png]]

## Addition mit einem String?

(work in progress)


---

> [!info]
> Wir üben die Auswertung verschiedener Ausdrücke, siehe Slides (Link unten). Achtet insbesondere auf: 
> - die precedence der Operationen
> - wird gecastet oder nicht?
> - arbeiten wir mit einem String?

---
## Short circuiting

Die Auswertung eines true/false Ausdruckes wird beendet, sobald das Ergebnis feststeht. Oft braucht man dafür nicht den gesamten Ausdruck betrachten. 

Beispielsweise wenn wir einen Ausdruck haben der zwei Ausdrücke mit && kombiniert—also müssen beide true sein, damit unser Ausdruck true ausgibt, denn nur true && true ergibt true—und der linke Ausdruck ist false, so kann unser gesamter Ausdruck nicht mehr true ergeben und wir müssen die rechte Seite nicht mal mehr betrachten. 

Wenn wir einen Ausdruck haben, der zwei Ausdrücke mit || kombiniert—also muss einer der beiden true sein, damit unser Ausdruck true ausgibt, denn true || false ergibt true, ebenso true || true—und der linke Ausdruck ist true, so kann unser gesamter Ausdruck nicht mehr false ergeben, und wir müssen die rechte Seite nichtmal mehr betrachten. 

Ihr seht im Bild, die Division durch 0 bereitet keinen Fehler, da nie durch 0 dividiert werden muss.

![[Pasted image 20260928133526.png]]
## Escape Characters

Mit \ "escapen" wir. Das bedeutet, wir wollen einen Teil innerhalb von einem String nicht direkt so ausgeben, sondern Java soll den Teil anders interpretieren. Eine Liste findet ihr hier—ihr müsst das aber keineswegs auswendig können.

z.B. `\n` steht für einen Zeilenumbruch.

Da `\` escapen bedeutet, müssen wir `\\` machen, um tatsächlich einen Backslash auszugeben.

![[Pasted image 20260928133703.png]]

Slides (work in progress)


---

![[Pasted image 20260928134152.png]]
![[Pasted image 20260928134214.png]]

![[Pasted image 20260928134233.png]]