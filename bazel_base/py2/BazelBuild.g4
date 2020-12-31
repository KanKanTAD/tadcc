grammar BazelBuild;

prog: stat* ;

stat:call_exp RN
	| single_exp 
	;

single_exp:STRING;

call_exp:NAME '(' argument_list? ')' ; 

argument_list: argument (',' argument)* ','? ;

argument: (NAME '=' )? value_exp;

value_exp : STRING 			   # signle_value
	| '[' (str_list ','?)? ']' # multi_value
	;

str_list:STRING (',' STRING )*;

NAME : [a-zA-Z_][a-zA-Z_0-9]* ;
NEWLINE : RN ;

STRING :
	SHORT_STRING
	|LONG_STRING
	;

KEY_WORD:LOAD
	|EXPORTS
	|WORKSPACE
	|LICENSES
	|PACKAGE_GROUP
	;

SKIP_ : RN | SPACES | COMMENT -> skip();

/*
 * fragments
 */
fragment LOAD : 'load';
fragment EXPORTS : 'exports_files';
fragment WORKSPACE : 'workspace';
fragment LICENSES : 'licenses';
fragment PACKAGE_GROUP : 'package_group';

fragment RN:
	('\r'? '\n')|('\r')|('\f');

fragment SHORT_STRING
 : '\'' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f'] )* '\''
 | '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f"] )* '"'
 ;

fragment LONG_STRING
 : '\'\'\'' LONG_STRING_ITEM*? '\'\'\''
 | '"""' LONG_STRING_ITEM*? '"""'
 ;

fragment LONG_STRING_ITEM
 : LONG_STRING_CHAR
 | STRING_ESCAPE_SEQ
 ;

fragment LONG_STRING_CHAR
 : ~'\\'
 ;

fragment STRING_ESCAPE_SEQ
 : '\\' .
 | '\\' NEWLINE
 ;

fragment SHORT_BYTES
 : '\'' ( SHORT_BYTES_CHAR_NO_SINGLE_QUOTE | BYTES_ESCAPE_SEQ )* '\''
 | '"' ( SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE | BYTES_ESCAPE_SEQ )* '"'
 ;

fragment LONG_BYTES
 : '\'\'\'' LONG_BYTES_ITEM*? '\'\'\''
 | '"""' LONG_BYTES_ITEM*? '"""'
 ;

/// longbytesitem  ::=  longbyteschar | bytesescapeseq
fragment LONG_BYTES_ITEM
 : LONG_BYTES_CHAR
 | BYTES_ESCAPE_SEQ
 ;

/// shortbyteschar ::=  <any ASCII character except "\" or newline or the quote>
fragment SHORT_BYTES_CHAR_NO_SINGLE_QUOTE
 : [\u0000-\u0009]
 | [\u000B-\u000C]
 | [\u000E-\u0026]
 | [\u0028-\u005B]
 | [\u005D-\u007F]
 ;

fragment SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE
 : [\u0000-\u0009]
 | [\u000B-\u000C]
 | [\u000E-\u0021]
 | [\u0023-\u005B]
 | [\u005D-\u007F]
 ;

/// longbyteschar  ::=  <any ASCII character except "\">
fragment LONG_BYTES_CHAR
 : [\u0000-\u005B]
 | [\u005D-\u007F]
 ;

/// bytesescapeseq ::=  "\" <any ASCII character>
fragment BYTES_ESCAPE_SEQ
 : '\\' [\u0000-\u007F]
 ;

fragment SPACES
 : [ \t]+
 ;

fragment COMMENT
 : '#' ~[\r\n\f]*
 ;
