from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Avg, Min
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView

from core.forms import EveryDayReportForm, EveryWeekReportForm
from core.models import EveryWeekReport, Page, Review
from tasks.models import Task, Plank
from users.forms import User


def active_check(user):
    return user.active


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['page'] = Page.objects.get(slug='about')
        context['reviews'] = Review.objects.all()
        return context


class AboutPage(DetailView):
    template_name = 'core/about.html'
    model = Page

    def get_object(self, queryset=None):
        return Page.objects.get(slug='about')


class EveryDayReportView(UserPassesTestMixin, TemplateView):
    template_name = 'core/everydayreport.html'
    form_class = EveryDayReportForm()
    success_url = '/'

    def test_func(self):
        if self.request.user.profile and self.request.user.profile.active:
            return True
        else:
            return False

    def handle_no_permission(self):
        return redirect('core:home')

    def get_context_data(self, **kwargs):
        context = super(EveryDayReportView,self).get_context_data(**kwargs)
        context['form'] = EveryDayReportForm
        return context

    def post(self, request):
        form = EveryDayReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('core:success')

        context = {'form': form}
        return render(request, self.template_name, context)


class EveryWeekReportView(UserPassesTestMixin, TemplateView):
    template_name = 'core/everyweekreport.html'
    form_class = EveryWeekReportForm()
    success_url = '/'

    def test_func(self):
        if self.request.user.profile and self.request.user.profile.active:
            return True
        else:
            return False

    def handle_no_permission(self):
        return redirect('core:home')

    def get_context_data(self, **kwargs):
        context = super(EveryWeekReportView,self).get_context_data(**kwargs)
        context['form'] = EveryWeekReportForm
        return context

    def post(self, request):
        form = EveryWeekReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('core:success')

        context = {'form': form}
        return render(request, self.template_name, context)


class Results(UserPassesTestMixin, TemplateView):
    template_name = 'core/results.html'

    def test_func(self):
        if self.request.user.profile and self.request.user.profile.active:
            return True
        else:
            return False

    def handle_no_permission(self):
        return redirect('core:home')

    def get_context_data(self, **kwargs):
        context = super(Results, self).get_context_data(**kwargs)
        user = User.objects.get(username=self.request.user)
        everyweekreports = EveryWeekReport.objects.filter(user=user)
        context['weight_average'] = everyweekreports.aggregate(average=Avg('weight'))
        context['weight_min'] = everyweekreports.aggregate(min=Min('weight'))
        context['report_list'] = everyweekreports
        if everyweekreports.count() > 1:
            context['report_previous'] = everyweekreports.order_by('-id')[1]
        context['report_last'] = everyweekreports.last()
        context['you_today_result_weight'] =  everyweekreports.first().weight - everyweekreports.order_by('-id')[1].weight
        context['you_today_result_neck'] = everyweekreports.first().neck - everyweekreports.order_by('-id')[1].neck
        context['you_today_result_waist'] = everyweekreports.first().waist - everyweekreports.order_by('-id')[1].waist
        context['you_today_result_hips'] = everyweekreports.first().hips - everyweekreports.order_by('-id')[1].hips
        return context


class AdminReview(UserPassesTestMixin, TemplateView):
    template_name = 'core/adminreview.html'

    def test_func(self):
        if self.request.user.profile and self.request.user.profile.active:
            return True
        else:
            return False

    def handle_no_permission(self):
        return redirect('core:home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(profile=self.request.user.profile).last()
        context['planks'] = Plank.objects.filter(profile__user=self.request.user)
        return context


class Success(TemplateView):
    template_name = 'core/success.html'


