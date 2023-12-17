def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

from .models import ViewCount
class ViewCountMixin:
    def get_object(self):
        # получаем объект из родительского класса
        obj = super().get_object()
        ip_address = get_client_ip(self.request)
        # если такой счетчик уже создан, выполнится get - получение
        # если его еще не было, выполнится create
        ViewCount.objects.get_or_create(article=obj, ip_address=ip_address)
        return obj