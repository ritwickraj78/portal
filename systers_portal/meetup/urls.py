from django.conf.urls import url

from .views import (MeetupView, AddMeetupView, DeleteMeetupView,
                    EditMeetupView, UpcomingMeetupsView, PastMeetupListView,
                    AddMeetupCommentView, EditMeetupCommentView,
                    DeleteMeetupCommentView, RsvpMeetupView, RsvpGoingView,
                    AddSupportRequestView, EditSupportRequestView, DeleteSupportRequestView,
                    SupportRequestView, SupportRequestsListView, ApproveSupportRequestView,
                    RejectSupportRequestView, UnapprovedSupportRequestsListView,
                    RequestMeetupView, NewMeetupRequestsListView, ViewMeetupRequestView,
                    ApproveRequestMeetupView, RejectMeetupRequestView, ApiForVmsView,
                    AllUpcomingMeetupsView, AddSupportRequestCommentView,
                    EditSupportRequestCommentView, DeleteSupportRequestCommentView,
                    UpcomingMeetupsSearchView, AddResourceView)

urlpatterns = [
    url(r'^upcoming/$', UpcomingMeetupsView.as_view(),
        name='upcoming_meetups'),
    url(r'^past/$', PastMeetupListView.as_view(),
        name='past_meetups'),
    url(r'^add/$', AddMeetupView.as_view(), name='add_meetup'),
    url(r'^(?P<meetup_slug>[\w-]+)/delete/$', DeleteMeetupView.as_view(),
        name='delete_meetup'),
    url(r'^(?P<meetup_slug>[\w-]+)/edit/$', EditMeetupView.as_view(),
        name="edit_meetup"),
    url(r'^(?P<meetup_slug>[\w-]+)/res/$', AddResourceView.as_view(),
        name="add_resource"),
    url(r'^request/$', RequestMeetupView.as_view(),
        name="request_meetup"),
    url(r'^view_meetup_requests/$', NewMeetupRequestsListView.as_view(),
        name="new_meetup_requests"),
    url(r'^(?P<meetup_slug>[\w-]+)/view_meetup_requests/$',
        ViewMeetupRequestView.as_view(), name="view_meetup_request"),
    url(r'^(?P<meetup_slug>[\w-]+)/approve_meetup_request/$',
        ApproveRequestMeetupView.as_view(), name="approve_meetup_request"),
    url(r'^(?P<meetup_slug>[\w-]+)/reject_meetup_request/$',
        RejectMeetupRequestView.as_view(), name="reject_meetup_request"),
    url(r'^all/search/$', UpcomingMeetupsSearchView.as_view(),
        name='search_meetups'),
    url(r'^all/$', AllUpcomingMeetupsView.as_view(),
        name='all_upcoming_meetups'),
    url(r'^(?P<meetup_slug>[\w-]+)/add_comment/$', AddMeetupCommentView.as_view(),
        name="add_meetup_comment"),
    url(r'^(?P<meetup_slug>[\w-]+)/edit_comment/(?P<comment_pk>\d+)/$',
        EditMeetupCommentView.as_view(),
        name="edit_meetup_comment"),
    url(r'^(?P<meetup_slug>[\w-]+)/delete_comment/(?P<comment_pk>\d+)/$',
        DeleteMeetupCommentView.as_view(),
        name="delete_meetup_comment"),
    url(r'^(?P<meetup_slug>[\w-]+)/rsvp/$', RsvpMeetupView.as_view(),
        name="rsvp_meetup"),
    url(r'^(?P<meetup_slug>[\w-]+)/going/$', RsvpGoingView.as_view(),
        name="rsvp_going"),
    url(r'^(?P<meetup_slug>[\w-]+)/add_support_request/$',
        AddSupportRequestView.as_view(),
        name='add_support_request'),
    url(r'^(?P<meetup_slug>[\w-]+)/edit_support_request/(?P<pk>\d+)/$',
        EditSupportRequestView.as_view(),
        name="edit_support_request"),
    url(r'^(?P<meetup_slug>[\w-]+)/delete_support_request/(?P<pk>\d+)/$',
        DeleteSupportRequestView.as_view(),
        name='delete_support_request'),
    url(r'^(?P<meetup_slug>[\w-]+)/support_request/(?P<pk>\d+)/$',
        SupportRequestView.as_view(),
        name="view_support_request"),
    url(r'^(?P<meetup_slug>[\w-]+)/support_requests_list/$',
        SupportRequestsListView.as_view(),
        name="list_support_requests"),
    url(r'^(?P<slug>[\w-]+)/unapproved_support_requests/$',
        UnapprovedSupportRequestsListView.as_view(),
        name="unapproved_support_requests"),
    url(r'^(?P<meetup_slug>[\w-]+)/support_request/approve/(?P<pk>\d+)/$',
        ApproveSupportRequestView.as_view(),
        name='approve_support_request'),
    url(r'^(?P<meetup_slug>[\w-]+)/support_request/reject/(?P<pk>\d+)/$',
        RejectSupportRequestView.as_view(),
        name='reject_support_request'),
    url(r'^(?P<meetup_slug>[\w-]+)/support_request/(?P<pk>\d+)/add_comment/$',
        AddSupportRequestCommentView.as_view(),
        name="add_support_request_comment"),
    url(r'^(?P<meetup_slug>[\w-]+)/support_request/(?P<pk>\d+)/edit_comment/'
        '(?P<comment_pk>\d+)/$',
        EditSupportRequestCommentView.as_view(),
        name="edit_support_request_comment"),
    url(r'^(?P<meetup_slug>[\w-]+)/support_request/(?P<pk>\d+)/delete_comment/'
        '(?P<comment_pk>\d+)/$',
        DeleteSupportRequestCommentView.as_view(),
        name="delete_support_request_comment"),
    url(r'^(?P<slug>[\w-]+)/$', MeetupView.as_view(), name="view_meetup"),
    url(r'^api/v1/request_meetup_data/$', ApiForVmsView.as_view(), name='vms_api'),
]
