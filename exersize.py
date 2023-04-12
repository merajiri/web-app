import streamlit
streamlit.title("To-Do")
list_todo = []
try :
    with open("todo.txt", "r") as file :
        for line in file.readlines() :
            if line == "" :
                print("empty")
            else :
                list_todo.append(line.removesuffix("\n"))
except :
    pass
for index,box in enumerate(list_todo) :
    if box != "" :
        status = streamlit.checkbox(box,key=box)
        if status :
            list_todo.pop(index)
            with open("todo.txt","w") as file :
                for item in list_todo :
                    file.writelines(item + "\n")
            streamlit.experimental_rerun()
def text_func() :
    text = streamlit.session_state["text_input"]
    if text != "" :
        list_todo.append(text)
    with open("todo.txt","w") as file :
        for item in list_todo :
            file.writelines(item + "\n")
    print(list_todo)
streamlit.text_input(label="input",on_change=text_func,key="text_input") 