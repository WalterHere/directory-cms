from core.cache import (
    AbstractDatabaseCacheSubscriber, RegionAwareCachePopulator
)

from great_international import models


class InternationalSectorPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalSectorPage
    subscriptions = [
        models.InternationalArticlePage,
        models.InternationalCampaignPage,
        models.CapitalInvestOpportunityPage
    ]


class InternationalHomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalHomePage
    subscriptions = [
        models.InternationalArticlePage,
    ]


class InternationalHomePageOldSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalHomePageOld
    subscriptions = [
        models.InternationalArticlePage,
    ]


class InternationalArticlePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalArticlePage
    subscriptions = []


class InternationalCampaignPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalCampaignPage
    subscriptions = []


class InternationalArticleListingPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    cache_populator = RegionAwareCachePopulator
    model = models.InternationalArticleListingPage
    subscriptions = [
        models.InternationalArticlePage,
        models.InternationalCampaignPage
    ]


class InternationalTopicLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalTopicLandingPage
    subscriptions = [
        models.InternationalArticlePage,
        models.InternationalArticleListingPage,
        models.InternationalSectorPage,
        models.InternationalCampaignPage
    ]


class InternationalCuratedTopicLandingPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.InternationalCuratedTopicLandingPage
    subscriptions = []


class InternationalGuideLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalGuideLandingPage
    subscriptions = [models.InternationalArticlePage]


class InternationalEUExitFormPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.InternationalEUExitFormPage
    subscriptions = []


class InternationalEUExitFormSuccessPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.InternationalEUExitFormSuccessPage
    subscriptions = []


class InternationalCapitalInvestLandingPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.InternationalCapitalInvestLandingPage
    subscriptions = [
        models.CapitalInvestRegionPage
    ]


class CapitalInvestRegionPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.CapitalInvestRegionPage
    subscriptions = []


class CapitalInvestOpportunityPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.CapitalInvestOpportunityPage
    subscriptions = [
        models.CapitalInvestOpportunityPage
    ]


class CapitalInvestOpportunityListingPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.CapitalInvestOpportunityListingPage
    subscriptions = [
        models.CapitalInvestOpportunityPage
    ]


class InvestInternationalHomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InvestInternationalHomePage
    subscriptions = [
        models.InternationalSectorPage,
        models.InvestHighPotentialOpportunityDetailPage
    ]


class InvestHighPotentialOpportunityFormPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.InvestHighPotentialOpportunityFormPage
    subscriptions = [
        models.InvestHighPotentialOpportunityDetailPage,
    ]


class InvestHighPotentialOpportunityDetailPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.InvestHighPotentialOpportunityDetailPage
    subscriptions = [
        models.InvestHighPotentialOpportunityDetailPage,
    ]


class InvestHighPotentialOpportunityFormSuccessPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.InvestHighPotentialOpportunityFormSuccessPage
    subscriptions = [
        models.InvestHighPotentialOpportunityDetailPage,
    ]


class InvestRegionLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InvestRegionLandingPage
    subscriptions = [
        models.InvestSectorPage,
    ]


class InvestSectorPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InvestSectorPage
    subscriptions = [
        # not a typo: each sector page contains a list of other sector pages
        models.InvestSectorPage,
    ]


class InternationalTradeHomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalTradeHomePage
    subscriptions = [
        models.InternationalSectorPage
    ]


class InternationalTradeIndustryContactPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.InternationalTradeIndustryContactPage
    subscriptions = [
        models.InternationalSectorPage,
    ]
