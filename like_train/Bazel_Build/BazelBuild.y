grammar BazelBuild;

prog: stat+ ;

stat:load_exp # LoadStat
	|target_exp # TargetStat
	|LongString # LongStrStat
	;

load_exp : Load OpenParen str_items CloseParen 
		 ;

target_exp: Symbol OpenParen assign_items CloseParen
		  ;

assign_items: assign_exp # SingleAttr
			| assign_exp ',' assign_items # MultiAttr
			;

assign_exp: left=Symbol '=' right=value_exp
		  ;

value_exp:ShortString # SingleValue
		 | list_exp #ListValue
		 ;

list_exp : OpenBracket CloseBracket  # EmptyListValue
		 |OpenBracket str_items CloseBracket # NoEmptyListValue
		 ;

str_items : ShortString # SingleShortString
		  | ShortString ',' str_items # MultiShortString
		  ;

Symbol : [a-zA-Z_]+[a-zA-Z_0-9]*
	   ;

Comment : '#' ~[\r\n\f]* -> skip ;

WS : [ \t\r\n]+ -> skip 
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



