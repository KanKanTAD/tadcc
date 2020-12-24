"""
Symbol = r'[a-zA-Z_]+[a-zA-Z_0-9]*'
Assign = '='
Open_Brackets = '('
Close_Brackets = ')'

Open_List='['
Close_List=']'

Transferred = r'\'

Open_Commit=r'/*'
Close_Commit=r'*/'

Str_Tag='["']'

Key_Load='load'

Commit_Line = '#.*\n'

InnerStringValue= (.*(\\"')*)*
StringValue = r'("(InnerStringValue)*")|('(InnerStringValue)*')'
ListValue=r'\[(StringValue Comma)*\]'

Value = ListValue | StringValue;

StringList_1_m_prime = |
            StringList_1_m_prime ',' StringValue
            ;

StringList_0_m = 
            |StringValue StringList_1_m_prime
            ;

assign_exp = Symbol Assign Value;

assign_exp_list = |
            assign_exp_list assign_exp ','
            ;

rule_exp = Symbol Open_Brackets assign_exp_list Close_Brackets

load_exp = Key_Load Open_Brackets  Close_Brackets

blkstr_exp = ''' .* ''' 
        | """ .* """
        ;

statement = rule_exp
        |load_exp
        |blkstr_exp
        ;
programs:
        |programs statement
        ;



"""


class FileInfo:
    def __init__(self, ctx: List[str]):
        self.ctx = ctx
        self.line = 0
        self.column = 0
        self.idx = 0

    def __calcTotalChars(self) -> int:
        pass

    def getTotalChars(self) -> int:
        pass

    def putIdx(self, idx):
        pass

    def __str__(self):
        pass


class TokenMaster:
    @staticmethod
    def split_line(content: str) -> List[str]:
        res = []
        begin = 0
        for i in range(len(content)):
            if content[i] == '\n':
                res.append(content[begin:i+1])
                begin = i+1
        return res

    def __init__(self, content: str):
        ctx = TokenMaster.split_line(content)
        self.__info = FileInfo(ctx)
        self.__info_bak = FileInfo(ctx)

    def __str__(self) -> str:
        return str(self.__info_bak)

    def isEnd(self) -> bool:
        pass

    def notEnd(self) -> bool:
        return not self.isEnd()

    def next(self) -> str:
        pass

    def skipChar(self, chars: str) -> bool:
        pass

    def matchBegin(self):
        self.__idx = self.__idx_back

    def matchEnd(self):
        self.__idx_back = self.__idx


class ParseUtil:
    ord_a = ord('a')
    ord_z = ord('z')
    ord_A = ord('A')
    ord_Z = ord('Z')
    ord_0 = ord('0')
    ord_9 = ord('9')
    ord__ = ord('_')

    @staticmethod
    def isMatch_n(c: str) -> bool:
        return c in ' \n\t\r'

    @staticmethod
    def isMatch_s(c: str) -> bool:
        return c in '~`!@#$%^&*()-+={}[]|\\:;\'"<>,./?'

    @staticmethod
    def isMatch_d(c: str) -> bool:
        o_c = ord(c)
        if ord_0 <= o_c <= ord_9:
            return True
        return False

    @staticmethod
    def isMatch_w(c: str) -> bool:
        o_c = ord(c)
        if ord_a <= o_c <= ord_z or ord_A <= o_c <= ord_Z or o_c == ord__:
            return True
        return False

    @staticmethod
    def isMatch_wd(c: str) -> bool:
        return ParseUtil.isMatch_d(c) or ParseUtil.isMatch_w(c)


class BazelParser:

    def __init__(self):
        self.__token = TokenMaster()

    def _match_linecommet(self) -> bool, str:
        pass

    def _match_symbol(self) -> bool, str:
        res = ''
        self.__token.matchBegin()
        if self.__token.isEnd():
            return False, ''
        while self.__token.notEnd():
            c = self.__token.next()
            if ParseUtil.isMatch_n(c):
                continue
            if not ParseUtil.isMatch_w(c):
                return False, ''
            else:
                res += c
                break
        while self.__token.notEnd():
            c = self.__token.next()
            if not ParseUtil.isMatch_wd(c):
                break
            else:
                res += c
        self.__token.matchEnd()
        return True, res

    def __match_sign(self, sign) -> bool, str:
        self.__token.matchBegin()
        while self.__token.notEnd():
            c = self.__token.next()
            if c == sign:
                self.__token.matchEnd()
                return True, sign
        return False, ''

    def _match_open_brackets(self) -> bool, str:
        return self.__match_sign('(')

    def _match_close_brackets(self) -> bool, str:
        return self.__match_sign(')')

    def _match_open_list(self) -> bool, str:
        return self.__match_sign('[')

    def _match_close_list(self) -> bool, str:
        return self.__match_sign(']')

    def _match_str_value(self) -> bool, str:
        self.__token.matchBegin()
        if self.__token.isEnd():
            return False, ''
        while self.__token.notEnd():
            pass
