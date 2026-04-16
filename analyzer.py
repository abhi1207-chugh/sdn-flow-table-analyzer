from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer

log = core.getLogger()
connections = []

def request_stats():
    for conn in connections:
        msg = of.ofp_stats_request(body=of.ofp_flow_stats_request())
        conn.send(msg)

def _handle_ConnectionUp(event):
    log.info("Switch connected: %s", event.dpid)
    connections.append(event.connection)

def _handle_FlowStatsReceived(event):
    log.info("===== FLOW TABLE for Switch %s =====", event.connection.dpid)

    if not event.stats:
        log.info("No flow entries")
        return

    for flow in event.stats:
        log.info("Match: %s", flow.match)
        log.info("Packets: %s Bytes: %s", flow.packet_count, flow.byte_count)

        if flow.packet_count > 0:
            log.info("Status: ACTIVE")
        else:
            log.info("Status: UNUSED")

        log.info("----------------------")

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("FlowStatsReceived", _handle_FlowStatsReceived)

    # 🔥 Request flow stats every 3 seconds
    Timer(3, request_stats, recurring=True)
