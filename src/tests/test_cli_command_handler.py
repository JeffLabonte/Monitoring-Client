import subprocess
from cli_handler.cli_commands_handler import CliCommandsHandler
from system.system_interaction import __interact_with_bash

# from nose import with_setup


def test_kernel_command():
    cli = CliCommandsHandler()
    kernel = cli.print_command(first_arg="kernel")
    assert kernel is not None
    assert kernel == __interact_with_bash(args=['uname', '-r'])

def test_system_distro():
    cli = CliCommandsHandler()
    distro = cli.print_command(first_arg="distro")
    assert distro is not None
    assert distro == __interact_with_bash(args=['cat', '/etc/os-release'])

def test_cpu_temperature():
    cli = CliCommandsHandler()
    temperature_cpu = cli.print_command(first_arg="cpu", second_arg="temperature")
    assert temperature_cpu is not None

def test_nvidia_temperature():
    cli = CliCommandsHandler()
    temperature_nvidia = cli.print_command(first_arg="nvidia", second_arg="temperature")
    assert temperature_nvidia is not None

def test_print_non_existant_first():
    cli = CliCommandsHandler()
    empty_result = cli.print_command(first_arg="I don;t")
    assert empty_result is None
