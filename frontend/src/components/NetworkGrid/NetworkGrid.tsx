import { useEffect, useState } from "react";
import ReactFlow, { addEdge, Controls, MarkerType, MiniMap, useEdgesState, useNodesState } from 'react-flow-renderer';
import { CanvasProps } from "reaflow";
import { getHosts, Host } from "../../api/Host";
import { fetchTopology, ITopology } from "../../api/Topology";
import { getHostByInterfaceId } from "./computations";
import { FloatingConnectionLine } from "./FloatingConnectionLine";
import FloatingEdge from "./FloatingEdge";

interface INetworkGridProps extends Partial<CanvasProps> {
  onHostClick: (host: Host | null) => void;
}

const edgeTypes = {
  floating: FloatingEdge,
};

function NetworkGrid(props: INetworkGridProps) {
  const [hosts, setHosts] = useState<Host[]>([]);
  const [topology, setTopology] = useState<ITopology | null>(null);
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const onConnect = (params: any) =>
    setEdges((eds) =>
      addEdge({ ...params, type: 'floating', markerEnd: { type: MarkerType.Arrow } }, eds)
    );
  function setHostsSetNodes(hosts: Host[]) {
    setHosts(hosts);
    setNodes(hosts.map((host: Host) => {
      return {
        id: host.id,
        data: { label: host.name ? host.name : `MACs: ${host.cards.map((card) => card.mac).join("\n")}`, host: host },
        position: { x: 250, y: 25 },
        // type: 'input',
        // ports: host.cards.flatMap((card) => card.interfaces.map(
        //   (inter) => {
        //     return {
        //       id: inter.id, height: 10, width: 10, side: "SOUTH", ip: inter.ip
        //     }
        //   }
        // ))
      }
    }));
  }

  function setTopologySetEdges(newTopology: ITopology) {
    setTopology(newTopology)
    setEdges(
      newTopology ? newTopology.interface_connections.map((inter) => {

        return {
          id: `${inter.origin.id}-${inter.destination.id}`,
          source: getHostByInterfaceId(hosts, inter.origin.id)?.id || "",
          target: getHostByInterfaceId(hosts, inter.destination.id)?.id || "",
          fromPort: inter.origin.id,
          toPort: inter.destination.id,
          type: 'floating',
        }
      }) : []
    );
  }

  useEffect(() => {
    getHosts(setHostsSetNodes);
    fetchTopology(setTopologySetEdges);
  }, [])

  return (
    <ReactFlow

      // height={window.innerHeight} 
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      fitView
      onNodeClick={(_, node) => props.onHostClick(node.data.host)}
      onConnect={onConnect}
      edgeTypes={edgeTypes}
      connectionLineComponent={FloatingConnectionLine}
    // node={<HostNode onHostClick={props.onHostClick} />} 
    >

      <MiniMap />
      <Controls />
    </ReactFlow>
  );
}

export default NetworkGrid