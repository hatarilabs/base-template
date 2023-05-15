from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm
from django.shortcuts import render
from mf6.home.models import Project, SuscriptionRecords
from django.forms import formset_factory


class Index(LoginRequiredMixin,View):
    template_name = 'home/index.html'
    model = Project
    def get(self,request,*args, **kwargs):
        user = self.request.user
        projects = self.model.objects.filter(user=user)

        ctx ={'projectlist':projects}

        try:
            suscription = SuscriptionRecords.objects.filter(user = user).order_by('id').latest('id')
            if not suscription:
                pass
            else:
                projects = Project.objects.filter(user = user)
                if len(projects) >= suscription.category.n_projects:
                    ctx['create_project'] = False
                else:
                     ctx['create_project'] = True

        except SuscriptionRecords.DoesNotExist:
            pass

        return render(request,self.template_name,ctx)

    def post(self,request,*args, **kwargs):
        project_token = request.POST['project_token']
        self.model.objects.get(token = project_token).delete()
        return HttpResponseRedirect(reverse_lazy('mf6-home'))

class AddProject(LoginRequiredMixin,View):
    model = Project
    template_name = 'home/project-add.html'
    form_class = ProjectForm

    def get(self, request, *args, **kwargs):
        user = self.request.user
        form = self.form_class(filtered = user)
        ctx = {'form':form}

        return render(request,self.template_name,ctx)

    def post(self, request, *args, **kwargs):
        user=self.request.user

        form = self.form_class(user,request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = self.request.user
            obj.save()

            return HttpResponseRedirect(reverse_lazy('mf6-home'))
        else:
            ctx = {'form':form}
            return render(request,self.template_name,ctx)
