
## Logisches Schliessen II

Um die Weakest Precondition eines Programmstückes zu finden, das if/else Verzweigungen enthält, müssen wir beide Fälle abdecken.

Beispiel: 
![[Bildschirmfoto 2026-10-28 um 18.26.51.png]]

Insbesondere, gibt es keinen else-Fall, betrachten wir dies als einen "leeren" else-Fall. 

- Falls die Postcondition `{ true }` ist, so ist `{ true }` die schwächste Vorbedingung. Alles impliziert die Postcondition, also insbesondere auch die schwächste Bedingung true.
- Falls die Postcondition  `{ false }` ist, so ist `{ false }` die schwächste Vorbedingung. Nur `{ false }` impliziert die Postcondition, demensprechend ist es die schwächste (und einzige) Vorbedingung.

Um die Gültigkeit eines Triples zu prüfen, finden wir unsere Weakest Precondition, und schauen, ob die gegebene Precondition die Weakest Precondition impliziert. 

Die gegebene Vorbedingung P muss stärker (oder gleich stark) sein als die WP.  z.B. wenn wir als WP finden `x > 0` und die gegebene precondition ist `x > 5` (also stärker), ist die precondition korrekt, da

$$
x>5   \implies    x>0
$$

Wir üben auch hier viele Beispiele. Achtet insbesondere bei der ==Ganzzahldivision==. 
Um die Gültigkeit bei if/else zu zeigen, gehen wir ebenso vor. Um das aber einfacher/übersichtlicher zu gestalten, betrachten wir die Implikationen der beiden if/else Teile getrennt.

![[Bildschirmfoto 2026-10-28 um 18.30.15.png]]
![[Bildschirmfoto 2026-10-28 um 18.30.36.png]]


## Rekursion

Wir schauen uns die Beispiele der Präfixkonstruktion und der *Towers of Hanoi* an. 


> [!success] Downloads
> Slides: [[u07.pdf|Slides Woche 7]]


