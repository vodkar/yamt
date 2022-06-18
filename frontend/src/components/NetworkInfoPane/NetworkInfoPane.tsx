import AddIcon from '@mui/icons-material/Add';
import DeleteIcon from '@mui/icons-material/Delete';
import HubIcon from '@mui/icons-material/Hub';
import LensIcon from '@mui/icons-material/Lens';
import { Divider, TextField } from "@mui/material";
import IconButton from '@mui/material/IconButton';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ListSubheader from '@mui/material/ListSubheader';
import { useEffect, useState } from "react";
import { getNetworks, putNetworks } from "../../api/Network";
import INetworkInfoProps from "./NetworkInfoProps";


function NetworkInfoPane(props: INetworkInfoProps) {
    const [networks, setNetworks] = useState<string[]>([])
    const [newNetwork, setNetwork] = useState<string>("")

    useEffect(() => {
        getNetworks(setNetworks);
    }, [])

    const removeNetwork = (network: string) => {
        const _networks = networks.filter((val) => val != network)
        console.log(_networks);
        putNetworks(_networks, () => { setNetworks(_networks) });
    }

    const addNetwork = () => {
        const _networks = networks.concat(newNetwork);
        putNetworks(_networks, () => { setNetworks(_networks) });
    }


    const handleNewNetworkChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setNetwork(event.target.value);
    };

    return (
        <>
            <List disablePadding
                subheader={
                    <ListSubheader component="div" id="nested-list-subheader">
                        Устройства и сеть
                    </ListSubheader>
                }>
                {networks.map((network, index) => {
                    return (
                        <><ListItem disablePadding >
                            <ListItemButton key={network}>
                                <ListItemIcon style={{ minWidth: "30px" }} >
                                    <HubIcon />
                                </ListItemIcon>
                                <ListItemText primary={network} />
                                <IconButton id={network} onClick={(event) => {
                                    removeNetwork(event.currentTarget.id);
                                }} edge="end" aria-label="delete">
                                    <DeleteIcon color="error" />
                                </IconButton>
                            </ListItemButton>
                        </ListItem>

                            <List component="div" disablePadding>
                                <ListItemButton sx={{ pl: 6 }}>
                                    <ListItemIcon style={{ minWidth: "30px" }} >
                                        <LensIcon sx={{ fontSize: 15 }} style={{ color: "#086CA2" }} />
                                    </ListItemIcon>
                                    <ListItemText primary="192.168.1.11" />
                                </ListItemButton>
                            </List>
                        </>
                    )
                }
                )}
                <Divider />
                <ListItemButton key="add-network" >
                    <TextField
                        id="outlined-basic"
                        value={newNetwork}
                        onChange={handleNewNetworkChange}
                        label="Добавить новую сеть"
                        variant="outlined"
                    />
                    <IconButton id="add-network" onClick={(event) => {
                        addNetwork();
                    }} edge="end" aria-label="delete">
                        <AddIcon />
                    </IconButton>
                </ListItemButton>
            </List>
        </>
    )
}

export default NetworkInfoPane
