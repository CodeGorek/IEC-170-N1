lnombre = ["Plumon", "Borrador", "Pizarra"]
lprecio = [1280.0, 3500.0, 13500.0]
lstock = [20, 8, 10]

def fn_actualizar_lista(lnombre, lprecio, lstock):
    productos = []
    for i in range(len(lnombre)):
        producto = {
            'nombre': lnombre[i],
            'precio': lprecio[i],
            'stock': lstock[i]
        }
        productos.append(producto)
