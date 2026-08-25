
→ siehe auch [[Slides zu Klassen und Objekte]]
→ siehe auch [[LinkedList.java]]
## Übersicht

| Konzept                           | Idee                 | Bedeutung                         |
| --------------------------------- | -------------------- | --------------------------------- |
| Klasse                            | `class`              | Bauplan für Objekte               |
| Objekt                            | `new`                | Instanz einer Klasse              |
| Attribut                          | Variablen in Klassen | Beschreiben Zustand               |
| Methode                           | Funktion in Klasse   | Beschreibt Verhalten              |
| [[#Das Schlüsselwort this\|this]] | Schlüsselwort        | Referenz auf aktuelles Objekt     |
| [[#Shadowing]]                    | Variablenüberdeckung | Lokale Variable verdeckt Attribut |
| [[#NullPointer]]                  | `if (obj != null)`   | Fehler vermeiden                  |
| [[#Vererbung]]                    |                      |                                   |
| [[#toString()]]                   |                      |                                   |
| [[#Konstruktoren]]                |                      |                                   |
| [[#Sichtbarkeit]]                 |                      |                                   |


Siehe auch die Slides bei [[Slides zu Klassen und Objekte]] und [[07_Klassen_und_Objekte.pdf]]

## Klassen und Attribute

- Eine Klasse ist ein Bauplan für Objekte.
- Eine Klasse kann beliebig viele Attribute beliebiger Typen haben.  
  
```java
  type name;
```

- Eine öffentliche Klasse (`public class Name`) muss in einer Datei `Name.java` gespeichert werden.
- Jedes Objekt hat seine eigenen Attributwerte.
- Die Menge aller Attributwerte bestimmt den Zustand (state) eines Objekts.

Beispiel:

```java
public class Auto {
    String marke;
    int ps;
}
```

## Attribute lesen und schreiben

- Zugriff erfolgt über Punktnotation (dot notation):
    
    - Lesen: `referenz.attrName`
    - Schreiben: `referenz.attrName = wert;`
        
- Eine Referenz wird dereferenziert, um auf das Objekt zuzugreifen.

```java
Auto a = new Auto();
a.marke = "Tesla";
int p = a.ps;
```

## Referenzen und Zuweisungen

- Variablen vom Klassentyp speichern Referenzen auf Objekte, nicht die Objekte selbst.
- Zuweisungen ändern die Referenz, also welches Objekt angesprochen wird.
- Zwei Referenzen können auf dasselbe Objekt zeigen.

```java
Point p1 = new Point();
Point p2 = p1;
p1.x = 10;
p2.y = 20;
```

`p1` und `p2` zeigen auf dasselbe Objekt → Änderungen über eine Referenz wirken auf beide.

## Methoden und Parameter (Beispiel: Point-Klasse)

- Übergibt man ein Objekt als Parameter, wird die Referenz übergeben, nicht eine Kopie.
- Änderungen am Objekt innerhalb der Methode wirken auch außerhalb.

```java
void copyAndInc(Point src, Point dst) {
    dst.x = src.x + 1;
    dst.y = src.y + 1;
}
```

Wenn `p1` und `p2` auf dasselbe Objekt zeigen, werden beide verändert.

## NullPointer

**NullPointer-Exceptions vermeiden**

- Eine Referenz kann `null` sein → Zugriff führt zu Laufzeitfehler.
- Vorher prüfen:

```java
if (obj != null) {
	obj.methode();
}
```

- Ziel: Exceptions vermeiden

## Das Schlüsselwort this

- In Methoden einer Klasse steht `this` für das aktuelle Objekt.
- Wird genutzt, um auf die eigenen Attribute oder Methoden zuzugreifen:

```java
public class Person {
	double[] hours;

	public double computeSalary() {
		double sum = 0;
		for (int i = 0; i < this.hours.length; i++) {
			sum += this.hours[i];
		}
		return sum * 30.7;
	}
}
 ```

- `this` ist automatisch vorhanden in jeder Objektmethode.

## Vererbung

→ siehe [[Vererbung und Polymorphismus]]

## toString()

### Beispiel

```java
public class Point {
    private int x;
    private int y;

    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}

Point p = new Point();
System.out.println(p); // (0, 0)
String s = "P is at " + p;
```


## Konstruktoren

![[07_Klassen_und_Objekte.pdf#page=78]]

## Shadowing

- Eine lokale Variable oder ein Parameter kann denselben Namen wie ein Attribut haben.
- Dann wird das Attribut verdeckt (shadowing).
- Zugriff auf das verdeckte Attribut nur mit `this`.

```java
public class Counter {
    int value;

    public void incrementBy(int value) {
        this.value = this.value + value; // Zugriff auf Attribut
    }
}
```


## Sichtbarkeit

```public > protected > default > private```

- Bei Override darf Sichtbarkeit nur vergrössert werden (oder gleich bleiben), nicht verkleinert werden

![[10_Vererbung.pdf#page=30]]
