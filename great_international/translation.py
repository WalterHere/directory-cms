from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from great_international import models


@register(models.GreatInternationalApp)
class GreatInternationalAppTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalMarketingPages)
class InternationalMarketingPagesTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalArticlePage)
class InternationalArticlePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalCampaignPage)
class InternationalCampaignPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalHomePage)
class InternationalHomePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalArticleListingPage)
class InternationalArticleListingPage(BaseTranslationOptions):
    fields = []


@register(models.InternationalUKHQPages)
class InternationalUKHQPagesTranslationOptions(BaseTranslationOptions):
    fields = []
