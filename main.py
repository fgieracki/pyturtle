import math
import time

from PIL import Image
import PySimpleGUI as sg
from PIL import ImageTk

from antlr4 import *

from logo.LogoLexer import LogoLexer
from logo.LogoParser import LogoParser
from logo.LogoVisitor import LogoVisitor
from antlr4.error.ErrorListener import ErrorListener

class Turtle:
    x = 0
    y = 0
    angle = 180
    old_x = 0
    old_y = 0
    old_angle = 180
    pen = True
    color = [0, 0, 0]

    def __init__(self, x, y, canvas, gui, icon):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.gui = gui
        self.base_icon = icon
        self.icon = None

    def __add__(self, value):
        self.old_x = self.x
        self.old_y = self.y
        self.x += value * round(math.sin(math.radians(self.angle)), 4)
        self.y += value * round(math.cos(math.radians(self.angle)), 4)
        if self.pen:
            self.canvas.create_line(self.old_x, self.old_y, self.x, self.y, fill=self.get_color(), width=1)
        self.render_turtle()
        return self

    def __sub__(self, value):
        self.old_x = self.x
        self.old_y = self.y
        self.x -= value * round(math.sin(math.radians(self.angle)), 4)
        self.y -= value * round(math.cos(math.radians(self.angle)), 4)
        if self.pen:
            self.canvas.create_line(self.old_x, self.old_y, self.x, self.y, fill=self.get_color(), width=1)
        self.render_turtle()
        return self

    def pen_up(self):
        self.pen = False

    def pen_down(self):
        self.pen = True

    def __str__(self):
        return f'{self.x} {self.y}, color: {self.color}'

    def rotate(self, angle):
        self.old_angle = self.angle
        self.angle -= angle
        self.render_turtle()

    def set_color(self, r: int, g: int, b: int):
        self.color = [r % 256, g % 256, b % 256]

    def get_color(self):
        return '#%02x%02x%02x' % tuple(self.color)

    def render_turtle(self):
        self.remove_turtle()
        base_icon = self.base_icon.rotate(180 + self.angle)
        self.old_angle = self.angle
        self.icon = ImageTk.PhotoImage(base_icon)
        self.gui = self.canvas.create_image(self.x, self.y, image=self.icon)
        window.read(timeout=0)

    def remove_turtle(self):
        self.canvas.delete(self.gui)


class MyErrorListener(ErrorListener):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("Oh no!! Syntax error!!")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print("Oh no!! Ambiguity error!!")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print("Oh no!! Full context error!!")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print("Oh no!! Context sensitivity error!!")

class MyVisitor(LogoVisitor):
    def __init__(self):
        self.commands = []
        self.variables = {}

    def visitForwardCommand(self, ctx):
        try:
            global turtle
            # turtle += float(ctx.expression().getText())
            turtle += float(self.visit(ctx.expression()))
            self.commands.append(f"forward {ctx.expression()}")
        except:
            pass

    def visitListCommand(self, ctx):
        try:
            self.commands.append(f"variable {','.join([x.getText() for x in ctx.expression()])}")
        except:
            pass

    def visitBackwardCommand(self, ctx):
        try:
            global turtle
            turtle -= float(self.visit(ctx.expression()))
            self.commands.append(f"backward {ctx.expression()}")
        except:
            pass

    def visitLeftCommand(self, ctx):
        try:
            global turtle
            turtle.rotate(-float(self.visit(ctx.expression())))
            self.commands.append(f"left {ctx.expression().getText()}")
        except:
            pass

    def visitRightCommand(self, ctx):
        try:
            global turtle
            turtle.rotate(float(self.visit(ctx.expression())))
            self.commands.append(f"right {ctx.expression().getText()}")
        except:
            pass

    def visitHeadCommand(self, ctx):
        try:
            global command_history
            pos = int(ctx.INT().getText())
            data = InputStream(command_history[pos % len(command_history)].strip().upper())
            # lexer
            lexer = LogoLexer(data)
            stream = CommonTokenStream(lexer)
            # parser
            parser = LogoParser(stream)
            # parser.addErrorListener(MyErrorListener())
            tree = parser.program()
            # evaluator
            visitor = MyVisitor()
            output = visitor.visit(tree)
        except:
            pass

    def visitTailCommand(self, ctx):
        try:
            global command_history
            pos = int(ctx.INT().getText())
            data = InputStream(command_history[len(command_history) - pos % len(command_history) - 1].strip().upper())
            # lexer
            lexer = LogoLexer(data)
            stream = CommonTokenStream(lexer)
            # parser
            parser = LogoParser(stream)
            # parser.addErrorListener(MyErrorListener())
            tree = parser.program()
            # evaluator
            visitor = MyVisitor()
            output = visitor.visit(tree)
        except:
            pass

    def visitPenUpCommand(self, ctx):
        try:
            turtle.pen_up()
            self.commands.append("pen up")
        except:
            pass

    def visitPenDownCommand(self, ctx):
        try:
            turtle.pen_down()
            self.commands.append("pen down")
        except:
            pass

    def visitSetColorCommand(self, ctx):
        try:
            global turtle

            new_colors = [int(c) for c in self.visit(ctx.color()).split(',')]

            turtle.set_color(*new_colors)
            self.commands.append(f"set color {ctx.color().getText()}")
        except:
            pass

    def visitFillColorCommand(self, ctx):
        try:
            fill_colors = [int(c) for c in self.visit(ctx.color()).split(',')]
            return fill_colors
        except:
            pass

    def visitClearCommand(self, ctx):
        try:
            global turtle
            global canvas
            canvas.delete("all")
            turtle.render_turtle()
        except:
            pass

    def visitRepeatCommand(self, ctx):
        try:
            loop_counter = int(ctx.expression().getText())
            for i in range(loop_counter):
                for statement in ctx.statement():
                    self.visit(statement)
            self.commands.append(f"repeat {ctx.expression().getText()}")
        except:
            pass

    def visitWhileCommand(self, ctx):
        try:
            comparison = self.visit(ctx.comparison())
            while comparison:
                for statement in ctx.statement():
                    self.visit(statement)
                comparison = self.visit(ctx.comparison())
        except:
            pass

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
        try:
            global variables
            id = self.visitVariableName(ctx.variable())
            # print(ctx.expression())
            if len(local_variables) > 0:
                local_variables[-1][id] = self.visit(ctx.expression())
            else:
                variables[id] = self.visit(ctx.expression())
        except:
            pass

    def visitIfCommand(self, ctx):
        try:
            comparison = self.visit(ctx.comparison())
            if comparison:
                for statement in ctx.ifstat.children:
                    self.visit(statement)
            else:
                if ctx.elsestat is not None:
                    for statement in ctx.elsestat.children:
                        self.visit(statement)
        except:
            pass

    def visitLoadCommand(self, ctx):
        try:
            filename = self.visit(ctx.fileName())
            with open(filename.lower(), 'r') as file:
                for line in file:
                    data = InputStream(line.strip().upper())
                    # lexer
                    lexer = LogoLexer(data)
                    stream = CommonTokenStream(lexer)
                    # parser
                    parser = LogoParser(stream)
                    parser.addErrorListener(MyErrorListener())
                    tree = parser.program()
                    # evaluator
                    visitor = MyVisitor()
                    output = visitor.visit(tree)
        except:
            pass

    def visitFileName(self, ctx):
        return ctx.getText()

    def visitFunctionCommand(self, ctx):
        try:
            global functions
            function_name = self.visit(ctx.functionName())
            variables = ctx.variable()
            statements = ctx.statement()
            functions[function_name] = (variables, statements)
            print(functions)
        except:
            pass

    def visitFunctionCall(self, ctx):
        global functions, local_variables, variables
        function_name = self.visit(ctx.functionName())
        function_expressions = [float(self.visit(expression)) for expression in ctx.expression()]

        local_variables.append(variables)
        function_variables, function_statements = functions[function_name]

        for idx, var in enumerate(function_variables):
            id_var = self.visitVariableName(var)
            local_variables[-1][id_var] = function_expressions[idx]

        for statement in function_statements:
            self.visit(statement)

        local_variables.pop()

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

    def visitID(self, ctx):
        return ctx.getText()

    def visitColor(self, ctx):
        return ctx.getText()

    def visitVariableName(self, ctx):
        return str(ctx.ID())

    def visitVariable(self, ctx):
        global variables, local_variables
        if len(local_variables) > 0:
            return local_variables[-1][str(ctx.ID())]
        return variables[str(ctx.ID())]

    def visitString(self, ctx):
        return ctx.getText()


    def visitFunctionName(self, ctx):
        # print(ctx.getText())
        # return ctx.getText()
        return str(ctx.ID())
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

    size = 800

    input_text = sg.InputText(key='-INPUT-', do_not_clear=False)

    layout = [[sg.Canvas(size=(size, size), key='-CANVAS-')],
              [input_text, sg.Button('Push', bind_return_key=True),
               sg.Button('Exit')],
              ]

    window = sg.Window('PyTurtle', layout, finalize=True)

    window.bind('<Up>', '-UP-')
    window.bind('<Down>', '-DOWN-')

    variables = {}
    local_variables = []
    functions = {}

    canvas = window['-CANVAS-'].TKCanvas

    # Show turtle
    icon_filename = 'icon.png'
    base_icon = Image.open(icon_filename)
    base_icon = base_icon.resize((60, 60), Image.ANTIALIAS)
    icon = ImageTk.PhotoImage(base_icon)
    gui_turtle = canvas.create_image(size // 2, size // 2, image=icon)

    turtle = Turtle(size // 2, size // 2, canvas, gui_turtle, base_icon)

    command_history = []
    idx = -1

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Push':
            command_history.append(values['-INPUT-'])
            data = InputStream(values['-INPUT-'].upper())
            idx = -1

            # lexer
            lexer = LogoLexer(data)
            stream = CommonTokenStream(lexer)
            # parser
            parser = LogoParser(stream)
            parser.addErrorListener(MyErrorListener())
            tree = parser.program()
            # evaluator
            visitor = MyVisitor()
            output = visitor.visit(tree)
        elif event == '-UP-':
            if len(command_history) > 0:
                idx -= 1
                if idx < -1:
                    idx = len(command_history) - 1
                if idx == -1:
                    input_text.update(value='')
                else:
                    input_text.update(value=command_history[idx])
        elif event == '-DOWN-':
            if len(command_history) > 0:
                idx += 1
                if idx >= len(command_history):
                    idx = -1
                if idx == -1:
                    input_text.update(value='')
                else:
                    input_text.update(value=command_history[idx])
    window.close()
