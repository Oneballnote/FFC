import ast
from tkinter import *


## ESTRUCTURA DE DATOS PARA ALMACENAR UN CIRCUITO BOOLEANO
class Nodo:
    __slots__ = 'etiqueta', 'hijos'

    def __init__(self, etiqueta, *hijos):
        self.etiqueta = etiqueta
        self.hijos = hijos

def postorden(nodoraiz):
    pila, descubiertos = [nodoraiz], set()
    while pila:
        u = pila[-1]
        if u in descubiertos:
            pila.pop()
            yield u
        else:
            descubiertos.add(u)
            pila.extend(reversed(u.hijos))

## USO DEL COMPILADOR DE AST (INTEGRADO EN PYTHON) PARA GENERAR CIRCUITOS
def compilar(expresion):
    def nodificar(nodo):
        if isinstance(nodo, ast.BoolOp) and isinstance(nodo.op, ast.And):
            etiqueta = 'and'
            hijos = nodo.values
        elif isinstance(nodo, ast.BoolOp) and isinstance(nodo.op, ast.Or):
            etiqueta = 'or'
            hijos = nodo.values
        elif isinstance(nodo, ast.UnaryOp) and isinstance(nodo.op, ast.Not):
            etiqueta = 'not'
            hijos = [nodo.operand]
        elif isinstance(nodo, ast.Name):
            etiqueta = nodo.id
            hijos = []
        else: raise RuntimeError(msj_error)
        return Nodo(etiqueta, *map(nodificar, hijos))
    msj_error = 'Expresión boolena no válida...'
    T = ast.parse(expresion, mode = 'eval')
    if not isinstance(T, ast.Expression): raise RuntimeError(msj_error)
    return nodificar(T.body)

## EVALUACION DE CIRCUITOS
def formula(nodo):
    if nodo.etiqueta == 'and':
        return '({})'.format(' ∧ '.join(map(formula, nodo.hijos)))
    elif nodo.etiqueta == 'or':
        return '({})'.format(' ∨ '.join(map(formula, nodo.hijos)))
    elif nodo.etiqueta == 'not':
        return '¬' + formula(nodo.hijos[0])
    else: return nodo.etiqueta

def evaluar_circuito(nodoraiz, asignacion):
    ev = dict()
    for nodo in postorden(nodoraiz):
        if nodo.etiqueta == 'and':
            s = 1
            for h in nodo.hijos:
                s = s and ev[h]
        elif nodo.etiqueta == 'or':
            s = 0
            for h in nodo.hijos:
                s = s or ev[h]
        elif nodo.etiqueta == 'not':
            s = not ev[nodo.hijos[0]]
        elif nodo.etiqueta in asignacion:
            s = asignacion[nodo.etiqueta]
        else: raise KeyError('No se pudo evaluar la compuerta {}'.format(nodo))
        ev[nodo] = int(s)
    return ev
        
def contador_binario(n):
    d = [0]*n
    while True:
        yield tuple(d)
        j = n - 1
        while j >= 0:
            d[j] = 1 - d[j]
            if d[j] == 1: break
            j -= 1
        if j < 0: break

def tabla_verdad(nodoraiz):
    variables, compuertas, formulas = set(), [], set()
    for u in postorden(nodoraiz):
        if u.etiqueta in ('and', 'or', 'not'):
            f = formula(u)
            if f not in formulas:
                formulas.add(f)
                compuertas.append(u)
        else: variables.add(u.etiqueta)
    variables = tuple(sorted(variables))
    yield variables + tuple(formula(u) for u in compuertas)
    for digitos in contador_binario(len(variables)):
        asignacion = dict(zip(variables, digitos))
        val = evaluar_circuito(nodoraiz, asignacion)
        yield digitos + tuple(val[c] for c in compuertas)

## OBTENCION DE FORMAS NORMALES
def formas_normales(nodoraiz):
    variables = set()
    for u in postorden(nodoraiz):
        if u.etiqueta not in ('and', 'or', 'not'):
            variables.add(u.etiqueta)
    variables = tuple(sorted(variables))
    clausulas, conjunciones = [], []
    for digitos in contador_binario(len(variables)):
        asignacion = dict(zip(variables, digitos))
        hijos = []
        if evaluar_circuito(nodoraiz, asignacion)[nodoraiz]:
            for (i, d) in enumerate(digitos):
                if d:
                    hijos.append(Nodo(variables[i]))
                else: hijos.append(Nodo('not', Nodo(variables[i])))
            conjunciones.append(Nodo('and', *hijos))
        else:
            for (i, d) in enumerate(digitos):
                if d:
                    hijos.append(Nodo('not', Nodo(variables[i])))
                else: hijos.append(Nodo(variables[i]))
            clausulas.append(Nodo('or', *hijos))
    return Nodo('and', *clausulas), Nodo('or', *conjunciones)

## INTERFAZ DE USUARIO

def imprimir_tabla(renglones):
    renglones = iter(renglones)
    encabezado = next(renglones)
    tam = tuple(map(len, encabezado))
    print('│'.join(encabezado))
    for renglon in renglones:
        print('│'.join(str(b).center(tam[i]) for i, b in enumerate(renglon)))

def main():
    print('Este programa funciona con expresiones booleanas de Python.\
\nEjemplo: not x or (not (y or w) and z)')
    f = input('Introduzca una fórmula: ')
    nodoraiz = compilar(f)
    print('Tabla de verdad:')
    imprimir_tabla(tabla_verdad(nodoraiz))
    fnc, fnd = formas_normales(nodoraiz)
    print('Forma normal conjuntiva:')
    print(formula(fnc))
    print('Forma normal disjuntiva:')
    print(formula(fnd))
main()
