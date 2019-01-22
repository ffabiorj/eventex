# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com python 3.7
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:ffabiorj/eventex.git eventex
cd eventex
python3 -m venv .venv
sourch .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

# Como fazer o deploy

1. Crie um instância no heroku
2. Envie as configurações para o heroku
3. Define uma SECRET_KEY segura para instância.
4. Defina  DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku

```
heroku create minhainstancia
heroku config:push
heroku config:set SECRETY=`python contrib/secret_ge.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```
