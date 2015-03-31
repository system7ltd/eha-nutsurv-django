from django.conf.urls import include, patterns, url

from rest_framework import routers

from tastypie.api import Api

from api.resources import HouseholdSurveyJSONResource

from .views import TeamsJSONView
from .views import AggregateSurveyDataJSONView
from .views import PersonnelJSONView
from .views import ActiveQuestionnaireSpecificationView
from .views import ClustersPerFirstAdminLevelJSONView
from .views import FirstAdminLevelJSONView
from .views import FirstAdminLevelsReserveClustersJSONView
from .views import ClustersJSONView
from .views import AlertViewSet
from .views import HouseholdSurveyJSONViewset
from .views import TeamMemberViewset


v1_api = Api(api_name='v1')
v1_api.register(HouseholdSurveyJSONResource())

router = routers.DefaultRouter()
router.register(r'alerts', AlertViewSet)
router.register(r'surveys', HouseholdSurveyJSONViewset)
router.register(r'teammembers', TeamMemberViewset)

urlpatterns = patterns('',
                       url(r'^api/', include(v1_api.urls)),

                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

                       url(r'^home$', 'dashboard.views.home', name='home'),

                       url(r'^fieldwork$',
                           'dashboard.views.fieldwork',
                           name='fieldwork'),
                       url(r'^age_distribution$',
                           'dashboard.views.age_distribution',
                           name='age_distribution'),
                       url(r'^survey_completed_teams$',
                           'dashboard.views.survey_completed_teams',
                           name='survey_completed_teams'),
                       url(r'^survey_completed_strata$',
                           'dashboard.views.survey_completed_strata',
                           name='survey_completed_strata'),
                       url(r'^missing_data$',
                           'dashboard.views.missing_data',
                           name='missing_data'),
                       url(r'^data_quality$',
                           'dashboard.views.data_quality',
                           name='data_quality'),
                       url(r'^personnel$',
                        'dashboard.views.personnel',
                        name='personnel'),
                       url(r'^time_of_data_collection$',
                        'dashboard.views.time_of_data_collection',
                        name='time_of_data_collection'),
                       url(r'^teamsjsonview/$', TeamsJSONView.as_view(),
                           name='teams-json-view'),
                       url(r'^personneljsonview/$', PersonnelJSONView.as_view(),
                           name='personnel-json-view'),
                       url(r'^aggregatesurveydatajsonview/$',
                           AggregateSurveyDataJSONView.as_view(),
                           name='aggregate-survey-data-json-view'),
                       url(r'^activequestionnairespecificationview/$',
                           ActiveQuestionnaireSpecificationView.as_view(),
                           name='active-questionnaire-specification-view'),
                       url(r'^clustersperfirstadminlevelsjsonview/$',
                           ClustersPerFirstAdminLevelJSONView.as_view(),
                           name='clusters-per-first-admin-level-json-view'),
                       url(r'^firstadminleveljsonview/$',
                           FirstAdminLevelJSONView.as_view(),
                           name='first-admin-levels-json-view'),
                       url(r'^firstadminlevelswithreserveclustersjsonview/$',
                           FirstAdminLevelsReserveClustersJSONView.as_view(),
                           name='first-admin-levels-with-reserve-clusters-json-view'),
                       url(r'^clustersjsonview/$',
                           ClustersJSONView.as_view(),
                           name='clusters-json-view'),
                       )
