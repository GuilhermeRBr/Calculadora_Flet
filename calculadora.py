import flet as ft
from flet import colors
from decimal import Decimal

botoes = [
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '±', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '*', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '-', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE}
]


def main (page: ft.Page):
    page.bgcolor = colors.BLACK
    page.title = 'CALCULADORA'
    page.window_always_on_top = True
    page.window_resizable = False
    page.window_width = 400
    page.window_height = 600
    

    resultado = ft.Text(value = '0', color = colors.WHITE, size=39)

    def calcule(operador, valor_atual):
        try:
            valor = eval(valor_atual)
            if operador == '%':
                valor /= 100
            elif operador == '±':
                valor = -valor
        except:
            return 'Error'
        digits = min(abs(Decimal(valor).as_tuple().exponent), 5)
        return format(valor, f'.{digits}f')

    def select(event):
        valor_atual = resultado.value if resultado.value not in ('0','Error') else ''
        valor = event.control.content.value

        if valor.isnumeric():
            valor = valor_atual + valor
        elif valor == 'AC':
            valor = '0'
        else:
            if valor_atual and valor_atual[-1] in ('/','*', '-', '+', '.'):
                valor_atual = valor_atual[:-1]
            valor = valor_atual + valor

            if valor[-1] in ('=','%','±'):
                valor = calcule(operador=valor[-1], valor_atual=valor_atual)

        resultado.value = valor
        resultado.update()
    display = ft.Row(
        width=400,
        height=75,
        controls=[resultado],
        alignment='end')

    botao = [ft.Container(
        content=ft.Text(value=botao['operador'], color=botao['fonte'], size=27 ),
        width=83,
        height=83,
        bgcolor= botao['fundo'],
        border_radius= 100,
        alignment=ft.alignment.center,
        on_click=select)
        for botao in botoes]
    
    Keyboard = ft.Row(
        width=400,
        wrap=True,
        controls=botao,
        alignment='end'
    )
    page.add(display, Keyboard)

ft.app(target = main)