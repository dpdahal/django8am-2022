from .models import Setting
def data_pass(request):

    data = {
        'title': "Django 8 AM Project",
        "settingData": Setting.objects.first(),
    }
    return data


