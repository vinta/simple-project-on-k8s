# coding: utf-8
import click

import simple_api


app = simple_api.create_app()
celery = app.celery


@app.cli.command()
@click.argument('name')
def hello(name):
    print(f'Hello {name}')
