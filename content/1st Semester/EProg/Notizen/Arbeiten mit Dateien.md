## Lesen
#### Code-Beispiel 

```java
import java.io.File;

File file = new File("example.txt"); // file handle

// delete file if too large
if (file.exists() && file.length() > 1000) {
    file.delete();
}
```

### Separierung

- whitespace trennt next-Ausdrücke
- ```\n``` (new line) hat keine Bedeutung

### File-Methoden

![[11_Arbeiten_mit_Dateien.pdf#page=6]]
![[11_Arbeiten_mit_Dateien.pdf#page=24]]
### Zeilenbasierte Dateien

| Name der Methode | Beschreibung der Methode |
|------------------|---------------------------|
| `nextLine()`     | returns next entire line of input |
| `hasNextLine()`  | returns `true` if there are any more lines of input to read (always true for console input) |

![[11_Arbeiten_mit_Dateien.pdf#page=38]]

#### Lines and Values

*use two separate scanners, one for lines, one for the contents within lines*
![[11_Arbeiten_mit_Dateien.pdf#page=41]] ![[11_Arbeiten_mit_Dateien.pdf#page=43]] 

## Schreiben

```java
import java.io.File; 
import java.io.PrintStream; 
File file = new File("output.txt"); 
PrintStream fileOutput = new PrintStream(file);
```

Ausgabemethoden von System.out funktionieren auch für PrintStream: 
- ```java fileOutput.print()``` statt System.out.print()
- ```java -fileOutput.println()``` statt System.out.println()

![[11_Arbeiten_mit_Dateien.pdf#page=47]] 