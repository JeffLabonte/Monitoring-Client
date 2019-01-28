import argparse
from system.system_prober import linux_system_prober
from system.system_updater import linux_update
from cli_handler.cli_commands_handler import CliCommandsHandler

import websocket

parser = argparse.ArgumentParser()
parser.add_argument("--print", "-p", dest="command", help="Print to console, one of the supported commands")
args = parser.parse_args()

if __name__ == "__main__":
    if args.command is not None:
        print("I am going to print: {}".format(args.command))
        pass
    else:
        print("Run a server")
