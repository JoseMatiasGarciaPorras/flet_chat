import flet as ft
from dataclasses import dataclass


class Mensaje:
    def __init__(self, usuario: str, texto: str):
        self.usuario = usuario
        self.texto = texto


def main(page: ft.Page):

    def send_click(e):
        page.pubsub.send_all(
            Mensaje(usuario=page.session.id, texto=nuevo_mensaje.value))
        nuevo_mensaje.value = ''

    def activar_mensaje(mensaje: Mensaje):
        chat.controls.append(ft.Text(f'{mensaje.usuario}: {mensaje.texto}'))
        page.update()

    chat = ft.Column()
    nuevo_mensaje = ft.TextField()
    boton_enviar = ft.Button('Send', on_click=send_click)
    page.pubsub.subscribe(activar_mensaje)
    page.add(chat, ft.Row(controls=[nuevo_mensaje, boton_enviar]))


ft.run(main)
