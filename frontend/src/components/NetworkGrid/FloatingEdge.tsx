import { useCallback } from 'react';
import { getBezierPath, useStore } from 'react-flow-renderer';

import { getEdgeParams } from './utils';

interface IFloatingEdge {
    id: string, source: string, target: string, markerEnd?: string, style?: any
}

function FloatingEdge(props: IFloatingEdge) {
    const sourceNode = useStore(useCallback((store) => store.nodeInternals.get(props.source), [props.source]));
    const targetNode = useStore(useCallback((store) => store.nodeInternals.get(props.target), [props.target]));

    if (!sourceNode || !targetNode) {
        return null;
    }

    const { sx, sy, tx, ty, sourcePos, targetPos } = getEdgeParams(sourceNode, targetNode);

    const d = getBezierPath({
        sourceX: sx,
        sourceY: sy,
        sourcePosition: sourcePos,
        targetPosition: targetPos,
        targetX: tx,
        targetY: ty,
    });

    return (
        <g className="react-flow__connection">
            <path id={props.id} className="react-flow__edge-path" d={d} markerEnd={props.markerEnd} style={props.style} />
        </g>
    );
}

export default FloatingEdge;
