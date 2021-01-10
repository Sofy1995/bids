from django.shortcuts import render, redirect
from django.utils.decorators import classonlymethod

from .models import Bid
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

def index(request):
    num_bids=Bid.objects.all().count()
    num_bids_a=Bid.objects.all().filter(status='a').count()
    num_bids_w=Bid.objects.all().filter(status='w').count()
    num_bids_f=Bid.objects.all().filter(status='f').count()

    print('Nu cho')
    if request.method == 'POST':
        print('eto vashe rabotaet??')
        if '_do_assept' in request.POST:
            print('RAZRESSHENOO')
        elif '_do_cancel' in request.POST:
            print(' nea Zapretiti')
        elif '_push_on_me' in request.POST:
            print('Najali na menya!!')
    print('ny epta, ti gde blya')
    return render(
        request,
        'index.html',
        context={'num_bids': num_bids, 'num_bids_a': num_bids_a, 'num_bids_w': num_bids_w, 'num_bids_f': num_bids_f},
    )


class BidListView(generic.ListView):
    model = Bid
    paginate_by = 10
    # def get_queryset(self):
    #     if 'change' in self.request.GET:
    #         message = 'You searched for:'
    #     else:
    #         message = 'You submitted an empty form.'
    #     return HttpResponse(message)


class BidDetailView(generic.DetailView):
    model = Bid

class MakingBidsByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Bid
    template_name ='system/bids_for_user.html'
    paginate_by = 5
    # login_url = '/login/'
    #     # redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Bid.objects.all().filter(maker=self.request.user)
        # return Bid.objects.all()


class BidCreate(LoginRequiredMixin, CreateView):
    model = Bid
    fields = ['text', 'type_bid', 'location', 'telephone_num', 'bider', 'maker', 'helper']


    def post(self, request):
        if request.POST['location'] == 'Location':
            super(BidCreate, self).post(request)
            location_max = request.POST['location']
        # login_password = request.POST['password1']
        # created_user = authenticate(username=login_username, password=login_password)

        # login(request, created_user)
        # return redirect('/')

            print(location_max)
            print('Napishi norm location, pidr')
            #raise ValidationError({'status': 'Нельзя завершить заявку без результата.'})

            return redirect('/system/bid/create/')
        else:

            #def form_valid(self, form, request):
            #    if request.POST['location'] == 'Location':
            #        return self.render_to_response(self.get_context_data(form=form))
            #    else:
            #        super(CreateView, self).form_valid(form)

            super(CreateView, self).post(request)
            #return reverse()
            return redirect('/system/bids/')

 #           path('bid/<int:pk>/update/', views.BidUpdate.as_view(), name='bid-update')


 #   def form_valid(self, form, request):
 #       if request.POST['location'] == 'Location':
 #           return self.render_to_response(self.get_context_data(form=form))
 #       else:
 #           super(CreateView, self).form_valid(form)


    print('Nu create, i cho')
#    print('Nu cho')
#    if CreateView.post:  # == 'POST':
#        print('eto vashe rabotaet??')
#        if '_do_assept' in CreateView.get_template_names(): #  request.POST:
#            print('RAZRESSHENOO')
#        elif '_do_cancel' in CreateView.get_template_names(): #  request.POST:
#            print(' nea Zapretiti')
#        elif '_push_on_me' in CreateView.get_template_names(): #  request.POST:
#            print('Najali na menya!!')
#    print('ny epta, ti gde blya')

    permission_required = 'system.can_mark_returned'


class BidUpdate(LoginRequiredMixin, UpdateView):
    model = Bid
    print('Nu update, i cho')
    fields = ['text', 'type_bid', 'location', 'telephone_num', 'bider', 'maker', 'helper', 'comment', 'result', 'status']
    permission_required = 'system.can_mark_returned'


class BidDelete(LoginRequiredMixin, DeleteView):
    model = Bid
    print('nu delete, i cho')
    success_url = reverse_lazy('bids')
    permission_required = 'system.can_mark_returned'
