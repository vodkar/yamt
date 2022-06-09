import { Node } from "reaflow";
import { NodeProps, NodeData } from "reaflow";
import { Host } from "../../api/Host";
import InterfacePort from "./InterfacePort";

interface IHostNodeProps extends Partial<NodeProps> {
    onHostClick: (host: Host) => void;
}

function HostNode(props: IHostNodeProps) {
    return (
        <Node {...props}
            onClick={(_event, data) => props.onHostClick({ ...data.data })}
            port={<InterfacePort />}
        />
    )
}

export default HostNode