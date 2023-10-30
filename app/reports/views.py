from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReportForm, ProblemReportedForm, ReportSelectLineForm
from .models import Report
from areas.models import ProductionLine
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, FormView
# Create your views here.

class HomeView(FormView):
    template_name = "reports/home.html"
    form_class = ReportSelectLineForm
    
    def get_form_kwargs(self):
        kwargs = super(HomeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def post(self, *args, **kwargs):
        prod_line = self.request.POST.get('prod_line')
        return redirect('reports:report-view', production_line=prod_line)
        
    


class ReportUpdateView(UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/update.html'
    
    def get_success_url(self):
        return self.request.path
    
    


@login_required
def delete_view(request, *args, **kwargs):
    r_id = kwargs.get("pk")
    obj = Report.objects.get(id=r_id)
    obj.delete()
    return redirect(request.META.get('HTTP_REFERER')) #redirect to current path/view

@login_required
def report_view(request, production_line):
    form = ReportForm(request.POST or None, production_line=production_line)
    pform = ProblemReportedForm(request.POST or None)
    queryset = Report.objects.filter(production_line__name = production_line)
    #print(queryset)
    line = get_object_or_404(ProductionLine, name = production_line)
    
    if 'submitbtn1'in request.POST:
        
        r_id = request.POST.get("report_id")
        print(r_id)
    
    
        if pform.is_valid():
            report = Report.objects.get(id=r_id)
            print("data here")
            obj = pform.save(commit=False)
            obj.user = request.user
            obj.report = report
            obj.save()
            #form = ReportForm()
            #pform = ProblemReportedForm()
            return redirect(request.META.get('HTTP_REFERER'))
            
    elif 'submitbtn2'in request.POST:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.production_line = line
            obj.save()
            #form = ReportForm()
            #pform = ProblemReportedForm()
            return redirect(request.META.get('HTTP_REFERER'))
       
    
       
    context = {
        'form': form,
        'pform': pform,
        'object_list': queryset,
    }
    
    return render(request, 'reports/report.html', context)
    