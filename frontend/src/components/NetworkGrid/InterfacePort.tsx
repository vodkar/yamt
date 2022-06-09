import { TextField } from "@mui/material";
import { color } from "@mui/system";
import { useState } from "react";
import { Port } from "reaflow";
import { PortProps } from "reaflow";
import { IPInterface } from "../../api/Host";

interface IInterfacePortProps extends Partial<PortProps> {

}

function InterfacePort(props: IInterfacePortProps) {
    const [selected, setSelected] = useState(false)
    return (
        <>
            <Port {...props}
                onEnter={() => {
                    console.log("Entered");
                    setSelected(true);
                }}
                onClick={(event) => {
                    console.log("Clicked");
                    event.currentTarget.blur()
                }}
            />
        </>
    )
}

export default InterfacePort