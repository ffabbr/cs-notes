
## Schleifen 

In der heutigen Übungsstunde schauen wir uns zuerst `for` und `while` Schleifen an. 

Eine `for` Schleife wiederholt den *body* solange die Schleifenkondition erfüllt ist. Meist wird der Ausdruck so verwendet: `for (int i = 0; i < limit; i++) {...}`. Die Schleifenvariable `i` können wir innerhalb der Schleife verwenden, um zu prüfen, in welcher Iteration wir gerade sind. 

Eine `while` Schleife wiederholt den *body* solange die Schleifenkondition erfüllt ist. Das klingt sehr ähnlich zu dem obigen Satz über `for`, denn tatsächlich sind for und while Schleifen semantisch Äquivalent. Wir schauen uns in der Übungsstunde Beispiele dazu an. 

![[Bildschirmfoto 2026-10-05 um 19.51.27.png]]![[Bildschirmfoto 2026-10-05 um 19.51.39.png]]

> [!info]
> Das Projekt-Template zum Herunterladen: [[Reihe-Projekt.zip]]

## Increment und Decrement

- `int b = a++` weißt b den Wert a zu und erhöht dannach die Variable `a` um 1
- `int b = ++a` erhöht die Variable `a` um 1 und weißt dann den neuen Wert b zu. 

Nutzt diese Schreibweise in dem Zusammenhang wie hier (z.B. `int b = a++`) **nicht**. Das Ziel ist, dass euer Code lesbar und einfach verständlich ist. Das hilft euch sehr beim Debuggen. Es gibt jedoch Instanzen, wo z.B. `a++` separat wo steht,  in etwa in dem *update* der for-Schleife, oder sonst einfach `a++`. Hier kann das durchaus nützlich sein. 

Zudem gibt es folgende weitere Kurzformen: 
- `variable += value` für `variable = variable + value;`
- `variable -= value` für `variable = variable - value;`
- `variable *= value` für `variable = variable * value;`
- `variable /= value` für `variable = variable / value;`
- `variable %= value` für `variable = variable % value;`

Auch hier gilt, nutzt sie nur, wenn ihr euch der Bedeutung unterbewusst klar seid. 

## String Methoden

- [[Bildschirmfoto 2026-10-05 um 20.02.06.png|String Methoden, die String liefern]]
- [[Bildschirmfoto 2026-10-05 um 20.02.14.png|Substrings]]
- [[Bildschirmfoto 2026-10-05 um 20.02.21.png|String Methoden, die int liefern]]
- [[Bildschirmfoto 2026-10-05 um 20.03.20.png|String Methoden, die boolean liefern]] (hier ist insbesondere `.equals()` wichtig, um 2 Strings zu vergleichen)

Wir üben die Anwendung dieser String Methoden mit verschiedenen Beispielen (siehe Slides).


> [!success] Slides
> → [[Slides Woche 4.pdf]]
