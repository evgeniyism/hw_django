from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.filter(product=pk)

    form = ReviewForm

    context = {
        'form': form,
        'product': product,
        'reviews': reviews
    }

    if request.method == 'POST' and form.is_valid:

        new_review = ReviewForm(request.POST)
        if pk not in request.session['reviewed'] or not request.session['reviewed']:
            Review.objects.create(product=product, text=new_review.data['text'])
            if not request.session['reviewed']:
                request.session.update({'reviewed': [pk, ]})
            else:
                request.session['reviewed'].append(pk)
        else:
            raise ValidationError

    return render(request, template, context)
