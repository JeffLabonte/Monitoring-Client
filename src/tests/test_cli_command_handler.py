import subprocess

from cli_handler import CliCommandsHandler
cli = None
def setup_cli_command():
    cli = CliCommandsHandler()

def teardown():
    pass

@with_setup(setup_cli_command, teardown)
def test_kernel_command():
    kernel = cli.print_command(first_arg="kernel")
    assert kernel == subprocess.check_output(['uname', '-r'])
