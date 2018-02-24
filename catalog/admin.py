from django.contrib import admin

# Import the models you've created and register each of them to the admin site

from .models import Author, Genre, Book, BookInstance, Language


# Django provide a default interface when registering models

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

# Customize interface for models

class BooksInline(admin.TabularInline):
    """
    Format for inline book insertion in AuthorAdmin
    """
    model = Book

# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    inlines = [BooksInstanceInline]

    # def display_genre(self):
    #     return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    # display_genre.short_description = 'Genre'


# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # list_filter creates filter box to the right of page
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )