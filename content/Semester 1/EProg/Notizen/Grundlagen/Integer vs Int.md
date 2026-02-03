
```java
// int: schnell, direkt
int a = 5;
int b = 10;
int sum = a + b; // 15

// Integer: Objekt, kann null sein
Integer x = null;
Integer y = 20;
Integer z = x; // erlaubt, auch wenn x null ist

// Autoboxing
int u = 5;
Integer f = u; // Boxing: int → Integer

Integer e = 10;
int s = e; // Unboxing: Integer → int
```

Integer ist die Wrapper-Klasse (Objekt) mit einer Referenz auf ein Objekt, das einen int enthält. Default Wert von int ist ja 0, von Integer *null*.

int verwenden, wenn man mit Zahlen rechnet
Integer verwenden wenn man nullable braucht

Java packt einen primitiven Typ (z.B.) int automatisch in sein Wrapper-Objekt (z.B. Integer), und vice versa. (siehe Beispiele)

![[Qual der Wahl.png]]