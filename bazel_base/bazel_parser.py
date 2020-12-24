"""
Symbol = r'[a-zA-Z_]+[a-zA-Z_0-9]*'
Assign = '='
Open_Brackets = '('
Close_Brackets = ')'

Open_List='['
Close_List=']'

Transferred = r'\'

Str_Tag='["']'

Comma = ','

Key_Load='load'
InnerStringValue= (.*(\\"')*)*
StringValue = r'("(InnerStringValue)*")|('(InnerStringValue)*')'
ListValue=r'\[(StringValue Comma)*\]'

Value = ListValue | StringValue;

assign_exp = Symbol Assign Value;

taget_exp = 'name' Assign Value;

rule_exp = Symbol Open_Brackets Close_Brackets




"""
