import flet as ft
from dataclasses import dataclass


@dataclass
class Mensaje:
    def __init__(self, usuario: str, texto: str, tipo_mensaje: str):
        self.usuario = usuario
        self.texto = texto
        self.tipo_mensaje = tipo_mensaje


def main(page: ft.Page):

    def join_click(e):
        if not nombre_usuario.value:
            nombre_usuario.error_text = 'El nombre de usuario no puede estar en blanco!'
        else:
            page.session.store.set('nombre_usuario', nombre_usuario.value)
            page.pop_dialog()
            page.pubsub.send_all(Mensaje(usuario=nombre_usuario.value,
                                         texto=f'{nombre_usuario.value} se ha unido al chat',
                                         tipo_mensaje='mensaje_login')
                                 )

    def send_click(e):
        page.pubsub.send_all(
            Mensaje(usuario=page.session.store.get('nombre_usuario'),
                    texto=nuevo_mensaje.value,
                    tipo_mensaje='mensaje_chat'))
        nuevo_mensaje.value = ''

    def activar_mensaje(mensaje: Mensaje):
        if mensaje.tipo_mensaje == 'mensaje_chat':
            chat.controls.append(
                ft.Text(f'{mensaje.usuario}: {mensaje.texto}'))
        elif mensaje.tipo_mensaje == 'mensaje_login':
            chat.controls.append(ft.Text(mensaje.texto,
                                         italic=True,
                                         color=ft.Colors.WHITE,
                                         size=12)
                                 )
        page.update()

    page.title = 'Flet_chat'
    page.window.width = 800
    page.window.height = 800
    chat = ft.Column()
    nombre_usuario = ft.TextField(label='Introduce tu nombre')
    nuevo_mensaje = ft.TextField()
    boton_enviar = ft.Button('Send', on_click=send_click)
    page.show_dialog(ft.AlertDialog(open=True,
                                    modal=True,
                                    title='¡Bienvenido!',
                                    content=ft.Column(
                                        [nombre_usuario], tight=True),
                                    actions=[
                                        ft.Button(content='Unirse al chat', on_click=join_click)],
                                    actions_alignment=ft.MainAxisAlignment.END
                                    )
                     )

    page.pubsub.subscribe(activar_mensaje)
    page.add(chat, ft.Row(controls=[nuevo_mensaje, boton_enviar]))


ft.run(main)
