from django.views.generic import TemplateView
from .models import YangiliklarModel, FloraTypeModel, FloraModel, XodimModels, DockModel, ElektronTypeModels, \
    ElektronModels
from django.shortcuts import render
from django.core.paginator import Paginator


class HomeView(TemplateView):

    def get(self, request):
        yangiliklar = YangiliklarModel.objects.order_by('-data')
        paginator = Paginator(yangiliklar, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'yangiliklar': yangiliklar,
            'page_obj': page_obj
        }
        return render(request, 'index.html', context)

    def post(self, request):
        pass


class AboutView(TemplateView):

    def get(self, request):
        yangiliklar = YangiliklarModel.objects.order_by('-data')
        paginator = Paginator(yangiliklar, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'yangiliklar': yangiliklar,
            'page_obj': page_obj
        }
        return render(request, 'about.html', context)

    def post(self):
        pass


class BlogView(TemplateView):
    template_name = 'blog.html'

    def get(self, request):
        type = FloraTypeModel.objects.all()
        flora = FloraModel.objects.all()
        paginator = Paginator(flora, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'type': type,
            'flora': flora,
            'page_obj': page_obj
        }
        return render(request, 'blog.html', context)


class BlogSingleView(TemplateView):
    def get(self):
        type = FloraTypeModel.objects.all()
        plant = FloraModel.objects.all()

        context = {
            'type': type,
            'plant': plant,
        }

        return render(self, 'portfolio.html', context)


class ContactView(TemplateView):
    template_name = 'contact.html'


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'


class PortfolioDetailView(TemplateView):
    template_name = 'portfolio-details.html'


class PricingView(TemplateView):

    def get(self, request):
        dockmodel = DockModel.objects.all()
        context = {
            'dockmodel': dockmodel
        }
        return render(request, 'pricing.html', context)


class ServiceView(TemplateView):
    template_name = 'services.html'


class TeamView(TemplateView):

    def get(self, request):
        team = XodimModels.objects.all()
        context = {
            'team': team,
        }

        return render(request, 'team.html', context)


def detailview(request, pk):
    yangiliklar = YangiliklarModel.objects.get(id=pk)
    context = {
        'yangiliklar': yangiliklar
    }
    return render(request, 'news.html', context)


class ElektronTypeView(TemplateView):

    def get(self, request):
        elektron_type = ElektronTypeModels.objects.all()
        context = {
            'elektront': elektron_type
        }
        return render(request, 'pricing.html', context)

    def post(self, request):
        pass


class ElektronView(TemplateView):
    def get(self, request, pk):
        elekton_type = ElektronTypeModels.objects.get(id=pk)
        elektron = ElektronModels.objects.filter(type_id=pk)

        context = {
            'elektront': elekton_type,
            'elektron': elektron
        }

        return render(request, 'pricing-detail.html', context)
