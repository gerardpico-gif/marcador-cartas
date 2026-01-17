import flet as ft

def main(page: ft.Page):
    page.title = "Marcador de Cartas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "adaptive"

    puntos_a = ft.Text("0", size=60, weight="bold")
    puntos_b = ft.Text("0", size=60, weight="bold")
    
    nombre_a = ft.TextField(value="Equipo A", label="Nombre Equipo 1", expand=True)
    nombre_b = ft.TextField(value="Equipo B", label="Nombre Equipo 2", expand=True)
    
    objetivo_input = ft.TextField(
        label="Objetivo (múltiplo de 5)", 
        value="30", 
        width=200, 
        keyboard_type=ft.KeyboardType.NUMBER,
        max_length=4
    )

    def sumar_puntos(e, equipo):
        try:
            limite = int(objetivo_input.value)
            if limite % 5 != 0:
                raise ValueError
        except ValueError:
            page.snack_bar = ft.SnackBar(ft.Text("Error: El objetivo debe ser un número múltiplo de 5"))
            page.snack_bar.open = True
            page.update()
            return

        if equipo == "A":
            actual = int(puntos_a.value) + 5
            puntos_a.value = str(actual)
            if actual >= limite: mostrar_ganador(nombre_a.value)
        else:
            actual = int(puntos_b.value) + 5
            puntos_b.value = str(actual)
            if actual >= limite: mostrar_ganador(nombre_b.value)
        page.update()

    def reset(e):
        puntos_a.value = "0"
        puntos_b.value = "0"
        page.update()

    def mostrar_ganador(nombre):
        dlg = ft.AlertDialog(
            title=ft.Text("¡Fin de la partida!"),
            content=ft.Text(f"Ha ganado: {nombre}"),
            on_dismiss=lambda e: reset(None)
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.add(
        ft.SafeArea(ft.Column([
            ft.Text("Configuración", size=20, weight="bold"),
            ft.Row([nombre_a, nombre_b]),
            ft.Row([objetivo_input], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),
            ft.Row([
                ft.Column([puntos_a, ft.ElevatedButton("+5", on_click=lambda e: sumar_puntos(e, "A"), height=80, width=140)], horizontal_alignment="center"),
                ft.VerticalDivider(width=20),
                ft.Column([puntos_b, ft.ElevatedButton("+5", on_click=lambda e: sumar_puntos(e, "B"), height=80, width=140)], horizontal_alignment="center"),
            ], alignment="center", spacing=40),
            ft.Divider(),
            ft.ElevatedButton("Reiniciar", icon=ft.icons.REFRESH, on_click=reset, color=ft.colors.RED)
        ], horizontal_alignment="center"))
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)