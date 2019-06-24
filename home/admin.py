from django.contrib import admin

from home.models import Book,Author,Genre,Issue


#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('id','name')
    fields=[('name','purchase_date'),('genre','author')]
    #note:RelatedonlyFieldList=>applicable when some fields are related to other tables
    list_filter = ('name','purchase_date',('author',admin.RelatedFieldListFilter))
    # list_filter=('name','purchase_date','Author')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    search_fields = ('name','id')
    fields=[('name','total_books_taken'),('issue_take','issue_return')]
    #note:RelatedonlyFieldList=>applicable when some fields are related to other tables
    list_filter = ('name','issue_take',('author',admin.RelatedFieldListFilter))
    # list_filter=('name','purchase_date','Author')

    