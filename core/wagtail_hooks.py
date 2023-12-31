from wagtail.admin.widgets import Button, PageListingButton
from wagtail import hooks
from wagtail.admin.wagtail_hooks import page_listing_buttons

from django.conf import settings
from django.templatetags.static import static
from django.urls import reverse
from django.utils.html import format_html
from core import helpers, models


@hooks.register('register_page_listing_more_buttons')
def add_copy_button(page, page_perms, next_url=None, is_parent=False):
    if isinstance(page, models.BasePage):
        yield Button(
            'Copy upstream',
            reverse('copy-upstream', kwargs={'pk': page.id}),
            attrs={'title': "Copy this page to another environment"},
            priority=80
        )
        yield Button(
            'Update upstream',
            reverse('update-upstream', kwargs={'pk': page.id}),
            attrs={'title': "Update this page on another environment"},
            priority=80
        )


@helpers.replace_hook('register_page_listing_buttons', page_listing_buttons)
def update_default_listing_buttons(page, page_perms, next_url=None, button_url_name=None):
    buttons = list(page_listing_buttons(page, page_perms, next_url))
    if isinstance(page, models.BasePage):
        for button in buttons:
            if (button_url_name and button_url_name == 'view_draft') or \
                    helpers.get_button_url_name(button) == 'view_draft':
                button.url = page.get_url(is_draft=True)

    else:
        # limit buttons for non-subclasses-of-BasePage
        allowed_urls = ['add_subpage']
        buttons = [
            button for button in buttons
            if helpers.get_button_url_name(button) in allowed_urls
        ]
        # since the drop-down is removed by the above, add a delete
        # button to this list
        if page_perms.can_delete():
            buttons.append(PageListingButton(
                'Delete',
                reverse('wagtailadmin_pages:delete', args=[page.id]),
                attrs={
                    'title': "Delete '%s'" % page.get_admin_display_title()
                },
            ))
    return buttons


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('core/css/editor.css')
    )


@hooks.register('insert_global_admin_css')
def global_admin_css():
    env_stylesheet = ''

    if settings.ENVIRONMENT_CSS_THEME_FILE:
        env_stylesheet = format_html(
            '<link rel="stylesheet" href="{}">',
            static(settings.ENVIRONMENT_CSS_THEME_FILE)
        )

    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('core/css/global.css')
    ) + env_stylesheet


@hooks.register('insert_editor_js')
def add_sum_required_fields_js():
    return format_html(
        '<script src="{0}"></script>',
        static('core/js/sum_required_localised_fields.js')
    )
