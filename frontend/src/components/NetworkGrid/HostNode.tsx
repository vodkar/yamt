import { Node, NodeProps } from "reaflow";
import { Host } from "../../api/Host";
import InterfacePort from "./InterfacePort";

interface IHostNodeProps extends Partial<NodeProps> {
    onHostClick: (host: Host) => void;
}

function HostNode(props: IHostNodeProps) {
    return (
        <Node dragType="node" {...props}
            onClick={(_event, data) => props.onHostClick({ ...data.data })}
            port={<InterfacePort parentNodeHeight={props.height} parentNodeWidth={props.width} />}
        >
        </Node>
    )
}

export default HostNode