import logging
import sys
import click

from zcan.main import main, listen, write, write_ventilation_level

from zcan.util import get_logger

LOGGER = get_logger()


@click.group(help="zcan Zehnder ComfoAir CAN bus adapter")
def cli():
    pass


@cli.command(help="run")
@click.option('--debug', '-d', is_flag=True, default=False, envvar='ZCAN_DEBUG', help="Debug output")
def run(debug):
    if debug:
        LOGGER.setLevel(logging.DEBUG)
    else:
        LOGGER.setLevel(logging.INFO)

    try:

        main()
    except Exception as e:
        LOGGER.error("Failed with unexpected error")
        LOGGER.exception(e)
        sys.exit(1)


@cli.command(help="show messages")
@click.option('--debug', '-d', is_flag=True, default=False, envvar='ZCAN_DEBUG', help="Debug output")
def show(debug):
    if debug:
        LOGGER.setLevel(logging.DEBUG)
    else:
        LOGGER.setLevel(logging.INFO)

    try:

        listen()
    except Exception as e:
        LOGGER.error("Failed with unexpected error")
        LOGGER.exception(e)
        sys.exit(1)


@cli.command(help="write")
@click.option('--debug', '-d', is_flag=True, default=False, envvar='ZCAN_DEBUG', help="Debug output")
def test(debug):
    if debug:
        LOGGER.setLevel(logging.DEBUG)
    else:
        LOGGER.setLevel(logging.INFO)

    try:
        payload = click.prompt("Payload")
        write(payload)
    except Exception as e:
        LOGGER.error("Failed with unexpected error")
        LOGGER.exception(e)
        sys.exit(1)

@cli.command(help="write")
@click.option('--debug', '-d', is_flag=True, default=False, envvar='ZCAN_DEBUG', help="Debug output")
def set_ventilation_level(debug):
    if debug:
        LOGGER.setLevel(logging.DEBUG)
    else:
        LOGGER.setLevel(logging.INFO)

    try:
        iterator = click.prompt("Iterator")
        write_ventilation_level(iterator)
    except Exception as e:
        LOGGER.error("Failed with unexpected error")
        LOGGER.exception(e)
        sys.exit(1)

if __name__ == "__main__":
    cli()