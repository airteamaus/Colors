from django.core import management

def run():
    management.call_command('interesting', interactive=False)
    management.call_command('process_flickr', interactive=False)
