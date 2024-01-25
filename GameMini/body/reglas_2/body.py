import reflex as rx

from GameMini.routers.routers import routers
from GameMini.styles.color import Color, TextoColor
from GameMini.styles.tamaños import Tamaños, TamañosTextos


def reglas_juego_uno() -> rx.Component():
    return rx.box(
        rx.center(
            rx.vstack(
            rx.hstack(
                rx.heading("Piedra🥌 , Papel📋 , Tijeras✂ , Lagarto🦎 , Spock 🖖" ,color=TextoColor.TITULO.value , font_size=TamañosTextos.TITULO .value)
            ),

            rx.hstack(
                rx.box(
                    rx.hstack(
                        rx.text("1.Piedra aplasta Tijeras : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value),
                        rx.text("La Piedra gana porque puede romper las Tijeras." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("2.Tijeras cortan Papel : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value),
                        rx.text("Las Tijeras ganan al cortar el Papel." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("3.Papel cubre Piedra : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("El Papel gana al cubrir la Piedra. " ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("4.Piedra aplasta Lagarto : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("La Piedra gana al aplastar al Lagarto." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("5.Lagarto envenena Spock :  " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("El Lagarto gana al envenenar a Spock." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("6.Spock destroza Tijeras:" ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("Spock gana al destrozar las Tijeras." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("7.Tijeras decapitan Lagarto : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("Las Tijeras ganan al decapitar al Lagarto." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("8.Lagarto come Papel : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("El Lagarto gana al comer el Papel" ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("9.Papel desautoriza Spock : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("El Papel gana al desautorizar a Spock." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("10.Spock vaporiza Piedra:" ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("Spock gana al vaporizar la Piedra." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    margin_y=Tamaños.MARGIN_Y.value,
                    text_align="left"
                    )
            ),

        ),
            border_radius= Tamaños.BORDER_RADIUS.value,
            background = Color.SEGUNDARIO.value,
            margin=Tamaños.MARGIN.value,
            padding=Tamaños.PADDING_X.value,
            border=Tamaños.BORDER.value,
            box_shadow= "1px 1px 1px 0px #FF5C00",


    ),
        width="100%"
)

def continuar_a_juego_1():
    return rx.button(
        rx.link(
            rx.text(
                "continuar" , font_size=TamañosTextos.TITULO.value
            ),
            href=routers.JUEGO_TRES.value
        ),
        border_radius= Tamaños.BORDER_RADIUS.value,
        background = Color.PRINCIPAL.value,
        border=Tamaños.BORDER.value,
        box_shadow= "1px 1px 1px 0px #32135A",
        margin_left = "75%"
        )

