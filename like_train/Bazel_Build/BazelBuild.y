grammar BazelBuild;

prog: stat+ ;

stat:load_exp 
	|target_exp
	|LongString
	;

load_exp : Load OpenParen str_items CloseParen ;

target_exp: Symbol OpenParen assign_items CloseParen ;

assign_items: assign_exp
			| assign_exp ',' assign_items
			;

assign_exp: left=Symbol '=' right=value_exp
		  ;

value_exp:ShortString
		 | list_exp
		 ;

list_exp : OpenBracket CloseBracket 
		 |OpenBracket str_items CloseBracket
		 ;

str_items : ShortString
		  | ShortString ',' str_items
		  ;

Symbol : [a-zA-Z_]+[a-zA-Z_0-9]*
	   ;

Comment : '#' ~[\r\n\f]* -> skip ;

WS : [\t\r\n]+ -> skip 
   ;

ShortString : '\'' ('\\' (RN | .) | ~[\\\r\n'])* '\''
			| '"' ('\\' (RN | .) | ~[\\\r\n"])* '"'
			;

LongString : '\'\'\'' LongStringItem*? '\'\'\''
		   | '"""' LongStringItem*? '"""'
		   ;

LongStringItem : ~'\\'
			   | '\\' (RN | .)
			   ;

RN : '\r'? '\n' ;

// OpenClose

OpenParen : '('
		  ;

CloseParen : ')'
		   ;

OpenBracket : '['
			;

CloseBracket : ']'
			 ;

// Keywords
Load : 'load'
	 ;



