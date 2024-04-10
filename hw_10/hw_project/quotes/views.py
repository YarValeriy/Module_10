# from .utils import get_mongodb
from django.core.paginator import Paginator
from .models import Quote
from django.shortcuts import render, get_object_or_404, redirect
from .models import Author
from .forms import AuthorForm, QuoteForm
from .models import Tag



# def main(request, page = 1):
#     db = get_mongodb()
#     quotes = db.quotes.find()
#     per_page = 10
#     paginator = Paginator(list(quotes), per_page)
#     quotes_on_page = paginator.page(page)
#     return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

def main(request, page=1):
    quotes = Quote.objects.all()

    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)

    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or back to the main page
            return redirect('quotes:root')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})



def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Save quote and associate tags
            quote = form.save(commit=False)
            quote.save()
            for tag_name in form.cleaned_data['tags']:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                quote.tags.add(tag)

            return redirect('quotes:root')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})
