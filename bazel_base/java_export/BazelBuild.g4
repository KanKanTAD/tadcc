grammar BazelBuild;

prog :
	stat* ;

stat:ID '(' arglist? ')' Newline*?
		;

arglist: argument ( ',' argument )*? ','?
		;

argument: ( ID '=' ) value ;

value : single_value | multi_value ;

multi_value:'[' val_list? ']'
	;

val_list: single_value ( ',' single_value )*? ','? 
		;

single_value: StringValue
		;

ID: [a-zA-Z_] [a-zA-Z_0-9]*
		;

StringValue : ( '"' ('\\"' | ~[\r\n\f"])*? '"'
		| '\'' ('\\\'' | ~[\r\n\f'])*? '\'')
		;


Whitespace
	:    [ \t]+
		-> skip 
	;

Newline
	:   ( '\r' '\n'?
	|    '\n'
	|    '\f'
	)
		-> skip
	;

BlockComment:
	('"""' .*? '"""'
	| '\'\'\'' .*? '\'\'\''
	)
		-> skip
	;

LineComment
	:   '#' ~[\r\n\f]*
	-> skip
	;
