import flet as ft
from enlaces import (
    ELEMENTOS_POR_ATOMO,
    categoria_elemento,
    clasificar_enlace,
    grupo_semiconductor,
    masa_combinada,
    resolver_elemento,
)

# (fila_0_a_8, columna_1_a_18)
# Filas 0..6: Periodos 1..7 | Fila 7: Lantanidos (57-71) | Fila 8: Actinidos (89-103)
POSICIONES = {
    1: (0, 1), 2: (0, 18),
    3: (1, 1), 4: (1, 2),
    5: (1, 13), 6: (1, 14), 7: (1, 15), 8: (1, 16), 9: (1, 17), 10: (1, 18),
    11: (2, 1), 12: (2, 2),
    13: (2, 13), 14: (2, 14), 15: (2, 15), 16: (2, 16), 17: (2, 17), 18: (2, 18),
    **{z: (3, z - 18) for z in range(19, 37)},
    **{z: (4, z - 36) for z in range(37, 55)},
    55: (5, 1), 56: (5, 2),
    **{z: (5, z - 54 + 2) for z in range(72, 87)},
    87: (6, 1), 88: (6, 2),
    **{z: (6, z - 86 + 2) for z in range(104, 119)},
    **{z: (7, z - 57 + 3) for z in range(57, 72)},
    **{z: (8, z - 89 + 3) for z in range(89, 104)},
}

COLORES_CAT = {
    "Gas noble": "#1E3A5F",
    "Metaloide": "#1E4D3B",
    "No metal": "#4A3519",
    "Metal": "#2A2438",
}


def buscar_elemento_flexible(texto: str):
    q = (texto or "").strip().lower().replace(",", ".")
    if not q:
        return None
    directo = resolver_elemento(q)
    if directo:
        return directo
    try:
        objetivo = float(q)
        candidatos = [e for e in ELEMENTOS_POR_ATOMO.values() if e.masa_atomica is not None]
        if candidatos:
            mejor = min(candidatos, key=lambda e: abs(e.masa_atomica - objetivo))
            if abs(mejor.masa_atomica - objetivo) <= 1.5:
                return mejor
    except ValueError:
        pass
    for e in ELEMENTOS_POR_ATOMO.values():
        if q in e.nombre.lower() or q == e.simbolo.lower():
            return e
    return None


def descripcion_ampliada(elem) -> str:
    cat = categoria_elemento(elem)
    grp = grupo_semiconductor(elem)
    masa = f"{elem.masa_atomica:g} u" if elem.masa_atomica is not None else "N/D"
    semi_txt = f" Pertenece al grupo semiconductor {grp}." if grp and grp != "-" else ""
    return (
        f"{elem.nombre.title()} ({elem.simbolo}, Z={elem.numero_atomico}, masa {masa}) "
        f"está clasificado como {cat}.{semi_txt} {elem.definicion}"
    )


def construir_explicacion_enlace(e1, e2, enlace: str, material: str | None) -> tuple[str, str]:
    cat1 = categoria_elemento(e1)
    cat2 = categoria_elemento(e2)
    texto_lower = (enlace or "").lower()
    no_es_enlace = (
        "no forma" in texto_lower
        or "no hay enlace" in texto_lower
        or "sin enlace" in texto_lower
        or "no enlace" in texto_lower
        or enlace.strip().lower() in {"no", "ninguno", "n/a", "-"}
    )
    if no_es_enlace:
        estado_titulo = f"NO ES ENLACE  •  {e1.simbolo} + {e2.simbolo} ({enlace})"
        if cat1 == "Gas noble" or cat2 == "Gas noble":
            gas = e1 if cat1 == "Gas noble" else e2
            otro = e2 if gas is e1 else e1
            explicacion = (
                f"No se forma enlace químico estable porque {gas.nombre.title()} ({gas.simbolo}) es un gas noble "
                f"con su capa de valencia prácticamente completa y muy baja tendencia a ceder, ganar o compartir electrones "
                f"en condiciones normales frente a {otro.nombre.title()} ({otro.simbolo})."
            )
        else:
            explicacion = (
                f"No se clasifica como un enlace químico formado entre {e1.nombre.title()} ({cat1}) y "
                f"{e2.nombre.title()} ({cat2}) bajo las reglas de este clasificador ({enlace}). "
                f"Para que haya enlace químico intervienen atracciones electrostáticas (iónico), compartición de electrones "
                f"(covalente) o deslocalización electrónica en redes metálicas (metálico)."
            )
        return estado_titulo, explicacion

    estado_titulo = f"SÍ ES ENLACE  •  {e1.simbolo} + {e2.simbolo}  ->  {enlace}"
    if "iónico" in texto_lower or "ionico" in texto_lower:
        base_exp = (
            f"Se forma un enlace iónico porque interactúa un elemento de carácter metálico/electropositivo con otro "
            f"de carácter no metálico/electronegativo ({e1.nombre.title()} [{cat1}] y {e2.nombre.title()} [{cat2}]), "
            f"favoreciendo la transferencia de electrones y la atracción entre iones de carga opuesta."
        )
    elif "covalente" in texto_lower:
        mat_txt = f" El material covalente resultante se clasifica como: {material}." if material else ""
        base_exp = (
            f"Se forma un enlace covalente porque {e1.nombre.title()} [{cat1}] y {e2.nombre.title()} [{cat2}] "
            f"comparten pares de electrones para estabilizar sus configuraciones electrónicas.{mat_txt}"
        )
    elif "metálico" in texto_lower or "metalico" in texto_lower:
        base_exp = (
            f"Se forma un enlace metálico porque {e1.nombre.title()} [{cat1}] y {e2.nombre.title()} [{cat2}] "
            f"aportan electrones de valencia a una nube o red compartida de cationes metálicos, lo que da conductividad "
            f"y cohesión característica de los metales."
        )
    else:
        mat_txt = f" Detalle adicional: {material}." if material else ""
        base_exp = (
            f"Se establece una interacción de tipo '{enlace}' entre {e1.nombre.title()} ({cat1}) y "
            f"{e2.nombre.title()} ({cat2}).{mat_txt}"
        )
    return estado_titulo, base_exp


def main(page: ft.Page):
    page.title = "Tabla Periodica y Enlaces Quimicos"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = ft.Padding.only(left=10, right=10, top=12, bottom=18)
    page.spacing = 8

    estado = {"sel": ELEMENTOS_POR_ATOMO[8], "e1": None, "e2": None}
    contenedores_celda = {}
    textos_z = {}
    textos_simbolo = {}
    espacios_vacio = []
    filas_row = []

    logo_mascota = ft.Image(
        src="Mascota.png",
        width=36,
        height=36,
        fit=ft.BoxFit.CONTAIN,
        border_radius=8,
    )

    txt_simbolo = ft.Text("", size=22, weight=ft.FontWeight.BOLD)
    txt_nombre_z = ft.Text("", size=13, weight=ft.FontWeight.BOLD)
    txt_peso = ft.Text("", size=12)
    txt_cat_semi = ft.Text("", size=11)
    txt_def = ft.Text("", size=11)

    c1_titulo = ft.Text("Elemento 1", size=12, weight=ft.FontWeight.BOLD)
    c1_simb = ft.Text("—", size=20, weight=ft.FontWeight.BOLD)
    c1_info = ft.Text("Sin confirmar\nToca un elemento y pulsa 'Confirmar Elem 1'.", size=11)

    c2_titulo = ft.Text("Elemento 2", size=12, weight=ft.FontWeight.BOLD)
    c2_simb = ft.Text("—", size=20, weight=ft.FontWeight.BOLD)
    c2_info = ft.Text("Sin confirmar\nToca un elemento y pulsa 'Confirmar Elem 2'.", size=11)

    txt_estado_enlace = ft.Text(
        "Clasificación pendiente: confirma Elemento 1 y Elemento 2 y pulsa 'Clasificar enlace'.",
        size=14,
        weight=ft.FontWeight.BOLD,
    )
    txt_explicacion = ft.Text("", size=13)
    txt_masa_y_detalle = ft.Text("", size=12)

    def estilo_celda(z: int):
        el = ELEMENTOS_POR_ATOMO[z]
        es_sel = estado["sel"].numero_atomico == z
        es_e1 = estado["e1"] is not None and estado["e1"].numero_atomico == z
        es_e2 = estado["e2"] is not None and estado["e2"].numero_atomico == z
        if es_sel:
            bg, fg, borde = "#FFFFFF", "#0F172A", ft.Border.all(2, "#FFFFFF")
        else:
            bg = COLORES_CAT.get(categoria_elemento(el), "#1E293B")
            fg = "#F8FAFC"
            if es_e1 and es_e2:
                borde = ft.Border.all(2, "#38BDF8")
            elif es_e1:
                borde = ft.Border.all(2, "#4ADE80")
            elif es_e2:
                borde = ft.Border.all(2, "#FBBF24")
            else:
                borde = ft.Border.all(1, "#475569")
        return bg, fg, borde

    def refrescar_celdas():
        for z, cont in contenedores_celda.items():
            bg, fg, borde = estilo_celda(z)
            cont.bgcolor = bg
            cont.border = borde
            if z in textos_z:
                textos_z[z].color = fg
            if z in textos_simbolo:
                textos_simbolo[z].color = fg

    def actualizar_cuadritos_confirmados():
        e1 = estado["e1"]
        if e1:
            m1 = f"{e1.masa_atomica:g} u" if e1.masa_atomica is not None else "N/D"
            c1_simb.value = e1.simbolo
            c1_info.value = (
                f"{e1.nombre.title()} (Z={e1.numero_atomico})\n"
                f"Peso: {m1}\n"
                f"{categoria_elemento(e1)} | Semicond: {grupo_semiconductor(e1)}\n"
                f"{e1.definicion}"
            )
        else:
            c1_simb.value = "—"
            c1_info.value = "Sin confirmar\nToca un elemento y pulsa 'Confirmar Elem 1'."

        e2 = estado["e2"]
        if e2:
            m2 = f"{e2.masa_atomica:g} u" if e2.masa_atomica is not None else "N/D"
            c2_simb.value = e2.simbolo
            c2_info.value = (
                f"{e2.nombre.title()} (Z={e2.numero_atomico})\n"
                f"Peso: {m2}\n"
                f"{categoria_elemento(e2)} | Semicond: {grupo_semiconductor(e2)}\n"
                f"{e2.definicion}"
            )
        else:
            c2_simb.value = "—"
            c2_info.value = "Sin confirmar\nToca un elemento y pulsa 'Confirmar Elem 2'."

    def actualizar_todo():
        el = estado["sel"]
        cat = categoria_elemento(el)
        grp = grupo_semiconductor(el)
        masa_str = f"{el.masa_atomica:g} u" if el.masa_atomica is not None else "N/D"
        txt_simbolo.value = el.simbolo
        txt_nombre_z.value = f"{el.nombre.title()}  (Z = {el.numero_atomico})"
        txt_peso.value = f"Peso atómico: {masa_str}"
        txt_cat_semi.value = f"Tipo: {cat}  |  Semiconductor: {grp}"
        txt_def.value = el.definicion
        actualizar_cuadritos_confirmados()
        refrescar_celdas()

    def elegir_z(z: int):
        estado["sel"] = ELEMENTOS_POR_ATOMO[z]
        actualizar_todo()
        page.update()

    def set_e1(e):
        estado["e1"] = estado["sel"]
        actualizar_todo()
        page.update()

    def set_e2(e):
        estado["e2"] = estado["sel"]
        actualizar_todo()
        page.update()

    def calcular_enlace(e):
        e1, e2 = estado["e1"], estado["e2"]
        if not e1 or not e2:
            txt_estado_enlace.value = "Falta confirmar ambos elementos (Elemento 1 y Elemento 2)."
            txt_explicacion.value = "Selecciona dos elementos en la tabla y confirma cada uno antes de clasificar."
            txt_masa_y_detalle.value = ""
            page.update()
            return
        enlace, material = clasificar_enlace(e1, e2)
        masa_tot = masa_combinada(e1, e2)
        tot_str = f"{masa_tot:g} u" if masa_tot is not None else "N/D"
        m1_str = f"{e1.masa_atomica:g} u" if e1.masa_atomica is not None else "N/D"
        m2_str = f"{e2.masa_atomica:g} u" if e2.masa_atomica is not None else "N/D"
        titulo, explicacion = construir_explicacion_enlace(e1, e2, enlace, material)
        mat_linea = f"\nMaterial covalente: {material}" if material else ""
        txt_estado_enlace.value = titulo
        txt_explicacion.value = explicacion
        txt_masa_y_detalle.value = (
            f"Peso combinado: {e1.simbolo} ({m1_str}) + {e2.simbolo} ({m2_str}) = {tot_str}{mat_linea}\n"
            f"• {descripcion_ampliada(e1)}\n"
            f"• {descripcion_ampliada(e2)}"
        )
        page.update()

    def limpiar(e):
        estado["e1"] = None
        estado["e2"] = None
        txt_estado_enlace.value = "Clasificación pendiente: confirma Elemento 1 y Elemento 2 y pulsa 'Clasificar enlace'."
        txt_explicacion.value = ""
        txt_masa_y_detalle.value = ""
        actualizar_todo()
        page.update()

    buscador = ft.TextField(
        label="Buscar por Z, símbolo, nombre o peso (ej. 15.999, Si, 79)",
        expand=True,
    )

    def al_escribir(e):
        found = buscar_elemento_flexible(buscador.value or "")
        if found:
            estado["sel"] = found
            actualizar_todo()
            page.update()

    buscador.on_change = al_escribir

    for z, (r, c) in POSICIONES.items():
        el = ELEMENTOS_POR_ATOMO[z]
        bg, fg, borde = estilo_celda(z)
        t_z = ft.Text(f"{z}", size=7, color=fg)
        t_sym = ft.Text(el.simbolo, size=11, weight=ft.FontWeight.BOLD, color=fg)
        textos_z[z] = t_z
        textos_simbolo[z] = t_sym
        celda = ft.Container(
            width=38,
            height=38,
            border_radius=4,
            border=borde,
            bgcolor=bg,
            on_click=lambda ev, num=z: elegir_z(num),
            content=ft.Column(
                [t_z, t_sym],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )
        contenedores_celda[z] = celda

    filas_ui = []
    for r in range(9):
        if r == 7:
            filas_ui.append(ft.Container(height=4))
        celdas_fila = []
        for c in range(1, 19):
            if (r, c) in POSICIONES.values():
                z_match = next(k for k, v in POSICIONES.items() if v == (r, c))
                celdas_fila.append(contenedores_celda[z_match])
            elif r == 5 and c == 3:
                esp = ft.Container(
                    width=38,
                    height=38,
                    content=ft.Column(
                        [ft.Text("57-71", size=7)],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                )
                espacios_vacio.append(esp)
                celdas_fila.append(esp)
            elif r == 6 and c == 3:
                esp = ft.Container(
                    width=38,
                    height=38,
                    content=ft.Column(
                        [ft.Text("89-103", size=7)],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                )
                espacios_vacio.append(esp)
                celdas_fila.append(esp)
            else:
                esp = ft.Container(width=38, height=38)
                espacios_vacio.append(esp)
                celdas_fila.append(esp)
        row_f = ft.Row(celdas_fila, spacing=2)
        filas_row.append(row_f)
        filas_ui.append(row_f)

    panel_actual = ft.Container(
        padding=12,
        border_radius=8,
        border=ft.Border.all(1, "#475569"),
        content=ft.Column(
            [
                ft.Row([txt_simbolo, txt_nombre_z], spacing=10, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                txt_peso,
                txt_cat_semi,
                txt_def,
            ],
            spacing=4,
        ),
    )

    cuadrito_e1 = ft.Container(
        padding=10,
        border_radius=8,
        border=ft.Border.all(2, "#4ADE80"),
        content=ft.Column(
            [ft.Row([c1_titulo, c1_simb], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), c1_info],
            spacing=4,
        ),
    )

    cuadrito_e2 = ft.Container(
        padding=10,
        border_radius=8,
        border=ft.Border.all(2, "#FBBF24"),
        content=ft.Column(
            [ft.Row([c2_titulo, c2_simb], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), c2_info],
            spacing=4,
        ),
    )

    fila_confirmados = ft.Column([cuadrito_e1, cuadrito_e2], spacing=8)

    columna_derecha = ft.Container(
        width=330,
        content=ft.Column([panel_actual, fila_confirmados], spacing=10),
    )

    tarjeta_resultado = ft.Container(
        padding=12,
        border_radius=8,
        border=ft.Border.all(1, "#475569"),
        content=ft.Column([txt_estado_enlace, txt_explicacion, txt_masa_y_detalle], spacing=5),
    )

    fila_botones = ft.Row(
        [
            ft.Button("Confirmar Elem 1", on_click=set_e1),
            ft.Button("Confirmar Elem 2", on_click=set_e2),
            ft.Button("Clasificar enlace", on_click=calcular_enlace),
            ft.Button("Limpiar", on_click=limpiar),
        ],
        wrap=True,
        run_spacing=6,
        spacing=6,
    )

    zona_controles_y_res = ft.Column(
        [
            ft.Row(
                [
                    logo_mascota,
                    ft.Text(
                        "Tabla Periodica y Enlaces Quimicos",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        overflow=ft.TextOverflow.ELLIPSIS,
                        max_lines=2,
                        expand=True,
                    ),
                ],
                spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            buscador,
            fila_botones,
            tarjeta_resultado,
        ],
        spacing=8,
        expand=True,
    )

    contenedor_superior = ft.Container(expand=True)
    tabla_scroll = ft.Row([ft.Column(filas_ui, spacing=2)], scroll=ft.ScrollMode.AUTO)

    def adaptar_orientacion(e=None):
        ancho = page.width or 0
        alto = page.height or 0
        es_vertical = ancho < alto if (ancho and alto) else True
        tam_celda = 32 if es_vertical else 38
        tam_z = 6.5 if es_vertical else 7
        tam_sym = 10 if es_vertical else 11
        espaciado_fila = 1.5 if es_vertical else 2

        for z, cont in contenedores_celda.items():
            cont.width = tam_celda
            cont.height = tam_celda
            if z in textos_z:
                textos_z[z].size = tam_z
            if z in textos_simbolo:
                textos_simbolo[z].size = tam_sym

        for esp in espacios_vacio:
            esp.width = tam_celda
            esp.height = tam_celda

        for rf in filas_row:
            rf.spacing = espaciado_fila

        if es_vertical:
            zona_controles_y_res.expand = False
            columna_derecha.width = None
            columna_derecha.expand = False
            contenedor_superior.content = ft.Column(
                [zona_controles_y_res, columna_derecha],
                spacing=10,
            )
        else:
            zona_controles_y_res.expand = True
            columna_derecha.width = 330
            columna_derecha.expand = False
            contenedor_superior.content = ft.Row(
                [zona_controles_y_res, columna_derecha],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=12,
            )

        page.update()

    actualizar_todo()
    page.on_resized = adaptar_orientacion
    page.add(contenedor_superior, ft.Divider(height=10), tabla_scroll)
    adaptar_orientacion()


if __name__ == "__main__":
    ft.run(main)