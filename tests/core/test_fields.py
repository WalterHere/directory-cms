import pytest
from django.utils import translation
from rest_framework.serializers import Serializer
from wagtail import blocks
from wagtail.fields import StreamField

from core import fields
from great_international.serializers import InternationalArticlePageSerializer
from tests.great_international.factories import InternationalArticlePageFactory


@pytest.mark.django_db
def test_meta_field(rf, international_root_page):
    article_page = InternationalArticlePageFactory(
        parent=international_root_page,
        slug='test-slug',
    )

    serializer = InternationalArticlePageSerializer(
        instance=article_page,
        context={'request': rf.get('/')}
    )
    assert serializer.data['meta'] == {
        'draft_token': None,
        'languages': [('en-gb', 'English')],
        'url': 'http://great.gov.uk/international/content/test-slug/',
        'localised_urls': [
            (
                'en-gb',
                'http://great.gov.uk/international/content/test-slug/'
            )
        ],
        'slug': 'test-slug',
        'pk': article_page.pk
    }


@pytest.mark.django_db
def test_meta_field_slug_translation(international_root_page, rf):
    article_page = InternationalArticlePageFactory(
        parent=international_root_page,
        slug='test-slug',
    )

    with translation.override('de'):
        serializer = InternationalArticlePageSerializer(
            instance=article_page,
            context={'request': rf.get('/')}
        )
        data = serializer.data['meta']

    assert data == {
        'draft_token': None,
        'languages': [('en-gb', 'English')],
        'url': 'http://great.gov.uk/international/content/test-slug/',
        'localised_urls': [
            (
                'en-gb',
                'http://great.gov.uk/international/content/test-slug/'
            )
        ],
        'slug': 'test-slug',
        'pk': article_page.pk,
    }


@pytest.mark.django_db
def test_meta_field_contains_draft_token(page_with_reversion, rf):
    serializer = InternationalArticlePageSerializer(
        instance=page_with_reversion,
        context={'request': rf.get('/')}
    )

    url = f'http://great.gov.uk/international/content/{page_with_reversion.slug}/'
    token = page_with_reversion.get_draft_token()
    assert serializer.data['meta']['draft_token'] == token
    assert serializer.data['meta']['languages'] == [
            ('en-gb', 'English'),
            ('de', 'Deutsch'),
            ('ja', '日本語'),
            ('zh-hans', '简体中文'),
            ('fr', 'Français'),
            ('es', 'español'),
            ('pt', 'Português'),
            ('ar', 'العربيّة'),
    ]
    assert sorted(serializer.data['meta']['localised_urls']) == [
        ('ar', '{}{}'.format(url, '?lang=ar')),
        ('de', '{}{}'.format(url, '?lang=de')),
        ('en-gb', url),
        ('es', '{}{}'.format(url, '?lang=es')),
        ('fr', '{}{}'.format(url, '?lang=fr')),
        ('ja', '{}{}'.format(url, '?lang=ja')),
        ('pt', '{}{}'.format(url, '?lang=pt')),
        ('zh-hans', '{}{}'.format(url, '?lang=zh-hans')),
    ]


@pytest.mark.django_db
def test_meta_field_draft(international_root_page, rf):
    article_page = InternationalArticlePageFactory(
        parent=international_root_page,
        slug='test-slug',
    )
    serializer = InternationalArticlePageSerializer(
        instance=article_page,
        context={'is_draft': True}
    )

    assert serializer.data['meta']['url'] == article_page.get_url(is_draft=True)


@pytest.mark.django_db
def test_markdown_to_html_field_without_slug_hyperlinks(international_root_page, rf):
    article_page = InternationalArticlePageFactory(
        parent=international_root_page,
        slug='test-slug',
    )
    article_page.hero_text_en_gb = (
        '[hyperlink](slug:{slug})'.format(slug=article_page.slug)
    )

    class TestSerializer(Serializer):
        hero_text_en_gb = fields.MarkdownToHTMLField()

    serializer = TestSerializer(
        instance=article_page,
        context={'request': rf.get('/')}
    )

    assert serializer.data == {
        'hero_text_en_gb': (
            '<p><a>hyperlink</a></p>'
        )
    }


@pytest.mark.django_db
def test_single_struct_block_stream_field_factory():
    field = fields.single_struct_block_stream_field_factory(
        'test',
        block_class_instance=blocks.TextBlock(),
        max_num=6,
        min_num=1,
        null=True,
        blank=True
    )
    assert isinstance(field, StreamField)
    assert field.null is True
    assert field.blank is True
    assert field.stream_block._constructor_kwargs == {'max_num': 6, 'min_num': 1, 'required': False}
    assert isinstance(field.stream_block.child_blocks['test'], blocks.TextBlock)
