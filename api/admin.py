from django.contrib import admin

from .models import Transaction, User, CoinAddress

# Register your models here.
admin.site.register(User)
admin.site.register(CoinAddress)
admin.site.register(Transaction)
