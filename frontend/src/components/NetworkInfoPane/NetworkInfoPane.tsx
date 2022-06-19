import AddIcon from '@mui/icons-material/Add';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import DeleteIcon from '@mui/icons-material/Delete';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { TreeView } from '@mui/lab';
import { Divider, Menu, TextField, Toolbar } from '@mui/material';
// import HubIcon from '@mui/icons-material/Hub';
// import LensIcon from '@mui/icons-material/Lens';
import Box from '@mui/material/Box';
// import { Divider, TextField } from "@mui/material";
import IconButton from '@mui/material/IconButton';
import Paper from '@mui/material/Paper';
// import List from '@mui/material/List';
// import ListItem from '@mui/material/ListItem';
// import ListItemButton from '@mui/material/ListItemButton';
// import ListItemIcon from '@mui/material/ListItemIcon';
// import ListItemText from '@mui/material/ListItemText';
// import ListSubheader from '@mui/material/ListSubheader';
import { useEffect, useState } from "react";
import { addNetworks, getNetworks, NetworkWithHosts } from "../../api/Network";
import INetworkInfoProps from "./NetworkInfoProps";
import NetworkTreeItem from "./NetworkTreeItem";


interface RenderTree {
    id: string;
    name: string;
    children?: readonly RenderTree[];
}

const iconStyle = {
    marginRight: 0
}

function NetworkInfoPane(props: INetworkInfoProps) {
    const [networks, setNetworks] = useState<NetworkWithHosts>(new Map())
    const [newNetwork, setNetwork] = useState<string>("")
    const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
    const isMenuOpen = Boolean(anchorEl);

    useEffect(() => {
        getNetworks(setNetworks);
    }, [])

    const addNetwork = () => {
        const _networks = networks.set(newNetwork, []);
        addNetworks([newNetwork], () => { setNetworks(_networks) });
        handleMenuClose();
    }


    const handleNewNetworkChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setNetwork(event.target.value);
    };

    const renderTree = (nodes: RenderTree) => {
        console.log(nodes)
        return (<NetworkTreeItem key={nodes.id} nodeId={nodes.id} label={nodes.name}>
            {Array.isArray(nodes.children) && nodes.children.length > 0
                ? nodes.children.map((node) => renderTree(node))
                : [<NetworkTreeItem nodeId="not-exists" label="Нет хостов в сети" disabled />]}
        </NetworkTreeItem>)
    };

    const handleAddNetworkOpen = (event: React.MouseEvent<HTMLElement>) => {
        setAnchorEl(event.currentTarget);
    };

    const handleMenuClose = () => {
        setAnchorEl(null);
    };

    const renderAddNetwork = (
        <Menu
            anchorEl={anchorEl}
            open={isMenuOpen}
            onClose={handleMenuClose}>
            <TextField
                label="IPv4 адрес сети"
                variant="outlined"
                size="small"
                value={newNetwork}
                onChange={handleNewNetworkChange}
                style={{ marginLeft: 5, marginRight: 5 }}
                onKeyUp={(event) => event.key === 'Enter' && addNetwork()} />
        </Menu>
    )


    return (
        <Box
            sx={{ m: 1 }}
        >
            <Paper>
                <Toolbar style={{ minHeight: 0, padding: 5 }}>
                    <Box >
                        <IconButton style={iconStyle} edge="end" onClick={handleAddNetworkOpen}>
                            <AddIcon fontSize="small" />
                        </IconButton>
                        <IconButton style={iconStyle} edge="end" aria-label="delete">
                            <DeleteIcon color="warning" fontSize="small" />
                        </IconButton>
                    </Box>
                </Toolbar>
                <Divider />
                <TreeView
                    aria-label="rich object"
                    defaultCollapseIcon={<ExpandMoreIcon />}
                    defaultExpanded={['root']}
                    defaultExpandIcon={<ChevronRightIcon />}
                >
                    {
                        Array.from(networks,
                            ([network, hosts]) => (renderTree({
                                id: network, name: network,
                                children: hosts.map((host) => ({ id: host.id, name: host.ip }))
                            }))
                        )
                    }
                </TreeView>
            </Paper>
            {renderAddNetwork}
        </Box>
    );
}

export default NetworkInfoPane
