import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysites.settings")

import django
django.setup()

def main():
    from hearthstone.models import Post
    f = open('db.txt')
    for line in f:
        line = line.replace('<li>','').replace('</li>','')
        Post.objects.create(hero_id=7, ka_name=line, author='未知', contributor = 'renmu', con_time='2017-07-14 06:26:00', ka_time='2017-07-14 06:26:00')
        print(line)
    f.close()

main()