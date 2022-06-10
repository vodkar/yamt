import React, { useEffect, useState } from "react";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { Host, updateHost } from "../../api/Host";
import { Button, Divider } from "@mui/material";

interface IHostInfoPaneProps {
    host?: Host | null
}

function HostInfoPane(props: IHostInfoPaneProps) {
    const [name, setName] = useState<string>(props.host ? props.host.name : "")

    useEffect(() => {
        setName(props.host ? props.host.name : "");
        console.log(name)
    }, [])

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
                    label="Название устройства"
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

                <Box
                    component="form"
                    sx={{
                        '& .MuiTextField-root': { m: 1, width: '25ch' },
                    }}
                    noValidate
                    autoComplete="off"
                >
                    <Divider style={{ margin: "20px" }} />
                    <p style={{ margin: "10px" }}>Для получения данных по SSH введите логин и пароль</p>
                    <div>
                        <TextField
                            required
                            id="outlined-required"
                            label="Логин"
                        />
                        <TextField
                            required
                            id="outlined-disabled"
                            type="password"
                            autoComplete="current-password"
                            label="Пароль"
                        />
                        <div>
                            <Button style={{ margin: "10px" }} variant="outlined">Сохранить</Button>
                        </div>
                    </div>
                </Box>
            </Box>
        </>
    )
}

export default HostInfoPane