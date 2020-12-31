grammar BazelBuild;

prog : stat* EOF ; 

stat : NAME '(' arg_list? ')' RN?  # callExp
		| LONG_STRING RN?          # noteExp
		;

arg_list: argument (',' argument)* ','? ;

argument:( NAME '=' )? value;

value: STRING_VALUE    # singleValue
	| '[' val_list ']' # multiValue
	;
	
val_list : STRING_VALUE (',' STRING_VALUE)* ',' ? ;

NAME : [a-zA-Z_] [a-zA-Z_0-9]* ;            

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

