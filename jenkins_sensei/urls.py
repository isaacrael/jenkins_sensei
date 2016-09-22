from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'jenkins_sensei.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^account/', include('registration.backends.default.urls')),
    url(r'^$', 'jenkins_sensei_quiz.views.index', name='index'),
#    url(r'^results/', 'jenkins_sensei_quiz.views.results', name='results'),
#    url(r'^account_administration/', 'jenkins_sensei_quiz.views.account_administration', name='account_administration'),
    url(r'^quiz_selection/', 'jenkins_sensei_quiz.views.quiz_selection', name='quiz_selection'),
#    url(r'^quiz_selection/', include('jenkins_sensei_quiz.urls', namespace="jenkins_sensei_quiz")),
    url(r'^quiz/', include('jenkins_sensei_quiz.urls', namespace="jenkins_sensei_quiz")),
    url(r'^quiz/', 'jenkins_sensei_quiz.views.git_quiz', name='git_quiz'),
    url(r'^resources/', 'jenkins_sensei_quiz.views.resources', name='resources'),
    url(r'^ch1/', 'jenkins_sensei_quiz.views.ch1', name='ch1'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^admin/', include(admin.site.urls)),
]
