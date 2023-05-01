# Generated from Logo.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LogoParser import LogoParser
else:
    from LogoParser import LogoParser

# This class defines a complete listener for a parse tree produced by LogoParser.
class LogoListener(ParseTreeListener):

    # Enter a parse tree produced by LogoParser#program.
    def enterProgram(self, ctx:LogoParser.ProgramContext):
        pass

    # Exit a parse tree produced by LogoParser#program.
    def exitProgram(self, ctx:LogoParser.ProgramContext):
        pass


    # Enter a parse tree produced by LogoParser#statement.
    def enterStatement(self, ctx:LogoParser.StatementContext):
        pass

    # Exit a parse tree produced by LogoParser#statement.
    def exitStatement(self, ctx:LogoParser.StatementContext):
        pass


    # Enter a parse tree produced by LogoParser#forwardCommand.
    def enterForwardCommand(self, ctx:LogoParser.ForwardCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#forwardCommand.
    def exitForwardCommand(self, ctx:LogoParser.ForwardCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#backwardCommand.
    def enterBackwardCommand(self, ctx:LogoParser.BackwardCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#backwardCommand.
    def exitBackwardCommand(self, ctx:LogoParser.BackwardCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#leftCommand.
    def enterLeftCommand(self, ctx:LogoParser.LeftCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#leftCommand.
    def exitLeftCommand(self, ctx:LogoParser.LeftCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#rightCommand.
    def enterRightCommand(self, ctx:LogoParser.RightCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#rightCommand.
    def exitRightCommand(self, ctx:LogoParser.RightCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#penUpCommand.
    def enterPenUpCommand(self, ctx:LogoParser.PenUpCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#penUpCommand.
    def exitPenUpCommand(self, ctx:LogoParser.PenUpCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#penDownCommand.
    def enterPenDownCommand(self, ctx:LogoParser.PenDownCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#penDownCommand.
    def exitPenDownCommand(self, ctx:LogoParser.PenDownCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#setColorCommand.
    def enterSetColorCommand(self, ctx:LogoParser.SetColorCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#setColorCommand.
    def exitSetColorCommand(self, ctx:LogoParser.SetColorCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#fillColorCommand.
    def enterFillColorCommand(self, ctx:LogoParser.FillColorCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#fillColorCommand.
    def exitFillColorCommand(self, ctx:LogoParser.FillColorCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#repeatCommand.
    def enterRepeatCommand(self, ctx:LogoParser.RepeatCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#repeatCommand.
    def exitRepeatCommand(self, ctx:LogoParser.RepeatCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#clearCommand.
    def enterClearCommand(self, ctx:LogoParser.ClearCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#clearCommand.
    def exitClearCommand(self, ctx:LogoParser.ClearCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#listCommand.
    def enterListCommand(self, ctx:LogoParser.ListCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#listCommand.
    def exitListCommand(self, ctx:LogoParser.ListCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#ifCommand.
    def enterIfCommand(self, ctx:LogoParser.IfCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#ifCommand.
    def exitIfCommand(self, ctx:LogoParser.IfCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#whileCommand.
    def enterWhileCommand(self, ctx:LogoParser.WhileCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#whileCommand.
    def exitWhileCommand(self, ctx:LogoParser.WhileCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#functionCommand.
    def enterFunctionCommand(self, ctx:LogoParser.FunctionCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#functionCommand.
    def exitFunctionCommand(self, ctx:LogoParser.FunctionCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#assignmentCommand.
    def enterAssignmentCommand(self, ctx:LogoParser.AssignmentCommandContext):
        pass

    # Exit a parse tree produced by LogoParser#assignmentCommand.
    def exitAssignmentCommand(self, ctx:LogoParser.AssignmentCommandContext):
        pass


    # Enter a parse tree produced by LogoParser#comparison.
    def enterComparison(self, ctx:LogoParser.ComparisonContext):
        pass

    # Exit a parse tree produced by LogoParser#comparison.
    def exitComparison(self, ctx:LogoParser.ComparisonContext):
        pass


    # Enter a parse tree produced by LogoParser#DefExp.
    def enterDefExp(self, ctx:LogoParser.DefExpContext):
        pass

    # Exit a parse tree produced by LogoParser#DefExp.
    def exitDefExp(self, ctx:LogoParser.DefExpContext):
        pass


    # Enter a parse tree produced by LogoParser#PlusMinus.
    def enterPlusMinus(self, ctx:LogoParser.PlusMinusContext):
        pass

    # Exit a parse tree produced by LogoParser#PlusMinus.
    def exitPlusMinus(self, ctx:LogoParser.PlusMinusContext):
        pass


    # Enter a parse tree produced by LogoParser#ParenthesisExpr.
    def enterParenthesisExpr(self, ctx:LogoParser.ParenthesisExprContext):
        pass

    # Exit a parse tree produced by LogoParser#ParenthesisExpr.
    def exitParenthesisExpr(self, ctx:LogoParser.ParenthesisExprContext):
        pass


    # Enter a parse tree produced by LogoParser#AssExp.
    def enterAssExp(self, ctx:LogoParser.AssExpContext):
        pass

    # Exit a parse tree produced by LogoParser#AssExp.
    def exitAssExp(self, ctx:LogoParser.AssExpContext):
        pass


    # Enter a parse tree produced by LogoParser#MultDiv.
    def enterMultDiv(self, ctx:LogoParser.MultDivContext):
        pass

    # Exit a parse tree produced by LogoParser#MultDiv.
    def exitMultDiv(self, ctx:LogoParser.MultDivContext):
        pass


    # Enter a parse tree produced by LogoParser#functionCall.
    def enterFunctionCall(self, ctx:LogoParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by LogoParser#functionCall.
    def exitFunctionCall(self, ctx:LogoParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by LogoParser#list.
    def enterList(self, ctx:LogoParser.ListContext):
        pass

    # Exit a parse tree produced by LogoParser#list.
    def exitList(self, ctx:LogoParser.ListContext):
        pass


    # Enter a parse tree produced by LogoParser#color.
    def enterColor(self, ctx:LogoParser.ColorContext):
        pass

    # Exit a parse tree produced by LogoParser#color.
    def exitColor(self, ctx:LogoParser.ColorContext):
        pass


    # Enter a parse tree produced by LogoParser#variable.
    def enterVariable(self, ctx:LogoParser.VariableContext):
        pass

    # Exit a parse tree produced by LogoParser#variable.
    def exitVariable(self, ctx:LogoParser.VariableContext):
        pass


    # Enter a parse tree produced by LogoParser#functionName.
    def enterFunctionName(self, ctx:LogoParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by LogoParser#functionName.
    def exitFunctionName(self, ctx:LogoParser.FunctionNameContext):
        pass



del LogoParser