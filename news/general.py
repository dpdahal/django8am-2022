from .models import Setting,Category
def data_pass(request):

    data = {
        'title': "Django 8 AM Project",
        "settingData": Setting.objects.first(),
        'menuCategory':Category.objects.all()
    }
    return data


