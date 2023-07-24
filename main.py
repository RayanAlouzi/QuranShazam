import transcribe as t
import search
import PySimpleGUI as sg


def main(): 

    layout = [[sg.Text("Click record to record your audio")],[sg.Button("Record")],[sg.Button("Close")]]

    # Create the window
    window = sg.Window(title = "Quran Shazam", layout = layout, margins = (200,100))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == sg.WIN_CLOSED:
            break
        elif event == 'Record':
            t.transcribeAudio()
            search.searching()

    window.close()
    # time = vr.recordingTime()
    # vr.record(time)

    return



main()


