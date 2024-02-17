from flet import *

#Criando uma lista dos botoes cor da fonte e do fundo na sequencia#
botoes = [
    {'operador': 'AC', 'fonte':colors.BLACK, 'fundo':colors.BLUE_GREY_100},
    {'operador': '+-', 'fonte':colors.BLACK, 'fundo':colors.BLUE_GREY_100},
    {'operador': '%', 'fonte':colors.BLACK, 'fundo':colors.BLUE_GREY_100},
    {'operador': '/', 'fonte':colors.WHITE, 'fundo':colors.ORANGE},
    {'operador': '7', 'fonte':colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '8', 'fonte':colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '9', 'fonte':colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '*', 'fonte':colors.WHITE, 'fundo':colors.ORANGE},
    {'operador': '4', 'fonte':colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '5', 'fonte':colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '6', 'fonte':colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '-', 'fonte':colors.WHITE, 'fundo':colors.ORANGE},
    {'operador': '1', 'fonte':colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '2', 'fonte':colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '3', 'fonte':colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '+', 'fonte':colors.WHITE, 'fundo':colors.ORANGE},
    {'operador': '0', 'fonte':colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '.', 'fonte':colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '=', 'fonte':colors.WHITE, 'fundo':colors.ORANGE},
]

#Funcao Pagina Principal#
def calculadora(page: Page):
    page.title = 'Calculadora' #Titulo da Pagina
    page.window_resizable = False #Redimensinar pagina off#
    page.window_width = 320 #Largura da Pagina#
    page.window_height = 490 #Altura da Pagina#
    page.bgcolor = '#000' #Cor de Fundo#
    page.window_always_on_top = True #Pagina inicializando sempre no top#    
               
    result =Text(value=0, color= colors.WHITE, size=45) #Criando uma caixa de texto#

    def calcule():
        ...

    def select(e):
        value_t = result.value if result.value != '0' else ''
        value = e.control.content.value

        if value.isdigit():
            value = str(value_t) + str(value)
        elif value == 'AC':
            value = '0'
        else:
            if value_t and value_t[-1] in ('/', '*', '-', '+', '.'):
                value_t = value_t[:-1]

            value = value_t + value
            if value[-1] in ('=', '%', '+-'):
                value = calcule()

        result.value = value
        result.update()
    
    display = Row(
        width=320, #largura da caixa de texto#
        controls=[result], #Chamando a caixa de texto#
        alignment='end', #Alinhando o texto no final da caixa#
    )

    btn = [Container(
        content=Text(value=btn['operador'], color=btn['fonte'], size=27), #Criando uma caixa de texto dos botoes#
        width=62, #largura da caixa de texto#
        height=62, #altura da caixa de texto#
        bgcolor=btn['fundo'], #Cor de fundo dos botoes
        border_radius=100, #Arredondando as bordas dos botoes#
        alignment=alignment.center, #Alinhando o texto dos botoes no centro# 
        on_click=select
    )for btn in botoes] #Percorrendo a lista dos nomes e cores dos botoes#

    keybord = Row(
        width=320,
        wrap=True, #Quebrando os botoes no final da pagina para linha de baixo#
        controls=btn, #Chamando a caixa de texto#
        alignment='end'
    )

    page.add(display, keybord)

app(target=calculadora)