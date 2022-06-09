import React from "react";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { Host } from "../../api/Host";

interface IHostInfoPaneProps {
    host?: Host | null
}

function HostInfoPane(props: IHostInfoPaneProps) {
    if (props.host == null || props.host == undefined) {
        return null
    }
    return (
        <>
            <Box
                component="form"
                sx={{
                    '& .MuiTextField-root': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
            >
                <TextField label="Device name" variant="outlined" value={props.host.name} />
                <TextField label="IP" variant="outlined" InputProps={{
                    readOnly: true,
                }} value={props.host.ip} />
            </Box>
        </>
    )
}

export default HostInfoPane