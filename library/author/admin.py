from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'get_books')  
    search_fields = ('name', 'surname')  
    list_filter = ('name', 'surname') 
    ordering = ('surname',)  

    def get_books(self, obj):
        books = obj.books.all()  
        books_list = [f"{i+1}) {book.name}" for i, book in enumerate(books)]  
        return " ".join(books_list)  

    get_books.short_description = 'Books'  

admin.site.register(Author, AuthorAdmin)
