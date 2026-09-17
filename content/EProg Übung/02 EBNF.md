**EBNF beschreibt die Syntax einer Sprache.** Eine EBNF Beschreibung legt fest, wie gültige ("legale") Wörter aussehen. Wir schauen uns in der Übung viele Aufgaben und auch alte Prüfungsaufgaben an. 
## Regeln

> [!success]
> - `( )` Gruppierung, wie in der Mathematik
> - `[ ]` optional
> - `{ }` beliebig oft, auch 0-mal möglich
> - `|` "oder"

## Ableitungen

- Wir wollen zeigen, wie wir prüfen, ob ein Wort legal oder nicht ist. 
- Start: Startregel
- Ende: Zeichenfolge
- schrittweise ersetzen wir den Namen LHS der Regeln mit der Definition 

Beispiel [[Ableitung als Tabelle.png|Ableitung als Tabelle]], Beispiel [[Ableitung als Baum.png|Ableitung als Baum]]

## Aufgaben

- Erstellen Sie eine Beschreibung `<palindrome>`, welche als legale Symbole alle Zahlen zulässt, die von vorne und hinten gleich gelesen werden und die nur die Ziffern von 1 bis 4 verwenden. Beispiele sind 11, 232, 444
- Erstellen Sie eine Beschreibung `five`, welche alle Summen von positiven Zahlen zulässt, welche 5 ergeben. Beispiele sind “1 + 4”, “2 + 1 + 1 + 1”, “5”
- Erstellen Sie eine Beschreibung für `oddEight`, die alle Zahlen enthält, in denen die Ziffer 8 ungerade oft vorkommt.
## Links

- [EBNF checker](https://www.thomasgassmann.com/ebnf)

## EBNF Quiz der Slides

<div style="width:100%;display:flex;flex-direction:column;gap:8px;min-height:635px;"><iframe src="https://wayground.com/embed/quiz/6aa86613fb2dec5b66f7885e" title=" - Wayground" style="flex:1;" frameBorder="0" allowfullscreen></iframe></div>


> [!success] Slides 
> Slides Woche 1: [[EProg Übung/media/Slides Woche 1.pdf|Slides Woche 1]]