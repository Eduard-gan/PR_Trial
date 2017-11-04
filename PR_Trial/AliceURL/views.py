from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from AliceURL.forms import ShortenForm
import random
import string
import datetime
from AliceURL.models import ShortURL, URLPass
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


def get_code():
    return ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(6)])


@login_required
def shorten(request):
    if request.method == 'GET':
        form = ShortenForm()
    elif request.method == 'POST':
        form = ShortenForm(request.POST)
        if form.is_valid():     # Если данные переданные в форме были валидными, дополняем и записываем в модель
            model_instance = form.save(commit=False)
            model_instance.code = get_code()
            model_instance.created_by = request.user
            model_instance.save()
            return render(request, template_name='AliceURL/URLCreated.html', # Возврат успеха
                          context={'target_link': model_instance.target_link,
                                   'code': model_instance.code
                                   }
                          )
    return render(request, template_name='AliceURL/CommitURL.html', context={'form':form}) # Возврат формы ввода


def process_url(request, **kwargs):
    code = kwargs.get('code')
    try: # Если удастся найти код в базе - работам дальше, иначе отбой.
        short_url_instance = ShortURL.objects.get(code=code)
    except ObjectDoesNotExist:
        return render(request,
                      template_name='AliceURL/Error_ShortLinkNotFound.html',
                      context={'code': code}
                      )
    visitor = request.META.get('REMOTE_ADDR')
    # Запрашиваем запись о переходе с этого IP по этому коду
    url_pass_instance = URLPass.objects.filter(visitor=visitor).filter(code=code)
    past_day = timezone.now() - datetime.timedelta(days=1)

    # Если запись есть, и она не старше суток - это не уникальный переход, ничего не пишем.
    if url_pass_instance.exists() and url_pass_instance.first().timestamp > past_day:
        pass
    # Иначе создаем запись о переходе.
    else:
        URLPass(visitor=visitor, code=short_url_instance).save()
    return HttpResponseRedirect(short_url_instance.target_link)
