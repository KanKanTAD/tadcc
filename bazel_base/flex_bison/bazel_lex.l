%{

%}

%%
.* {return ANY;}

[a-zA-Z_]+[a-zA-Z_0-9]* {return SYMBOL;}

; { return EOL;}

'"""' {return THREE_DQ;}

'\'\'\'' {return THREE_SQ;}

%%
