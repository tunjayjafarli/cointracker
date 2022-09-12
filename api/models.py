from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.views.decorators.debug import sensitive_variables

class UserManager(BaseUserManager):

    @sensitive_variables('password')
    def create_user(self, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    @sensitive_variables('password')
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(
        max_length=255, unique=True,
        verbose_name=('Email'),
        help_text=("The email is used as the username when signing in."),
        error_messages={
            'unique': ("A user with this email already exists.")
        })

    name = models.CharField(
        max_length=255, blank=True,
        verbose_name=('Name'),
        help_text=("Full name"))

    is_staff = models.BooleanField(
        default=False,
        verbose_name=("Has Admin Access?"),
        help_text=("True if the user has access to the admin page."))

    country_of_residence = models.CharField(
        max_length=255, blank=True,
        verbose_name=("Country of residence"))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def get_name(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return "/users/{}/".format(self.id)

    def __str__(self):
        return str(self.name) or "(Anonymous Member: {})".format(self.email)

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")
        ordering = ('email',)


class CoinAddress(models.Model):

    address = models.CharField(
        max_length=35, blank=False, unique=True,
        verbose_name=('Address'))
    
    address_hash = models.CharField(
        max_length=160, blank=True, null=True, 
        verbose_name=('Address Hash'))

    coin_name = models.CharField(
        max_length=255, blank=True,
        verbose_name=('Coin Name'),
        help_text=("Name of the coin or blockchain"))

    owner = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)

    total_transactions = models.IntegerField(verbose_name="Total number of transcations")
    total_received = models.IntegerField()
    total_sent = models.IntegerField()
    final_balance = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Coin Address")
        verbose_name_plural = ("Coin Addresses")


class Transaction(models.Model):
    """
    This model not used for data storage/persistence as of yet.
    """

    transaction_hash = models.CharField(
        max_length=255, blank=False, unique=True,
        verbose_name=('Tx hash'))

    fee = models.IntegerField()
    status = models.CharField(max_length=255, blank=False)
    timestamp = models.IntegerField()
    block_index = models.IntegerField()
    
    address = models.ForeignKey(
        CoinAddress, on_delete=models.CASCADE,
        blank=False, null=False)

    class Meta:
        verbose_name = ("Transaction")
        verbose_name_plural = ("Transactions")
