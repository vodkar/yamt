import { Box, Button, Divider, Paper, Typography } from "@mui/material";
import TextField from '@mui/material/TextField';
import React, { useEffect, useState } from "react";
import { Host, updateHost } from "../../api/Host";

interface IHostInfoPaneProps {
    host?: Host | null
}

function HostInfoPane(props: IHostInfoPaneProps) {
    const [name, setName] = useState<string>(props.host ? props.host.name : "")

    useEffect(() => {
        setName(props.host ? props.host.name : "");
        console.log(name)
    }, [])

    if (props.host == null || props.host === undefined) {
        return null
    }


    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setName(event.target.value);
    };

    const paperPadding = 5;

    return (
        <Box sx={{
            m: 1,
            '& .MuiTextField-root': { m: 1, width: '20ch' }
        }} >
            <Paper style={{ padding: paperPadding }}>
                <Typography variant="h6" m={1}>Информация об устройстве</Typography>
                <TextField
                    key="Sample dev name"
                    label="Название устройства"
                    variant="outlined"
                    value={name}
                    size="small"
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
                            }} value={inter.ip}
                                size="small" />)
                        }
                    )
                })}
                <Divider style={{ marginLeft: -paperPadding, marginRight: -paperPadding }} />
                <p style={{ margin: "10px" }}>Для получения данных по SSH введите логин и пароль</p>
                <TextField
                    required
                    id="outlined-required"
                    label="Логин"
                    size="small"
                />
                <TextField
                    required
                    id="outlined-disabled"
                    type="password"
                    autoComplete="current-password"
                    label="Пароль"
                    size="small"
                />
                <Button style={{ margin: "8px" }} variant="outlined">Сохранить</Button>
            </Paper>
        </Box>
    )
}

export default HostInfoPane