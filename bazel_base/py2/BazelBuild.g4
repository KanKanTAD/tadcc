grammar BazelBuild;

prog : stat* EOF ; 

stat : NAME '(' arg_list? ')' RN? 
		| LONG_STRING RN?
		;

NAME : [a-zA-Z_] [a-zA-Z_0-9]* ;            
arg_list: argument (',' argument)* ','? ;

argument:( NAME '=' )? value;

value: STRING_VALUE
	| '[' val_list ']'
	;
	
val_list : STRING_VALUE (',' STRING_VALUE)* ',' ? ;

STRING_VALUE : '\'' ('\\' . | '\\' RN | ~[\\\r\n\f'])* '\''
			| '"' ('\\' . | '\\' RN | ~[\\\r\n\f'])* '"'
			;

LONG_STRING : '"""' LONG_STRING_ITEM*? '"""' 
			| '\'\'\'' LONG_STRING_ITEM*? '\'\'\''
			;
			
LONG_STRING_ITEM : ~'\\' | '\\' . | '\\' RN ;


RN : ('\r'? '\n') | ('\r') | ('\f' ) ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

CMT: '#' ~[\r\n\f]* -> skip ;

