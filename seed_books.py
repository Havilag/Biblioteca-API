import os
import django

# Configurar el entorno de Django apuntando a tu carpeta 'biblioteca_api'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_api.settings')
django.setup()

from books.models import Book

# Lista de libros de prueba
books_data = [
    {
        "title": "Cien años de soledad",
        "author": "Gabriel García Márquez",
        "isbn": "9780307474728",
        "publication_year": 1967,
        "category": "NOVEL",
        "status": "AVAILABLE"
    },
    {
        "title": "El problema de los tres cuerpos",
        "author": "Cixin Liu",
        "isbn": "9788466659734",
        "publication_year": 2008,
        "category": "SCIENCE",
        "status": "AVAILABLE"
    },
    {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "isbn": "9780132350884",
        "publication_year": 2008,
        "category": "TECHNOLOGY",
        "status": "BORROWED"
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "isbn": "9780441172719",
        "publication_year": 1965,
        "category": "FANTASY",
        "status": "AVAILABLE"
    },
    {
        "title": "Sapiens: De animales a dioses",
        "author": "Yuval Noah Harari",
        "isbn": "9788499926223",
        "publication_year": 2011,
        "category": "HISTORY",
        "status": "MAINTENANCE"
    }
]

def run():
    print("Insertando libros de prueba...")
    created_count = 0
    
    for book in books_data:
        # get_or_create evita duplicar libros si ya existe el ISBN
        obj, created = Book.objects.get_or_create(
            isbn=book["isbn"],
            defaults=book
        )
        if created:
            created_count += 1
            print(f"✔ Creado: {obj.title}")
        else:
            print(f"⚠ Ya existía: {obj.title}")
            
    print(f"\n¡Proceso finalizado! Se agregaron {created_count} nuevos libros.")

if __name__ == "__main__":
    run()