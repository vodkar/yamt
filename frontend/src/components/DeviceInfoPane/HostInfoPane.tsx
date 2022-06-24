import { Box, Button, Divider, FormControl, InputLabel, Modal, OutlinedInput, Paper, Typography } from "@mui/material";
import TextField from '@mui/material/TextField';
import React, { useEffect, useState } from "react";
import { Host, updateHost } from "../../api/Host";
import { LinearProgressWithLabel } from "./LinearProgress";

interface IHostInfoPaneProps {
    host?: Host | null
}

const modalStyle = {
    position: 'absolute' as 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};

function HostInfoPane(props: IHostInfoPaneProps) {
    const [name, setName] = useState<string>(props.host ? props.host.name : "")
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

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
                <TextField
                    key="Mac dev"
                    label="MAC-адрес"
                    variant="outlined"
                    value={props.host.cards[0].mac}
                    InputProps={{
                        readOnly: true,
                    }}
                    size="small"
                />
                <Divider style={{ marginLeft: -paperPadding, marginRight: -paperPadding }} />
                <p style={{ margin: "10px" }}>Данные для доступа по SSH</p>
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
            <Paper>
                <Typography variant="h6" m={1}>SSH мониторинг</Typography>
                <Box sx={{
                    m: 1,
                    '& .MuiTextField-root': { m: 1 }
                }} >
                    <Typography>Версия ОС: Linux - Ubuntu 20.04.2 LTS</Typography>
                </Box>
                <Box sx={{
                    m: 1,
                    '& .MuiTextField-root': { m: 1 }
                }} >
                    <Typography>ЦПУ</Typography>
                    <LinearProgressWithLabel value={1} color="info" />
                </Box>
                <Box sx={{
                    m: 1,
                    '& .MuiTextField-root': { m: 1 }
                }} >
                    <Typography>ОЗУ</Typography>
                    <LinearProgressWithLabel value={58} color='warning' />
                </Box>
                <Divider style={{ marginLeft: -paperPadding, marginRight: -paperPadding }} />
                <Box sx={{
                    m: 1,
                    '& .MuiTextField-root': { m: 1 }
                }} >
                    <Typography variant="h6">Поиск уязвимостей</Typography>
                    <FormControl fullWidth sx={{ m: 1, paddingRight: 1 }}>
                        <InputLabel htmlFor="outlined-adornment-amount">CPE</InputLabel>
                        <OutlinedInput
                            id="outlined-adornment-amount"
                            value='cpe:2.3:o:canonical:ubuntu_linux:20.04.2:*:*:*:lts:*:*:*'
                            label="CPE"
                        />
                        <Button style={{ marginTop: "8px" }} variant="outlined">Поиск уязвимостей в NVD</Button>
                    </FormControl>
                    <Modal
                        open={false}
                        aria-labelledby="modal-modal-title"
                        aria-describedby="modal-modal-description"
                    >
                        <Box sx={modalStyle}>
                            <Typography variant="h6">Всего уязвимостей: 2</Typography>
                            <a id="modal-modal-title" href="https://kb.cert.org/vuls/id/605641/">
                                CVE-2019-9516
                            </a>
                            <br></br>
                            <a id="modal-modal-description" href="https://kb.cert.org/vuls/id/605641/">
                                CVE-2019-9513
                            </a>
                        </Box>
                    </Modal>
                </Box>

            </Paper>
        </Box>
    )
}

export default HostInfoPane