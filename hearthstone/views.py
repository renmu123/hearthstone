from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    post_list_1 = Post.objects.filter(hero_id=1) # 猎人
    post_list_2 = Post.objects.filter(hero_id=2) # 萨满
    post_list_3 = Post.objects.filter(hero_id=3) # 术士
    post_list_4 = Post.objects.filter(hero_id=4) # 盗贼
    post_list_5 = Post.objects.filter(hero_id=5) # 骑士
    post_list_6 = Post.objects.filter(hero_id=6) # 法师
    post_list_7 = Post.objects.filter(hero_id=7) # 战士
    post_list_8 = Post.objects.filter(hero_id=8) # 德鲁伊
    post_list_9 = Post.objects.filter(hero_id=9) # 牧师
    return render(request, 'hearthstone/index.html', context={'post_list_1': post_list_1,
                                                                   'post_list_2': post_list_2,
                                                                   'post_list_3': post_list_3,
                                                                   'post_list_4': post_list_4,
                                                                   'post_list_5': post_list_5,
                                                                   'post_list_6': post_list_6,
                                                                   'post_list_7': post_list_7,
                                                                   'post_list_8': post_list_8,
                                                                   'post_list_9': post_list_9,
                                                                  })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'hearthstone/detail.html', context={'post': post})