from re import search

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.db.models import Q, Count # Q - объекты позволяют кратко записывать условия
from pygments.lexers.webassembly import keywords

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 3: # Условие что значение будет цифра или меньше(равно) 3
        return Products.objects.filter(id=int(query)) # фильтр по id

    vector = SearchVector('name', 'description')
    query = SearchQuery(query)
    result = (Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank"))

    result = result.annotate(
        headline=SearchHeadline("name", query, start_sel='<span style="background-color: yellow;">',
                                stop_sel="</span>",))
    result = result.annotate(
        bodyline=SearchHeadline("description", query, start_sel='<span style="background-color: yellow;">',
                                stop_sel="</span>", ))
    return result

    # keywords = [word for word in query.split() if len(word) > 2]
    #
    # q_objects = Q()
    #
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token) # Или равно, поиск по описанию
    #     q_objects |= Q(name__icontains=token) # Или равно, поиск по названию
    #
    # return Products.objects.filter(q_objects)