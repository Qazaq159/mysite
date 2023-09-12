import threading
import random
from polls.models import Publication, Article


def populate():

    for i in range(100):
        Article.objects.create(headline=f'headline{i}')
        Publication.objects.create(title=f'title{i}')

    print('Created objects')


class MyThread(threading.Thread):

    def run(self):
        for q in range(1, 100):
            for i in range(1, 5):
                pub = Publication.objects.all()[random.randint(1, 2)]
                for j in range(1, 5):
                    article = Article.objects.all()[random.randint(1, 15)]
                    pub.article_set.add(article)
                    # ap, c = article.publications.through.objects.get_or_create(article=article, publication=pub)
            print(self.name)


# class MyThread2(threading.Thread):
#
#     def run(self) -> None:
#         for q in range(1, 100):
#             for i in range(1, 5):
#                 pub = Publication.objects.all()[random.randint(1, 2)]
#                 for j in range(1, 5):
#                     article = Article.objects.all()[random.randint(1, 15)]
#                     ap, c = ArticlePublication.objects.get_or_create(article=article, publication=pub)
#             print('Get or create', self.name)




Article.objects.all().delete()
Publication.objects.all().delete()

populate()
t1 = MyThread()
t2 = MyThread()
t3 = MyThread()


t1.start()
t2.start()
t3.start()
