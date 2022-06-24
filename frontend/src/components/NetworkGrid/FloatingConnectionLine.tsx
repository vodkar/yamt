import { getBezierPath } from 'react-flow-renderer';

import { getEdgeParams } from './utils';

export interface IFloatingConnectionLine {
    targetX: number, targetY: number, sourcePosition?: any, targetPosition?: any, sourceNode?: any
}

export function FloatingConnectionLine(props: IFloatingConnectionLine) {
    if (!props.sourceNode) {
        return <></>;
    }

    const targetNode = {
        id: 'connection-target',
        width: 1, height: 1, position: { x: props.targetX, y: props.targetY },
    };

    const { sx, sy } = getEdgeParams(props.sourceNode, targetNode);
    const d = getBezierPath({
        sourceX: sx,
        sourceY: sy,
        sourcePosition: props.sourcePosition,
        targetPosition: props.targetPosition,
        targetX: props.targetX,
        targetY: props.targetY,
    });

    return (
        <g>
            <path fill="none" stroke="#222" strokeWidth={1.5} className="animated" d={d} />
            <circle cx={props.targetX} cy={props.targetY} fill="#fff" r={3} stroke="#222" strokeWidth={1.5} />
        </g>
    );
}
