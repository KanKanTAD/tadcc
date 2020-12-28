%{

%}

%token ANY
%token THREE_DQ THREE_SQ
%token EOL 
%token SYMBOL
%start bazel_build
%%

bazel_build:
		   |statement bazel_build
		   ;

statement:block_commit
		 |load_exp
		 |target_exp
		 ;

block_commit:THREE_SQ ANY THREE_SQ
			|THREE_DQ ANY THREE_DQ
			;
load_exp:'load' '(' ')'
%%
