→ Slides [[14_Collections.pdf]]

```java.util.Collections```

## Arten

### Collection

- keine Schlüssel, nur Werte

![[14_Collections.pdf#page=9]]

### Liste

- keine Schlüssel, nur Werte
- Geordnet (0-basiert)

![[14_Collections.pdf#page=11]]

### Linked List

- Doppelt verkettet
- hat Index
- Stack und Queue


### ArrayList

![[14_Collections.pdf#page=13]]


## Nutzung

![[14_Collections.pdf#page=14]]
![[14_Collections.pdf#page=15]]
![[14_Collections.pdf#page=16]] 

## Subtyping

![[14_Collections.pdf#page=18]]

## Achtung

- beim Hinzufügen oder Löschen von Elementen ändern sich die Indizes

![[14_Collections.pdf#page=22]]

## Compare To

![[14_Collections.pdf#page=29]]
![[14_Collections.pdf#page=31]]

## Sortieren

- benötigt Comparable

![[14_Collections.pdf#page=35]]
![[14_Collections.pdf#page=38]]


## Sets

- keine Schlüssel, nur Werte
- Keine Duplikate 
- Nicht geordnet, keine Reihenfolge, kein Index-basierter Zugriff

```java
public interface Set<E> extends Collection<E> {
	public void add(E element);
	public boolean remove(Object o);
	public boolean cotains(E element);
	public boolean isEmpty();
	...
}
```

![[14_Collections.pdf#page=41]]

### Treeset

- sortiert
- keine Duplikate
- ```E``` muss Interface ```Comparable<E>``` und Methode ```compareTo(E)``` implementieren

![[14_Collections.pdf#page=43]]

### Hashset

- keine Reihenfolge
- keine doppelten Elemente
- einfacher zu Implementieren, wenn man nur schauen will ob ein Element vorkommt

![[14_Collections.pdf#page=47]]
![[14_Collections.pdf#page=49]]
![[14_Collections.pdf#page=50]]

---

## Beispiel Priority Queue

![[14_Collections.pdf#page=56]]

---

![[14_Collections.pdf#page=60]]

---

## Map Interface

- Key-Value-Paare
- jeder Key ist eindeutig, Values dürfen sich wiederholen
- Ungeordnet

**Beispiel**

```java
Map<String, Integer> age = new HashMap<>();
age.put("Alice", 20);
age.put("Bob", 22);
```

```java 
  .getOrDefault("test", -1);
  ```


![[14_Collections.pdf#page=65]]

![[14_Collections.pdf#page=67]]

### Implementation

![[14_Collections.pdf#page=77]]
![[14_Collections.pdf#page=78]]
![[14_Collections.pdf#page=81]]
![[14_Collections.pdf#page=82]]
![[14_Collections.pdf#page=83]]

## Comparator

![[14_Collections.pdf#page=89]]
![[14_Collections.pdf#page=92]]
![[14_Collections.pdf#page=93]]


## Iteration

![[14_Collections.pdf#page=105]]
![[14_Collections.pdf#page=107]]
![[14_Collections.pdf#page=108]]