from django.core.cache import cache
from django.db.models import F


class ViewCountMixin:
    """Work only with retrieve views"""

    view_count_field = "view_count"

    def _count_view(self):
        fingerprint = self.request.headers.get("fingerprint")
        instance = self.get_object()
        model_name = instance.__class__.__name__
        uniq_key = f"unique_prefix:view_count:{model_name}:{instance.pk}:{fingerprint}"
        data = cache.get(uniq_key)
        if not data:
            setattr(instance, self.view_count_field, F(self.view_count_field) + 1)
            instance.save(update_fields=[self.view_count_field])
            cache.set(uniq_key, True, 60 * 60 * 2)  # 2 hours

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        self._count_view()
        return response
