import re

from system.system_interaction import __interact_with_bash

def get_kernel_version():
    return __interact_with_bash(args=['uname', '-r'])

def get_system_distro():
    return __interact_with_bash(args=['cat', '/etc/os-release'])

def get_system_temperature():
    return __interact_with_bash(args=['sensors'])

def get_system_uptime():
    return __interact_with_bash(args=['uptime', '-p'])

def get_nvidia_smi():
    """
        :return tuple: (temperatue, cards)
    """
    nvidia = __interact_with_bash(args=['nvidia-smi'])
    temperatures = re.findall(r'\d+C', nvidia)
    cards = re.findall(r'Geforce GTX \d+', nvidia)
    return (temperatures, cards)
