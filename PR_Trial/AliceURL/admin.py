from django.contrib import admin
from AliceURL.models import ShortURL
from django.db.models import Count


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):

    def get_queryset(self, request):                            # Дополнение сета подсчетом связей по вн. ключу
        qs = super(ShortURLAdmin, self).get_queryset(request)
        return qs.annotate(visits_count=Count('urlpass'))

    def visits_count(self, inst):
        return inst.visits_count

    list_filter = ['created_by']
    list_display = ['created_by', 'code', 'target_link', 'visits_count']
