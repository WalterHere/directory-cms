import wagtail

import components.models
import components.serializers
import core.serializers
import export_readiness.models
import export_readiness.serializers
import great_international.models
import great_international.serializers
import find_a_supplier.models
import find_a_supplier.serializers
import invest.models
import invest.serializers


MODELS_SERIALIZERS_MAPPING = {
    # core page
    wagtail.core.models.Page: core.serializers.WagtailPageSerializer,
    # export_readiness
    export_readiness.models.TermsAndConditionsPage: export_readiness.serializers.GenericBodyOnlyPageSerializer,  # NOQA
    export_readiness.models.PrivacyAndCookiesPage: export_readiness.serializers.GenericBodyOnlyPageSerializer,  # NOQA
    export_readiness.models.GetFinancePage: export_readiness.serializers.GetFinancePageSerializer,  # NOQA
    export_readiness.models.PerformanceDashboardPage: export_readiness.serializers.PerformanceDashboardPageSerializer,  # NOQA
    export_readiness.models.PerformanceDashboardNotesPage: export_readiness.serializers.GenericBodyOnlyPageSerializer,  # NOQA
    export_readiness.models.ArticlePage: export_readiness.serializers.ArticlePageSerializer,  # NOQA
    export_readiness.models.MarketingArticlePage: export_readiness.serializers.MarketingArticlePageSerializer,  # NOQA
    export_readiness.models.HomePage: export_readiness.serializers.HomePageSerializer,  # NOQA
    export_readiness.models.HomePageOld: export_readiness.serializers.HomePageSerializer,  # NOQA
    export_readiness.models.ArticleListingPage: export_readiness.serializers.ArticleListingPageSerializer,  # NOQA
    export_readiness.models.TopicLandingPage: export_readiness.serializers.TopicLandingPageSerializer,  # NOQA
    export_readiness.models.InternationalLandingPage: export_readiness.serializers.InternationalLandingPageSerializer,  # NOQA
    export_readiness.models.CampaignPage: export_readiness.serializers.CampaignPageSerializer,  # NOQA
    export_readiness.models.EUExitInternationalFormPage: export_readiness.serializers.EUExitInternationalFormPageSerializer,  # NOQA
    export_readiness.models.EUExitDomesticFormPage: export_readiness.serializers.EUExitDomesticFormPageSerializer,  # NOQA
    export_readiness.models.EUExitFormSuccessPage: export_readiness.serializers.EUExitFormSuccessPageSerializer,  # NOQA
    export_readiness.models.ContactUsGuidancePage: export_readiness.serializers.ContactUsGuidancePageSerializer,  # NOQA
    export_readiness.models.ContactSuccessPage: export_readiness.serializers.ContactSuccessPageSerializer,  # NOQA
    export_readiness.models.SuperregionPage: export_readiness.serializers.SuperregionPageSerializer,  # NOQA
    export_readiness.models.CountryGuidePage: export_readiness.serializers.CountryGuidePageSerializer,  # NOQA
    # great international
    great_international.models.great_international.BaseInternationalSectorPage: great_international.serializers.BaseInternationalSectorPageSerializer,  # NOQA
    great_international.models.great_international.InternationalSectorPage: great_international.serializers.InternationalSectorPageSerializer,  # NOQA
    great_international.models.great_international.InternationalSubSectorPage: great_international.serializers.BaseInternationalSectorPageSerializer,  # NOQA
    great_international.models.great_international.InternationalHomePage: great_international.serializers.InternationalHomePageSerializer,  # NOQA
    great_international.models.great_international.InternationalHomePageOld: great_international.serializers.InternationalHomePageSerializer,  # NOQA
    great_international.models.great_international.InternationalArticlePage: great_international.serializers.InternationalArticlePageSerializer,  # NOQA
    great_international.models.great_international.InternationalCampaignPage: great_international.serializers.InternationalCampaignPageSerializer,  # NOQA
    great_international.models.great_international.InternationalArticleListingPage: great_international.serializers.InternationalArticleListingPageSerializer,  # NOQA
    great_international.models.great_international.InternationalTopicLandingPage: great_international.serializers.InternationalTopicLandingPageSerializer,  # NOQA
    great_international.models.great_international.InternationalCuratedTopicLandingPage: great_international.serializers.InternationalCuratedTopicLandingPageSerializer,  # NOQA
    great_international.models.great_international.InternationalGuideLandingPage: great_international.serializers.InternationalGuideLandingPageSerializer,  # NOQA
    great_international.models.great_international.InternationalEUExitFormPage: great_international.serializers.InternationalEUExitFormPageSerializer,  # NOQA
    great_international.models.great_international.InternationalEUExitFormSuccessPage: great_international.serializers.InternationalEUExitFormSuccessPageSerializer,  # NOQA
    great_international.models.great_international.AboutDitLandingPage: great_international.serializers.AboutDitLandingPageSerializer,  # NOQA
    great_international.models.great_international.AboutDitServicesPage: great_international.serializers.AboutDitServicesPageSerializer,  # NOQA
    great_international.models.capital_invest.InternationalCapitalInvestLandingPage: great_international.serializers.InternationalCapitalInvestLandingPageSerializer,  # NOQA
    great_international.models.capital_invest.CapitalInvestRegionPage: great_international.serializers.CapitalInvestRegionPageSerializer,  # NOQA
    great_international.models.capital_invest.CapitalInvestOpportunityListingPage: great_international.serializers.CapitalInvestOpportunityListingSerializer,  # NOQA
    great_international.models.capital_invest.CapitalInvestOpportunityPage: great_international.serializers.CapitalInvestOpportunityPageSerializer,  # NOQA
    great_international.models.invest.InvestInternationalHomePage: great_international.serializers.InvestInternationalHomePageSerializer,  # NOQA
    great_international.models.invest.InvestHighPotentialOpportunityFormSuccessPage: great_international.serializers.InvestHighPotentialOpportunityFormSuccessPageSerializer,  # NOQA
    great_international.models.invest.InvestHighPotentialOpportunityFormPage: great_international.serializers.InvestHighPotentialOpportunityFormPageSerializer,  # NOQA
    great_international.models.invest.InvestHighPotentialOpportunityDetailPage: great_international.serializers.InvestHighPotentialOpportunityDetailPageSerializer,   # NOQA
    great_international.models.find_a_supplier.InternationalTradeHomePage: great_international.serializers.InternationalTradeHomePageSerializer,  # NOQA
    great_international.models.find_a_supplier.InternationalTradeIndustryContactPage: great_international.serializers.InternationalTradeIndustryContactPageSerializer,  # NOQA
    great_international.models.invest.InvestSectorPage: great_international.serializers.InvestSectorPageSerializer,  # NOQA
    great_international.models.invest.InvestRegionLandingPage: great_international.serializers.InvestRegionalLandingPageSerializer,  # NOQA
    # invest
    invest.models.SectorLandingPage: invest.serializers.SectorLandingPageGenericSerializer,  # NOQA
    invest.models.RegionLandingPage: invest.serializers.SectorLandingPageGenericSerializer,  # NOQA
    invest.models.SectorPage: invest.serializers.SectorPageSerializer,
    invest.models.SetupGuideLandingPage: invest.serializers.SetupGuideLandingPageSerializer,  # NOQA
    invest.models.SetupGuidePage: invest.serializers.SetupGuidePageSerializer,
    invest.models.InvestHomePage: invest.serializers.InvestHomePageSerializer,
    invest.models.InfoPage: invest.serializers.InfoPageSerializer,
    invest.models.HighPotentialOpportunityFormPage: invest.serializers.HighPotentialOpportunityFormPageSerializer,  # NOQA
    invest.models.HighPotentialOpportunityDetailPage: invest.serializers.HighPotentialOpportunityDetailPageSerializer,  # NOQA
    invest.models.HighPotentialOpportunityFormSuccessPage: invest.serializers.HighPotentialOpportunityFormSuccessPageSerializer,  # NOQA
    # find a supplier
    find_a_supplier.models.IndustryPage: find_a_supplier.serializers.IndustryPageSerializer,  # NOQA
    find_a_supplier.models.IndustryLandingPage: find_a_supplier.serializers.IndustryLandingPageSerializer,  # NOQA
    find_a_supplier.models.IndustryArticlePage: find_a_supplier.serializers.IndustryArticlePageSerializer,  # NOQA
    find_a_supplier.models.LandingPage: find_a_supplier.serializers.LandingPageSerializer,  # NOQA
    find_a_supplier.models.IndustryContactPage: find_a_supplier.serializers.IndustryContactPageSerializer,  # NOQA
    # components
    components.models.BannerComponent: components.serializers.BannerComponentPageSerializer  # NOQA
}
