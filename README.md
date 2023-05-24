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

NUMBER: MINUS? INT | FLOAT;
INT: [0-9]+;
FLOAT: INT '.' [0-9]+;

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

### Krótka instrukcja obsługi,

### Przykład
