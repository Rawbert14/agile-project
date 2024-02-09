from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReportForm, ProblemReportedForm, ReportSelectLineForm, ReportResultForm
from .models import Report, ProblemReported
from areas.models import ProductionLine
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def main_report_summary(request):
    try:
        day = request.session.get('day', None)
        prod_id = request.session.get('production_line', None)
        #print(day)

        production_line = ProductionLine.objects.get(id=prod_id)
        execution = Report.objects.get_by_line_and_day(day, prod_id).aggregate_execution()['execution__sum']
        plan = Report.objects.get_by_line_and_day(day, prod_id).aggregate_plan()['plan__sum']   
        problems = ProblemReported.objects.get_problems_by_day_and_line(day, production_line)
        #execution_agg = Report.objects.aggregate_execution()['execution__sum']
        #print(execution_agg)
        
        
    except:
        return redirect('reports:select-view')
    context = {
        'execution': execution,
        'plan': plan,
        'problems_reported': problems,
        'day': day,
        'line': production_line,
        
    }
    
    del request.session['day']
    del request.session['production_line']
    
    
    return render(request, 'reports/summary.html', context)

    
    
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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the production lines
        context['production_lines'] = ProductionLine.objects.all().prefetch_related('products')
        return context
 
        
        
class SelectView(FormView):
    template_name = 'reports/select.html'
    form_class = ReportResultForm
    success_url = reverse_lazy('reports:summary-view')
    
    def form_valid(self, form):
        self.request.session['day'] = self.request.POST.get('day', None)
        self.request.session['production_line'] = self.request.POST.get('production_line', None)

        #print(self.request.session['day'])
        return super(SelectView, self).form_valid(form)
        
    
    


class ReportUpdateView(LoginRequiredMixin, UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/update.html'
    
    def get_success_url(self):
        return reverse_lazy('reports:summary-view')
    
    



def delete_view(request, *args, **kwargs):
    r_id = kwargs.get("pk")
    obj = Report.objects.get(id=r_id)
    obj.delete()
    return redirect(request.META.get('HTTP_REFERER')) #redirect to current path/view


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
    

