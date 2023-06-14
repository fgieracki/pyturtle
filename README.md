# pyturtle
Pyturtle made for TKiK

### Dane studenta(-ów):
- Adrian Jaśkowiec
- Filip Gieracki

### Założenia programu
interpreter języka logo wraz z poprawną obsługą list oraz zwiększonymi funkcjonalnościami

### Spis tokenów

| Token     | Opis                                  |
|-----------|---------------------------------------|
| `FD`      | Przesunięcie do przodu                |
| `BK`      | Przesunięcie do tyłu                  |
| `LT`      | Obrót w lewo                          |
| `RT`      | Obrót w prawo                         |
| `PU`      | Podniesienie pisaka                   |
| `PD`      | Opuszczenie pisaka                    |
| `SETCOLOR`| Ustawienie koloru                     |
| `REPEAT`  | Powtórzenie                           |
| `CLEAR`   | Wyczyszczenie ekranu                  |
| `LLIST`   | Lewy nawias kwadratowy                |
| `RLIST`   | Prawy nawias kwadratowy               |
| `IF`      | Warunek                               |
| `ELSE`    | W przeciwnym wypadku                  |
| `WHILE`   | Pętla while                           |
| `TO`      | Definicja funkcji                     |
| `END`     | Koniec definicji funkcji              |
| `EQ`      | Równa się                             |
| `NEQ`     | Różne od                              |
| `LT`      | Mniejsze niż                          |
| `LTE`     | Mniejsze lub równe niż                |
| `GT`      | Większe niż                           |
| `GTE`     | Większe lub równe niż                 |
| `PLUS`    | Dodawanie                             |
| `MINUS`   | Odejmowanie                           |
| `MULT`    | Mnożenie                              |
| `DIV`     | Dzielenie                             |
| `ID`      | Identyfikator                         |
| `NUMBER`  | Liczba                                |
| `,`       | Przecinek                             |
| `LOAD`    | Wczytamoe danych z pliku              |

### Gramatyka przetwarzanego formatu

Symbol początkowy:
```
program
```

Symbole terminalne:
```
'FD'
'BK'
'LT'
'RT'
'PU'
'PD'
'SETCOLOR'
'REPEAT'
'CLEAR'
'LOAD'
'='
'['
']'
'IF'
'ELSE'
'WHILE'
'TO'
'END'
'<>'
'<'
'<='
'>'
'>='
':'
','
'+'
'-'
'*'
'/'
'('
')'
```
Symbole nieterminalne:
```
program
statement
forwardCommand
backwardCommand
leftCommand
rightCommand
penUpCommand
penDownCommand
setColorCommand
repeatCommand
clearCommand
listCommand
ifCommand
whileCommand
functionCommand
assignmentCommand
loadCommand
comparison
expression
functionCall
list
color
variable
functionName
INT
FLOAT
```

Lista produkcji:
```antlr
grammar Logo;

program: statement+;

statement:
    forwardCommand
    | backwardCommand
    | leftCommand
    | rightCommand
    | penUpCommand
    | penDownCommand
    | setColorCommand
    | repeatCommand
    | clearCommand
    | listCommand
    | ifCommand
    | whileCommand
    | functionCommand
    | loadCommand
    | assignmentCommand;

forwardCommand: 'FD' expression ';';
backwardCommand: 'BK' expression ';';
leftCommand: 'LT' expression ';';
rightCommand: 'RT' expression ';';
penUpCommand: 'PU' ';';
penDownCommand: 'PD' ';';
setColorCommand: 'SETCOLOR' color ';';
repeatCommand: 'REPEAT' expression LLIST statement+ RLIST ';';
clearCommand: 'CLEAR' ';';
listCommand: variable EQ LLIST expression (',' expression)* RLIST ';';
ifCommand: 'IF' comparison LLIST statement+ RLIST ( 'ELSE' LLIST statement+ RLIST )?;
whileCommand: 'WHILE' comparison LLIST statement+ RLIST ';';
functionCommand: 'TO' functionName LLIST variable* RLIST statement+ 'END' ';';
loadCommand: 'LOAD' fileName ';';
assignmentCommand: variable EQ expression ';';

comparison:
    expression operator=(EQ | NEQ | LT | LTE | GT | GTE) expression;

expression:
    NUMBER
    | variable
    | list
    | '(' expression ')'
    | expression operator=(MULT | DIV) expression
    | expression operator=(PLUS | MINUS) expression
    | functionCall;

functionCall: functionName '(' (expression (',' expression)*)? ')';

list: LLIST (expression (',' expression)*)? RLIST;

color: NUMBER ',' NUMBER ',' NUMBER;

variable: ':' ID;
functionName: ID;
fileName: FILENAME LOGO;

NUMBER: MINUS? INT | FLOAT;
INT: [0-9]+;
FLOAT: INT '.' [0-9]+;

FILENAME: [a-zA-Z]+;
ID: [a-zA-Z]+;

LLIST: '[';
RLIST: ']';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
EQ: '=';
NEQ: '<>';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';

WS: [ \t\n\r]+ -> skip;

```

### Informacja o stosowanych generatorach skanerów/parserów, pakietach zewnętrznych,

- ANTLR4 - generator parserów, język w którym została napisana składnia
- ImageTk - GUI
- dodatkowe mniejsze pakiety wykorzystywane do implementacji logiki takie jak math
- Cała logika została napisana od zera, bez użycia zewnętrznych bibliotek (takich jak np. turtle)

### Krótka instrukcja obsługi
- Pobranie kodu źródłowego
- uruchomienie pliku main.py z użyciem interpretera języka python
- wpisywanie komend w pole tekstowe widoczne w dolnej części GUI
- w celu ułatwienia korzystania z aplikacji, w przypadku gdy pole tekstowe jest aktywne, strzałki w górę i w dół umożliwiają przechodzenie pomiędzy kolejnymi komendami w historii komend sesji.

### Przykład
![image](https://github.com/fgieracki/pyturtle/assets/48069247/b89d3605-9ad4-43a6-ae75-f9bac167a8f6)
![image](https://github.com/fgieracki/pyturtle/assets/48069247/fdd89961-8207-4ace-8957-f1f7174a730e)
![image](https://github.com/fgieracki/pyturtle/assets/47687092/a04275a6-bf07-4a90-a50f-d3a05ad4daa7)
![image](https://github.com/fgieracki/pyturtle/assets/47687092/74255bc0-7624-4a69-9b7b-68f978b721f7)
![image](https://github.com/fgieracki/pyturtle/assets/47687092/f048ea9f-923e-4513-8af3-c9d146d086ff)

