import PySimpleGUI as sg

size = 400

layout = [[sg.Canvas(size=(size, size), key='-CANVAS-')],
          [sg.Button('Draw'), sg.Button('Exit')]]

window = sg.Window('PyTurtle', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Draw':
        canvas = window['-CANVAS-'].TKCanvas
        canvas.create_oval(size // 2 - 5, size // 2 - 5, size // 2 + 5, size // 2 + 5, fill='black')
window.close()