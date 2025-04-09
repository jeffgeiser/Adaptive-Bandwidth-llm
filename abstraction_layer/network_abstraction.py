class NetworkAbstractionLayer:
    def __init__(self, sdn_manager):
        self.sdn = sdn_manager

    def get_telemetry(self):
        raw = self.sdn.get_telemetry()
        # Normalize to standard format
        return {
            "latency_ms": raw["latency_ms"],
            "jitter_ms": raw["jitter_ms"],
            "packet_loss_percent": raw["packet_loss_percent"]
        }

    def adjust_bandwidth(self, action):
        # Map generic actions to SDN-specific commands
        if action == "increase_throughput":
            self.sdn.adjust_bandwidth("increase_throughput", "20%")
        elif action == "set_priority":
            self.sdn.adjust_bandwidth("set_priority_queue", "high")
        # Blockchain stub
    def fetch_consensus_decision(self):
        # Placeholder for Claim 8; returns dummy data for now
        return {"bandwidth": "default"}

if __name__ == "__main__":
    from sdn_control.sdn_manager import SDNManager
    sdn = SDNManager()
    nal = NetworkAbstractionLayer(sdn)
    print("Normalized Telemetry:", nal.get_telemetry())
    nal.adjust_bandwidth("increase_throughput")
