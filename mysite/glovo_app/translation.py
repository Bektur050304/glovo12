from .models import *
from modeltranslation.translator import TranslationOptions,register



@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )



@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description', )


@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('store_name', 'description', 'address')


@register(Combo)
class ComboTranslationOptions(TranslationOptions):
    fields = ('combo_name', 'description', )

