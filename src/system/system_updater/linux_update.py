from system.system_interaction import __interact_with_bash

SUPPORTED_DISTROS = {
            "debian": update_debian_linux,
            "ubuntu": update_debian_linux,
            "arch": update_arch_linux,
            "manjaro": update_arch_linux
        }

def update_linux(distro):
    if SUPPORTED_DISTROS.get(distro, None) is not None:
        result_update = SUPPORTED_DISTROS.get(distro, None)()
    else:
        raise Exception("Distro is not supported")


def update_debian_linux():
    update_debian = __interact_with_bash(args=["mkdir", "apt_log", "&&", "apt", "update", "&>", "apt_log/update_debian_based"])
    upgrade_debian = __interact_with_bash(args=["apt", "upgrade", "-y", "&>", "apt_log/upgrade_debian_based"])

def update_arch_linux():
    update_arch = __interact_with_bash(args=["mkdir", "yay_log", "&&", "yay", "-Syyu", "&>", "yay_log/update_arch_based"])

