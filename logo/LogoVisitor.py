# Generated from Logo.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LogoParser import LogoParser
else:
    from LogoParser import LogoParser

# This class defines a complete generic visitor for a parse tree produced by LogoParser.

class LogoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LogoParser#program.
    def visitProgram(self, ctx:LogoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#statement.
    def visitStatement(self, ctx:LogoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#forwardCommand.
    def visitForwardCommand(self, ctx:LogoParser.ForwardCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#backwardCommand.
    def visitBackwardCommand(self, ctx:LogoParser.BackwardCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#leftCommand.
    def visitLeftCommand(self, ctx:LogoParser.LeftCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#rightCommand.
    def visitRightCommand(self, ctx:LogoParser.RightCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#penUpCommand.
    def visitPenUpCommand(self, ctx:LogoParser.PenUpCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#penDownCommand.
    def visitPenDownCommand(self, ctx:LogoParser.PenDownCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#setColorCommand.
    def visitSetColorCommand(self, ctx:LogoParser.SetColorCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#fillColorCommand.
    def visitFillColorCommand(self, ctx:LogoParser.FillColorCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#repeatCommand.
    def visitRepeatCommand(self, ctx:LogoParser.RepeatCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#clearCommand.
    def visitClearCommand(self, ctx:LogoParser.ClearCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#listCommand.
    def visitListCommand(self, ctx:LogoParser.ListCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#ifCommand.
    def visitIfCommand(self, ctx:LogoParser.IfCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#whileCommand.
    def visitWhileCommand(self, ctx:LogoParser.WhileCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#functionCommand.
    def visitFunctionCommand(self, ctx:LogoParser.FunctionCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#loadCommand.
    def visitLoadCommand(self, ctx:LogoParser.LoadCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#assignmentCommand.
    def visitAssignmentCommand(self, ctx:LogoParser.AssignmentCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#comparison.
    def visitComparison(self, ctx:LogoParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#DefExp.
    def visitDefExp(self, ctx:LogoParser.DefExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#PlusMinus.
    def visitPlusMinus(self, ctx:LogoParser.PlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#ParenthesisExpr.
    def visitParenthesisExpr(self, ctx:LogoParser.ParenthesisExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#AssExp.
    def visitAssExp(self, ctx:LogoParser.AssExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#MultDiv.
    def visitMultDiv(self, ctx:LogoParser.MultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#functionCall.
    def visitFunctionCall(self, ctx:LogoParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#list.
    def visitList(self, ctx:LogoParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#color.
    def visitColor(self, ctx:LogoParser.ColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#variable.
    def visitVariable(self, ctx:LogoParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#functionName.
    def visitFunctionName(self, ctx:LogoParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogoParser#fileName.
    def visitFileName(self, ctx:LogoParser.FileNameContext):
        return self.visitChildren(ctx)



del LogoParser