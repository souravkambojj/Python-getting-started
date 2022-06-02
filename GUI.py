import PySimpleGUI as sg
from Main import Run
sg.change_look_and_feel('LightGrey6')    # for default look and feel

# Designing layout
layout = [[sg.Text("")], [sg.Text("\t\t\t\t\tSelect Dataset\t"), sg.Combo(['BOT-IOT','kdd'], size=(10,20)),sg.Text("\n")],
          [sg.Text("\t\t\t\t\tTraining data (%)\t"), sg.InputText(size=(12, 2)), sg.Text("  "), sg.Button("START", size=(10, 1))], [sg.Text("\n")],

          [sg.Text("\t\t\t\t\tROUTING",font=('Bold')),sg.Text("\n")],
          [sg.Text("\t\t\t         Cluster-based routing\t   SDN-based routing\tWCV routing protocol \tProposed FAO ")],
          [sg.Text('\t\t    Energy   '), sg.In(key='11',size=(20,20)), sg.In(key='12',size=(20,20)), sg.In(key='13',size=(20,20)), sg.In(key='14',size=(20,20))],
          [sg.Text('\t\t    Trust      '), sg.In(key='21',size=(20,20)), sg.In(key='22',size=(20,20)), sg.In(key='23',size=(20,20)), sg.In(key='24',size=(20,20)),sg.Text("\n")],
          [sg.Text("\n")],
          [sg.Text("\t\t\t\t\tDETECTION",font=('Bold')),sg.Text("\n")],
          [sg.Text("\t\t        SSAE+Softmax\t       CMEHA+DNN\t\t          MABC\t\t    SVM  \t\tProposed FASMO-based DMN ")],
          [sg.Text('\tPrecision'), sg.In(key='31', size=(20, 20)), sg.In(key='32', size=(20, 20)),
           sg.In(key='33', size=(20, 20)), sg.In(key='34', size=(20, 20)),sg.In(key='35', size=(20, 20)),sg.Text("\n")],
          [sg.Text('\tRecall    '), sg.In(key='41',size=(20,20)), sg.In(key='42',size=(20,20)), sg.In(key='43',size=(20,20)), sg.In(key='44',size=(20,20)),sg.In(key='45',size=(20,20))],

          [sg.Text("\n")],
          [sg.Text("\t\t\t\t\t\t    "),sg.Button('Close', size=(10, 1))], [sg.Text("")]]


# Create the Window layout
window = sg.Window('GUI', layout)

# event loop
while True:
    event, value = window.read()  # displays the window
    if event == "START":
        ds,tr_per = value[0], int(value[1])
        Energy, Trust, Precision,Recall = Run.callmain(ds, tr_per)
        window.element('11').Update(Energy[0])
        window.element('12').Update(Energy[1])
        window.element('13').Update(Energy[2])
        window.element('14').Update(Energy[3])

        window.element('21').Update(Trust[0])
        window.element('22').Update(Trust[1])
        window.element('23').Update(Trust[2])
        window.element('24').Update(Trust[3])

        window.element('31').Update(Precision[0])
        window.element('32').Update(Precision[1])
        window.element('33').Update(Precision[2])
        window.element('34').Update(Precision[3])
        window.element('35').Update(Precision[4])

        window.element('41').Update(Recall[0])
        window.element('42').Update(Recall[1])
        window.element('43').Update(Recall[2])
        window.element('44').Update(Recall[3])
        window.element('45').Update(Recall[4])



    if event == 'Close':
        window.close()
        break

