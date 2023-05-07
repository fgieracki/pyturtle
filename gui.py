import PySimpleGUI as sg
from antlr4 import CommonTokenStream

from logo.LogoLexer import LogoLexer
from logo.LogoParser import LogoParser
from main import MyVisitor, Turtle

size = 400

layout = [[sg.Canvas(size=(size, size), key='-CANVAS-')],
          [sg.InputText(key='-INPUT-'), sg.Button('Push'), sg.Button('Exit')],
          ]

window = sg.Window('PyTurtle', layout)

turtle = Turtle(size//2, size//2)
variables = {}
local_variables = None
functions = {}

# Show turtle
event, values = window.read()
window['-CANVAS-'].TKCanvas.create_oval(turtle.x - 5, turtle.y - 5, turtle.x + 5, turtle.y + 5, fill='black')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Push':
        canvas = window['-CANVAS-'].TKCanvas
        data = values['-INPUT-']

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
        canvas.create_oval(turtle.x - 5, turtle.y - 5, turtle.x + 5, turtle.y + 5, fill='black')
window.close()