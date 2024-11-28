import PySimpleGUI as sg

choices = ["Option 1", "Option 2", "Option 3"]
radio_dic = {0:2,1:3,2:4}
layout = [
    [sg.Radio(item[1], key=item[0], group_id='0') for item in radio_dic.items()],
    #          値      辞書のキー     ラジオボタンのグループ  リスト内包表記  値の組をリストで取得       
    [sg.Button("Submit")]
]
window = sg.Window("Listbox Widget Example", layout)
i = 0

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        for x in range(len(radio_dic)):
            if values[x]:
                i = x
        i = (i + 1)%len(radio_dic)
        window[i].update(True)

        
        

window.close()
