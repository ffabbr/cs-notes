n Objekte, k Gruppen, 
mindestens eine Gruppe enthält mindestens $\lceil \frac{n}{k} \rceil$ Objekte, keine Gruppe ist leer.

> [!abstract] Bildhaft
> Wenn du 10 Tauben hast, die du auf 9 Boxen aufteilen willst, müssen in mindestens eine Box zwei Tauben kommen.

### Beispiel

In einer Gruppe an Menschen kennen mindestens zwei Personen gleich viele Personen. Dabei gilt, jede Person kennt mindestens eine Person, und man kennt sich gegenseitig (also A und B sind Freunde und vice versa). 

Da man mit sich selbst nicht befreundet ist, kann man maximal mit $n-1$ Personen befreundet sein. Also entweder man hat 

$1$ Freund, oder
$2$ Freunde, oder
..., bis
$n-1$ Freunde

Man kann somit bis zu $n-1$ Freunde haben. Da es jedoch $n$ Personen sind, und $n-1$ Möglichkeiten, Freunde zu haben, kennen mindestens zwei Personen gleich viele. 

$$\left\lceil  \frac{n}{n-1}  \right\rceil=2$$

zeigt das mit dem Pigeonhole Principle.