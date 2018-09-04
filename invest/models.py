from directory_constants.constants import cms
from wagtail.api import APIField
from wagtail.admin.edit_handlers import (
    FieldPanel, ObjectList, MultiFieldPanel, FieldRowPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmedia.widgets import AdminMediaChooser

from django.db import models

from core.fields import (
    APIFormFieldField,
    APIImageField, APIMetaField,
    APIMarkdownToHTMLField,
    APIVideoField,
    MarkdownField,
)
from core.helpers import make_translated_interface
from core.models import BaseApp, BasePage, ExclusivePageMixin
from core.panels import SearchEngineOptimisationPanel

from invest import fields


class InvestApp(ExclusivePageMixin, BaseApp):
    service_name_value = cms.INVEST
    slug_identity = 'invest-app'

    @classmethod
    def get_required_translatable_fields(cls):
        return []


# Sector models

class SectorLandingPage(ExclusivePageMixin, BasePage):
    service_name_value = cms.INVEST
    subpage_types = ['invest.sectorPage']
    slug_identity = 'sector-landing-page'
    view_path = 'industries/'

    # page fields
    heading = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]
    content_panels = [
        FieldPanel('heading'),
        SearchEngineOptimisationPanel()

    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIField('heading'),
        APIImageField('hero_image'),
        fields.APIChildrenSectorPageListField('children_sectors'),
        APIMetaField('meta')
    ]


class RegionLandingPage(ExclusivePageMixin, BasePage):
    service_name_value = cms.INVEST
    subpage_types = ['invest.sectorPage']
    slug_identity = 'uk-region-landing-page'
    view_path = 'uk-regions/'

    # page fields
    heading = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]
    content_panels = [
        FieldPanel('heading'),
        SearchEngineOptimisationPanel()
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIField('heading'),
        APIImageField('hero_image'),
        fields.APIChildrenSectorPageListField('children_sectors'),
        APIMetaField('meta')
    ]


class SectorPage(BasePage):
    # Related sector are implemented as subpages
    service_name_value = cms.INVEST
    subpage_types = ['invest.sectorPage']
    view_path = 'industries/'

    featured = models.BooleanField(default=False)
    description = models.TextField()  # appears in card on external pages

    # page fields
    heading = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    pullout_text = MarkdownField(blank=True, null=True)
    pullout_stat = models.CharField(max_length=255, blank=True, null=True)
    pullout_stat_text = models.CharField(max_length=255, blank=True, null=True)

    subsection_title_one = models.CharField(max_length=200)
    subsection_content_one = MarkdownField()
    subsection_map_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_two = models.CharField(max_length=200)
    subsection_content_two = MarkdownField()
    subsection_map_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_three = models.CharField(max_length=200, blank=True)
    subsection_content_three = MarkdownField(blank=True)
    subsection_map_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_four = models.CharField(max_length=200, blank=True)
    subsection_content_four = MarkdownField(blank=True)
    subsection_map_four = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_five = models.CharField(max_length=200, blank=True)
    subsection_content_five = MarkdownField(blank=True)
    subsection_map_five = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_six = models.CharField(max_length=200, blank=True)
    subsection_content_six = MarkdownField(blank=True)
    subsection_map_six = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_seven = models.CharField(max_length=200, blank=True)
    subsection_content_seven = MarkdownField(blank=True)
    subsection_map_seven = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    # subsections end

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]
    content_panels = [
        FieldPanel('description'),
        FieldPanel('heading'),
        MultiFieldPanel(
            [
                FieldPanel('pullout_text'),
                FieldPanel('pullout_stat'),
                FieldPanel('pullout_stat_text')
            ],
            heading='Pullout',
            classname='collapsible'
        ),
        # subsections panels
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_one'),
                FieldPanel('subsection_content_one'),
                ImageChooserPanel('subsection_map_one')
            ],
            heading='subsections one',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_two'),
                FieldPanel('subsection_content_two'),
                ImageChooserPanel('subsection_map_two')
            ],
            heading='subsections two',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_three'),
                FieldPanel('subsection_content_three'),
                ImageChooserPanel('subsection_map_three')
            ],
            heading='subsections three',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_four'),
                FieldPanel('subsection_content_four'),
                ImageChooserPanel('subsection_map_four')
            ],
            heading='subsections four',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_five'),
                FieldPanel('subsection_content_five'),
                ImageChooserPanel('subsection_map_five')
            ],
            heading='subsections five',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_six'),
                FieldPanel('subsection_content_six'),
                ImageChooserPanel('subsection_map_six')
            ],
            heading='subsections six',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_seven'),
                FieldPanel('subsection_content_seven'),
                ImageChooserPanel('subsection_map_seven')
            ],
            heading='Subsection seven',
            classname='collapsible collapsed'
        ),
        SearchEngineOptimisationPanel()
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('featured')
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIField('description'),
        APIField('featured'),
        APIField('heading'),
        APIImageField('hero_image'),
        # pullout
        APIMarkdownToHTMLField('pullout_text'),
        APIField('pullout_stat'),
        APIField('pullout_stat_text'),
        # subsections
        APIField('subsection_title_one'),
        APIMarkdownToHTMLField('subsection_content_one'),
        APIImageField('subsection_map_one'),

        APIField('subsection_title_two'),
        APIMarkdownToHTMLField('subsection_content_two'),
        APIImageField('subsection_map_two'),

        APIField('subsection_title_three'),
        APIMarkdownToHTMLField('subsection_content_three'),
        APIImageField('subsection_map_three'),

        APIField('subsection_title_four'),
        APIMarkdownToHTMLField('subsection_content_four'),
        APIImageField('subsection_map_four'),

        APIField('subsection_title_five'),
        APIMarkdownToHTMLField('subsection_content_five'),
        APIImageField('subsection_map_five'),

        APIField('subsection_title_six'),
        APIMarkdownToHTMLField('subsection_content_six'),
        APIImageField('subsection_map_six'),

        APIField('subsection_title_seven'),
        APIMarkdownToHTMLField('subsection_content_seven'),
        APIImageField('subsection_map_seven'),

        fields.APIChildrenSectorPageListField('children_sectors'),
        APIMetaField('meta')
    ]


# Setup guide models

class SetupGuideLandingPage(ExclusivePageMixin, BasePage):
    service_name_value = cms.INVEST
    subpage_types = ['invest.SetupGuidePage']
    slug_identity = 'setup-guide-landing-page'
    view_path = 'setup-guide-landing/'

    # page fields
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    lead_in = models.TextField(blank=True)

    content_panels = [
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        FieldPanel('lead_in'),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIField('heading'),
        APIField('sub_heading'),
        APIField('lead_in'),
        fields.APIChildrenSetupGuidePageListField('children_setup_guides'),
        APIMetaField('meta')
    ]


class SetupGuidePage(BasePage):
    service_name_value = cms.INVEST
    view_path = 'setup-guides/'

    description = models.TextField()  # appears in card on external pages

    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)

    # subsections
    subsection_title_one = models.CharField(max_length=255)
    subsection_content_one = MarkdownField()

    subsection_title_two = models.CharField(max_length=255)
    subsection_content_two = MarkdownField()

    subsection_title_three = models.CharField(max_length=255, blank=True)
    subsection_content_three = MarkdownField(blank=True)

    subsection_title_four = models.CharField(max_length=255, blank=True)
    subsection_content_four = MarkdownField(blank=True)

    subsection_title_five = models.CharField(max_length=255, blank=True)
    subsection_content_five = MarkdownField(blank=True)

    subsection_title_six = models.CharField(max_length=255, blank=True)
    subsection_content_six = MarkdownField(blank=True)

    subsection_title_seven = models.CharField(max_length=255, blank=True)
    subsection_content_seven = MarkdownField(blank=True)

    content_panels = [
        FieldPanel('description'),
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        # subsections

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_one'),
                FieldPanel('subsection_content_one'),
            ],
            heading='subsections one',
            classname='collapsible'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_two'),
                FieldPanel('subsection_content_two'),
            ],
            heading='subsections two',
            classname='collapsible'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_three'),
                FieldPanel('subsection_content_three'),
            ],
            heading='subsections three',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_four'),
                FieldPanel('subsection_content_four'),
            ],
            heading='subsections four',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_five'),
                FieldPanel('subsection_content_five'),
            ],
            heading='subsections five',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_six'),
                FieldPanel('subsection_content_six'),
            ],
            heading='subsections six',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_seven'),
                FieldPanel('subsection_content_seven'),
            ],
            heading='subsections seven',
            classname='collapsible collapsed'
        ),

        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIField('description'),
        APIField('heading'),
        APIField('sub_heading'),
        # subsections
        APIField('subsection_title_one'),
        APIMarkdownToHTMLField('subsection_content_one'),

        APIField('subsection_title_two'),
        APIMarkdownToHTMLField('subsection_content_two'),

        APIField('subsection_title_three'),
        APIMarkdownToHTMLField('subsection_content_three'),

        APIField('subsection_title_four'),
        APIMarkdownToHTMLField('subsection_content_four'),

        APIField('subsection_title_five'),
        APIMarkdownToHTMLField('subsection_content_five'),

        APIField('subsection_title_six'),
        APIMarkdownToHTMLField('subsection_content_six'),

        APIField('subsection_title_seven'),
        APIMarkdownToHTMLField('subsection_content_seven'),

        fields.APIChildrenSetupGuidePageListField('children_setup_guides'),
        APIMetaField('meta')
    ]


class InvestHomePage(ExclusivePageMixin, BasePage):
    service_name_value = cms.INVEST
    slug_identity = 'home-page'
    view_path = ''

    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # subsections
    subsection_title_one = models.CharField(max_length=255)
    subsection_content_one = MarkdownField()

    subsection_title_two = models.CharField(max_length=255)
    subsection_content_two = MarkdownField()

    subsection_title_three = models.CharField(max_length=255, blank=True)
    subsection_content_three = MarkdownField(blank=True)

    subsection_title_four = models.CharField(max_length=255, blank=True)
    subsection_content_four = MarkdownField(blank=True)

    subsection_title_five = models.CharField(max_length=255, blank=True)
    subsection_content_five = MarkdownField(blank=True)

    subsection_title_six = models.CharField(max_length=255, blank=True)
    subsection_content_six = MarkdownField(blank=True)

    subsection_title_seven = models.CharField(max_length=255, blank=True)
    subsection_content_seven = MarkdownField(blank=True)

    sector_title = models.TextField(
        default="Discover UK Industries",
        max_length=255)

    sector_button_text = models.TextField(
        default="See more industries",
        max_length=255)

    setup_guide_title = models.CharField(
        default='Set up an overseas business in the UK',
        max_length=255)

    setup_guide_lead_in = models.TextField(
        blank=True,
        null=True)

    how_we_help_title = models.CharField(default='How we help', max_length=255)
    how_we_help_lead_in = models.TextField(blank=True, null=True)
    # how we help
    how_we_help_text_one = models.CharField(max_length=255)
    how_we_help_icon_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_two = models.CharField(max_length=255)
    how_we_help_icon_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_three = models.CharField(max_length=255)
    how_we_help_icon_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_four = models.CharField(max_length=255)
    how_we_help_icon_four = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_five = models.CharField(max_length=255)
    how_we_help_icon_five = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_six = models.CharField(max_length=255)

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]

    content_panels = [
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        # subsections
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_one'),
                FieldPanel('subsection_content_one'),
            ],
            heading='subsections one',
            classname='collapsible'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_two'),
                FieldPanel('subsection_content_two'),
            ],
            heading='subsections two',
            classname='collapsible'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_three'),
                FieldPanel('subsection_content_three'),
            ],
            heading='subsections three',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_four'),
                FieldPanel('subsection_content_four'),
            ],
            heading='subsections four',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_five'),
                FieldPanel('subsection_content_five'),
            ],
            heading='subsections five',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_six'),
                FieldPanel('subsection_content_six'),
            ],
            heading='subsections six',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_seven'),
                FieldPanel('subsection_content_seven'),
            ],
            heading='subsections seven',
            classname='collapsible collapsed'
        ),

        FieldPanel('sector_title'),
        FieldPanel('sector_button_text'),
        FieldPanel('setup_guide_title'),
        FieldPanel('setup_guide_lead_in'),
        FieldPanel('how_we_help_title'),
        FieldPanel('how_we_help_lead_in'),
        MultiFieldPanel(
            [
                FieldPanel('how_we_help_text_one'),
                ImageChooserPanel('how_we_help_icon_one')
            ],
            heading='How we help one',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('how_we_help_text_two'),
                ImageChooserPanel('how_we_help_icon_two')
            ],
            heading='How we help two',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('how_we_help_text_three'),
                ImageChooserPanel('how_we_help_icon_three')
            ],
            heading='How we help three',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('how_we_help_text_four'),
                ImageChooserPanel('how_we_help_icon_four')
            ],
            heading='How we help four',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('how_we_help_text_five'),
                ImageChooserPanel('how_we_help_icon_five')
            ],
            heading='How we help five',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('how_we_help_text_six'),
            ],
            heading='How we help six',
            classname='collapsible'
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIField('heading'),
        APIField('sub_heading'),
        APIImageField('hero_image'),
        # subsections
        APIField('subsection_title_one'),
        APIMarkdownToHTMLField('subsection_content_one'),

        APIField('subsection_title_two'),
        APIMarkdownToHTMLField('subsection_content_two'),

        APIField('subsection_title_three'),
        APIMarkdownToHTMLField('subsection_content_three'),

        APIField('subsection_title_four'),
        APIMarkdownToHTMLField('subsection_content_four'),

        APIField('subsection_title_five'),
        APIMarkdownToHTMLField('subsection_content_five'),

        APIField('subsection_title_six'),
        APIMarkdownToHTMLField('subsection_content_six'),

        APIField('subsection_title_seven'),
        APIMarkdownToHTMLField('subsection_content_seven'),

        APIField('sector_title'),
        APIField('sector_button_text'),
        APIField('setup_guide_title'),
        APIField('setup_guide_lead_in'),
        APIField('how_we_help_title'),
        APIField('how_we_help_lead_in'),
        # how we help
        APIField('how_we_help_text_one'),
        APIImageField('how_we_help_icon_one'),

        APIField('how_we_help_text_two'),
        APIImageField('how_we_help_icon_two'),

        APIField('how_we_help_text_three'),
        APIImageField('how_we_help_icon_three'),

        APIField('how_we_help_text_four'),
        APIImageField('how_we_help_icon_four'),

        APIField('how_we_help_text_five'),
        APIImageField('how_we_help_icon_five'),

        APIField('how_we_help_text_six'),

        fields.APISectorPageListField(
            'sectors',
            queryset=(
                SectorPage.objects.all()
                .filter(featured=True)
                .live()
                .order_by('heading')
            )
        ),
        fields.APISetupGuidePageListField(
            'guides',
            queryset=(
                SetupGuidePage.objects.all()
                .live()
                .order_by('heading')
            )
        ),
        APIMetaField('meta')
    ]


class InfoPage(BasePage):
    """
    Markdown page - used for terms and conditions
    and privacy policy
    """
    service_name_value = cms.INVEST
    view_path = 'info/'
    content = MarkdownField()

    content_panels = [
        FieldPanel('content'),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug')
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIMarkdownToHTMLField('content'),
        APIMetaField('meta')
    ]


class FormHelpTextField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs = {
            'max_length': 200,
            'verbose_name': 'Help text',
            'null': True,
            'blank': True,
            **kwargs,
        }
        super().__init__(*args, **kwargs)


class FormLabelField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs = {
            'max_length': 200,
            'verbose_name': 'label',
            **kwargs,
        }
        super().__init__(*args, **kwargs)


class HighPotentialOpportunityFormPage(ExclusivePageMixin, BasePage):
    fields_order = [
        'full_name',
        'role_in_company',
        'email_address',
        'phone_number',
        'company_name',
        'website_url',
        'country',
        'company_size',
        'opportunities',
        'comment',
        'terms_agreed',
    ]

    service_name_value = cms.INVEST
    view_path = 'high-potential-opportunities/'
    slug_identity = 'high-potential-opportunity-form'

    comment_help_text = FormHelpTextField()
    comment_label = FormLabelField()
    company_name_help_text = FormHelpTextField()
    company_name_label = FormLabelField()
    company_size_help_text = FormHelpTextField()
    company_size_label = FormLabelField()
    country_help_text = FormHelpTextField()
    country_label = FormLabelField()
    email_address_help_text = FormHelpTextField()
    email_address_label = FormLabelField()
    full_name_help_text = FormHelpTextField()
    full_name_label = FormLabelField()
    opportunities_help_text = FormHelpTextField()
    opportunities_label = FormLabelField()
    phone_number_help_text = FormHelpTextField()
    phone_number_label = FormLabelField()
    role_in_company_help_text = FormHelpTextField()
    role_in_company_label = FormLabelField()
    terms_agreed_help_text = FormHelpTextField()
    terms_agreed_label = FormLabelField()
    website_url_help_text = FormHelpTextField()
    website_url_label = FormLabelField()

    content_panels = [
        MultiFieldPanel(
            heading=name.replace('_', ' '),
            children=[
                FieldPanel(name + '_label'),
                FieldPanel(name + '_help_text'),
            ]
        ) for name in fields_order
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    api_fields = [APIFormFieldField(name) for name in fields_order]


class HighPotentialOpportunityDetailPage(BasePage):
    service_name_value = cms.INVEST
    view_path = 'high-potential-opportunities/'

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    contact_proposition = MarkdownField(blank=False)
    contact_button = models.CharField(max_length=500)
    proposition_one = MarkdownField(blank=False)
    proposition_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    proposition_one_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    opportunity_list_title = models.CharField(max_length=300)
    opportunity_list_item_one = MarkdownField()
    opportunity_list_item_two = MarkdownField()
    opportunity_list_item_three = MarkdownField()
    opportunity_list_image = models.ForeignKey(
        'wagtailimages.Image',
        related_name='+'
    )
    proposition_two = MarkdownField(blank=False)
    proposition_two_list_item_one = MarkdownField()
    proposition_two_list_item_two = MarkdownField()
    proposition_two_list_item_three = MarkdownField()
    proposition_two_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    proposition_two_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    competative_advantages_title = models.CharField(max_length=300)
    competative_advantages_list_item_one = MarkdownField()
    competative_advantages_list_item_two = MarkdownField()
    competative_advantages_list_item_three = MarkdownField()
    testimonial = MarkdownField()
    companies_list_text = MarkdownField()
    companies_list_item_image_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_four = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_five = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_six = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_seven = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_eight = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_list_title = models.CharField(max_length=300)
    case_study_one_text = MarkdownField(blank=True)
    case_study_one_image = models.ForeignKey(
        'wagtailimages.Image',
        related_name='+'
    )
    case_study_two_text = MarkdownField(blank=True)
    case_study_two_image = models.ForeignKey(
        'wagtailimages.Image',
        related_name='+'
    )
    case_study_three_text = MarkdownField(blank=True)
    case_study_three_image = models.ForeignKey(
        'wagtailimages.Image',
        related_name='+'
    )
    case_study_four_text = MarkdownField(blank=True)
    case_study_four_image = models.ForeignKey(
        'wagtailimages.Image',
        related_name='+'
    )

    content_panels = [
        MultiFieldPanel(
            heading='Hero',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('heading'),
                ImageChooserPanel('hero_image'),
            ]
        ),
        MultiFieldPanel(
            heading='Contact us',
            children=[
                FieldRowPanel(
                    children=[
                        FieldPanel('contact_proposition'),
                        FieldPanel('contact_button'),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Proposition one',
            children=[
                FieldRowPanel(
                    children=[
                        FieldPanel('proposition_one'),
                        MultiFieldPanel(
                            children=[
                                ImageChooserPanel('proposition_one_image'),
                                FieldPanel(
                                    'proposition_one_video',
                                    widget=AdminMediaChooser
                                ),
                            ]
                        )
                    ]
                )

            ]
        ),
        MultiFieldPanel(
            heading='Opportunity list',
            children=[
                FieldPanel('opportunity_list_title'),
                FieldRowPanel(
                    children=[
                        MultiFieldPanel(
                            children=[
                                FieldPanel('opportunity_list_item_one'),
                                FieldPanel('opportunity_list_item_two'),
                                FieldPanel('opportunity_list_item_three'),
                            ]
                        ),
                        ImageChooserPanel('opportunity_list_image'),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Opportunity list',
            children=[
                FieldRowPanel(
                    children=[
                        MultiFieldPanel(
                            children=[
                                FieldPanel('proposition_two'),
                                FieldPanel('proposition_two_list_item_one'),
                                FieldPanel('proposition_two_list_item_two'),
                                FieldPanel('proposition_two_list_item_three'),
                            ]
                        ),
                        MultiFieldPanel(
                            children=[
                                ImageChooserPanel('proposition_two_image'),
                                FieldPanel(
                                    'proposition_two_video',
                                    widget=AdminMediaChooser
                                ),
                            ]
                        )
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Competitive advantage',
            children=[
                FieldPanel('competative_advantages_title'),
                FieldRowPanel(
                    children=[
                        FieldPanel('competative_advantages_list_item_one'),
                        FieldPanel('competative_advantages_list_item_two'),
                        FieldPanel('competative_advantages_list_item_three'),
                    ]
                )
            ]
        ),
        FieldPanel('testimonial'),
        MultiFieldPanel(
            heading='Company list',
            children=[
                FieldPanel('companies_list_text'),
                FieldRowPanel(
                    children=[
                        ImageChooserPanel('companies_list_item_image_one'),
                        ImageChooserPanel('companies_list_item_image_two'),
                        ImageChooserPanel('companies_list_item_image_three'),
                        ImageChooserPanel('companies_list_item_image_four'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        ImageChooserPanel('companies_list_item_image_five'),
                        ImageChooserPanel('companies_list_item_image_six'),
                        ImageChooserPanel('companies_list_item_image_seven'),
                        ImageChooserPanel('companies_list_item_image_eight'),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Company list',
            children=[
                FieldPanel('case_study_list_title'),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_one_text'),
                        ImageChooserPanel('case_study_one_image'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_two_text'),
                        ImageChooserPanel('case_study_two_image'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_three_text'),
                        ImageChooserPanel('case_study_three_image'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_four_text'),
                        ImageChooserPanel('case_study_four_image'),
                    ]
                )
            ]
        )

    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    api_fields = [
        APIField('breadcrumbs_label'),
        APIField('heading'),
        APIImageField('hero_image'),
        APIMarkdownToHTMLField('contact_proposition'),
        APIField('contact_button'),
        APIMarkdownToHTMLField('proposition_one'),
        APIMarkdownToHTMLField('proposition_one_image'),
        APIVideoField('proposition_one_video'),
        APIField('opportunity_list_title'),
        APIMarkdownToHTMLField('opportunity_list_item_one'),
        APIMarkdownToHTMLField('opportunity_list_item_two'),
        APIMarkdownToHTMLField('opportunity_list_item_three'),
        APIMarkdownToHTMLField('opportunity_list_image'),
        APIMarkdownToHTMLField('proposition_two'),
        APIMarkdownToHTMLField('proposition_two_list_item_one'),
        APIMarkdownToHTMLField('proposition_two_list_item_two'),
        APIMarkdownToHTMLField('proposition_two_list_item_three'),
        APIMarkdownToHTMLField('proposition_two_image'),
        APIVideoField('proposition_two_video'),
        APIField('competative_advantages_title'),
        APIMarkdownToHTMLField('competative_advantages_list_item_one'),
        APIMarkdownToHTMLField('competative_advantages_list_item_two'),
        APIMarkdownToHTMLField('competative_advantages_list_item_three'),
        APIMarkdownToHTMLField('testimonial'),
        APIMarkdownToHTMLField('companies_list_text'),
        APIMarkdownToHTMLField('companies_list_item_image_one'),
        APIMarkdownToHTMLField('companies_list_item_image_two'),
        APIMarkdownToHTMLField('companies_list_item_image_three'),
        APIMarkdownToHTMLField('companies_list_item_image_four'),
        APIMarkdownToHTMLField('companies_list_item_image_five'),
        APIMarkdownToHTMLField('companies_list_item_image_six'),
        APIMarkdownToHTMLField('companies_list_item_image_seven'),
        APIMarkdownToHTMLField('companies_list_item_image_eight'),
        APIField('case_study_list_title'),
        APIMarkdownToHTMLField('case_study_one_text'),
        APIMarkdownToHTMLField('case_study_one_image'),
        APIMarkdownToHTMLField('case_study_two_text'),
        APIMarkdownToHTMLField('case_study_two_image'),
        APIMarkdownToHTMLField('case_study_three_text'),
        APIMarkdownToHTMLField('case_study_three_image'),
        APIMarkdownToHTMLField('case_study_four_text'),
        APIMarkdownToHTMLField('case_study_four_image'),
    ]
