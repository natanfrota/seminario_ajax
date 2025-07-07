import requests
from django.core.management.base import BaseCommand
from usuario.models import Usuario 

class Command(BaseCommand):
    help = 'Importa usuários da API Random User e salva no banco'

    def handle(self, *args, **kwargs):
        url = 'https://randomuser.me/api/?results=500&nat=br'
        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR('Erro ao acessar API'))
            return

        dados = response.json()
        usuarios = dados['results']

        for u in usuarios:
            obj, criado = Usuario.objects.get_or_create(
                email=u['email'],
                defaults={
                    'first_name': u['name']['first'],
                    'last_name': u['name']['last'],
                    'city': u['location']['city'],
                    'thumbnail_url': u['picture']['thumbnail'],
                }
            )
            if criado:
                self.stdout.write(self.style.SUCCESS(f'Criado: {obj}'))
            else:
                self.stdout.write(f'Já existe: {obj}')
