import { useEffect, useState } from "react";

import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton'
import ListItemText from '@mui/material/ListItemText';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';
import IconButton from '@mui/material/IconButton';
import { getNetworks, putNetworks } from "../../api/Network";
import { TextField } from "@mui/material";

function NetworkButtonsList() {
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
        <List component="div" disablePadding>
            {networks.map((network, index) => {
                return (
                    <ListItemButton key={network}>
                        <ListItemText primary={network} />
                        <IconButton id={network} onClick={(event) => {
                            removeNetwork(event.currentTarget.id);
                        }} edge="end" aria-label="delete">
                            <DeleteIcon />
                        </IconButton>
                    </ListItemButton>
                )
            }
            )}
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
    )
}

export default NetworkButtonsList
