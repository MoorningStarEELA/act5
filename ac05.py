import flet as ft

def divVncer(lista, page):
    # Caso base: si la lista tiene un solo elemento, retornamos ese elemento
    if len(lista) == 1:
        page.add(ft.Text(f"Sumando: {lista[0]}"))
        return lista[0]
    else:
        # Dividimos la lista en dos mitades
        mitad = len(lista) // 2
        # Llamada recursiva para sumar la primera mitad de la lista
        page.add(ft.Text(f"Dividiendo lista en dos mitades: {lista[:mitad]} y {lista[mitad:]}"))
        smnIzq = divVncer(lista[:mitad], page)
        # Llamada recursiva para sumar la segunda mitad de la lista
        suma_derecha = divVncer(lista[mitad:], page)
        # Sumamos los resultados de ambas llamadas recursivas y retornamos la suma
        page.add(ft.Text(f"Sumando subtotales: {smnIzq} y {suma_derecha}"))
        total = smnIzq + suma_derecha
        page.add(ft.Text(f"Total parcial: {total}"))
        return total

def main(page):
    def btn_click(e):
        if not txt_cadena.value:
            txt_cadena.error_text = "Ingrese los números separados por espacios"
            page.update()
        else:
            nms = txt_cadena.value.split()
            # Convertimos los elementos de la lista a números enteros
            nms = [int(num) for num in nms]
            page.clean()
            resultado = divVncer(nms, page)
            page.add(ft.Text(f"La suma de los elementos de la lista es: {resultado}"))

    txt_cadena = ft.TextField(label="Ingrese los números separados por espacios")
    page.add(txt_cadena, ft.ElevatedButton("Sumar", on_click=btn_click))

ft.app(target=main)
