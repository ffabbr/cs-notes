## Introduction

- können nicht von String to int casten
- → [[u12.pdf#page=22|Übungsstunde]] 

![[Pasted image 20251203162941.png]]
![[12_Exceptions.pdf#page=9]]![[12_Exceptions.pdf#page=11]] ![[12_Exceptions.pdf#page=14]]![[12_Exceptions.pdf#page=16]]
![[12_Exceptions.pdf#page=17]]
![[12_Exceptions.pdf#page=18]]
![[12_Exceptions.pdf#page=20]]
![[12_Exceptions.pdf#page=21]]
![[12_Exceptions.pdf#page=22]]
![[12_Exceptions.pdf#page=23]]
![[12_Exceptions.pdf#page=24]]

## Exceptions werfen

```java
throw new IllegalArgumentException ( "Favourite course must be one of {EProg, EProg}");
```

**Beispiel**

```java
class Person { 
	String name; // INV: neither null nor "" 
	Person(String name) { 
		if (name == null) {
			throw new IllegalArgumentException("name must not be null"); 
		}
		if (name == "") {
			throw new IllegalArgumentException("name must not be empty"); 
		}
		this.name = name; 
	} 
}
```