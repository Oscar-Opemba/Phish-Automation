from .config import CONFIG

class SimulationError(Exception):
    pass

class Simulator:
    def run(self):
        if CONFIG.allow_network_io:
            raise SimulationError("Network I/O is disabled by design")
        return {
            "opens": 42,
            "clicks": 3,
            "reported": 12,
        }
