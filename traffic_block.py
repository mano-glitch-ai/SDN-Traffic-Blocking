from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

packet_count = {}
blocked = set()
THRESHOLD = 10

def _handle_PacketIn(event):
    packet = event.parsed
    ip_packet = packet.find('ipv4')

    if ip_packet:
        src = str(ip_packet.srcip)

        # count packets
        packet_count[src] = packet_count.get(src, 0) + 1
        log.info("Host %s count = %d", src, packet_count[src])

        # block once
        if src not in blocked and packet_count[src] > THRESHOLD:
            log.info("BLOCKING %s due to high traffic", src)
            blocked.add(src)
            return

        # already blocked
        if src in blocked:
            return

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
