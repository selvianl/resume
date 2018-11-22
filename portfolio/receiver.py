from django.dispatch import receiver
from portfolio.signals import saved

@receiver(saved)
def method_to_do_stuff(sender, **kwargs):
    sender = kwargs['user']
    table = kwargs['table'].__name__
    print(str(sender) + " saved at table of " + table +
          ". Attributes " + str(kwargs['header']) +
          " and " + str(kwargs['name']))

