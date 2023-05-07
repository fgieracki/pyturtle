import PySimpleGUI as sg

layout = [[sg.Canvas(size=(400, 400), key='-CANVAS-')],
          [sg.Button('Draw'), sg.Button('Exit')]]

window = sg.Window('PyTurtle', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Draw':
        canvas = window['-CANVAS-'].TKCanvas
window.close()