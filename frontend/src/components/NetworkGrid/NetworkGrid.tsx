import React, { useEffect, useState } from "react";
import { Canvas, NodeData, CanvasProps } from "reaflow";
import { fetchHosts, Host } from "../../api/Host";
import HostNode from "./HostNode";

interface INetworkGridProps extends Partial<CanvasProps> {
  onHostClick: (host: Host | null) => void;
}



function NetworkGrid(props: INetworkGridProps) {
  const [hosts, setHosts] = useState<Host[]>([]);

  useEffect(() => {
    fetchHosts(setHosts)
  }, [])

  return (
    <Canvas height={window.innerHeight} nodes={hosts.map((host: Host) => {
      return { id: host.ip, text: host.ip, data: host }
    })}
      node={<HostNode onHostClick={props.onHostClick} />} />
  );
}

export default NetworkGrid