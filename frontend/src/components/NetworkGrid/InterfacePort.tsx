import { Chip } from "@mui/material";
import { useState } from "react";
import { Port, PortChildProps, PortData } from "reaflow";
import { PortProps } from "reaflow";

interface IInterfacePortProps extends Partial<PortProps> {
    parentNodeHeight?: number
    parentNodeWidth?: number
}

interface IPInterfacePortData extends PortData {
    ip?: string
}

interface IPInterfaceChildProps extends PortChildProps {
    port: IPInterfacePortData
}

function InterfacePort(props: IInterfacePortProps) {
    const [selected, setSelected] = useState(false)

    return (
        <>
            <Port {...props}
                onEnter={() => {
                    setSelected(true);
                }}
                onClick={(event) => {
                    event.currentTarget.blur()
                }}
            >

                {(event: IPInterfaceChildProps) => {
                    if (selected) {
                        return (
                            <foreignObject height={props.parentNodeHeight! + 100} width={props.parentNodeWidth! + 100}>
                                <div style={{ position: "fixed", left: props.x! - 10, top: props.y! - 10 }}>
                                    <Chip style={{ backgroundColor: "White" }}
                                        onDelete={() => setSelected(false)}
                                        label={event.port.ip} variant="outlined" />
                                </div>
                            </foreignObject>)
                    }
                }
                }
            </Port>
        </>
    )
}

export default InterfacePort