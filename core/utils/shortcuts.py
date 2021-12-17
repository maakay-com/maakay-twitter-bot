import requests
import os

from ..models.wallets import ThenewbostonWallet
from ..models.users import User
from django.conf import settings


def get_or_create_tnbc_wallet(user):

    obj, created = ThenewbostonWallet.objects.get_or_create(user=user)

    return obj


def get_or_create_user(user_id):

    obj, created = User.objects.get_or_create(user_id=str(user_id))

    return obj


def convert_to_decimal(amount):

    amount = amount / settings.TNBC_MULTIPLICATION_FACTOR
    rounded_amount = round(amount, 4)
    return rounded_amount


def convert_to_int(amount):

    amount = int(amount / settings.TNBC_MULTIPLICATION_FACTOR)
    return amount


def get_wallet_balance(account_number):

    try:
        bank_config = requests.get(f"http://{os.environ['BANK_IP']}/config?format=json").json()
        wallet_balance = requests.get(f"{bank_config['primary_validator']['protocol']}://{bank_config['primary_validator']['ip_address']}/accounts/{account_number}/balance?format=json").json()['balance']
        return wallet_balance

    except Exception:

        return 0
