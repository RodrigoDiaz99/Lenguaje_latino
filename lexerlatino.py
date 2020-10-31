import ply.lex as lex
# resultado del analisis
resultado_lexema = []
reservada = (
     # Palabras Reservadas
    'INCLUIR',
    'USANDO',
    'ESPACIONOMBRE',
    'SALIDA',
    'ENTRADA',
    'OBTENER',
    'CADENA',
    'RETORNAR',
    'VACIO',
    'ENTERO',
    'ENDL',
)
tokens = reservada + (
    'IDENTIFICADOR',
    'ASIGNAR',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',
    'MINUSMINUS',
    'PLUSPLUS',
    #Condiciones
    'SI',
    'SINO',
    #Ciclos
    'MIENTRAS',
    'PARA',
    #lógica
    'Y',
    'O',
    'NO',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',
    # Símbolos
    'NUMERAL',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',
    # Otros
    'PUNTOCOMA',
    'COMA',
    'COMDOB',
    'MAYORDER', #>>
    'MAYORIZQ', #<<
)
# Reglas de Expresiones Regulares para token de Contexto simple
t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
# t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'
t_ASIGNAR = r'='
# Expresiones Lógicas
t_Y = r'\&\&'
t_O = r'\|{2}'
t_NO = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = ';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_COMDOB = r'\"'
def t_INCUIR(t):
    r'INCLUIR'
    return t
def t_USANDO(t):
    r'USANDO'
    return t
def t_ESPACIONOMBRE(t):
    r'ESPACIONOMBRE'
    return t

def t_SALIDA(t):
    r'salida'
    return t
def t_ENTRADA(t):
    r'entrada'
    return t
def t_OBTENER(t):
    r'obtener'
    return t
def t_FIN(t):
    r'fin'
    return t
def t_SINO(t):
    r'else'
    return t
def t_SI(t):
    r'if'
    return t
def t_RETORNO(t):
    r'return'
    return t
def t_VACIO(t):
    r'vacio'
    return t
def t_MIENTRAS(t):
    r'mientras'
    return t
def t_PARA(t):
    r'for'
    return t
def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_CADENA(t):
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t
def t_NUMERAL(t):
    r'\#'
    return t
def t_PLUSPLUS(t):
    r'\+\+'
    return t
def t_MENORIGUAL(t):
    r'<='
    return t
def t_MAYORIGUAL(t):
    r'>='
    return t
def t_IGUAL(t):
    r'=='
    return t
def t_MAYORDER(t):
    r'<<'
    return t
def t_MAYORIZQ(t):
    r'>>'
    return t
def t_DISTINTO(t):
 r'!='
 return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 10
    print("Comentario de una linea")
t_ignore =' \t'

def t_error( t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno),
        str(t.value), str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(10)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema
    analizador = lex.lex()
    analizador.input(data)
    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
         # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type)
            ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema
# instanciamos el analizador lexico
analizador = lex.lex()

while True:
    data = input("ingrese: ")
    prueba(data)
    print(resultado_lexema)