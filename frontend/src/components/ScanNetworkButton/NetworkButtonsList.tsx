import { useState } from "react";

import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton'
import ListItemText from '@mui/material/ListItemText';
import DeleteIcon from '@mui/icons-material/Delete';
import IconButton from '@mui/material/IconButton';
import { getNetworks } from "../../api/Network";

function NetworkButtonsList() {
    const [networks, setNetworks] = useState<string[]>(getNetworks())

    const removeNetwork = (network: string) => {
        const netIdx = networks.indexOf(network);
        const _networks = networks.splice(netIdx, 1);
        setNetworks(_networks)
    }

    return (
        <List component="div" disablePadding>
            {networks.map((network, index) => {
                return (
                    <ListItemButton key={network} sx={{ pl: 4 }}>
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
        </List>
    )
}

export default NetworkButtonsList
