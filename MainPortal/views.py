from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from . import models


class WebsiteProductListView(ListView):
    model = models.Website
    template_name = 'home_page.html'
    context_object_name = 'websites'

    def get_context_data(self, **kwargs):
        context = super(WebsiteProductListView, self).get_context_data(**kwargs)
        context['products'] = models.Product.objects.all()
        return context


class AddWebsiteView(CreateView):
    model = models.Website
    fields = ('name', 'url', 'account_email', 'account_password')
    template_name = 'add_website.html'
    success_url = reverse_lazy('home')


class DeleteWebsiteView(DeleteView):
    model = models.Website
    template_name = 'delete_website.html'
    success_url = reverse_lazy('home')


class WebsiteDetailView(DetailView):
    model = models.Website
    template_name = 'website_detail.html'
    context_object_name = 'website'

    def get_context_data(self, **kwargs):
        context = super(WebsiteDetailView, self).get_context_data(**kwargs)
        context['products'] = models.Product.objects.filter(website=self.kwargs['pk'])
        return context


class ProductCreateView(CreateView):
    model = models.Product
    fields = (
        'website',
        'url',
        'name',
        'price',
        'size',
        'color',
    )
    template_name = 'product_create.html'
    context_object_name = 'product'
    success_url = reverse_lazy('home')


class ProductUpdateView(UpdateView):
    model = models.Product
    fields = (
        'url',
        'name',
        'price',
        'size',
        'color',
    )
    template_name = 'product_detail.html'
    context_object_name = 'product'
    success_url = reverse_lazy('website')

    def get_success_url(self):
        return reverse('website', kwargs={"pk": self.object.website.pk})


class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('website')

    def get_success_url(self):
        return reverse('website', kwargs={"pk": self.object.website.pk})


class SettingsDetailView(DetailView):
    model = models.Settings
    template_name = 'settings.html'
    context_object_name = 'settings'


class SettingsUpdateView(UpdateView):
    model = models.Settings
    fields = ('email', 'paypal_email', 'paypal_password',
              'address', 'checking_interval')
    template_name = 'settings_update.html'
    context_object_name = 'settings'
    success_url = reverse_lazy('home')
