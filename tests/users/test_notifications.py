from unittest.mock import patch
import pytest
from users.notifications import (
    notifications_client,
    notify_user_of_access_request_approval,
    notify_team_leader_of_pending_access_request,
)

pytestmark = pytest.mark.django_db


def test_notify_user_of_access_request_approval(rf):
    request = rf.get('/')
    kwargs = dict(
        user_name='Jon Snow',
        user_email='jon.snow@winterfell.gov.uk',
        reviewer_name='Ygritte',
    )

    # patching with autospect=True so that incorrect argument names
    # will raise errors
    with patch.object(
        notifications_client,
        'send_email_notification',
        autospec=True
    ) as mocked_method:
        notify_user_of_access_request_approval(request, **kwargs)

    expected_call_args = dict(
        email_address=kwargs['user_email'],
        email_reply_to_id=None,
        template_id='approved-template-id',
        personalisation=dict(
            name=kwargs['user_name'],
            reviewer_name=kwargs['reviewer_name'],
            sign_in_url='http://testserver/admin/login/',
        ),
    )
    mocked_method.assert_called_with(**expected_call_args)


def test_notify_team_leader_of_pending_access_request(rf):
    request = rf.get('/')
    kwargs = dict(
        team_leader_name='Daenerys Targaryen',
        team_leader_email='theunburnt@dragonstone.gov.uk',
        user_id=123,
        user_name='Jorah Mormont',
        user_email='jorah.mormont@nowhere.com',
        user_role='Knight',
    )

    # patching with autospect=True so that incorrect argument names
    # will raise errors
    with patch.object(
        notifications_client,
        'send_email_notification',
        autospec=True
    ) as mocked_method:
        notify_team_leader_of_pending_access_request(request, **kwargs)

    expected_call_args = dict(
        email_address=kwargs['team_leader_email'],
        email_reply_to_id=None,
        template_id='pending-template-id',
        personalisation=dict(
            name=kwargs['team_leader_name'],
            user_name=kwargs['user_name'],
            user_email=kwargs['user_email'],
            user_role=kwargs['user_role'],
            review_url='http://testserver/admin/dit_users/%s/' % kwargs['user_id'],
        ),
    )
    mocked_method.assert_called_with(**expected_call_args)
