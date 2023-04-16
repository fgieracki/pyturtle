import math

from antlr4 import *
from logo.LogoLexer import LogoLexer
from logo.LogoParser import LogoParser
from logo.LogoVisitor import LogoVisitor


class Turtle:
    x = 0
    y = 0
    angle = 0
    pen = True
    color = "black"

    def __add__(self, value):
        self.x += value * math.sin(math.radians(self.angle))
        self.y += value * math.cos(math.radians(self.angle))
        return self

    def __sub__(self, value):
        self.x -= value * math.sin(math.radians(self.angle))
        self.y -= value * math.cos(math.radians(self.angle))
        return self

    def pen_up(self):
        self.pen = False

    def pen_down(self):
        self.pen = True

    def __str__(self):
        return f'{self.x} {self.y}'

    def rotate(self, angle):
        self.angle += angle


class MyVisitor(LogoVisitor):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        # self.pen = True
        # self.color = "black"
        self.commands = []


    def visitForwardCommand(self, ctx):
        global turtle
        # turtle += float(ctx.expression().getText())
        turtle += float(self.visit(ctx.expression()))
        print(turtle)
        self.commands.append(f"forward {ctx.expression()}")

    def visitListCommand(self, ctx):
        self.commands.append(f"variable {','.join([x.getText() for x in ctx.expression()])}")

    def visitBackwardCommand(self, ctx):
        global turtle
        turtle -= float(ctx.expression())
        print(turtle)
        self.commands.append(f"backward {ctx.expression()}")

    def visitLeftCommand(self, ctx):
        global turtle
        turtle.rotate(-float(ctx.expression().getText()))
        self.commands.append(f"left {ctx.expression().getText()}")

    def visitRightCommand(self, ctx):
        global turtle
        turtle.rotate(float(ctx.expression().getText()))
        self.commands.append(f"right {ctx.expression().getText()}")

    def visitPenUpCommand(self, ctx):
        turtle.pen_up()
        self.commands.append("pen up")

    def visitPenDownCommand(self, ctx):
        turtle.pen_down()
        self.commands.append("pen down")

    def visitSetColorCommand(self, ctx):
        self.commands.append(f"set color {ctx.expression().getText()}")

    def visitRepeatCommand(self, ctx):
        self.commands.append(f"repeat {ctx.expression().getText()}")

    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)
        return self.commands

    def visitDefExp(self, ctx):
        return ctx.getText()

    def visitNumber(self, ctx):
        return ctx.getText()

    def visitColor(self, ctx):
        return ctx.getText()

    def visitVariable(self, ctx):
        return ctx.getText()

    def visitString(self, ctx):
        return ctx.getText()

    # def visitParenthesis(self, ctx):
    #     return self.visit(ctx.expression())

    def visitMultDiv(self, ctx):
        if (ctx.operator.text == "*"):
            return float(self.visit(ctx.expression(0))) * float(self.visit(ctx.expression(1)))
        else:
            return float(self.visit(ctx.expression(0))) / float(self.visit(ctx.expression(1)))

    def visitPlusMinus(self, ctx):
        if(ctx.operator.text == "-"):
            return float(self.visit(ctx.expression(0))) - float(self.visit(ctx.expression(1)))
        else:
            return float(self.visit(ctx.expression(0))) + float(self.visit(ctx.expression(1)))
        # return f"{self.visit(ctx.expression(0))} {ctx.operator.text} {self.visit(ctx.expression(1))}"

    def visitParenthesisExpr(self, ctx):
        return self.visit(ctx.expression())


if __name__ == "__main__":
    # turtle
    turtle = Turtle()
    while True:
        data = InputStream(input(">>> "))
        # lexer
        lexer = LogoLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = LogoParser(stream)
        tree = parser.program()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)
