<iframe src="/static/ebnf-animation.html" title="EBNF Animation" style="border: 0; border-radius: 10px; width: 100%; height: 480px;"></iframe>

Eine EBNF-Produktion ist ein Rezept. Die Operatoren expandieren das Muster zu einem konkreten String. Dieselbe Regel kann `+42` und `7` erzeugen, je nachdem, ob `[]` genommen und `{}` wiederholt wird.

Die Animation liegt in [[Pages/EBNF Animation.html|Pages/EBNF Animation.html]] und wird hier per iframe eingebunden.

## Notation

| Syntax | Bedeutung |
| --- | --- |
| `<name>` | Nonterminal, wird durch eine Produktion ersetzt |
| `terminal` | Zeichen, das so im String steht |
| `A \| B` | Alternative: genau eine Seite |
| `[A]` | Optional: A oder nichts |
| `{A}` | Wiederholung: null- oder mehrmals A |
| `(A)` | Gruppierung |
| `<=` | definiert |

```ebnf
<int> <= [+ | -] <digit> {<digit>}
<digit> <= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```
