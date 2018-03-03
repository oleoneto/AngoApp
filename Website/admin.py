"""
Written by Leo N.
Updated on November 19, 2017
"""

from django.contrib import admin
from Website.models import *
from Website.models import Message



#_____________________________________________________
# Admin panel actions: Publish, Draft, Feature, Unfeature

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark elements as published"

def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')
make_draft.short_description = "Mark elements as draft"

def make_featured(modeladmin, request, queryset):
    queryset.update(featured=True)
make_featured.short_description = "Mark as featured content"

def make_unfeatured(modeladmin, request, queryset):
    queryset.update(destaque=False)
make_unfeatured.short_description = "Unmark as featured content"

#____________________________________________________

class PhotoInline(admin.TabularInline):
    model = Photo


# The admin class for the Doc model
# fields are self-explanatory
class ArticleAdmin(admin.ModelAdmin):
    ordering = ['-publishedDate']
    list_display = ['title', 'author', 'slug',
                    'publishedDate','status']
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_draft, make_published]
    short_description = 'title'


# Person admin class featuring model actions
class PersonAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'role']
    prepopulated_fields = {"slug": ("name",)}
    actions = [make_published, make_draft]
    short_description = 'name'


# Project admin class featuring the Color model and model actions
class ProjectAdmin(admin.ModelAdmin):
    ordering = ['-publishedDate']
    list_display = ['title', 'client', 'type',
                    'publishedDate', 'status', 'featured']
    actions = [make_featured, make_draft, make_published, make_unfeatured]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PhotoInline]

# parterns
class PartnerAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'link']



class PartnerAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'link']

class MessageAdmin(admin.ModelAdmin):
    ordering = ['first_name']
    list_display = ['first_name', 'last_name', 'email',
                    'cellphone', 'tipo_de_servico','created']



###___________________________________________




# Registering Project and Person admin classes...
# If models are not beeing displayed in the admin dashboard,
# try logging in as a superuser
admin.site.site_header = "AngoApp"
admin.site.register(Article, ArticleAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Message,MessageAdmin)