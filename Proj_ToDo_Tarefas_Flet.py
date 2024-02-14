from flet import *

def todo_tarefa(page: Page):
    page.title = 'ToDo - Tarefas'
    page.horizontal_alignment = 'center'
    page.scroll = 'adaptive'
    
    page.update()

    txt = TextField(value="Digite aqui a sua tarefa", text_align='center', width=250, text_size=20, color='blue')

    page.add(txt)

app(target=todo_tarefa)