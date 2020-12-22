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

"bool" {return T_BOOL;}
"int" {return T_INT;}
"long" {return T_LONG;}
"char" {return T_CHAR;}
"unsigned" {return T_UNSIGNED;}
"float" {return T_FLOAT;}
"double" {return T_DOUBLE;}

"class" {return D_CLASS;}
"struct" {return D_STRUCT;}
"union" {return D_UNION;}
"enum" {return D_ENUM;}

"virtual" {return F_VIRTUAL;}
"override" {return F_OVERRIDE;}

"true" {return B_TRUE;}
"false" {return B_FALSE;}

"nullptr" {return P_NULL;}

"static" {return A_STATIC;}
"extern" {return A_EXTERN;}
"auto" {return A_AUTO;}
"const" {return A_CONST;}

"__orm_id__" {return ORM_ID;}
"__orm_foreign__" {return ORM_FOREIGN;}
%%
