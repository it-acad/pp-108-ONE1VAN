from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'count', 'get_authors_list')
    list_filter = ('count', 'name')
    search_fields = ('name', 'description')
    ordering = ('name',)
    fieldsets = (
        ('Static Information', {
            'fields': ('name', 'get_authors_list'),
            'description': 'This section contains information that does not change.',
        }),
        ('Dynamic Information', {
            'fields': ('description', 'count'),
            'description': 'This section contains information that can change.',
        }),
    )
    readonly_fields = ('name', 'get_authors_list')  

    def get_authors_list(self, obj):
        authors = obj.authors.all() 
        return ", ".join([f"{author.name} {author.surname}" for author in authors])

    get_authors_list.short_description = 'Authors'

admin.site.register(Book, BookAdmin)
