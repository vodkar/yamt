import React, { useState } from "react";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { Host, updateHost } from "../../api/Host";

interface IHostInfoPaneProps {
    host?: Host | null
}

function HostInfoPane(props: IHostInfoPaneProps) {
    const [name, setName] = useState<string>(props.host ? props.host.name : "")

    if (props.host == null || props.host == undefined) {
        return null
    }

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setName(event.target.value);
    };

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
                <TextField
                    key="Sample dev name"
                    label="Device name"
                    variant="outlined"
                    value={name}
                    onChange={handleChange}
                    onBlur={(event) => {
                        props.host && updateHost(props.host.id, { name: event.currentTarget.value })
                    }}
                />
                {props.host.cards.map((card) => {
                    return card.interfaces.map(
                        (inter) => {
                            return (<TextField key={inter.id} label="IP" variant="outlined" InputProps={{
                                readOnly: true,
                            }} value={inter.ip} />)
                        }
                    )
                })}
            </Box>
        </>
    )
}

export default HostInfoPane