from core.cache import AbstractDatabaseCacheSubscriber

from great_international import models


class InternationalSectorPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalSectorPage
    subscriptions = [
        models.InternationalArticlePage,
        models.InternationalCampaignPage
    ]


class InternationalHomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalHomePage
    subscriptions = [
        models.InternationalArticlePage,
        models.InternationalMarketingPages
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
    model = models.InternationalArticleListingPage
    subscriptions = [
        models.InternationalArticlePage
    ]


class InternationalTopicLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalTopicLandingPage
    subscriptions = [
        models.InternationalArticlePage,
        models.InternationalArticleListingPage,
    ]
