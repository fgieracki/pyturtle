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
    | functionCommand;

forwardCommand: 'FD' expression ';';
backwardCommand: 'BK' expression ';';
leftCommand: 'LT' expression ';';
rightCommand: 'RT' expression ';';
penUpCommand: 'PU' ';';
penDownCommand: 'PD' ';';
setColorCommand: 'SETCOLOR' color ';';
repeatCommand: 'REPEAT' expression '[' statement+ ']' ';';
clearCommand: 'CLEAR' ';';
listCommand: LIST variable '=' '[' expression (',' expression)* ']' ';';
ifCommand: 'IF' comparison '[' statement+ ']' ( 'ELSE' '[' statement+ ']' )?;
whileCommand: 'WHILE' comparison '[' statement+ ']' ';';
functionCommand: 'TO' functionName '[' variable* ']' statement+ 'END' functionName ';';

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

list: '[' (expression (',' expression)*)? ']';

color: NUMBER ',' NUMBER ',' NUMBER;

variable: ':' ID;
functionName: ID;

NUMBER: '-'? INT | FLOAT;
INT: [0-9]+;
FLOAT: INT '.' [0-9]+;

ID: [a-zA-Z]+;

LIST: '[';
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