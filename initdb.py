# coding:utf-8

from __future__ import unicode_literals
import random
from myfirstDjango.wsgi import *
from blog.models import *

author_name_list = ['Ltao','Ajoker','Lushan','YTXX']
article_title_list = ['Django教程','Git入门','Java从入门到放弃','Vue&Python快速构建web应用']


def createAuthors():
    for author_name in author_name_list:
        author,created = Author.objects.get_or_create(name = author_name)
        author.qq = ''.join( 
            str(random.choice(range(10))) for _ in range(9)   
        )
        author.addr = 'addr_%s' %(random.randrange(1,3))
        author.email = '%s@qq.com' %(author.addr)
        author.save()

def createArticleAndTag():
    #随机生成文章
    for article_title in article_title_list:
        tagname = article_title.split(' ',1)[0]
        tag,created = Tag.objects.get_or_create(name = tagname)

        random_author = random.choice(Author.objects.all())

        for i in range(1,21):
            title = '%s_%s' % (article_title,i)
            article,created = Article.objects.get_or_create(
                title = title,defaults = {
                    'author':random_author,
                    'content':'%s 正文' % title,
                    'score': random.randrange(70,101),
                }
            )
            article.tags.add(tag)


def main():
    createAuthors()
    createArticleAndTag()

if __name__ == '__main__':
    main()
    print('Done Success!')