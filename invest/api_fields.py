from wagtail.api import APIField

from core.api_serializers import APIQuerysetSerializer
from invest.api_serializers import (
    APIChildrenSectorSerializer,
    APIChildrenSetupGuideSerializer,
    APIHighPotentialOpportunityDetailQuerysetSerializer,
)


class APIChildrenSetupGuidePageListField(APIField):
    def __init__(self, name):
        field_names = [
            'meta',
            'description',
            'heading',
            'sub_heading',
        ]
        # see explanation of the `fields_config` syntax here:
        # https://github.com/wagtail/wagtail/blob/
        # db6d36845f3f2c5d7009a22421c2efab9968aa24/wagtail/api/v2/utils.py#L68
        serializer = APIChildrenSetupGuideSerializer(
            name,
            fields_config=[(name, False, None) for name in field_names],
        )
        super().__init__(name=name, serializer=serializer)


class APISectorPageListField(APIField):
    def __init__(self, name, queryset, field_names=None):
        field_names = field_names or [
            'meta',
            'featured',
            'description',
            'heading',
            'hero_image',
        ]
        # see explanation of the `fields_config` syntax here:
        # https://github.com/wagtail/wagtail/blob/
        # db6d36845f3f2c5d7009a22421c2efab9968aa24/wagtail/api/v2/utils.py#L68
        serializer = APIQuerysetSerializer(
            name,
            fields_config=[(name, False, None) for name in field_names],
            queryset=queryset,
        )
        super().__init__(name=name, serializer=serializer)


class APISetupGuidePageListField(APIField):
    def __init__(self, name, queryset, field_names=None):
        field_names = field_names or [
            'meta',
            'description',
            'heading',
            'sub_heading',
        ]
        # see explanation of the `fields_config` syntax here:
        # https://github.com/wagtail/wagtail/blob/
        # db6d36845f3f2c5d7009a22421c2efab9968aa24/wagtail/api/v2/utils.py#L68
        serializer = APIQuerysetSerializer(
            name,
            fields_config=[(name, False, None) for name in field_names],
            queryset=queryset,
        )
        super().__init__(name=name, serializer=serializer)


class APIHighPotentialOpportunityDetailPageListField(APIField):
    def __init__(self, name, field_names=None):
        field_names = field_names or [
            'meta',
            'hero_image',
            'heading',
        ]
        # see explanation of the `fields_config` syntax here:
        # https://github.com/wagtail/wagtail/blob/
        # db6d36845f3f2c5d7009a22421c2efab9968aa24/wagtail/api/v2/utils.py#L68
        serializer = APIHighPotentialOpportunityDetailQuerysetSerializer(
            name,
            fields_config=[(name, False, None) for name in field_names],
        )
        super().__init__(name=name, serializer=serializer)
