import logging
import json
from websocket import WebSocket

from cli_handler.cli_commands_handler import CliCommandsHandler

class MonitoringWebSocket(WebSocket):
    cli_command_handler = CliCommandsHandler()

    def recv_frame(self):
        frame = super().recv_frame()
        json_frame = json.loads(frame)
        self.send(self.cli_command_handler.print_command(first_arg=json_frame["device"], second_arg=json_frame.get("command", None)))

