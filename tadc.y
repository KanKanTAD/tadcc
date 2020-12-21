%{
%}

%token EOS
%token Symbol 
%token ADD SUB MUL DIV MOD
%token A_STATIC A_EXTERN A_AUTO A_CONST
%token ORM_ID
%%
programs:
		|programs statement EOS
		|
		;

mem_desc:A_STATIC 
		|A_EXTERN
		|
		;

function_dec:mem_desc type_dec Symbol '(' args_dec ')' EOS
			;

function_define:mem_desc type_dec Symbol '(' args_define ')' '{' function_body '}'
			   ;


%%
