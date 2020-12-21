NUM [0-9]+
SYM [a-zA-Z_]+[a-zA-Z_0-9]*
FLOAT (((NUM)?\.(NUM))|((NUM)\.(NUM)?))((E|e)[+-]?(NUM))
%{
%}

%%
SYM { return Symbol;}
NUM {return INT_VALUE;}
NUM(L|l) {return LONG_VALUE;}
FLOAT {return DOUBLE_VALUE;}
FLOAT(F|f) {return FLOAT_VALUE;}

"static" {return A_STATIC;}
"extern" {return A_EXTERN;}
"__orm_id__" {return ORM_ID;}
"__orm_foreign__" {return ORM_FOREIGN;}
%%
