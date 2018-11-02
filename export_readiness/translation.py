from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from export_readiness import models


@register(models.TermsAndConditionsPage)
class TermsAndConditionsPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.PrivacyAndCookiesPage)
class PrivacyAndCookiesPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.DeprecatedGetFinancePage)
class DeprecatedGetFinancePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.NewGetFinancePage)
class NewGetFinancePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.ExportReadinessApp)
class ExportReadinessAppTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.PerformanceDashboardPage)
class PerformanceDashboardPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.PerformanceDashboardNotesPage)
class PerformanceDashboardNotesPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.TopicLandingPage)
class TopicLandingPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.ArticleListingPage)
class ArticleListingPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.ArticlePage)
class ArticlePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.HomePage)
class HomePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.EUExitInternationalFormPage)
class EUExitInternationalFormPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.EUExitDomesticFormPage)
class EUExitDomesticFormPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.EUExitFormSuccessPage)
class EUExitFormSuccessPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalLandingPage)
class InternationalLandingPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.ExportOpportunitiesGuidancePage)
class ExportOpportunitiesGuidancePageTranslationOptions(
    BaseTranslationOptions
):
    fields = []
