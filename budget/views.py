from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView

from .models import Project


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
