from directory_constants.constants import choices
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel, MultiFieldPanel, ObjectList, PageChooserPanel
)
from wagtail.api import APIField
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from django.db import models

from core import constants
from core.models import BasePage, ExcludeivePageMixin
from core.helpers import make_translated_interface
from core.fields import APIRichTextField, APIImageField, APIMetaField
from find_a_supplier import fields


class ImageChooserPanel(ImageChooserPanel):
    classname = ""


class IndustryPage(BasePage):

    view_app = constants.FIND_A_SUPPLIER
    view_path = 'industries/'

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_text = RichTextField(blank=False)
    introduction_text = RichTextField(blank=False)
    introduction_column_one_text = RichTextField(blank=False)
    introduction_column_two_text = RichTextField(blank=False)
    introduction_column_three_text = RichTextField(blank=False)
    introduction_column_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    introduction_column_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    introduction_column_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    sector_label = models.CharField(
        max_length=255,
    )
    sector_value = models.CharField(
        max_length=255,
        choices=choices.INDUSTRIES,
    )
    company_list_text = RichTextField(
        blank=False,
    )
    company_list_call_to_action_text = models.CharField(
        max_length=255,
    )

    article_one = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_two = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_three = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_four = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_five = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_six = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    image_panels = [
        ImageChooserPanel('hero_image'),
    ]
    content_panels = [
        MultiFieldPanel(
            heading='Hero',
            children=[
                FieldPanel('hero_text', classname='full'),
                FieldPanel('sector_label'),
            ]
        ),
        MultiFieldPanel(
            heading='Introduction',
            children=[
                FieldPanel('introduction_text', classname='full'),
                FieldRowPanel(
                    classname='full field-row-panel',
                    children=[
                        MultiFieldPanel([
                            FieldPanel('introduction_column_one_text'),
                            ImageChooserPanel('introduction_column_one_icon'),
                        ]),
                        MultiFieldPanel([
                            FieldPanel('introduction_column_two_text'),
                            ImageChooserPanel('introduction_column_two_icon'),
                        ]),
                        MultiFieldPanel([
                            FieldPanel('introduction_column_three_text'),
                            ImageChooserPanel(
                                'introduction_column_three_icon'
                            ),
                        ])
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Companies',
            children=[
                FieldPanel('company_list_text'),
                FieldPanel('company_list_call_to_action_text'),
            ]
        ),
        MultiFieldPanel(
            heading='Search Engine Optimisation',
            children=[
                FieldPanel('slug'),
                FieldPanel('seo_title'),
                FieldPanel('search_description'),
            ]
        )
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('sector_value'),
    ]
    article_panels = [
        PageChooserPanel('article_one', 'find_a_supplier.IndustryArticlePage'),
        PageChooserPanel('article_two', 'find_a_supplier.IndustryArticlePage'),
        PageChooserPanel(
            'article_three', 'find_a_supplier.IndustryArticlePage'
        ),
        PageChooserPanel(
            'article_four', 'find_a_supplier.IndustryArticlePage'
        ),
        PageChooserPanel(
            'article_five', 'find_a_supplier.IndustryArticlePage'
        ),
        PageChooserPanel('article_six', 'find_a_supplier.IndustryArticlePage'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
            ObjectList(article_panels, heading='Articles')
        ]
    )

    api_fields = [
        APIImageField('hero_image'),
        APIRichTextField('hero_text'),
        APIRichTextField('introduction_text'),
        APIRichTextField('introduction_column_one_text'),
        APIRichTextField('introduction_column_two_text'),
        APIRichTextField('introduction_column_three_text'),
        APIImageField('introduction_column_one_icon'),
        APIImageField('introduction_column_two_icon'),
        APIImageField('introduction_column_three_icon'),
        APIRichTextField('company_list_text'),
        APIField('company_list_call_to_action_text'),
        APIField('sector_label'),
        APIField('sector_value'),
        APIField('title'),
        APIField('article_one'),
        APIField('article_two'),
        APIField('article_three'),
        APIField('article_four'),
        APIField('article_five'),
        APIField('article_six'),
        APIField('seo_title'),
        APIField('search_description'),
        APIMetaField('meta'),
    ]


class IndustryLandingPage(ExcludeivePageMixin, BasePage):
    view_app = constants.FIND_A_SUPPLIER
    view_path = 'industries/'

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    hero_title = models.CharField(max_length=500)
    proposition_text = models.CharField(max_length=500)
    call_to_action_text = models.CharField(max_length=500)
    breadcrumbs_label = models.CharField(max_length=500)

    @property
    def url_path_parts(self):
        return [self.view_path]

    api_fields = [
        APIField('hero_title'),
        APIImageField('hero_image'),
        APIField('proposition_text'),
        APIField('call_to_action_text'),
        APIField('title'),
        APIField('breadcrumbs_label'),
        APIField('seo_title'),
        APIField('search_description'),
        APIMetaField('meta'),
        fields.APIIndustriesListField(
            'industries',
            queryset=IndustryPage.objects.all()[0:9],
        ),
    ]

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        FieldPanel('hero_title'),
        MultiFieldPanel(
            heading='Contact us',
            children=[
                FieldRowPanel(
                    children=[
                        FieldPanel('proposition_text'),
                        FieldPanel('call_to_action_text'),
                    ],
                    classname='full field-row-panel'
                ),
            ]
        ),
        MultiFieldPanel(
            heading='Search Engine Optimisation',
            children=[
                FieldPanel('slug'),
                FieldPanel('seo_title'),
                FieldPanel('search_description'),
            ]
        )
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )


class IndustryArticlePage(BasePage):

    view_app = constants.FIND_A_SUPPLIER
    view_path = 'industry-articles/'

    introduction_title = models.CharField(max_length=255)
    body = RichTextField(blank=False)
    author_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    date = models.DateField()

    content_panels = [
        MultiFieldPanel(
            heading='Article',
            children=[
                FieldPanel('introduction_title'),
                FieldPanel('body', classname='full'),
            ]
        ),
        MultiFieldPanel(
            heading='Author',
            children=[
                FieldPanel('author_name'),
                FieldPanel('job_title'),
                FieldPanel('date'),
            ]
        ),
        MultiFieldPanel(
            heading='Search Engine Optimisation',
            children=[
                FieldPanel('slug'),
                FieldPanel('seo_title'),
                FieldPanel('search_description'),
            ]
        )
    ]

    settings_panels = [
        FieldPanel('title_en_gb')
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )

    api_fields = [
        APIField('author_name'),
        APIField('job_title'),
        APIField('date'),
        APIRichTextField('body'),
        APIField('title'),
        APIField('seo_title'),
        APIField('search_description'),
        APIMetaField('meta'),
    ]


class LandingPage(ExcludeivePageMixin, BasePage):
    view_app = constants.FIND_A_SUPPLIER
    view_path = '/'

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_text = RichTextField(blank=False)
    search_field_placeholder = models.CharField(max_length=500)
    search_button_text = models.CharField(max_length=500)
    proposition_text = RichTextField(blank=False)
    call_to_action_text = models.CharField(max_length=500)
    industries_list_text = RichTextField(blank=False)
    industries_list_call_to_action_text = models.CharField(max_length=500)
    services_list_text = RichTextField(blank=False)
    services_column_one = RichTextField(blank=False)
    services_column_two = RichTextField(blank=False)
    services_column_three = RichTextField(blank=False)
    services_column_four = RichTextField(blank=False)
    services_column_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    services_column_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    services_column_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    services_column_four_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    article_one = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_two = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_three = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_four = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_five = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_six = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    @property
    def url_path_parts(self):
        return [self.view_path]

    api_fields = [
        APIImageField('hero_image'),
        APIRichTextField('hero_text'),
        APIField('search_field_placeholder'),
        APIField('search_button_text'),
        APIRichTextField('proposition_text'),
        APIField('call_to_action_text'),
        APIRichTextField('industries_list_text'),
        APIField('industries_list_call_to_action_text'),
        APIRichTextField('services_list_text'),
        APIRichTextField('services_column_one'),
        APIRichTextField('services_column_two'),
        APIRichTextField('services_column_three'),
        APIRichTextField('services_column_four'),
        APIImageField('services_column_one_icon'),
        APIImageField('services_column_two_icon'),
        APIImageField('services_column_three_icon'),
        APIImageField('services_column_four_icon'),
        APIField('article_one'),
        APIField('article_two'),
        APIField('article_three'),
        APIField('article_four'),
        APIField('article_five'),
        APIField('article_six'),
        APIField('title'),
        APIField('search_description'),
        APIField('seo_title'),
        fields.APIIndustriesListField(
            'industries',
            queryset=IndustryPage.objects.all()[0:9],
        ),
        APIMetaField('meta'),
    ]

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]
    article_panels = [
        PageChooserPanel('article_one', 'find_a_supplier.IndustryArticlePage'),
        PageChooserPanel('article_two', 'find_a_supplier.IndustryArticlePage'),
        PageChooserPanel(
            'article_three', 'find_a_supplier.IndustryArticlePage'
        ),
        PageChooserPanel(
            'article_four', 'find_a_supplier.IndustryArticlePage'
        ),
        PageChooserPanel(
            'article_five', 'find_a_supplier.IndustryArticlePage'
        ),
        PageChooserPanel('article_six', 'find_a_supplier.IndustryArticlePage'),
    ]

    content_panels = [
        MultiFieldPanel(
            heading='Hero',
            children=[
                FieldPanel('hero_text'),
                FieldPanel('search_field_placeholder'),
                FieldPanel('search_button_text'),
            ],
            classname='collapsible',
        ),
        MultiFieldPanel(
            heading='Contact us',
            children=[
                FieldPanel('proposition_text'),
                FieldPanel('call_to_action_text'),
            ],
            classname='collapsible',
        ),
        MultiFieldPanel(
            heading='Industries',
            children=[
                FieldPanel('industries_list_text'),
                FieldPanel('industries_list_call_to_action_text'),
            ],
            classname='collapsible',
        ),
        MultiFieldPanel(
            heading='Services',
            children=[
                FieldPanel('services_list_text'),
                FieldRowPanel(
                    classname='full field-row-panel',
                    children=[
                        MultiFieldPanel([
                            ImageChooserPanel('services_column_one_icon'),
                            FieldPanel('services_column_one'),
                        ]),
                        MultiFieldPanel([
                            ImageChooserPanel('services_column_two_icon'),
                            FieldPanel('services_column_two'),
                        ]),
                        MultiFieldPanel([
                            ImageChooserPanel('services_column_three_icon'),
                            FieldPanel('services_column_three'),
                        ]),
                        MultiFieldPanel([
                            ImageChooserPanel('services_column_four_icon'),
                            FieldPanel('services_column_four'),
                        ]),
                    ]
                ),
            ],
            classname='collapsible',
        ),
        MultiFieldPanel(
            heading='Search Engine Optimisation',
            children=[
                FieldPanel('slug'),
                FieldPanel('seo_title'),
                FieldPanel('search_description'),
            ]
        )
    ]

    settings_panels = [FieldPanel('title_en_gb')]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
            ObjectList(article_panels, heading='Articles'),
        ]
    )
