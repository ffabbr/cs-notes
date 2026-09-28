Diese Woche schauen wir uns zum ersten Mal Java an, insbesondere unterschiedliche Operationen. Den eigentlichen Inhalt dieser Übungsstunde findet ihr hier (→ [[04 Operationen, short circuiting, escape characters]]). Das hier ist eine Übersicht über grundlegende Java Syntax. 

>Versucht sie nicht auswendig zu lernen, sondern durch das wiederholte Anwenden zu verinnerlichen. 

**IntelliJ** hilft euch sehr (das schauen wir uns in der Übungsstunde auch an)
- tippt den Anfang von wie ihr glaubt, dass die Syntax aussieht, und schaut, ob IntelliJ etwas passendes vorschlägt
- anschließend zeigt IntelliJ, welche Parameter ihr braucht. 

---

## General

```java
public class HelloWorld {  // ist Dateiname
	// void = keine Rückgabe
    public static void main(String[] args) {  
        System.out.println("Hello World!");
    }  
}
```

## Printing

```java
System.out.println(3+5); // addition
System.out.println("Hello " + "World!");   // String-Verkettung
```

## Variablen und Datentypen

```java
int age = 25;              // Ganzzahl
double price = 19.99;      // Kommazahl
boolean isActive = true;   // Wahrheitswert
char grade = 'A';           // Einzelnes Zeichen
String name = "Fabian";     // Text
```

## If-else 

```java
int number = 10;

if (number > 0) {
    System.out.println("Positive");
} else if (number < 0) {
    System.out.println("Negative");
} else {
    System.out.println("Zero");
}
```

## Schleifen

```java
// For-Schleife
for (int i = 0; i < 5; i++) {
    System.out.println("i = " + i);
}

// While-Schleife
int j = 0;
while (j < 5) {
    System.out.println("j = " + j);
    j++;
}

// Do-While-Schleife
int k = 0;
do {
    System.out.println("k = " + k);
    k++;
} while (k < 5);

// Enhanced For-Schleife (für Arrays/Collections)
int[] numbers = {1,2,3,4,5};
for (int n : numbers) {
    System.out.println(n);
}
```

## Methoden 

```java
public class Calculator {
    public static void main(String[] args) {
        int sum = add(5, 3);
        System.out.println(sum);
        printHello("Fabian");
    }
    
    // Funktion, die int zurückgibt
    public static int add(int a, int b) { 
        return a + b;
    }

    // Funktion ohne Rückgabewert
    public static void printHello(String name) {
        System.out.println("Hello " + name);
    }
}
```


## Logik

```java
boolean a = true;
boolean b = false;

System.out.println(a && b);  // AND -> false
System.out.println(a || b);  // OR -> true
System.out.println(!a);      // NOT -> false

int x = 5;
int y = 10;
System.out.println(x > 0 && y < 20);  // true
```

## Switch

```java
int day = 3;
switch (day) { 
	case 1: 
		System.out.println("Monday"); 
		break; 
	case 2: 
		System.out.println("Tuesday"); 
		break; 
	case 3: 
		System.out.println("Wednesday"); 
		break; 
	default: 
		System.out.println("Other day"); }
```

## Wiederholungen 

```java
for (int i = 0; i < 10; i++) {
    if (i == 5) break; // gesamte for abbrechen
    if (i % 2 == 0) continue; // Überspringen
}
```


## Scanner (Inputs)

```java 
import java.util.Scanner;

public class InputExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Name: ");
        
        String name = scanner.nextLine();  // ganze Zeile
        int age = scanner.nextInt();       // int
        double height = scanner.nextDouble(); // double
        
        scanner.close();  // Scanner immer schließen!
    }
}
```

## Random (Zufallszahlen)

```java
import java.util.Random;

public class RandomExample {
    public static void main(String[] args) {
        Random rand = new Random();

        int randomInt = rand.nextInt(10); // 0 bis 9
        int randomIntRange = rand.nextInt(5, 11); // 5 bis 10
        double randomDouble = rand.nextDouble();  // 0.0 bis <1.0
        boolean randomBool = rand.nextBoolean();  // true oder false
    }
}
```

