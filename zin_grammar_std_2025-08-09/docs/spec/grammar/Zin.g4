grammar Zin;

// Parser rules
program       : (declaration | statement)* EOF ;

declaration   : functionDecl
              | varDecl
              | structDecl
              | importDecl
              ;

functionDecl  : (K_FONCTION|K_FN) IDENT '(' params? ')' returnType? block ;
params        : param (',' param)* ;
param         : typeSpec IDENT ;
returnType    : '->' typeSpec ;

varDecl       : typeSpec IDENT ('=' expression)? terminator ;

structDecl    : (K_STRUCTURE|K_STRUCT) IDENT '{' structField* '}' ;
structField   : typeSpec IDENT terminator ;

importDecl    : (K_IMPORTE|K_IMPORTER|K_IMPORT) modulePath terminator ;
modulePath    : IDENT ('.' IDENT)* ;

statement     : block
              | ifStmt
              | whileStmt
              | forStmt
              | returnStmt
              | printStmt
              | sleepStmt
              | exprStmt
              ;

block         : '{' statement* '}' ;

ifStmt        : (K_SI|K_IF) '(' expression ')' block ((K_SINON|K_ELSE) block)? ;

whileStmt     : (K_TANTQUE|K_WHILE) '(' expression ')' block ;

forStmt       : (K_POUR|K_FOR) IDENT (K_DE|K_FROM) expression (K_A|K_TO) expression block ;

returnStmt    : (K_RETOURNE|K_RETURN) expression? terminator ;

printStmt     : (K_AFFICHE|K_PRINT) expression terminator ;
sleepStmt     : (K_PAUSE|K_SLEEP) expression terminator ;

exprStmt      : expression terminator ;

terminator    : ';'? ;

// Expressions
expression    : assignment ;
assignment    : logic_or (('='|'+='|'-='|'*='|'/=') assignment)? ;
logic_or      : logic_and ('||' logic_and)* ;
logic_and     : equality ('&&' equality)* ;
equality      : comparison (('=='|'!=') comparison)* ;
comparison    : addition (('>'|'>='|'<'|'<=') addition)* ;
addition      : multiplication (('+'|'-') multiplication)* ;
multiplication: unary (('*'|'/'|'%') unary)* ;
unary         : ('!'|'-'|'+') unary | call ;
call          : primary ('(' args? ')')* ;
args          : expression (',' expression)* ;
primary       : NUMBER | STRING | boolean | IDENT | '(' expression ')' ;
boolean       : K_TRUE | K_VRAI | K_FALSE | K_FAUX ;
typeSpec      : K_NUM_T | K_NOMBRE | K_STR_T | K_TEXTE | K_BOOL_T | K_BOOLEEN | IDENT ;

// Lexer rules
K_SI      : 'si' ;
K_IF      : 'if' ;
K_SINON   : 'sinon' ;
K_ELSE    : 'else' ;

K_FONCTION: 'fonction' ;
K_FN      : 'fn' ;
K_RETOURNE: 'retourne' ;
K_RETURN  : 'return' ;

K_POUR    : 'pour' ;
K_FOR     : 'for' ;
K_DE      : 'de' ;
K_FROM    : 'from' ;
K_A       : 'à' | 'a' ;
K_TO      : 'to' ;

K_TANTQUE : 'tantque' ;
K_WHILE   : 'while' ;

K_AFFICHE : 'affiche' ;
K_PRINT   : 'print' ;

K_PAUSE   : 'pause' ;
K_SLEEP   : 'sleep' ;

K_IMPORTE   : 'importe' ;
K_IMPORTER  : 'importer' ;
K_IMPORT    : 'import' ;

K_STRUCTURE : 'structure' ;
K_STRUCT    : 'struct' ;

K_TRUE    : 'true' ;
K_VRAI    : 'vrai' ;
K_FALSE   : 'false' ;
K_FAUX    : 'faux' ;

K_NOMBRE  : 'nombre' ;
K_NUM_T   : 'num' ;
K_TEXTE   : 'texte' ;
K_STR_T   : 'str' ;
K_BOOLEEN : 'booleen' | 'booléen' ;
K_BOOL_T  : 'bool' ;

IDENT     : [A-Za-z_][A-Za-z0-9_]* ;
NUMBER    : '0' | [1-9][0-9]* ('.' [0-9]+)? | '0x' [0-9a-fA-F]+ ;
STRING    : '"' ( '\\"' | '\\\\' | '\\n' | '\\t' | '\\r' | ~["\\] )* '"' ;

LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT: '/*' .*? '*/' -> skip ;
WS        : [ \t\r\n]+ -> skip ;
