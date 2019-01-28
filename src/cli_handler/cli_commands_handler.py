from system.system_prober import linux_system_prober

class CliCommandsHandler(object):
    """
        Handler to retrieve commands and return them to console
    """

    def __init__(self):
        self.available_commands = {
                    "kernel": linux_system_prober.get_kernel_version,
                    "distro": linux_system_prober.get_system_distro,
                    "cpu": {
                            "temperature": linux_system_prober.get_system_temperature
                        },
                    "nvidia": {
                            "temperature": linux_system_prober.get_nvidia_smi
                        }
                }

    def print_command(self, first_arg, second_arg=None):
        """
            :first_arg type: str
        """
        result = self.available_commands.get(first_arg, None)
        if isinstance(result, dict):
            if second_arg is not None:
                result = result.get(second_arg, None)
        return result()


