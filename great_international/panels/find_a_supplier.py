from wagtail.admin.panels import (
    FieldPanel, FieldRowPanel, MultiFieldPanel, ObjectList
)

from core.helpers import make_translated_interface
from core.panels import SearchEngineOptimisationPanel


class InternationalTradeHomePagePanels:

    image_panels = [
        FieldPanel('hero_image'),
        FieldPanel('mobile_hero_image'),
    ]

    content_panels = [
        FieldPanel('title'),
        MultiFieldPanel(
            heading='Hero',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('hero_text'),
                FieldPanel('hero_image_caption'),
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
                            FieldPanel('services_column_one_icon'),
                            FieldPanel('services_column_one'),
                        ]),
                        MultiFieldPanel([
                            FieldPanel('services_column_two_icon'),
                            FieldPanel('services_column_two'),
                        ]),
                        MultiFieldPanel([
                            FieldPanel('services_column_three_icon'),
                            FieldPanel('services_column_three'),
                        ]),
                        MultiFieldPanel([
                            FieldPanel('services_column_four_icon'),
                            FieldPanel('services_column_four'),
                        ]),
                    ],
                ),
                FieldPanel('how_we_help_cta_text'),
                FieldPanel('how_we_help_cta_link'),
            ],
            classname='collapsible',
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )


class InternationalTradeIndustryContactPagePanels:

    content_panels = [
        FieldPanel('title'),
        MultiFieldPanel(
            heading='Contact form',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('introduction_text'),
                FieldPanel('submit_button_text'),
            ]
        ),
        MultiFieldPanel(
            heading='Success page',
            children=[
                FieldPanel('success_message_text'),
                FieldPanel('success_back_link_text'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]
    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )
