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
functionCommand: 'TO' functionName LLIST variable* RLIST statement+ 'END' functionName ';';
assignmentCommand: variable EQ expression ';';


comparison:
    expression operator=(EQ | NEQ | LT | LTE | GT | GTE) expression;

expression:
    NUMBER # DefExp
    | variable # DefExp
    | list # DefExp
    | '(' expression ')' # ParenthesisExpr
    | expression operator=(MULT | DIV) expression # MultDiv
    | expression operator=(PLUS | MINUS) expression # PlusMinus
    | functionCall # DefExp;

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
