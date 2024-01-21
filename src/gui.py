import PySimpleGUI as sg

def UI():
    layout=[[sg.Text("Select Workout: ")],sg.Column([sg.Button("Chest and Shoulders")]),sg.Column([sg.Button("Arms")]),sg.Column([sg.Button("Back")]),sg.Column([sg.Button("Legs")])]
    window = sg.Window("Workout Mixer", layout)

    while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break
    window.close()