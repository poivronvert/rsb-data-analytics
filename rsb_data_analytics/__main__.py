import click


@click.group()
def cli():
    pass 


@click.command(help="Start Web Svc.")
@click.option(
    '-h',
    '--host',
    type=str,
    default='localhost',
    help="host IP",
    show_default=True
)
@click.option(
    '-p',
    '--port',
    type=int,
    default=21116,
    help="Service port",
    show_default=True
)
def run(host:str, port:int):
    import uvicorn
    try:
        uvicorn.run(app='rsb_data_analytics.app:app', host=host, port=port, reload=True)
    except Exception as e:
        print(e)

cli.add_command(run)
cli()