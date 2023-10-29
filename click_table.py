import PySimpleGUI as sg

nameDict = {'A1': 'Albedo',
            'A2': 'Barbara',
            'A3': 'Chongyun',
            'A4': 'Diluc',
            'A5': 'Eula',
            'A6': 'Fischl',
            'A7': 'Ganyu',
            'A8': 'Hu Tao',
            'A9': 'Jean',
            'A10': 'Kazuha'}

nameList = [[1, nameDict["A1"], 3.5],
            [2, nameDict["A2"], 3.6],
            [3, nameDict["A3"], 3.7],
            [4, nameDict["A4"], 3.8],
            [5, nameDict["A5"], 3.9],
            [6, nameDict["A6"], 4.0],
            [7, nameDict["A7"], 4.1],
            [8, nameDict["A8"], 4.2],
            [9, nameDict["A9"], 4.3],
            [10, nameDict["A10"], 4.4]]

headings = ['Index', 'Name', 'Cumulative GPA']


activeStudent = [
    [sg.Text("Name:"), sg.Text('', enable_events=True,key='-activeStudent-')],
    [sg.Text("Math Result:"), sg.Text('', enable_events=True, key='-math-')],
    [sg.Text("English Result:"), sg.Text('', enable_events=True, key='-english-')],
    [sg.Text("Science Result:"), sg.Text('', enable_events=True, key='-science-')],
]


result = [
    [sg.Table(values=nameList, headings=headings, max_col_width=100,
              auto_size_columns=True,
              display_row_numbers=False,
              justification='center',
              num_rows=10,
              key='hello',
              row_height=55,
              tooltip='Results',
              enable_events=True), sg.Frame('', activeStudent, size=(800, 550))],
    ]

resultsWindow = sg.Window("Register Results", result, size=(1000, 500), finalize=True, )

while True:
    event, values = resultsWindow.read()

    if event == "Submit" or event == sg.WIN_CLOSED:
        break
    elif event == "hello":
        data_selected = [nameList[row] for row in values[event]]
        print(data_selected)
        resultsWindow['-activeStudent-'].update(data_selected[0][1])
    else:
        continue
