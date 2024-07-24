from django.forms import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import item
from django.template import loader
from .forms import Itemform
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# def index(request):

#     item_list=item.objects.all()
#     context={
#         'item_list':item_list,
#     }
#     return render(request,'food/index.html',context)



class IndexClassView(ListView):
     model=item;
     template_name='food/index.html'
     context_object_name='item_list'
   



def bkl(request):
    return HttpResponse("<h1>teri maa ki choot</h1>")

# def detail(request,item_id):
#         Item=item.objects.get(pk=item_id)
#         context={
#         'item':Item,
#          }
#         return render(request,'food/detail.html',context)



class FoodDetail(DetailView):
     model=item;
     template_name='food/detail.html'
     



# def create_item(request):
#      form = Itemform(request.POST or None)
     
#      if form.is_valid():
#           form.save()
#           return redirect('food:index')
     
#      return render(request,'food/item-form.html',{'form':form})



class CreateItem(CreateView):
     model=item
     fields=['item_name','item_desc','item_price','item_image']
     template_name='food/item-form.html'

     def form_valid(self, form):
          form.instance.user_name=self.request.user

          return super().form_valid(form)






def update_item(request,id):
     
     Item=item.objects.get(id=id)
     form=Itemform(request.POST or None,instance=Item)

     if form.is_valid():
          form.save()
          return redirect('food:index')
     
     return render(request,'food/item-form.html',{'form':form,'item':Item})

   
def delete_item(request,id):
     Item=item.objects.get(id=id)

     if request.method=='POST':
          Item.delete()
          return redirect('food:index')
     
     return render(request,'food/item-delete.html',{'item':Item})
