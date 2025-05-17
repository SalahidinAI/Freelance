from .models import Skill, Category, Project
from modeltranslation.translator import TranslationOptions,register

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('skill_name',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
