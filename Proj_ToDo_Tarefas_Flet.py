#Bibliotecas#
from flet import *

#Funcao Pagina Principal#
def todo_tarefa(page: Page):
    page.title = 'ToDo - Tarefas'#Titulo da Pagina
    page.horizontal_alignment = 'center'#Alinhamento#
    page.scroll = 'adaptive'
    page.bgcolor = colors.DEEP_PURPLE_50#Cor de Fundo#
    page.window_width = 350#Largura da Pagina#
    page.window_height = 450#Altura da Pagina#
    page.window_resizable = False#Redimensinar pagina off#
    page.window_always_on_top = True#Pagina inicializando sempre no top#
    
    page.update()#Atualizando a pagina#

    task = TextField(hint_text="Digite aqui a sua tarefa", expand=True)#Caixa de entrada#

    input_bar = Row(
        controls=[
            task,
            FloatingActionButton(icon=icons.ADD)
        ]#Criando um botao para adicionar#
    )

    tabs = Tabs(
        selected_index=0,
        tabs=[
            Tab(text='Todos'),
            Tab(text='Em Andamento'),
            Tab(text='Finalizados')
        ]#Criando selecao de lista status das tarefas#
    )

    page.add(input_bar, tabs)

app(target=todo_tarefa)