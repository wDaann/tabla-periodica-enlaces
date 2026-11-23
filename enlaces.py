# Hecho por: alumnos: Angel Daniel Hernandez Arteag y Fernando Cruz Calderon

from dataclasses import dataclass


@dataclass(frozen=True)
class Elemento:
    numero_atomico: int
    simbolo: str
    nombre: str
    masa_atomica: float
    definicion: str


# (Z, simbolo, nombre, masa_atomica, definicion_corta)
ELEMENTOS_DATA = [
    (1, "H", "hidrogeno", 1.008, "Gas más ligero y abundante del universo; forma agua y compuestos orgánicos."),
    (2, "He", "helio", 4.0026, "Gas noble incoloro y muy ligero; se usa en criogenia y globos."),
    (3, "Li", "litio", 6.94, "Metal alcalino blando y ligero; clave en baterías recargables."),
    (4, "Be", "berilio", 9.0122, "Metal alcalinotérreo rígido y ligero; usado en aleaciones aeroespaciales."),
    (5, "B", "boro", 10.81, "Metaloide del grupo III; útil en vidrios resistentes al calor y dopaje tipo P."),
    (6, "C", "carbono", 12.011, "No metal base de la química orgánica; forma grafito, diamante y nanotubos."),
    (7, "N", "nitrogeno", 14.007, "Gas no metálico que compone la mayor parte del aire terrestre."),
    (8, "O", "oxigeno", 15.999, "No metal reactivo esencial para la respiración y la combustión."),
    (9, "F", "fluor", 18.998, "Halógeno más electronegativo y reactivo; presente en compuestos fluorados."),
    (10, "Ne", "neon", 20.180, "Gas noble que emite luz rojiza-naranja en tubos de descarga."),
    (11, "Na", "sodio", 22.990, "Metal alcalino muy reactivo; forma sal común (NaCl) con el cloro."),
    (12, "Mg", "magnesio", 24.305, "Metal alcalinotérreo ligero; usado en aleaciones y clorofila."),
    (13, "Al", "aluminio", 26.982, "Metal ligero, dúctil y resistente a la corrosión; del grupo III."),
    (14, "Si", "silicio", 28.085, "Metaloide semiconductor del grupo IV; base de chips y celdas solares."),
    (15, "P", "fosforo", 30.974, "No metal del grupo V; clave en fertilizantes, ADN y dopaje tipo N."),
    (16, "S", "azufre", 32.06, "No metal amarillo; usado en ácido sulfúrico y vulcanización."),
    (17, "Cl", "cloro", 35.45, "Halógeno de olor penetrante; usado en desinfección y sales."),
    (18, "Ar", "argon", 39.948, "Gas noble inerte; protege soldaduras y lámparas."),
    (19, "K", "potasio", 39.098, "Metal alcalino blando y reactivo; esencial en biología y fertilizantes."),
    (20, "Ca", "calcio", 40.078, "Metal alcalinotérreo presente en huesos, caliza y yeso."),
    (21, "Sc", "escandio", 44.956, "Metal de transición ligero; mejora aleaciones de aluminio."),
    (22, "Ti", "titanio", 47.867, "Metal de transición fuerte, ligero y resistente a la corrosión."),
    (23, "V", "vanadio", 50.942, "Metal de transición usado para dar dureza al acero."),
    (24, "Cr", "cromo", 51.996, "Metal de transición brillante y resistente; clave en acero inoxidable."),
    (25, "Mn", "manganeso", 54.938, "Metal de transición usado en aleaciones de acero y pilas."),
    (26, "Fe", "hierro", 55.845, "Metal de transición magnético y estructural; base del acero."),
    (27, "Co", "cobalto", 58.933, "Metal de transición usado en imanes de alta resistencia y baterías."),
    (28, "Ni", "niquel", 58.693, "Metal de transición resistente a la oxidación; usado en monedas y aleaciones."),
    (29, "Cu", "cobre", 63.546, "Metal rojizo con excelente conductividad eléctrica y térmica."),
    (30, "Zn", "zinc", 65.38, "Metal usado para galvanizar hierro y protegerlo de la corrosión."),
    (31, "Ga", "galio", 69.723, "Metal del grupo III que se funde cerca de los 30 °C; usado en semiconductores."),
    (32, "Ge", "germanio", 72.630, "Metaloide semiconductor del grupo IV empleado en óptica y electrónica."),
    (33, "As", "arsenico", 74.922, "Metaloide del grupo V; usado en semiconductores compuestos como GaAs."),
    (34, "Se", "selenio", 78.971, "No metal con propiedades fotoconductoras y antioxidantes."),
    (35, "Br", "bromo", 79.904, "Halógeno líquido a temperatura ambiente de color rojizo oscuro."),
    (36, "Kr", "kripton", 83.798, "Gas noble pesado usado en iluminación especializada."),
    (37, "Rb", "rubidio", 85.468, "Metal alcalino muy reactivo; usado en investigación y relojes atómicos."),
    (38, "Sr", "estroncio", 87.62, "Metal alcalinotérreo que produce tonos rojos en pirotecnia."),
    (39, "Y", "itrio", 88.906, "Metal usado en fósforos, láseres y materiales superconductores."),
    (40, "Zr", "zirconio", 91.224, "Metal resistente a la corrosión; común en reactores nucleares."),
    (41, "Nb", "niobio", 92.906, "Metal refractario usado en aleaciones y superconductores."),
    (42, "Mo", "molibdeno", 95.95, "Metal de alto punto de fusión que refuerza aceros especiales."),
    (43, "Tc", "tecnecio", 98.0, "Elemento radiactivo sintético usado en medicina nuclear."),
    (44, "Ru", "rutenio", 101.07, "Metal del grupo del platino; útil como catalizador y en contactos."),
    (45, "Rh", "rodio", 102.91, "Metal noble reflectante; usado en convertidores catalíticos."),
    (46, "Pd", "paladio", 106.42, "Metal noble capaz de absorber hidrógeno; usado en catálisis y electrónica."),
    (47, "Ag", "plata", 107.87, "Metal con la mayor conductividad eléctrica; usado en joyería y electrónica."),
    (48, "Cd", "cadmio", 112.41, "Metal blando usado en recubrimientos y ciertas celdas."),
    (49, "In", "indio", 114.82, "Metal blando del grupo III; clave en pantallas táctiles (ITO)."),
    (50, "Sn", "estano", 118.71, "Metal maleable del grupo IV; usado en soldadura y bronce."),
    (51, "Sb", "antimonio", 121.76, "Metaloide del grupo V; usado en retardantes de llama y aleaciones."),
    (52, "Te", "telurio", 127.60, "Metaloide semiconductor usado en aleaciones y paneles solares."),
    (53, "I", "yodo", 126.90, "Halógeno esencial para la tiroides y usado como antiséptico."),
    (54, "Xe", "xenon", 131.29, "Gas noble denso usado en lámparas de descarga y propulsión iónica."),
    (55, "Cs", "cesio", 132.91, "Metal alcalino muy reactivo; base de estándares de tiempo atómico."),
    (56, "Ba", "bario", 137.33, "Metal alcalinotérreo usado en contrastes médicos y cerámicas."),
    (57, "La", "lantano", 138.91, "Primer lantánido; usado en lentes ópticas y aleaciones."),
    (58, "Ce", "cerio", 140.12, "Lantánido abundante; usado en catalizadores y pulido óptico."),
    (59, "Pr", "praseodimio", 140.91, "Lantánido usado en imanes potentes y vidrios filtrantes."),
    (60, "Nd", "neodimio", 144.24, "Lantánido famoso por imanes permanentes de alta potencia."),
    (61, "Pm", "prometio", 145.0, "Lantánido radiactivo raro con aplicaciones especiales."),
    (62, "Sm", "samario", 150.36, "Lantánido usado en imanes estables a altas temperaturas."),
    (63, "Eu", "europio", 151.96, "Lantánido usado en fósforos rojos y azules de pantallas."),
    (64, "Gd", "gadolinio", 157.25, "Lantánido paramagnético; usado como contraste en resonancia magnética."),
    (65, "Tb", "terbio", 158.93, "Lantánido usado en dispositivos luminiscentes y sensores."),
    (66, "Dy", "disprosio", 162.50, "Lantánido empleado en imanes de alto rendimiento."),
    (67, "Ho", "holmio", 164.93, "Lantánido con altas propiedades magnéticas; usado en láseres."),
    (68, "Er", "erbio", 167.26, "Lantánido clave en amplificadores de fibra óptica."),
    (69, "Tm", "tulio", 168.93, "Lantánido poco abundante usado en fuentes portátiles de rayos X."),
    (70, "Yb", "iterbio", 173.05, "Lantánido usado en láseres de fibra y relojes ópticos."),
    (71, "Lu", "lutecio", 174.97, "Último lantánido; denso y usado en detectores de tomografía."),
    (72, "Hf", "hafnio", 178.49, "Metal refractario usado en microprocesadores avanzados y control nuclear."),
    (73, "Ta", "tantalio", 180.95, "Metal muy resistente a la corrosión; común en capacitores electrónicos."),
    (74, "W", "wolframio", 183.84, "Metal con el punto de fusión más alto; usado en filamentos y corte."),
    (75, "Re", "renio", 186.21, "Metal denso y refractario; usado en superaleaciones de turbinas."),
    (76, "Os", "osmio", 190.23, "Uno de los elementos naturales más densos; usado en aleaciones duras."),
    (77, "Ir", "iridio", 192.22, "Metal muy denso y resistente a la corrosión a altas temperaturas."),
    (78, "Pt", "platino", 195.08, "Metal noble precioso; muy usado en catálisis química y joyería."),
    (79, "Au", "oro", 196.97, "Metal noble maleable, inoxidable y conductor; usado en electrónica y joyería."),
    (80, "Hg", "mercurio", 200.59, "Único metal líquido en condiciones ambientales estándar."),
    (81, "Tl", "talio", 204.38, "Metal blando del grupo III; tóxico y usado en óptica/electrónica."),
    (82, "Pb", "plomo", 207.2, "Metal denso del grupo IV; usado en baterías y blindaje contra radiación."),
    (83, "Bi", "bismuto", 208.98, "Metal pesado del grupo V, diamagnético y de baja toxicidad relativa."),
    (84, "Po", "polonio", 209.0, "Metaloide radiactivo raro descubierto por Marie y Pierre Curie."),
    (85, "At", "astato", 210.0, "Halógeno/metaloide radiactivo extremadamente escaso en la naturaleza."),
    (86, "Rn", "radon", 222.0, "Gas noble radiactivo que se forma por desintegración natural."),
    (87, "Fr", "francio", 223.0, "Metal alcalino radiactivo muy inestable y escaso."),
    (88, "Ra", "radio", 226.0, "Metal alcalinotérreo radiactivo luminiscente en compuestos históricos."),
    (89, "Ac", "actinio", 227.0, "Primer actínido; radiactivo y fuente de neutrones en investigación."),
    (90, "Th", "torio", 232.04, "Actínido radiactivo con potencial como combustible nuclear."),
    (91, "Pa", "protactinio", 231.04, "Actínido radiactivo denso y poco abundante."),
    (92, "U", "uranio", 238.03, "Actínido radiactivo pesado; combustible principal en reactores nucleares."),
    (93, "Np", "neptunio", 237.0, "Elemento transuránico radiactivo obtenido artificialmente."),
    (94, "Pu", "plutonio", 244.0, "Elemento radiactivo transuránico usado en energía nuclear."),
    (95, "Am", "americio", 243.0, "Elemento sintético radiactivo usado en detectores de humo."),
    (96, "Cm", "curio", 247.0, "Elemento sintético radiactivo empleado en investigación científica."),
    (97, "Bk", "berkelio", 247.0, "Elemento sintético radiactivo nombrado en honor a Berkeley."),
    (98, "Cf", "californio", 251.0, "Elemento sintético radiactivo emisor de neutrones."),
    (99, "Es", "einstenio", 252.0, "Elemento sintético radiactivo nombrado en honor a Albert Einstein."),
    (100, "Fm", "fermio", 257.0, "Elemento sintético radiactivo obtenido en experimentos nucleares."),
    (101, "Md", "mendelevio", 258.0, "Elemento sintético radiactivo en honor a Dmitri Mendeléyev."),
    (102, "No", "nobelio", 259.0, "Elemento sintético radiactivo del grupo de los actínidos."),
    (103, "Lr", "lawrencio", 266.0, "Último actínido sintético radiactivo."),
    (104, "Rf", "rutherfordio", 267.0, "Elemento superpesado sintético de vida muy corta."),
    (105, "Db", "dubnio", 268.0, "Elemento superpesado sintético altamente inestable."),
    (106, "Sg", "seaborgio", 269.0, "Elemento superpesado sintético en honor a Glenn T. Seaborg."),
    (107, "Bh", "bohrio", 270.0, "Elemento superpesado sintético en honor a Niels Bohr."),
    (108, "Hs", "hassio", 277.0, "Elemento superpesado sintético con propiedades químicas de metal de transición."),
    (109, "Mt", "meitnerio", 278.0, "Elemento superpesado sintético en honor a Lise Meitner."),
    (110, "Ds", "darmstadtio", 281.0, "Elemento superpesado sintético de corta duración."),
    (111, "Rg", "roentgenio", 282.0, "Elemento superpesado sintético en honor a Wilhelm Röntgen."),
    (112, "Cn", "copernicio", 285.0, "Elemento superpesado sintético en honor a Nicolás Copérnico."),
    (113, "Nh", "nihonio", 286.0, "Elemento sintético del grupo III de vida muy breve."),
    (114, "Fl", "flerovio", 289.0, "Elemento superpesado sintético del grupo IV."),
    (115, "Mc", "moscovio", 290.0, "Elemento sintético del grupo V de existencia fugaz."),
    (116, "Lv", "livermorio", 293.0, "Elemento superpesado sintético altamente inestable."),
    (117, "Ts", "tenesino", 294.0, "Elemento superpesado sintético con rasgos de halógeno."),
    (118, "Og", "oganeson", 294.0, "Elemento superpesado sintético de mayor número atómico conocido."),
]

ELEMENTOS_POR_ATOMO = {
    z: Elemento(z, simb, nom, masa, desc)
    for z, simb, nom, masa, desc in ELEMENTOS_DATA
}
ELEMENTOS_POR_SIMBOLO = {e.simbolo.lower(): e for e in ELEMENTOS_POR_ATOMO.values()}
ELEMENTOS_POR_NOMBRE = {e.nombre.lower(): e for e in ELEMENTOS_POR_ATOMO.values()}

NO_METAL = {1, 6, 7, 8, 9, 15, 16, 17, 34, 35, 53, 54, 86, 118}
METALOIDES = {5, 14, 32, 33, 51, 52, 84, 85}
GASES_NOBLES = {2, 10, 18, 36, 54, 86, 118}

GRUPO_III = {5, 13, 31, 49, 81, 113}
GRUPO_IV = {6, 14, 32, 50, 82, 114}
GRUPO_V = {7, 15, 33, 51, 83, 115}


def normalizar(texto: str) -> str:
    return texto.strip().lower()


def quitar_acentos(texto: str) -> str:
    reemplazos = str.maketrans("áéíóúüñ", "aeiouun")
    return texto.translate(reemplazos)


def resolver_elemento(texto: str):
    bruto = texto.strip()
    if not bruto:
        return None

    if bruto.isdigit():
        return ELEMENTOS_POR_ATOMO.get(int(bruto))

    clave = quitar_acentos(normalizar(bruto))
    if clave in ELEMENTOS_POR_SIMBOLO:
        return ELEMENTOS_POR_SIMBOLO[clave]
    if clave in ELEMENTOS_POR_NOMBRE:
        return ELEMENTOS_POR_NOMBRE[clave]
    return None


def es_metal(elemento: Elemento) -> bool:
    return (
        elemento.numero_atomico not in NO_METAL
        and elemento.numero_atomico not in METALOIDES
        and elemento.numero_atomico not in GASES_NOBLES
    )


def es_no_metal(elemento: Elemento) -> bool:
    return elemento.numero_atomico in NO_METAL


def es_metaloide(elemento: Elemento) -> bool:
    return elemento.numero_atomico in METALOIDES


def es_gas_noble(elemento: Elemento) -> bool:
    return elemento.numero_atomico in GASES_NOBLES


def categoria_elemento(elemento: Elemento) -> str:
    if es_gas_noble(elemento):
        return "Gas noble"
    if es_metaloide(elemento):
        return "Metaloide"
    if es_no_metal(elemento):
        return "No metal"
    return "Metal"


def grupo_semiconductor(elemento: Elemento) -> str:
    z = elemento.numero_atomico
    if z in GRUPO_III:
        return "Grupo III"
    if z in GRUPO_IV:
        return "Grupo IV"
    if z in GRUPO_V:
        return "Grupo V"
    return "-"


def tipo_material_covalente(elemento1: Elemento, elemento2: Elemento) -> str:
    a = elemento1.numero_atomico
    b = elemento2.numero_atomico

    if (a in GRUPO_III and b in GRUPO_IV) or (b in GRUPO_III and a in GRUPO_IV):
        return "Extrinseco tipo P"
    if (a in GRUPO_V and b in GRUPO_IV) or (b in GRUPO_V and a in GRUPO_IV):
        return "Extrinseco tipo N"
    return "Intrinseco"


def clasificar_enlace(elemento1: Elemento, elemento2: Elemento):
    if es_gas_noble(elemento1) or es_gas_noble(elemento2):
        return "No es posible hacer un enlace estable en este modelo escolar.", None

    metal1 = es_metal(elemento1)
    metal2 = es_metal(elemento2)
    no_metal1 = es_no_metal(elemento1)
    no_metal2 = es_no_metal(elemento2)
    metaloide1 = es_metaloide(elemento1)
    metaloide2 = es_metaloide(elemento2)

    if metal1 and metal2:
        return "Metalico", None

    if (metal1 and no_metal2) or (metal2 and no_metal1):
        return "Ionico", None

    if (no_metal1 or metaloide1) and (no_metal2 or metaloide2):
        return "Covalente", tipo_material_covalente(elemento1, elemento2)

    if (metal1 and metaloide2) or (metal2 and metaloide1):
        return "Covalente", tipo_material_covalente(elemento1, elemento2)

    return "No es posible determinar un enlace simple con este par.", None


def masa_combinada(elemento1: Elemento, elemento2: Elemento) -> float:
    return round(elemento1.masa_atomica + elemento2.masa_atomica, 4)