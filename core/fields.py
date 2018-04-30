from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField
from wagtailmarkdown.fields import MarkdownField as OriginalMarkdownField

from core import serializers, widgets


class APIMarkdownToHTMLField(APIField):
    def __init__(self, name):
        serializer = serializers.APIMarkdownToHTMLSerializer()
        super().__init__(name=name, serializer=serializer)


class APIImageField(APIField):
    def __init__(self, name):
        serializer = ImageRenditionField('original')
        super().__init__(name=name, serializer=serializer)


class APIMetaField(APIField):
    def __init__(self, name):
        serializer = serializers.APIMetaSerializer(name)
        super().__init__(name=name, serializer=serializer)


class APIBreadcrumbsField(APIField):
    def __init__(self, name, app_label):
        serializer = serializers.APIBreadcrumsSerializer(
            app_label
        )
        super().__init__(name=name, serializer=serializer)


class APIVideoField(APIField):
    def __init__(self, name):
        serializer = serializers.APIVideoSerializer()
        super().__init__(name=name, serializer=serializer)


class MarkdownField(OriginalMarkdownField):
    def formfield(self, **kwargs):
        kwargs['widget'] = widgets.MarkdownTextarea
        return super().formfield(**kwargs)
