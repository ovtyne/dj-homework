from django.conf import settings
from django.core.cache import cache

from hw.models import Product


def get_cached_subjects_for_student(product_pk):
    if settings.CACHE_ENABLED:
        key = f'users_list_{object.pk}'
        users_list = cache.get(key)
        if users_list is None:
            users_list = Product.objects.filter(product__pk=product_pk)
            cache.set(key, users_list)
    else:
        subject_list = Product.objects.filter(product__pk=product_pk)

    return users_list
