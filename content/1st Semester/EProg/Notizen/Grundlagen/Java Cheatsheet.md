## General 

```java

public class HelloWorld {  // Klasse ist Dateiname, UpperCamelCase
	// void wenn keine Rückgabe
    public static void main(String[] args) {  // lowerCamelCase (main)
        System.out.println("Hello World!");
    }  
}


```

## System

```java

System.out.println("Hello World!");
System.out.println("Hello World!".toUpperCase());
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

// Switch-Case
int day = 3;
switch(day) {
    case 1 -> System.out.println("Monday");
    case 2 -> System.out.println("Tuesday");
    case 3 -> System.out.println("Wednesday");
    default -> System.out.println("Other day");
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

## Funktionen 

```java
public class Calculator {

    // Funktion, die int zurückgibt
    public static int add(int a, int b) { // Rückgabetyp int
        return a + b;
    }

    // Funktion ohne Rückgabewert
    public static void printHello(String name) {
        System.out.println("Hello " + name);
    }

    public static void main(String[] args) {
        int sum = add(5, 3);
        System.out.println(sum);      // 8
        printHello("Fabian");         // Hello Fabian
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

## Wiederholungen 

```java
for (int i = 0; i < 10; i++) {
    if (i == 5) break;     // Schleife abbrechen
    if (i % 2 == 0) continue; // Überspringe gerade Zahlen
    System.out.println(i); // Ausgabe: 1,3
}
```

## Arrays

[[Arrays]]

```java 
int[] arr = {1, 2, 3, 4};
System.out.println(arr[0]);  // Zugriff auf erstes Element

arr[2] = 10;                // Wert ändern
System.out.println(arr[2]); // 10
```

## Casting und Konvertierung

```java
// Implizites Casting (wird automatisch gemacht, "Widening")
int i = 10;
double d = i;  // int -> double
System.out.println(d);  // 10.0

// Explizites Casting (muss manuell gemacht werden, "Narrowing")
double pi = 3.14159;
int piInt = (int) pi;   // double -> int (Nachkommastellen fallen weg)
System.out.println(piInt); // 3

// Beispiel Addition verschiedener Typen
int a = 5;
double b = 2.5;

double sum = a + b;   // int wird automatisch zu double konvertiert
System.out.println(sum); // 7.5

// Beispiel Division verschiedener Typen
int x = 7;
int y = 2;

double result1 = x / y;       // int / int -> int -> dann automatisch zu double: 3.0
double result2 = (double)x / y; // int wird zu double: 7.0 / 2 = 3.5
System.out.println(result1);  // 3.0
System.out.println(result2);  // 3.5

// Casting bei char
char ch = 'A';
int chInt = (int) ch;  // char -> int (ASCII-Wert)
System.out.println(chInt); // 65

int num = 66;
char numChar = (char) num; // int -> char
System.out.println(numChar); // B
```


## Scanner (Inputs)

```java 
import java.util.Scanner;  // Import nötig

public class InputExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  // Scanner-Objekt erstellen

        System.out.print("Gib deinen Namen ein: ");
        String name = scanner.nextLine();  // Liest ganze Zeile

        System.out.print("Gib dein Alter ein: ");
        int age = scanner.nextInt();       // Liest Ganzzahl

        System.out.print("Gib deine Körpergröße ein: ");
        double height = scanner.nextDouble(); // Liest Kommazahl

        System.out.println("Hallo " + name + ", du bist " + age + " Jahre alt und " + height + "m groß.");

        scanner.close();  // Scanner immer schließen!
    }
}

```

## Scanner von Datei

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadFileExample {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("data.txt"));
        int[] laengen = liesLaengen(scanner);
        scanner.close();
    }

    static int[] liesLaengen(Scanner scanner) {
        int n = scanner.nextInt();         // erste Zahl = Anzahl Werte
        int[] laengen = new int[n];
        for (int i = 0; i < n; i++) {
            laengen[i] = scanner.nextInt();
        }
        return laengen;
    }
}
```

→ Slides about the [[Scanner.pdf]]
## Random (Zufallszahlen)

```java
import java.util.Random;

public class RandomExample {
    public static void main(String[] args) {
        Random rand = new Random();

        int randomInt = rand.nextInt(10);      // 0 bis 9
        int randomIntRange = rand.nextInt(5, 11); // 5 bis 10 (Java 17+)
        double randomDouble = rand.nextDouble();  // 0.0 bis <1.0
        boolean randomBool = rand.nextBoolean();  // true oder false

        System.out.println(randomInt);
        System.out.println(randomIntRange);
        System.out.println(randomDouble);
        System.out.println(randomBool);
    }
}
```


## Strings

- Strings sind unveränderbar (immutable)
- ```string.charAt()```
- ```string.indexOf()```

```java
String name = "Dylan";
char startsWith = name.charAt(0);
char endsWith = name.charAt(name.length()-1); //letzter Wert im String)
```

### String-Methoden

```java
String text = "Hello everyone!";
text = text.toUpperCase();

// sonst
.stubstring(i1, i2); // z.B: (0, 3) i1 inklusive, i2 exklusive
.stripLeading();
.length();
.indexOf(s); // -1 wird ausgegeben falls nicht gefunden
.indexOf(s, fromIndex)

String vorlesung = "Einfuehrung in die Programmierung"; 
int index = vorlesung.indexOf("die");
vorlesung.substring(index, index + "die".length()); // "die" ausgeben

```

## Arrays

- mehrere Werte des gleichen Typs gespeichert

```java
import java.util.Arrays;

type[] name = new type[length]; // nach deklaration voller default 0/false Werten

double[] prices; // deklaration ohne Länge
names[i] = "Pip";

date[data.length - 1];

```


## Aliasing

![[Bildschirmfoto 2025-10-10 um 09.46.32.png]]![[Bildschirmfoto 2025-10-10 um 09.50.09.png]]![[Bildschirmfoto 2025-10-10 um 09.52.10.png]]