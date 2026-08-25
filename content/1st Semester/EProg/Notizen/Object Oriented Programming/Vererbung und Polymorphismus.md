- Gedanke, wenn es eine "B ist ein A" Beziehung gibt, kann B von A erben. 
- Vorstellung, alles was in A ist wird copy-pasted in B
- Syntax `extends`, to check use ```instanceof```
- Die Unterklasse übernimmt Attribute & Methoden der Oberklasse
- kann nur von einer Klasse erben
- Superklassen-Konstruktor muss aufgerufen werden 

## Override

- freiwillige Annotation ```@Override``` für Compiler-Warnungen
- ist nur ein Override, wenn gleiche Signatur

```java
public class Dog extends Animal {
	// everything that is in class Animal and this:
	public void bark() {
		System.out.println("Woof! ");
	}
}
```

## Super

- bei mehreren Vererbungen bezieht sich ```super``` immer auf den direkten Vorgänger

```java
public class Dog extends Animal {
    @Override
    public void eat() {
        super.eat(); // Animal.eat()
        System.out.print(" Sausage!");
    }
}
```

## Instance Of

```java
if (p instanceof Fluxkompensator) {  
    fluxCount++;  
}
```

**Achtung Compilerfehler**

![[instanceof compiler error.png]]

## Konstruktoren

- Konstruktoren werden nicht vererbt
- Konstruktor der Superklasse wird aufgerufen, entweder
	- explizit mit ```super(...);``` als erste Anweisung, oder
	- automatisch (default constructor)
- Sichtbarkeit immer nur allgemeiner machen nicht einschränken (public > protected > default > private)

→ siehe [[Vererbung und Default Constructors.png]]

![[Vererbung und Konstruktoren.png]]

## Subtyping

- statischer Typ (hier Animal) kann sich nicht ändern 
- dynamischer Typ (zuerst Cat, dann Dog) kann sich ändern, muss ein Subtyp (oder gleicher Typ) des statischen Typs sein

![[10_Vererbung.pdf#page=40]]
## Casts

- kann nur "nach unten" casten, macht auch Sinn, können Dog als Animal behandeln aber nicht andersherum
- Casts ändern nicht den dynamischen Typ
- **Runtime Error** wenn falsch gecastet, **Compiler error** wenn nicht gecastet (und incompaible)

![[10_Vererbung.pdf#page=44]]

## Dynamic Binding

```java 
Animal a = new Cat(); 
a.meow(); // compiler error, da a ist animal und animal hat nicht unbedingt meow
((Cat) a).meow(); // funktioniert mit cast
```

```java
Animal a = new Dog(); 
a.eat(); // dog kann eat overriden 
```

### Beispiele

**statischer Typ entscheidet über die Argumente (Argument in dem Aufruf egal, siehe unten)**. 
nutze → [[#Casts]]

#### Attribute

![[Pasted image 20251126164102.png]]
![[Pasted image 20251126164215.png]]

#### Methoden

*Methoden werden anhand vom **dynamischen** Typ ausgewählt*
- hat ein Subtyp die gescuht Methode nicht, dann wird in den parents aufsteigend nach der Methode gesucht, dort wo gefunden wird sie ausgeführt (inkl. der Werte von dort)

![[Pasted image 20251126165717.png]]
![[10_Vererbung.pdf#page=61]]![[10_Vererbung.pdf#page=62]]
#learn erste Zeile von der dritten box

![[Qual der Wahl.png]]

## Klasse Object

- Object hat keine Superklasse, ist über allen Klassen (außer ```null```) 
- Somit erbt jede Klasse automatisch die Methoden von Objekt
	- equals
	- toString
	- getClass
	- hashCode
	- notify
	- wait

**Achtung, == funktioniert nicht mit Objekten, nur mit primitiven Typen. Lösung: equals()**

![[10_Vererbung.pdf#page=80]]
![[10_Vererbung.pdf#page=81]] 
![[10_Vererbung.pdf#page=89]]

## Final

- primitiver Typ: Wert unveränderbar
- Referenztypen: Referenz unveränderbar
- finale Klassen: kein extends möglich
- Methoden: kein Override möglich

### Abstracte Klassen

- verbietet subklassen
![[10_Vererbung.pdf#page=103]] ![[10_Vererbung.pdf#page=105]] 