import math
import PySimpleGUI as sg

from antlr4 import *


from logo.LogoLexer import LogoLexer
from logo.LogoParser import LogoParser
from logo.LogoVisitor import LogoVisitor

class Turtle:
    x = 0
    y = 0
    angle = 0
    pen = True
    color = [0, 0, 0]
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, value):
        self.x += value * round(math.sin(math.radians(self.angle)), 4)
        self.y += value * round(math.cos(math.radians(self.angle)), 4)
        return self

    def __sub__(self, value):
        self.x -= value * round(math.sin(math.radians(self.angle)), 4)
        self.y -= value * round(math.cos(math.radians(self.angle)), 4)
        return self

    def pen_up(self):
        self.pen = False

    def pen_down(self):
        self.pen = True

    def __str__(self):
        return f'{self.x} {self.y}, color: {self.color}'

    def rotate(self, angle):
        self.angle += angle

    def set_color(self, r: int, g: int, b: int):
        self.color = [r % 256, g % 256, b % 256]


class MyVisitor(LogoVisitor):
    def __init__(self):
        self.commands = []
        self.variables = {}

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
        turtle.rotate(float(self.visit(ctx.expression())))
        self.commands.append(f"right {ctx.expression().getText()}")

    def visitPenUpCommand(self, ctx):
        turtle.pen_up()
        self.commands.append("pen up")

    def visitPenDownCommand(self, ctx):
        turtle.pen_down()
        self.commands.append("pen down")

    def visitSetColorCommand(self, ctx):
        global turtle

        new_colors = [int(c) for c in self.visit(ctx.color()).split(',')]

        turtle.set_color(*new_colors)
        self.commands.append(f"set color {ctx.color().getText()}")

    def visitFillColorCommand(self, ctx):
        fill_colors = [int(c) for c in self.visit(ctx.color()).split(',')]
        return fill_colors

    def visitRepeatCommand(self, ctx):
        loop_counter = int(ctx.expression().getText())
        for i in range(loop_counter):
            for statement in ctx.statement():
                self.visit(statement)
        self.commands.append(f"repeat {ctx.expression().getText()}")

    def visitWhileCommand(self, ctx):
        comparison = self.visit(ctx.comparison())
        while comparison:
            for statement in ctx.statement():
                self.visit(statement)
            comparison = self.visit(ctx.comparison())

    def visitComparison(self, ctx):
        left = float(self.visit(ctx.expression(0)))
        right = float(self.visit(ctx.expression(1)))
        operator = ctx.operator.text
        if operator == '<':
            return left < right
        elif operator == '>':
            return left > right
        elif operator == '=':
            return left == right
        elif operator == '<>':
            return left != right

    def visitAssignmentCommand(self, ctx):
        global variables
        id = self.visitVariableName(ctx.variable())
        # print(ctx.expression())
        if local_variables != None:
            local_variables[id] = self.visit(ctx.expression())
        else:
            variables[id] = self.visit(ctx.expression())

    def visitIfCommand(self, ctx):
        comparison = self.visit(ctx.comparison())
        if comparison:
            for statement in ctx.ifstat.children:
                self.visit(statement)
        else:
            for statement in ctx.elsestat.children:
                self.visit(statement)

    def visitFunctionCommand(self, ctx):
        global functions
        function_name = self.visit(ctx.functionName())
        variables = ctx.variable()
        statements = ctx.statement()
        functions[function_name] = (variables, statements)
        print(functions)

    def visitFunctionCall(self, ctx):
        global functions, local_variables, variables
        function_name = self.visit(ctx.functionName())
        function_expressions = [float(self.visit(expression)) for expression in ctx.expression()]

        local_variables = variables
        function_variables, function_statements = functions[function_name]

        for idx, var in enumerate(function_variables):
            id_var = self.visitVariableName(var)
            local_variables[id_var] = function_expressions[idx]

        for statement in function_statements:
            self.visit(statement)

        local_variables = None

    def visitAssExp(self, ctx):
        return self.visitVariable(ctx.variable())

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

    def visitVariableName(self, ctx):
        return str(ctx.ID())

    def visitVariable(self, ctx):
        global variables, local_variables
        if local_variables is not None:
            return local_variables[str(ctx.ID())]
        return variables[str(ctx.ID())]

    def visitString(self, ctx):
        return ctx.getText()

    def visitFunctionName(self, ctx):
        return self.visitVariableName(ctx)

    # def visitParenthesis(self, ctx):
    #     return self.visit(ctx.expression())

    def visitMultDiv(self, ctx):
        if (ctx.operator.text == "*"):
            return float(self.visit(ctx.expression(0))) * float(self.visit(ctx.expression(1)))
        else:
            return float(self.visit(ctx.expression(0))) / float(self.visit(ctx.expression(1)))

    def visitPlusMinus(self, ctx):
        if (ctx.operator.text == "-"):
            return float(self.visit(ctx.expression(0))) - float(self.visit(ctx.expression(1)))
        else:
            return float(self.visit(ctx.expression(0))) + float(self.visit(ctx.expression(1)))
        # return f"{self.visit(ctx.expression(0))} {ctx.operator.text} {self.visit(ctx.expression(1))}"

    def visitParenthesisExpr(self, ctx):
        return self.visit(ctx.expression())


if __name__ == "__main__":

    size = 400

    layout = [[sg.Canvas(size=(size, size), key='-CANVAS-')],
              [sg.InputText(key='-INPUT-'), sg.Button('Push'), sg.Button('Exit')],
              ]

    window = sg.Window('PyTurtle', layout, finalize=True)

    turtle = Turtle(size // 2, size // 2)
    variables = {}
    local_variables = None
    functions = {}

    canvas = window['-CANVAS-'].TKCanvas

    # Show turtle
    gui_turtle = canvas.create_oval(turtle.x - 5, turtle.y - 5, turtle.x + 5, turtle.y + 5, fill='black')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Push':
            old_x, old_y = turtle.x, turtle.y

            data = InputStream(values['-INPUT-'].upper())

            # lexer
            lexer = LogoLexer(data)
            stream = CommonTokenStream(lexer)
            # parser
            parser = LogoParser(stream)

            tree = parser.program()
            # evaluator
            visitor = MyVisitor()
            output = visitor.visit(tree)
            # print(output)
            canvas.move(gui_turtle, turtle.x - old_x, turtle.y - old_y)
    window.close()