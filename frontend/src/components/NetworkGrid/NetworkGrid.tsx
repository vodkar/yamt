import React, { useEffect, useState } from "react";
import { Canvas, CanvasProps } from "reaflow";
import { getHosts, Host } from "../../api/Host";
import { fetchTopology, ITopology } from "../../api/Topology";
import { getHostByInterfaceId } from "./computations";
import HostNode from "./HostNode";

interface INetworkGridProps extends Partial<CanvasProps> {
  onHostClick: (host: Host | null) => void;
}



function NetworkGrid(props: INetworkGridProps) {
  const [hosts, setHosts] = useState<Host[]>([]);
  const [topology, setTopology] = useState<ITopology | null>(null);

  useEffect(() => {
    getHosts(setHosts);
    fetchTopology(setTopology);
  }, [])

  return (
    <>
      <Canvas arrow={null} height={window.innerHeight} nodes={hosts.map((host: Host) => {
        return {
          id: host.id,
          text: host.name ? host.name : `MACs: ${host.cards.map((card) => card.mac).join("\n")}`,
          data: host,
          ports: host.cards.flatMap((card) => card.interfaces.map(
            (inter) => {
              return {
                id: inter.id, height: 10, width: 10, side: "SOUTH", ip: inter.ip
              }
            }
          ))
        }
      })}
        edges={
          topology?.interface_connections.map((inter) => {
            return {
              id: `${inter.origin.id}-${inter.destination.id}`,
              from: getHostByInterfaceId(hosts, inter.origin.id)?.id,
              to: getHostByInterfaceId(hosts, inter.destination.id)?.id,
              fromPort: inter.origin.id,
              toPort: inter.destination.id
            }
          })
        }
        node={<HostNode onHostClick={props.onHostClick} />} />
    </>
  );
}

export default NetworkGrid