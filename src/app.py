import argparse
from system.system_prober import linux_system_prober
from system.system_updater import linux_update

import websocket

parser = argparse.ArgumentParser()
parser.add_argument("--print", "-p", help="Print to console, one of the supported commands")
parser.parse_args()

if __name__ == "__main__":
     pass
