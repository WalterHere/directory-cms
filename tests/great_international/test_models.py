import pytest
from wagtail.core.models import Page

from great_international.models import (
    great_international, invest, capital_invest, find_a_supplier
)
from . import factories
from tests.export_readiness import factories as exread_factories


def test_models_hierarchy():
    # homepage / app root
    assert great_international.InternationalHomePage.allowed_subpage_models() \
        == [
        great_international.InternationalArticleListingPage,
        great_international.InternationalTopicLandingPage,
        great_international.InternationalCuratedTopicLandingPage,
        great_international.InternationalGuideLandingPage,
        great_international.InternationalRegionPage,
        great_international.InternationalEUExitFormPage,
        great_international.InternationalEUExitFormSuccessPage,
        great_international.AboutDitLandingPage,
        great_international.AboutUkLandingPage,
        capital_invest.InternationalCapitalInvestLandingPage,
        capital_invest.CapitalInvestOpportunityListingPage,
        capital_invest.CapitalInvestRegionPage,
        invest.InvestInternationalHomePage,
        find_a_supplier.InternationalTradeHomePage
    ]
    assert invest.InvestInternationalHomePage.allowed_subpage_models() == [
        invest.InvestHighPotentialOpportunitiesPage,
        invest.InvestRegionLandingPage,
    ]
    assert invest.InvestHighPotentialOpportunitiesPage.allowed_subpage_models() == [
        invest.InvestHighPotentialOpportunityDetailPage,
        invest.InvestHighPotentialOpportunityFormPage,
    ]
    assert invest.InvestHighPotentialOpportunityFormPage.allowed_subpage_models() == [
        invest.InvestHighPotentialOpportunityFormSuccessPage,
    ]
    assert great_international.InternationalHomePage.allowed_parent_page_models() == [Page]
    # region page
    assert great_international.InternationalRegionPage.allowed_subpage_models() == []
    # regional folder page
    assert great_international.InternationalLocalisedFolderPage.allowed_subpage_models() == []
    # topic landing
    assert great_international.InternationalTopicLandingPage.allowed_subpage_models() == [
            great_international.InternationalArticleListingPage,
            great_international.InternationalCampaignPage,
            great_international.InternationalSectorPage,
        ]
    # curated topic landing
    assert great_international.InternationalCuratedTopicLandingPage.allowed_subpage_models() == []
    # guide landing
    assert great_international.InternationalGuideLandingPage.allowed_subpage_models() == [
            great_international.InternationalArticlePage,
        ]
    # article listing
    assert great_international.InternationalArticleListingPage.allowed_subpage_models() == [
            great_international.InternationalArticlePage,
            great_international.InternationalCampaignPage
        ]
    # campaign
    assert great_international.InternationalCampaignPage.allowed_subpage_models() == [
            great_international.InternationalArticlePage,
        ]
    # EU Exit forms
    assert great_international.InternationalEUExitFormPage.allowed_subpage_models() == [
            great_international.InternationalEUExitFormSuccessPage,
        ]
    assert great_international.InternationalEUExitFormSuccessPage.allowed_parent_page_models() == [
            great_international.InternationalEUExitFormPage,
        ]
    assert capital_invest.InternationalCapitalInvestLandingPage.allowed_subpage_models() == [
            capital_invest.CapitalInvestContactFormPage,
        ]
    assert capital_invest.CapitalInvestOpportunityListingPage.allowed_subpage_models() == [
            capital_invest.CapitalInvestOpportunityPage,
        ]
    assert capital_invest.CapitalInvestContactFormPage.allowed_subpage_models() == [
            capital_invest.CapitalInvestContactFormSuccessPage
        ]
    assert capital_invest.CapitalInvestContactFormSuccessPage.allowed_subpage_models() == []
    assert great_international.InternationalSectorPage.allowed_subpage_models() == [
            great_international.InternationalSubSectorPage,
            great_international.InternationalArticlePage
        ]
    assert great_international.AboutDitLandingPage.allowed_subpage_models() == [
            great_international.AboutDitServicesPage
        ]
    assert great_international.AboutUkLandingPage.allowed_subpage_models() == [
            great_international.AboutUkWhyChooseTheUkPage,
            great_international.AboutUkRegionListingPage
        ]
    assert great_international.AboutUkRegionListingPage.allowed_subpage_models() == [
            great_international.AboutUkRegionPage
        ]
    assert great_international.AboutUkRegionPage.allowed_subpage_models() == []


@pytest.mark.django_db
def test_article_inherit_tags_from_parent(international_root_page):
    tag1 = exread_factories.TagFactory(name='foo')
    tag2 = exread_factories.TagFactory(name='bar')
    tag3 = exread_factories.TagFactory(name='xyz')
    article_listing_page = factories.InternationalArticleListingPageFactory(
        parent=international_root_page
    )
    article_listing_page.tags = [tag1, tag2]
    article_listing_page.save()

    article = factories.InternationalArticlePageFactory(
        parent=article_listing_page
    )
    article.tags = [tag3, ]
    article.save()

    assert list(
        article.tags.values_list('pk', flat=True)
    ) == [tag1.pk, tag2.pk, tag3.pk]


@pytest.mark.django_db
def test_campaign_inherit_tags_from_parent(international_root_page):
    tag1 = exread_factories.TagFactory(name='foo')
    tag2 = exread_factories.TagFactory(name='bar')
    tag3 = exread_factories.TagFactory(name='xyz')
    marketing_page = factories.InternationalArticleListingPageFactory(
        parent=international_root_page
    )
    marketing_page.tags = [tag1, tag2]
    marketing_page.save()

    campaign = factories.InternationalArticlePageFactory(
        parent=marketing_page
    )
    campaign.tags = [tag3, ]
    campaign.save()

    assert list(
        campaign.tags.values_list('pk', flat=True)
    ) == [tag1.pk, tag2.pk, tag3.pk]


@pytest.mark.django_db
def test_adding_new_tag_to_parent_propagate_to_descendants(
        international_root_page
):
    tag1 = exread_factories.TagFactory(name='foo')
    tag2 = exread_factories.TagFactory(name='bar')
    article_listing_page = factories.InternationalArticleListingPageFactory(
        parent=international_root_page
    )
    article_listing_page.tags.add(tag1)
    article_listing_page.save()

    article1 = factories.InternationalArticlePageFactory(
        parent=article_listing_page
    )
    article2 = factories.InternationalArticlePageFactory(
        parent=article_listing_page
    )

    assert list(
        article1.tags.values_list('pk', flat=True)
    ) == [tag1.pk]
    assert list(
        article2.tags.values_list('pk', flat=True)
    ) == [tag1.pk]

    article_listing_page.tags.add(tag2)
    article_listing_page.save()

    assert list(
        article1.tags.values_list('pk', flat=True)
    ) == [tag1.pk, tag2.pk]
    assert list(
        article2.tags.values_list('pk', flat=True)
    ) == [tag1.pk, tag2.pk]


@pytest.mark.django_db
def test_international_folder_page_append_parent_slug(international_root_page):
    region = factories.InternationalRegionPageFactory(
        slug='canada',
        parent=international_root_page
    )
    folder_page = factories.InternationalLocalisedFolderPageFactory(
        parent=region,
        slug='test'
    )
    assert folder_page.slug == 'test-canada'


@pytest.mark.django_db
def test_international_folder_page_append_parent_slug_only_on_creation(
    international_root_page
):
    region = factories.InternationalRegionPageFactory(
        slug='canada',
        parent=international_root_page
    )
    folder_page = factories.InternationalLocalisedFolderPageFactory(
        parent=region,
        slug='test'
    )
    assert folder_page.slug == 'test-canada'

    folder_page.save()
    assert folder_page.slug == 'test-canada'


@pytest.mark.django_db
def test_uses_tree_base_routing_always_true(international_root_page):
    page = factories.InternationalArticleListingPageFactory(
        parent=international_root_page
    )
    assert page.uses_tree_based_routing is True


@pytest.mark.django_db
def test_hpo_folder_page(international_root_page):
    int_home = factories.InternationalHomePageFactory(
        parent=international_root_page
    )
    invest_home = factories.InvestInternationalHomePageFactory(
        parent=int_home
    )
    invest_hpo_folder = factories.InvestHighPotentialOpportunitiesPageFactory(
        parent=invest_home
    )

    assert invest_hpo_folder.title == 'High potential opportunities'