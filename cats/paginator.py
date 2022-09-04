from rest_framework.pagination import PageNumberPagination


class CatsPaginator(PageNumberPagination):

    page_size = 20
