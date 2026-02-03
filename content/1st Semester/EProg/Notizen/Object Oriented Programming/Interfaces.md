## Quick-Facts

- Interfaces sind wie ein Versprechen, dass eine Klasse bestimmte Methoden (die im Interface notiert werden) bereitstellt.
- Ein Interface könnte ein anderes extenden (```public interface J extends I```, J und I sind Interfaces)
- Ein Interface darf kein public Attribut haben (```public static final``` geht)

## Code-Beispiel

```java
interface ComparableToInt { // NIE private interface (Compilerfehler)
	boolean smallerThan(int x)
}

class Rational implements ComparableToInt {
	int n; 
	int d; 
	Rational(int n, int d) { this.n = n; this.d = d;} 
	
	public boolean smallerThan(int x) {
		return n < x * d;
	}
}
```

## Slides

![[13_Interfaces.pdf#page=9]]
![[13_Interfaces.pdf#page=5]]
![[13_Interfaces.pdf#page=6]]


## Mehrere Implements

![[13_Interfaces.pdf#page=12]]

## Interfaces und Vererbung

![[13_Interfaces.pdf#page=10]]

![[Klassen und Interfaces.png]]