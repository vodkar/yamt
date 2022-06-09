import { height } from "@mui/system";
import React, { useEffect, useState } from "react";
import { Canvas, NodeData, CanvasProps } from "reaflow";
import { fetchHosts, Host } from "../../api/Host";
import { fetchTopology, ITopology } from "../../api/Topology";
import HostNode from "./HostNode";

interface INetworkGridProps extends Partial<CanvasProps> {
  onHostClick: (host: Host | null) => void;
}



function NetworkGrid(props: INetworkGridProps) {
  const [hosts, setHosts] = useState<Host[]>([]);
  const [topology, setTopology] = useState<ITopology | null>(null);

  useEffect(() => {
    fetchHosts(setHosts);
    fetchTopology(setTopology);
  }, [])

  return (
    <Canvas height={window.innerHeight} nodes={hosts.map((host: Host) => {
      return {
        id: host.id,
        text: host.name == null ? host.name : `MACs: ${host.cards.map((card) => card.mac).join("\n")}`,
        data: host,
        ports: host.cards.flatMap((card) => card.interfaces.map((inter) => { return { id: inter.id, height: 10, width: 10, side: "SOUTH" } }))
      }
    })}
      node={<HostNode onHostClick={props.onHostClick} />} />
  );
}

export default NetworkGrid