import click


@click.group()
def cli():
    pass 


@click.command(help="Start Web Svc.")
def run():
    import uvicorn
    from rsb_data_analytics.app import app
    try:
        uvicorn.run(app='rsb_data_analytics.app:app', host='localhost', port=21116)
    except Exception as e:
        print(e)

cli.add_command(run)
cli()