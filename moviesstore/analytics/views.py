from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.db.models import Sum, Count

# Create your views here.
@staff_member_required
def top_purchaser(request):
    users = (User.objects.annotate(movies_purchased=Sum('order__item__quantity'))
             .filter(movies_purchased__gt=0)
             .order_by('-movies_purchased')
    )

    top_users = []
    if users:
        top_count = users[0].movies_purchased
        top_users = [u for u in users if u.movies_purchased == top_count]

    template_data = {}
    template_data['title'] = 'Top Purchaser'
    template_data['top_users'] = top_users

    return render(request, 'analytics/top_purchaser.html', 
                  {'template_data': template_data})


@staff_member_required
def top_commenter(request):
    users = (
        User.objects
        .annotate(comments_posted=Count('review'))
        .filter(comments_posted__gt=0)
        .order_by('-comments_posted')
    )

    top_users = []
    if users:
        top_count = users[0].comments_posted
        top_users = [u for u in users if u.comments_posted == top_count]

    template_data = {}
    template_data['title'] = 'Top Commenter'
    template_data['top_users'] = top_users

    return render(request, 'analytics/top_commenter.html',
                  {'template_data': template_data})

@staff_member_required
def top_commenter(request):
    users = (User.objects.annotate(comments_posted=Count("review"))
             .filter(comments_posted__gt=0)
             .order_by("-comments_posted")
    )

    top_users = []
    if users:
        top_count = users[0].comments_posted
        top_users = [u for u in users if u.comments_posted == top_count]

    template_data = {}
    template_data["title"] = "Top Commenter"
    template_data["top_users"] = top_users

    return render(request, "analytics/top_commenter.html",
                  {"template_data": template_data})
