**EBNF beschreibt die Syntax einer Sprache.** Eine EBNF Beschreibung legt fest, wie gültige ("legale") Wörter aussehen. Meistens müsst ihr in Prüfungsaufgaben kein EBNF selber schreiben, sondern nur Wörter auf Gültigkeit prüfen oder selber Wörter finden, die gewisse Eigenschaften haben. Wir schauen uns in der Übung viele Aufgaben und auch alte Prüfungsaufgaben an. 
## Regeln

> [!success]
> - `( )` Gruppierung, wie in der Mathematik
> - `[ ]` optional
> - `{ }` beliebig oft, auch 0-mal möglich
> - `|` "oder"

## Aufgaben

- Erstellen Sie eine Beschreibung `<palindrome>`, welche als legale Symbole alle Zahlen zulässt, die von vorne und hinten gleich gelesen werden und die nur die Ziffern von 1 bis 4 verwenden. Beispiele sind 11, 232, 444
- Erstellen Sie eine Beschreibung `five`, welche alle Summen von positiven Zahlen zulässt, welche 5 ergeben. Beispiele sind “1 + 4”, “2 + 1 + 1 + 1”, “5”
- Erstellen Sie eine Beschreibung für `oddEight`, die alle Zahlen enthält, in denen die Ziffer 8 ungerade oft vorkommt.
