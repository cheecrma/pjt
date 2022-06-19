from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_safe, require_POST
from .models import Movierate, Rate
from django.core.paginator import Paginator
from .forms import RateForm

# Create your views here.
@require_safe
def index(request):
    movies = Movierate.objects.all()
    paginator = Paginator(movies, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': page_obj,
    }
    return render(request, 'rates/index.html', context)



@require_safe
def detail(request, movie_pk):
    movierate = get_object_or_404(Movierate, pk=movie_pk)
    rate_form = RateForm()
    rates = movierate.rates.all()[::-1]
    context = {
        'movierate': movierate,
        'rate_form': rate_form,
        'rates': rates,
    }
    return render(request, 'rates/detail.html', context)


@require_POST
def rate_create(request, movie_pk):
    if request.user.is_authenticated:
        movierate = get_object_or_404(Movierate, pk = movie_pk)
        rating = movierate.rates.filter(user=request.user).first()
        rate_form = RateForm(request.POST)

        if not rating:
            if rate_form.is_valid():
                rate = rate_form.save(commit=False)
                rate.movierate = movierate
                rate.user = request.user
                rate.save()
            return redirect('rates:detail', movie_pk)
        
        else:
            # 기존 한줄평 삭제
            if request.user == rating.user:
                rating.delete()
            # 새로운 한줄평 등록
                rate = rate_form.save(commit=False)
                rate.movierate = movierate
                rate.user = request.user
                rate.save()
            return redirect('rates:detail', movie_pk)

    return redirect('accounts:login')

@require_POST
def rate_delete(request, movie_pk, rate_pk):
    if request.user.is_authenticated:
        rate = get_object_or_404(Rate, pk=rate_pk)
        if request.user == rate.user:
            rate.delete()
        return redirect('rates:detail', movie_pk)
    return redirect('accounts:login')