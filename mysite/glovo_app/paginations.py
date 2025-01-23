from rest_framework.pagination import PageNumberPagination


class ProductNumberPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


class ComboNumberPagination(PageNumberPagination):
    page_size = 1
    gage_size_query_param = 'page_size'
    max_page_size = 100