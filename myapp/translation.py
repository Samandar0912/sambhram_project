from modeltranslation.translator import translator, TranslationOptions
from myapp.models import (
    NewsArticle, ElonArticle, HavolaImages, RectoratUserModel,
    UserModel, FacultetUserModel, FacultetInUserModel, MarkazUserModel,
    MarkazInUserModel, BulimUserModel, BulimInUserModel, KafedraUserModel,
    KafedraInUserModel
)

class NewsArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

class ElonArticleTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'body')

class HavolaImagesTranslationOptions(TranslationOptions):
    fields = ('name',)

class RectoratUserModelTranslationOptions(TranslationOptions):
    fields = ('name', 'body', 'rang', 'qabul_day')

class UserModelTranslationOptions(TranslationOptions):
    fields = ('name', 'rang', 'tg')

class FacultetUserModelTranslationOptions(TranslationOptions):
    fields = ('name', 'body', 'rang', 'qabul_day')

class FacultetInUserModelTranslationOptions(TranslationOptions):
    fields = ('name', 'rang', 'tg')

class MarkazUserModelTranslationOptions(TranslationOptions):
    fields = ('name', 'body', 'rang', 'qabul_day')

class MarkazInUserModelTranslationOptions(TranslationOptions):
    fields = ('name', 'rang', 'tg')

class BulimUserModelTranslationOptions(TranslationOptions):
    fields = ('name', 'body', 'rang', 'qabul_day')

class BulimInUserModelTranslationOptions(TranslationOptions):
    fields = ('name', 'rang', 'tg')

class KafedraUserModelTranslationOptions(TranslationOptions):
    fields = ('name', 'body', 'rang', 'qabul_day')

class KafedraInUserModelTranslationOptions(TranslationOptions):
    fields = ('name', 'rang', 'tg')

translator.register(NewsArticle, NewsArticleTranslationOptions)
translator.register(ElonArticle, ElonArticleTranslationOptions)
translator.register(HavolaImages, HavolaImagesTranslationOptions)
translator.register(RectoratUserModel, RectoratUserModelTranslationOptions)
translator.register(UserModel, UserModelTranslationOptions)
translator.register(FacultetUserModel, FacultetUserModelTranslationOptions)
translator.register(FacultetInUserModel, FacultetInUserModelTranslationOptions)
translator.register(MarkazUserModel, MarkazUserModelTranslationOptions)
translator.register(MarkazInUserModel, MarkazInUserModelTranslationOptions)
translator.register(BulimUserModel, BulimUserModelTranslationOptions)
translator.register(BulimInUserModel, BulimInUserModelTranslationOptions)
translator.register(KafedraUserModel, KafedraUserModelTranslationOptions)
translator.register(KafedraInUserModel, KafedraInUserModelTranslationOptions)