from django.shortcuts import render

PRODUCTOS = {
    "wedding-dog": {
        "nombre": "Wedding Dog",
        "precio": "$650",
        "imagen": "tienda/img/wedding-dog.jpg",
        "descripcion": "Un diseño elegante para celebraciones y ocasiones especiales.",
    },
    "tactical-dog": {
        "nombre": "Tactical Dog",
        "precio": "$300",
        "imagen": "tienda/img/tactical-dog.jpg",
        "descripcion": "Un diseño resistente y divertido para los perros con actitud.",
    },
    "christmas-dog": {
        "nombre": "Christmas Dog",
        "precio": "$250",
        "imagen": "tienda/img/christmas-dog.jpg",
        "descripcion": "El look perfecto para celebrar la temporada navideña.",
    },
    "dog-sweater": {
        "nombre": "Dog Sweater",
        "precio": "$125",
        "imagen": "tienda/img/dog-sweater.jpg",
        "descripcion": "Un suéter cómodo y adorable para tu compañero.",
    },
}

def inicio(request):
    return render(request, "tienda/inicio.html")

def productos(request):
    return render(request, "tienda/productos.html", {"productos": PRODUCTOS})

def detalle(request, producto):
    item = PRODUCTOS.get(producto)
    if item is None:
        return render(request, "tienda/detalle.html", {"producto": None}, status=404)
    return render(request, "tienda/detalle.html", {"producto": item})
