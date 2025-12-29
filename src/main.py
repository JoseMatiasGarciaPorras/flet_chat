import flet as ft


def main(page: ft.Page):

    def send_click(e):
        chat.controls.append(ft.Text(nuevo_mensaje.value))
        nuevo_mensaje.value = ''

    chat = ft.Column()
    nuevo_mensaje = ft.TextField()
    boton_enviar = ft.Button('Send', on_click=send_click)

    page.add(chat, ft.Row(controls=[nuevo_mensaje, boton_enviar]))


ft.run(main)
