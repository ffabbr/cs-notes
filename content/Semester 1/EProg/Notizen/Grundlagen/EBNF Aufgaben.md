
[EBNF Checker](https://thomasgassmann.com/ebnf)

## Tasks

### Palindrome

```ebnf
<digit> <= 1 | 2 | 3 | 4

<palindrome> <= <digit> | (1 [<palindrome>] 1 | 2 [<palindrome>] 2 | 3 [<palindrome>] 3 | 4 [<palindrome>] 4)
```

### Five (ACHTUNG 0)

``` EBNF
<one> <= 1
<two> <= (2) | (<one> + <one>)
<three> <= (3) | (<one> + <two>) | (<two> + <one>)
<four> <= (4) | (<three> + <one>) | (<one> + <three>) | (<two> + <two>)

<five> <= (5) | (<four> + <one>) | (<one> + <four>) | (<three> + <two>) | (<two> + <three>)
```

### Odd-Eight

```ebnf
<nichtacht> <= 1 | 2 | 3 | 4 | 5 | 6 | 7 | 9 | 0

<zweiachter> <= {<nichtacht>}8{<nichtacht>}8{<nichtacht>}
<oddeight> <= {<nichtacht>}8{<nichtacht>}{<zweiachter>}
```
