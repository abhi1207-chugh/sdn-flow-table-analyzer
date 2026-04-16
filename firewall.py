from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_PacketIn(event):
    packet = event.parsed
    ip_packet = packet.find('ipv4')

    if ip_packet:
        src = str(ip_packet.srcip)
        dst = str(ip_packet.dstip)

        # BLOCK h1 -> h3
        if src == "10.0.0.1" and dst == "10.0.0.3":
            log.info("BLOCKED: %s -> %s", src, dst)
            return  # drop packet

    # Allow all others
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
