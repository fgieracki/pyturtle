# Generated from Logo.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,250,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,4,0,50,8,0,11,0,12,0,51,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,70,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,10,4,10,106,8,10,11,10,12,10,107,1,10,1,10,1,10,
        1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,5,12,122,8,12,10,12,
        12,12,125,9,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,4,13,134,8,13,
        11,13,12,13,135,1,13,1,13,1,13,1,13,4,13,142,8,13,11,13,12,13,143,
        1,13,1,13,3,13,148,8,13,1,13,1,13,1,14,1,14,1,14,1,14,4,14,156,8,
        14,11,14,12,14,157,1,14,1,14,1,14,1,15,1,15,1,15,1,15,5,15,167,8,
        15,10,15,12,15,170,9,15,1,15,1,15,4,15,174,8,15,11,15,12,15,175,
        1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,198,8,18,1,18,1,18,1,18,
        1,18,1,18,1,18,5,18,206,8,18,10,18,12,18,209,9,18,1,19,1,19,1,19,
        1,19,1,19,5,19,216,8,19,10,19,12,19,219,9,19,3,19,221,8,19,1,19,
        1,19,1,19,1,20,1,20,1,20,1,20,5,20,230,8,20,10,20,12,20,233,9,20,
        3,20,235,8,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,
        1,22,1,23,1,23,1,23,0,1,36,24,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,0,3,1,0,31,36,1,0,29,30,1,0,27,
        28,258,0,49,1,0,0,0,2,69,1,0,0,0,4,71,1,0,0,0,6,75,1,0,0,0,8,79,
        1,0,0,0,10,83,1,0,0,0,12,87,1,0,0,0,14,90,1,0,0,0,16,93,1,0,0,0,
        18,97,1,0,0,0,20,101,1,0,0,0,22,112,1,0,0,0,24,115,1,0,0,0,26,129,
        1,0,0,0,28,151,1,0,0,0,30,162,1,0,0,0,32,180,1,0,0,0,34,185,1,0,
        0,0,36,197,1,0,0,0,38,210,1,0,0,0,40,225,1,0,0,0,42,238,1,0,0,0,
        44,244,1,0,0,0,46,247,1,0,0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,51,
        1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,1,1,0,0,0,53,70,3,4,2,0,54,
        70,3,6,3,0,55,70,3,8,4,0,56,70,3,10,5,0,57,70,3,12,6,0,58,70,3,14,
        7,0,59,70,3,16,8,0,60,70,3,18,9,0,61,70,3,20,10,0,62,70,3,22,11,
        0,63,70,3,24,12,0,64,70,3,26,13,0,65,70,3,28,14,0,66,70,3,30,15,
        0,67,70,3,38,19,0,68,70,3,32,16,0,69,53,1,0,0,0,69,54,1,0,0,0,69,
        55,1,0,0,0,69,56,1,0,0,0,69,57,1,0,0,0,69,58,1,0,0,0,69,59,1,0,0,
        0,69,60,1,0,0,0,69,61,1,0,0,0,69,62,1,0,0,0,69,63,1,0,0,0,69,64,
        1,0,0,0,69,65,1,0,0,0,69,66,1,0,0,0,69,67,1,0,0,0,69,68,1,0,0,0,
        70,3,1,0,0,0,71,72,5,1,0,0,72,73,3,36,18,0,73,74,5,2,0,0,74,5,1,
        0,0,0,75,76,5,3,0,0,76,77,3,36,18,0,77,78,5,2,0,0,78,7,1,0,0,0,79,
        80,5,4,0,0,80,81,3,36,18,0,81,82,5,2,0,0,82,9,1,0,0,0,83,84,5,5,
        0,0,84,85,3,36,18,0,85,86,5,2,0,0,86,11,1,0,0,0,87,88,5,6,0,0,88,
        89,5,2,0,0,89,13,1,0,0,0,90,91,5,7,0,0,91,92,5,2,0,0,92,15,1,0,0,
        0,93,94,5,8,0,0,94,95,3,42,21,0,95,96,5,2,0,0,96,17,1,0,0,0,97,98,
        5,9,0,0,98,99,3,42,21,0,99,100,5,2,0,0,100,19,1,0,0,0,101,102,5,
        10,0,0,102,103,3,36,18,0,103,105,5,25,0,0,104,106,3,2,1,0,105,104,
        1,0,0,0,106,107,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,109,
        1,0,0,0,109,110,5,26,0,0,110,111,5,2,0,0,111,21,1,0,0,0,112,113,
        5,11,0,0,113,114,5,2,0,0,114,23,1,0,0,0,115,116,3,44,22,0,116,117,
        5,31,0,0,117,118,5,25,0,0,118,123,3,36,18,0,119,120,5,12,0,0,120,
        122,3,36,18,0,121,119,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,
        124,1,0,0,0,124,126,1,0,0,0,125,123,1,0,0,0,126,127,5,26,0,0,127,
        128,5,2,0,0,128,25,1,0,0,0,129,130,5,13,0,0,130,131,3,34,17,0,131,
        133,5,25,0,0,132,134,3,2,1,0,133,132,1,0,0,0,134,135,1,0,0,0,135,
        133,1,0,0,0,135,136,1,0,0,0,136,137,1,0,0,0,137,147,5,26,0,0,138,
        139,5,14,0,0,139,141,5,25,0,0,140,142,3,2,1,0,141,140,1,0,0,0,142,
        143,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,145,1,0,0,0,145,
        146,5,26,0,0,146,148,1,0,0,0,147,138,1,0,0,0,147,148,1,0,0,0,148,
        149,1,0,0,0,149,150,5,2,0,0,150,27,1,0,0,0,151,152,5,15,0,0,152,
        153,3,34,17,0,153,155,5,25,0,0,154,156,3,2,1,0,155,154,1,0,0,0,156,
        157,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,
        160,5,26,0,0,160,161,5,2,0,0,161,29,1,0,0,0,162,163,5,16,0,0,163,
        164,3,46,23,0,164,168,5,25,0,0,165,167,3,44,22,0,166,165,1,0,0,0,
        167,170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,171,1,0,0,0,
        170,168,1,0,0,0,171,173,5,26,0,0,172,174,3,2,1,0,173,172,1,0,0,0,
        174,175,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,
        177,178,5,17,0,0,178,179,5,2,0,0,179,31,1,0,0,0,180,181,3,44,22,
        0,181,182,5,31,0,0,182,183,3,36,18,0,183,184,5,2,0,0,184,33,1,0,
        0,0,185,186,3,36,18,0,186,187,7,0,0,0,187,188,3,36,18,0,188,35,1,
        0,0,0,189,190,6,18,-1,0,190,198,5,21,0,0,191,198,3,44,22,0,192,198,
        3,40,20,0,193,194,5,18,0,0,194,195,3,36,18,0,195,196,5,19,0,0,196,
        198,1,0,0,0,197,189,1,0,0,0,197,191,1,0,0,0,197,192,1,0,0,0,197,
        193,1,0,0,0,198,207,1,0,0,0,199,200,10,2,0,0,200,201,7,1,0,0,201,
        206,3,36,18,3,202,203,10,1,0,0,203,204,7,2,0,0,204,206,3,36,18,2,
        205,199,1,0,0,0,205,202,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,
        207,208,1,0,0,0,208,37,1,0,0,0,209,207,1,0,0,0,210,211,3,46,23,0,
        211,220,5,18,0,0,212,217,3,36,18,0,213,214,5,12,0,0,214,216,3,36,
        18,0,215,213,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,1,0,
        0,0,218,221,1,0,0,0,219,217,1,0,0,0,220,212,1,0,0,0,220,221,1,0,
        0,0,221,222,1,0,0,0,222,223,5,19,0,0,223,224,5,2,0,0,224,39,1,0,
        0,0,225,234,5,25,0,0,226,231,3,36,18,0,227,228,5,12,0,0,228,230,
        3,36,18,0,229,227,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,
        1,0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,234,226,1,0,0,0,234,235,
        1,0,0,0,235,236,1,0,0,0,236,237,5,26,0,0,237,41,1,0,0,0,238,239,
        5,21,0,0,239,240,5,12,0,0,240,241,5,21,0,0,241,242,5,12,0,0,242,
        243,5,21,0,0,243,43,1,0,0,0,244,245,5,20,0,0,245,246,5,24,0,0,246,
        45,1,0,0,0,247,248,5,24,0,0,248,47,1,0,0,0,17,51,69,107,123,135,
        143,147,157,168,175,197,205,207,217,220,231,234
    ]

class LogoParser ( Parser ):

    grammarFileName = "Logo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'FD'", "';'", "'BK'", "'LT'", "'RT'", 
                     "'PU'", "'PD'", "'SETCOLOR'", "'FILL'", "'REPEAT'", 
                     "'CLEAR'", "','", "'IF'", "'ELSE'", "'WHILE'", "'TO'", 
                     "'END'", "'('", "')'", "':'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'['", "']'", "'+'", "'-'", 
                     "'*'", "'/'", "'='", "'<>'", "'<'", "'<='", "'>'", 
                     "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "INT", "FLOAT", "ID", "LLIST", 
                      "RLIST", "PLUS", "MINUS", "MULT", "DIV", "EQ", "NEQ", 
                      "LT", "LTE", "GT", "GTE", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_forwardCommand = 2
    RULE_backwardCommand = 3
    RULE_leftCommand = 4
    RULE_rightCommand = 5
    RULE_penUpCommand = 6
    RULE_penDownCommand = 7
    RULE_setColorCommand = 8
    RULE_fillColorCommand = 9
    RULE_repeatCommand = 10
    RULE_clearCommand = 11
    RULE_listCommand = 12
    RULE_ifCommand = 13
    RULE_whileCommand = 14
    RULE_functionCommand = 15
    RULE_assignmentCommand = 16
    RULE_comparison = 17
    RULE_expression = 18
    RULE_functionCall = 19
    RULE_list = 20
    RULE_color = 21
    RULE_variable = 22
    RULE_functionName = 23

    ruleNames =  [ "program", "statement", "forwardCommand", "backwardCommand", 
                   "leftCommand", "rightCommand", "penUpCommand", "penDownCommand", 
                   "setColorCommand", "fillColorCommand", "repeatCommand", 
                   "clearCommand", "listCommand", "ifCommand", "whileCommand", 
                   "functionCommand", "assignmentCommand", "comparison", 
                   "expression", "functionCall", "list", "color", "variable", 
                   "functionName" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    NUMBER=21
    INT=22
    FLOAT=23
    ID=24
    LLIST=25
    RLIST=26
    PLUS=27
    MINUS=28
    MULT=29
    DIV=30
    EQ=31
    NEQ=32
    LT=33
    LTE=34
    GT=35
    GTE=36
    WS=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogoParser.StatementContext)
            else:
                return self.getTypedRuleContext(LogoParser.StatementContext,i)


        def getRuleIndex(self):
            return LogoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LogoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.statement()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogoParser.T__0) | (1 << LogoParser.T__2) | (1 << LogoParser.T__3) | (1 << LogoParser.T__4) | (1 << LogoParser.T__5) | (1 << LogoParser.T__6) | (1 << LogoParser.T__7) | (1 << LogoParser.T__8) | (1 << LogoParser.T__9) | (1 << LogoParser.T__10) | (1 << LogoParser.T__12) | (1 << LogoParser.T__14) | (1 << LogoParser.T__15) | (1 << LogoParser.T__19) | (1 << LogoParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forwardCommand(self):
            return self.getTypedRuleContext(LogoParser.ForwardCommandContext,0)


        def backwardCommand(self):
            return self.getTypedRuleContext(LogoParser.BackwardCommandContext,0)


        def leftCommand(self):
            return self.getTypedRuleContext(LogoParser.LeftCommandContext,0)


        def rightCommand(self):
            return self.getTypedRuleContext(LogoParser.RightCommandContext,0)


        def penUpCommand(self):
            return self.getTypedRuleContext(LogoParser.PenUpCommandContext,0)


        def penDownCommand(self):
            return self.getTypedRuleContext(LogoParser.PenDownCommandContext,0)


        def setColorCommand(self):
            return self.getTypedRuleContext(LogoParser.SetColorCommandContext,0)


        def fillColorCommand(self):
            return self.getTypedRuleContext(LogoParser.FillColorCommandContext,0)


        def repeatCommand(self):
            return self.getTypedRuleContext(LogoParser.RepeatCommandContext,0)


        def clearCommand(self):
            return self.getTypedRuleContext(LogoParser.ClearCommandContext,0)


        def listCommand(self):
            return self.getTypedRuleContext(LogoParser.ListCommandContext,0)


        def ifCommand(self):
            return self.getTypedRuleContext(LogoParser.IfCommandContext,0)


        def whileCommand(self):
            return self.getTypedRuleContext(LogoParser.WhileCommandContext,0)


        def functionCommand(self):
            return self.getTypedRuleContext(LogoParser.FunctionCommandContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(LogoParser.FunctionCallContext,0)


        def assignmentCommand(self):
            return self.getTypedRuleContext(LogoParser.AssignmentCommandContext,0)


        def getRuleIndex(self):
            return LogoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LogoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.forwardCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.backwardCommand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.leftCommand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.rightCommand()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.penUpCommand()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.penDownCommand()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 59
                self.setColorCommand()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 60
                self.fillColorCommand()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 61
                self.repeatCommand()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 62
                self.clearCommand()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 63
                self.listCommand()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 64
                self.ifCommand()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 65
                self.whileCommand()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 66
                self.functionCommand()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 67
                self.functionCall()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 68
                self.assignmentCommand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForwardCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LogoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LogoParser.RULE_forwardCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForwardCommand" ):
                listener.enterForwardCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForwardCommand" ):
                listener.exitForwardCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForwardCommand" ):
                return visitor.visitForwardCommand(self)
            else:
                return visitor.visitChildren(self)




    def forwardCommand(self):

        localctx = LogoParser.ForwardCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_forwardCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(LogoParser.T__0)
            self.state = 72
            self.expression(0)
            self.state = 73
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BackwardCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LogoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LogoParser.RULE_backwardCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackwardCommand" ):
                listener.enterBackwardCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackwardCommand" ):
                listener.exitBackwardCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBackwardCommand" ):
                return visitor.visitBackwardCommand(self)
            else:
                return visitor.visitChildren(self)




    def backwardCommand(self):

        localctx = LogoParser.BackwardCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_backwardCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(LogoParser.T__2)
            self.state = 76
            self.expression(0)
            self.state = 77
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeftCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LogoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LogoParser.RULE_leftCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeftCommand" ):
                listener.enterLeftCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeftCommand" ):
                listener.exitLeftCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeftCommand" ):
                return visitor.visitLeftCommand(self)
            else:
                return visitor.visitChildren(self)




    def leftCommand(self):

        localctx = LogoParser.LeftCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_leftCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(LogoParser.T__3)
            self.state = 80
            self.expression(0)
            self.state = 81
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RightCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LogoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LogoParser.RULE_rightCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRightCommand" ):
                listener.enterRightCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRightCommand" ):
                listener.exitRightCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRightCommand" ):
                return visitor.visitRightCommand(self)
            else:
                return visitor.visitChildren(self)




    def rightCommand(self):

        localctx = LogoParser.RightCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rightCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(LogoParser.T__4)
            self.state = 84
            self.expression(0)
            self.state = 85
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PenUpCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogoParser.RULE_penUpCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPenUpCommand" ):
                listener.enterPenUpCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPenUpCommand" ):
                listener.exitPenUpCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPenUpCommand" ):
                return visitor.visitPenUpCommand(self)
            else:
                return visitor.visitChildren(self)




    def penUpCommand(self):

        localctx = LogoParser.PenUpCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_penUpCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(LogoParser.T__5)
            self.state = 88
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PenDownCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogoParser.RULE_penDownCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPenDownCommand" ):
                listener.enterPenDownCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPenDownCommand" ):
                listener.exitPenDownCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPenDownCommand" ):
                return visitor.visitPenDownCommand(self)
            else:
                return visitor.visitChildren(self)




    def penDownCommand(self):

        localctx = LogoParser.PenDownCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_penDownCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(LogoParser.T__6)
            self.state = 91
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetColorCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def color(self):
            return self.getTypedRuleContext(LogoParser.ColorContext,0)


        def getRuleIndex(self):
            return LogoParser.RULE_setColorCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetColorCommand" ):
                listener.enterSetColorCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetColorCommand" ):
                listener.exitSetColorCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetColorCommand" ):
                return visitor.visitSetColorCommand(self)
            else:
                return visitor.visitChildren(self)




    def setColorCommand(self):

        localctx = LogoParser.SetColorCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_setColorCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(LogoParser.T__7)
            self.state = 94
            self.color()
            self.state = 95
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FillColorCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def color(self):
            return self.getTypedRuleContext(LogoParser.ColorContext,0)


        def getRuleIndex(self):
            return LogoParser.RULE_fillColorCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFillColorCommand" ):
                listener.enterFillColorCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFillColorCommand" ):
                listener.exitFillColorCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFillColorCommand" ):
                return visitor.visitFillColorCommand(self)
            else:
                return visitor.visitChildren(self)




    def fillColorCommand(self):

        localctx = LogoParser.FillColorCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_fillColorCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(LogoParser.T__8)
            self.state = 98
            self.color()
            self.state = 99
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LogoParser.ExpressionContext,0)


        def LLIST(self):
            return self.getToken(LogoParser.LLIST, 0)

        def RLIST(self):
            return self.getToken(LogoParser.RLIST, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogoParser.StatementContext)
            else:
                return self.getTypedRuleContext(LogoParser.StatementContext,i)


        def getRuleIndex(self):
            return LogoParser.RULE_repeatCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeatCommand" ):
                listener.enterRepeatCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeatCommand" ):
                listener.exitRepeatCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeatCommand" ):
                return visitor.visitRepeatCommand(self)
            else:
                return visitor.visitChildren(self)




    def repeatCommand(self):

        localctx = LogoParser.RepeatCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_repeatCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(LogoParser.T__9)
            self.state = 102
            self.expression(0)
            self.state = 103
            self.match(LogoParser.LLIST)
            self.state = 105 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.statement()
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogoParser.T__0) | (1 << LogoParser.T__2) | (1 << LogoParser.T__3) | (1 << LogoParser.T__4) | (1 << LogoParser.T__5) | (1 << LogoParser.T__6) | (1 << LogoParser.T__7) | (1 << LogoParser.T__8) | (1 << LogoParser.T__9) | (1 << LogoParser.T__10) | (1 << LogoParser.T__12) | (1 << LogoParser.T__14) | (1 << LogoParser.T__15) | (1 << LogoParser.T__19) | (1 << LogoParser.ID))) != 0)):
                    break

            self.state = 109
            self.match(LogoParser.RLIST)
            self.state = 110
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClearCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogoParser.RULE_clearCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClearCommand" ):
                listener.enterClearCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClearCommand" ):
                listener.exitClearCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClearCommand" ):
                return visitor.visitClearCommand(self)
            else:
                return visitor.visitChildren(self)




    def clearCommand(self):

        localctx = LogoParser.ClearCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_clearCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(LogoParser.T__10)
            self.state = 113
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(LogoParser.VariableContext,0)


        def EQ(self):
            return self.getToken(LogoParser.EQ, 0)

        def LLIST(self):
            return self.getToken(LogoParser.LLIST, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LogoParser.ExpressionContext,i)


        def RLIST(self):
            return self.getToken(LogoParser.RLIST, 0)

        def getRuleIndex(self):
            return LogoParser.RULE_listCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListCommand" ):
                listener.enterListCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListCommand" ):
                listener.exitListCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListCommand" ):
                return visitor.visitListCommand(self)
            else:
                return visitor.visitChildren(self)




    def listCommand(self):

        localctx = LogoParser.ListCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_listCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.variable()
            self.state = 116
            self.match(LogoParser.EQ)
            self.state = 117
            self.match(LogoParser.LLIST)
            self.state = 118
            self.expression(0)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LogoParser.T__11:
                self.state = 119
                self.match(LogoParser.T__11)
                self.state = 120
                self.expression(0)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.match(LogoParser.RLIST)
            self.state = 127
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ifstat = None # StatementContext
            self.elsestat = None # StatementContext

        def comparison(self):
            return self.getTypedRuleContext(LogoParser.ComparisonContext,0)


        def LLIST(self, i:int=None):
            if i is None:
                return self.getTokens(LogoParser.LLIST)
            else:
                return self.getToken(LogoParser.LLIST, i)

        def RLIST(self, i:int=None):
            if i is None:
                return self.getTokens(LogoParser.RLIST)
            else:
                return self.getToken(LogoParser.RLIST, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogoParser.StatementContext)
            else:
                return self.getTypedRuleContext(LogoParser.StatementContext,i)


        def getRuleIndex(self):
            return LogoParser.RULE_ifCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfCommand" ):
                listener.enterIfCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfCommand" ):
                listener.exitIfCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfCommand" ):
                return visitor.visitIfCommand(self)
            else:
                return visitor.visitChildren(self)




    def ifCommand(self):

        localctx = LogoParser.IfCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(LogoParser.T__12)
            self.state = 130
            self.comparison()
            self.state = 131
            self.match(LogoParser.LLIST)
            self.state = 133 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 132
                localctx.ifstat = self.statement()
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogoParser.T__0) | (1 << LogoParser.T__2) | (1 << LogoParser.T__3) | (1 << LogoParser.T__4) | (1 << LogoParser.T__5) | (1 << LogoParser.T__6) | (1 << LogoParser.T__7) | (1 << LogoParser.T__8) | (1 << LogoParser.T__9) | (1 << LogoParser.T__10) | (1 << LogoParser.T__12) | (1 << LogoParser.T__14) | (1 << LogoParser.T__15) | (1 << LogoParser.T__19) | (1 << LogoParser.ID))) != 0)):
                    break

            self.state = 137
            self.match(LogoParser.RLIST)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LogoParser.T__13:
                self.state = 138
                self.match(LogoParser.T__13)
                self.state = 139
                self.match(LogoParser.LLIST)
                self.state = 141 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 140
                    localctx.elsestat = self.statement()
                    self.state = 143 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogoParser.T__0) | (1 << LogoParser.T__2) | (1 << LogoParser.T__3) | (1 << LogoParser.T__4) | (1 << LogoParser.T__5) | (1 << LogoParser.T__6) | (1 << LogoParser.T__7) | (1 << LogoParser.T__8) | (1 << LogoParser.T__9) | (1 << LogoParser.T__10) | (1 << LogoParser.T__12) | (1 << LogoParser.T__14) | (1 << LogoParser.T__15) | (1 << LogoParser.T__19) | (1 << LogoParser.ID))) != 0)):
                        break

                self.state = 145
                self.match(LogoParser.RLIST)


            self.state = 149
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(LogoParser.ComparisonContext,0)


        def LLIST(self):
            return self.getToken(LogoParser.LLIST, 0)

        def RLIST(self):
            return self.getToken(LogoParser.RLIST, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogoParser.StatementContext)
            else:
                return self.getTypedRuleContext(LogoParser.StatementContext,i)


        def getRuleIndex(self):
            return LogoParser.RULE_whileCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileCommand" ):
                listener.enterWhileCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileCommand" ):
                listener.exitWhileCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileCommand" ):
                return visitor.visitWhileCommand(self)
            else:
                return visitor.visitChildren(self)




    def whileCommand(self):

        localctx = LogoParser.WhileCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_whileCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(LogoParser.T__14)
            self.state = 152
            self.comparison()
            self.state = 153
            self.match(LogoParser.LLIST)
            self.state = 155 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 154
                self.statement()
                self.state = 157 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogoParser.T__0) | (1 << LogoParser.T__2) | (1 << LogoParser.T__3) | (1 << LogoParser.T__4) | (1 << LogoParser.T__5) | (1 << LogoParser.T__6) | (1 << LogoParser.T__7) | (1 << LogoParser.T__8) | (1 << LogoParser.T__9) | (1 << LogoParser.T__10) | (1 << LogoParser.T__12) | (1 << LogoParser.T__14) | (1 << LogoParser.T__15) | (1 << LogoParser.T__19) | (1 << LogoParser.ID))) != 0)):
                    break

            self.state = 159
            self.match(LogoParser.RLIST)
            self.state = 160
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionName(self):
            return self.getTypedRuleContext(LogoParser.FunctionNameContext,0)


        def LLIST(self):
            return self.getToken(LogoParser.LLIST, 0)

        def RLIST(self):
            return self.getToken(LogoParser.RLIST, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogoParser.VariableContext)
            else:
                return self.getTypedRuleContext(LogoParser.VariableContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogoParser.StatementContext)
            else:
                return self.getTypedRuleContext(LogoParser.StatementContext,i)


        def getRuleIndex(self):
            return LogoParser.RULE_functionCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCommand" ):
                listener.enterFunctionCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCommand" ):
                listener.exitFunctionCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCommand" ):
                return visitor.visitFunctionCommand(self)
            else:
                return visitor.visitChildren(self)




    def functionCommand(self):

        localctx = LogoParser.FunctionCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_functionCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(LogoParser.T__15)
            self.state = 163
            self.functionName()
            self.state = 164
            self.match(LogoParser.LLIST)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LogoParser.T__19:
                self.state = 165
                self.variable()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 171
            self.match(LogoParser.RLIST)
            self.state = 173 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 172
                self.statement()
                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogoParser.T__0) | (1 << LogoParser.T__2) | (1 << LogoParser.T__3) | (1 << LogoParser.T__4) | (1 << LogoParser.T__5) | (1 << LogoParser.T__6) | (1 << LogoParser.T__7) | (1 << LogoParser.T__8) | (1 << LogoParser.T__9) | (1 << LogoParser.T__10) | (1 << LogoParser.T__12) | (1 << LogoParser.T__14) | (1 << LogoParser.T__15) | (1 << LogoParser.T__19) | (1 << LogoParser.ID))) != 0)):
                    break

            self.state = 177
            self.match(LogoParser.T__16)
            self.state = 178
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(LogoParser.VariableContext,0)


        def EQ(self):
            return self.getToken(LogoParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(LogoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LogoParser.RULE_assignmentCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentCommand" ):
                listener.enterAssignmentCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentCommand" ):
                listener.exitAssignmentCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentCommand" ):
                return visitor.visitAssignmentCommand(self)
            else:
                return visitor.visitChildren(self)




    def assignmentCommand(self):

        localctx = LogoParser.AssignmentCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignmentCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.variable()
            self.state = 181
            self.match(LogoParser.EQ)
            self.state = 182
            self.expression(0)
            self.state = 183
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.operator = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LogoParser.ExpressionContext,i)


        def EQ(self):
            return self.getToken(LogoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(LogoParser.NEQ, 0)

        def LT(self):
            return self.getToken(LogoParser.LT, 0)

        def LTE(self):
            return self.getToken(LogoParser.LTE, 0)

        def GT(self):
            return self.getToken(LogoParser.GT, 0)

        def GTE(self):
            return self.getToken(LogoParser.GTE, 0)

        def getRuleIndex(self):
            return LogoParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = LogoParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.expression(0)
            self.state = 186
            localctx.operator = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogoParser.EQ) | (1 << LogoParser.NEQ) | (1 << LogoParser.LT) | (1 << LogoParser.LTE) | (1 << LogoParser.GT) | (1 << LogoParser.GTE))) != 0)):
                localctx.operator = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 187
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogoParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DefExpContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(LogoParser.NUMBER, 0)
        def list_(self):
            return self.getTypedRuleContext(LogoParser.ListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefExp" ):
                listener.enterDefExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefExp" ):
                listener.exitDefExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefExp" ):
                return visitor.visitDefExp(self)
            else:
                return visitor.visitChildren(self)


    class PlusMinusContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogoParser.ExpressionContext
            super().__init__(parser)
            self.operator = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LogoParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(LogoParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(LogoParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlusMinus" ):
                listener.enterPlusMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlusMinus" ):
                listener.exitPlusMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlusMinus" ):
                return visitor.visitPlusMinus(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(LogoParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesisExpr" ):
                listener.enterParenthesisExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesisExpr" ):
                listener.exitParenthesisExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesisExpr" ):
                return visitor.visitParenthesisExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssExpContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(LogoParser.VariableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssExp" ):
                listener.enterAssExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssExp" ):
                listener.exitAssExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssExp" ):
                return visitor.visitAssExp(self)
            else:
                return visitor.visitChildren(self)


    class MultDivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogoParser.ExpressionContext
            super().__init__(parser)
            self.operator = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LogoParser.ExpressionContext,i)

        def MULT(self):
            return self.getToken(LogoParser.MULT, 0)
        def DIV(self):
            return self.getToken(LogoParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultDiv" ):
                listener.enterMultDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultDiv" ):
                listener.exitMultDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultDiv" ):
                return visitor.visitMultDiv(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LogoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LogoParser.NUMBER]:
                localctx = LogoParser.DefExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 190
                self.match(LogoParser.NUMBER)
                pass
            elif token in [LogoParser.T__19]:
                localctx = LogoParser.AssExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 191
                self.variable()
                pass
            elif token in [LogoParser.LLIST]:
                localctx = LogoParser.DefExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 192
                self.list_()
                pass
            elif token in [LogoParser.T__17]:
                localctx = LogoParser.ParenthesisExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 193
                self.match(LogoParser.T__17)
                self.state = 194
                self.expression(0)
                self.state = 195
                self.match(LogoParser.T__18)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 205
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = LogoParser.MultDivContext(self, LogoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 199
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 200
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LogoParser.MULT or _la==LogoParser.DIV):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 201
                        self.expression(3)
                        pass

                    elif la_ == 2:
                        localctx = LogoParser.PlusMinusContext(self, LogoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 202
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 203
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LogoParser.PLUS or _la==LogoParser.MINUS):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 204
                        self.expression(2)
                        pass

             
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionName(self):
            return self.getTypedRuleContext(LogoParser.FunctionNameContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LogoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LogoParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = LogoParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.functionName()
            self.state = 211
            self.match(LogoParser.T__17)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogoParser.T__17) | (1 << LogoParser.T__19) | (1 << LogoParser.NUMBER) | (1 << LogoParser.LLIST))) != 0):
                self.state = 212
                self.expression(0)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LogoParser.T__11:
                    self.state = 213
                    self.match(LogoParser.T__11)
                    self.state = 214
                    self.expression(0)
                    self.state = 219
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 222
            self.match(LogoParser.T__18)
            self.state = 223
            self.match(LogoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLIST(self):
            return self.getToken(LogoParser.LLIST, 0)

        def RLIST(self):
            return self.getToken(LogoParser.RLIST, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LogoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LogoParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = LogoParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(LogoParser.LLIST)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogoParser.T__17) | (1 << LogoParser.T__19) | (1 << LogoParser.NUMBER) | (1 << LogoParser.LLIST))) != 0):
                self.state = 226
                self.expression(0)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LogoParser.T__11:
                    self.state = 227
                    self.match(LogoParser.T__11)
                    self.state = 228
                    self.expression(0)
                    self.state = 233
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 236
            self.match(LogoParser.RLIST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(LogoParser.NUMBER)
            else:
                return self.getToken(LogoParser.NUMBER, i)

        def getRuleIndex(self):
            return LogoParser.RULE_color

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColor" ):
                listener.enterColor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColor" ):
                listener.exitColor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColor" ):
                return visitor.visitColor(self)
            else:
                return visitor.visitChildren(self)




    def color(self):

        localctx = LogoParser.ColorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_color)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(LogoParser.NUMBER)
            self.state = 239
            self.match(LogoParser.T__11)
            self.state = 240
            self.match(LogoParser.NUMBER)
            self.state = 241
            self.match(LogoParser.T__11)
            self.state = 242
            self.match(LogoParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LogoParser.ID, 0)

        def getRuleIndex(self):
            return LogoParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = LogoParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(LogoParser.T__19)
            self.state = 245
            self.match(LogoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LogoParser.ID, 0)

        def getRuleIndex(self):
            return LogoParser.RULE_functionName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionName" ):
                listener.enterFunctionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionName" ):
                listener.exitFunctionName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionName" ):
                return visitor.visitFunctionName(self)
            else:
                return visitor.visitChildren(self)




    def functionName(self):

        localctx = LogoParser.FunctionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_functionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(LogoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




