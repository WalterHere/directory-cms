from collections import namedtuple

import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.test import Client
from wagtail.core.models import GroupPagePermission, PAGE_PERMISSION_TYPES

from export_readiness.tests.factories import (
    ArticleListingPageFactory,
    ArticlePageFactory,
    TopicLandingPageFactory,
)

User = get_user_model()
Branch = namedtuple(
    'Branch', ['listing', 'article', 'group', 'user', 'client']
)
TwoBranchesWithEditorModeratorAdmin = namedtuple(
    'TwoBranchesWithEditorModeratorAdmin', [
        'admins',
        'admin',
        'admin_client',
        'landing_1',
        'article_1',
        'editors_1',
        'editor_1',
        'editor_1_client',
        'moderators_1',
        'moderator_1',
        'moderator_1_client',
        'landing_2',
        'article_2',
        'editors_2',
        'editor_2',
        'editor_2_client',
        'moderators_2',
        'moderator_2',
        'moderator_2_client',
    ]
)


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Sequence(lambda n: "group %s" % n)


class GroupPagePermissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupPagePermission

    group = factory.SubFactory(GroupFactory)
    page = factory.SubFactory(ArticleListingPageFactory)
    permission_type = 'add'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user %s" % n)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_superuser = False
    is_staff = False

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.groups.add(group)


def branch_with_user(
        root_page,
        *,
        permissions=[],
        password='test',
        is_superuser=False,
        is_staff=False
):
    """Returns a listing page with a child page, user group, user & client.

    For Wagtail permission model check:
    http://docs.wagtail.io/en/v2.0/topics/permissions.html#page-permissions
    """
    # ensure that only permissions supported by Wagtail are used
    available_permissions = [p for p, _, _ in PAGE_PERMISSION_TYPES]
    assert not (set(permissions) - set(available_permissions))

    listing_page = ArticleListingPageFactory(parent=root_page)
    article_page = ArticlePageFactory(parent=listing_page)

    group = GroupFactory()
    group.permissions.add(Permission.objects.get(codename='access_admin'))

    for permission in permissions:
        GroupPagePermissionFactory(
            page=listing_page, group=group, permission_type=permission)

    user = UserFactory(
        is_superuser=is_superuser, is_staff=is_staff, groups=[group]
    )
    user_password = password or 'test'
    user.set_password(user_password)
    user.save()

    client = Client()
    client.login(username=user.username, password=user_password)

    return Branch(listing_page, article_page, group, user, client)


def two_branches_with_users(root_page):
    """
    Create 2 independent landing pages (also called branches),
    with an article page, editor and moderator in each branch.
    It also creates an Admin user associated with root_page.
    """

    def set_permissions(page, user_group, permissions):
        for perm in permissions:
            GroupPagePermissionFactory(
                page=page, group=user_group, permission_type=perm)

    landing_page_1, landing_page_2 = TopicLandingPageFactory.create_batch(
        2, parent=root_page, live=True
    )

    article_1 = ArticlePageFactory(parent=landing_page_1)
    article_2 = ArticlePageFactory(parent=landing_page_2)

    editors_1, moderators_1, editors_2, moderators_2, admins = \
        GroupFactory.create_batch(5)
    for group in [editors_1, moderators_1, editors_2, moderators_2, admins]:
        group.permissions.add(Permission.objects.get(codename='access_admin'))

    set_permissions(
        root_page,
        admins,
        ['add', 'edit', 'publish', 'bulk_delete', 'lock']
    )
    set_permissions(landing_page_1, editors_1, ['add', 'edit'])
    set_permissions(landing_page_1, moderators_1, ['add', 'edit', 'publish'])
    set_permissions(landing_page_2, editors_2, ['add', 'edit'])
    set_permissions(landing_page_2, moderators_2, ['add', 'edit', 'publish'])

    password = 'test'

    admin = UserFactory(
        is_superuser=True, is_staff=True, groups=[admins]
    )
    admin.set_password(password)
    admin.save()

    editor_1 = UserFactory(
        is_superuser=False, is_staff=False, groups=[editors_1]
    )
    editor_1.set_password(password)
    editor_1.save()

    moderator_1 = UserFactory(
        is_superuser=False, is_staff=False, groups=[moderators_1]
    )
    moderator_1.set_password(password)
    moderator_1.save()

    editor_2 = UserFactory(
        is_superuser=False, is_staff=False, groups=[editors_2]
    )
    editor_2.set_password(password)
    editor_2.save()

    moderator_2 = UserFactory(
        is_superuser=False, is_staff=False, groups=[moderators_2]
    )
    moderator_2.set_password(password)
    moderator_2.save()

    admin_client = Client()
    admin_client.login(username=admin.username, password=password)

    editor_1_client = Client()
    editor_1_client.login(username=editor_1.username, password=password)

    moderator_1_client = Client()
    moderator_1_client.login(username=moderator_1.username, password=password)

    editor_2_client = Client()
    editor_2_client.login(username=editor_2.username, password=password)

    moderator_2_client = Client()
    moderator_2_client.login(username=moderator_2.username, password=password)

    return TwoBranchesWithEditorModeratorAdmin(
        admins, admin, admin_client,
        landing_page_1, article_1,
        editors_1, editor_1, editor_1_client,
        moderators_1, moderator_1, moderator_1_client,
        landing_page_2, article_2,
        editors_2, editor_2, editor_2_client,
        moderators_2, moderator_2, moderator_2_client,
    )


class BranchEditorFactory:
    @staticmethod
    def get(root_page, *, permissions=['add', 'edit'], **kwargs):
        return branch_with_user(root_page, permissions=permissions, **kwargs)


class BranchModeratorFactory:
    @staticmethod
    def get(root_page, *, permissions=['add', 'edit', 'publish'], **kwargs):
        return branch_with_user(root_page, permissions=permissions, **kwargs)


class AdminFactory:
    @staticmethod
    def get(
            root_page,
            *,
            permissions=['add', 'edit', 'publish', 'bulk_delete', 'lock'],
            **kwargs
    ):
        return branch_with_user(
            root_page,
            permissions=permissions,
            is_superuser=True,
            is_staff=True,
            **kwargs
        )
