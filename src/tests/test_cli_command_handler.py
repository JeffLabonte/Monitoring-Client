import subprocess
from cli_handler.cli_commands_handler import CliCommandsHandler
from system.system_interaction import __interact_with_bash

# from nose import with_setup


def test_kernel_command():
    cli = CliCommandsHandler()
    kernel = cli.print_command(first_arg="kernel")
    assert kernel is not None
    assert kernel == __interact_with_bash(args=['uname', '-r'])
