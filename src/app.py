import argparse
from system.system_prober import linux_system_prober
from system.system_updater import linux_update
from cli_handler.cli_commands_handler import CliCommandsHandler

import websocket

def convert_list_to_dict(arguments):
    idx = 0
    dictionnary = {}
    for a in arguments:
        dictionnary[str(idx)] = a
        idx = idx + 1
    return dictionnary

parser = argparse.ArgumentParser()
prober = parser.add_argument_group("Print system information")
prober.add_argument("--print", "-p", dest="command", action="store_true", help="Print to console, one of the supported commands")
prober.add_argument("--args", "-a", dest="arguments", action="append", help="Arguments that you want to print")
server = parser.add_argument_group("Run server for long term monitoring")
server.add_argument("--host", dest="server_information", action="append", help="The hostname of the server hosting Home Monitoring")
server.add_argument("--port", "-pt", dest="server_information", required=False, default=8080, action="append", help="The port of the server host Home Monitoring")
server.add_argument("--http", dest="server_information", default="https", action="append", help="Not Recommended to use HTTP")
args = parser.parse_args()

if __name__ == "__main__":
    if args.command is not None:
        cli_arguments = convert_list_to_dict(arguments=args.arguments)
        if len(cli_arguments) > 2:
            raise SystemError("This tools can take up to 2 args maximum")
        CLI = CliCommandsHandler()
        result = CLI.print_command(first_arg=cli_arguments.get("0", None), second_arg=cli_arguments.get("1", None))
        print(result)
    else:
        print("Run a server")
