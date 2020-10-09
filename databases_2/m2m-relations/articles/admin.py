from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleTag, Tag


# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     pass

@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class ArticleTagInlineFormset(BaseInlineFormSet):
    @property
    def clean(self):
        main_tag_counter = 0
        for form in self.forms:
            if not form.cleaned_data['main']:
                main_tag_counter += 1
        if main_tag_counter > 1:
            raise ValidationError('Выберите только один главный тэг')
        if main_tag_counter < 1:
            raise ValidationError('Выберите главный тэг')
        else:
            return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline]
