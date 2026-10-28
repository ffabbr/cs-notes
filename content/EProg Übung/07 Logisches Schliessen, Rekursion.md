
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

Wir schauen uns die Beispiele der Präfixkonstruktion und der *Towers of Hanoi* an. Den Code der Präfixkonstruktion aus der Übung findet ihr unten. Das ist meine alternative Lösung, ein wenig anders als die Lösung, die ihr in dem `u06-sol` Ordner findet (gerne beides anschauen und vergleichen).


> [!success] Downloads
> Slides: [[u07.pdf|Slides Woche 7]]



----




## Präfixkonstruktion

```java
public class PrefixAlternativ {  
  
    // SIGNATUR gleich belassen  
    public boolean isPrefixConstruction(String s, String t, int n) {  
  
        if (s.isEmpty()) return true;  
        if (n==0) return false;  
  
        return tryPrefix(s, t, n, 1); // start mit präfix länge 1  
    }  
  
    // Reststring s, Referenzstring t, n mögliche Restbausteine, Länge des Präfix-Abschnitts len  
    public boolean tryPrefix(String restString, String referenzString, int n, int prefixLen) {  
  
        if (prefixLen > restString.length()) return false;  
        if (prefixLen > referenzString.length()) return false;  
  
        // stimmt das Zeichen an der aktuellen Stelle überein?  
        if (restString.charAt(prefixLen - 1) == referenzString.charAt(prefixLen - 1)) {  
            // option 1, "abschneiden" und den rest prüfen  
            if (isPrefixConstruction(restString.substring(prefixLen), referenzString, n - 1)) {
	            return true;  
			}
            // option 2, falls option 1 nicht funktioniert:  
            // versuche alles mit längerem präfix            
            return tryPrefix(restString, referenzString, n, prefixLen + 1);  
        }  
        return false; // zeichen stimmen nicht überein  
    }  
}
```