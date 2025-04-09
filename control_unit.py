import requests
import time
from abstraction_layer.network_abstraction import NetworkAbstractionLayer
from sdn_control.sdn_manager import SDNManager

class ControlUnit:
    def __init__(self):
        self.nal = NetworkAbstractionLayer(SDNManager())
        self.inference_endpoint = "http://localhost:5000/infer"

    def monitor_and_adjust(self):
        while True:
            # Get LLM metrics
            llm_response = requests.post(self.inference_endpoint).json()
            metrics = llm_response["metrics"]
            latency = metrics["query_latency_ms"]

            # Get network telemetry
            telemetry = self.nal.get_telemetry()

            # Simple rule-based adjustment (replace with RL later)
            if latency > 200 or telemetry["latency_ms"] > 200:
                print(f"High latency detected: LLM={latency}ms, Network={telemetry['latency_ms']}ms")
                self.nal.adjust_bandwidth("increase_throughput")
                self.nal.adjust_bandwidth("set_priority")
            time.sleep(5)  # Poll every 5s

if __name__ == "__main__":
    control = ControlUnit()
    control.monitor_and_adjust()
