%{
%}

%token EOS
%token Symbol 
%token ADD SUB MUL DIV MOD
%token A_STATIC A_EXTERN A_AUTO A_CONST
%token F_VIRTUAL F_OVERRIDE F_NOEXCEPT
%token B_TRUE B_FALSE
%token D_CLASS D_STRUCT D_UNION D_ENUM
%token T_INT T_LONG T_BOOL T_CHAR T_UNSIGNED T_FLOAT T_DOUBLE
%token P_NULL
%token ORM_ID ORM_FOREIGN 
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
