from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.text import slugify
from django.views.generic import CreateView

from .models import Category, Project


# Create your views here.
def project_list(request):
    return render(request, 'budget/project-list.html')


def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    expanse_list = project.expenses.all()
    return render(request, 'budget/project-detail.html',
                  {'project': project,
                   'expense_list': expanse_list})


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'budget/add-project.html'
    fields = ('name', 'budget')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST['categoriesString'].split(',')
        for category in categories:
            Category.objects.create(
                project=Project.objects.get(id=self.object.id),
                name=category
            ).save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['name'])
