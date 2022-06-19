import AddIcon from '@mui/icons-material/Add';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import DeleteIcon from '@mui/icons-material/Delete';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { TreeView } from '@mui/lab';
import { Divider, Toolbar } from '@mui/material';
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
import { getNetworks, putNetworks } from "../../api/Network";
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

    const renderTree = (nodes: RenderTree) => (
        <NetworkTreeItem key={nodes.id} nodeId={nodes.id} label={nodes.name}>
            {Array.isArray(nodes.children)
                ? nodes.children.map((node) => renderTree(node))
                : null}
        </NetworkTreeItem>
    );

    return (
        <Box
            sx={{ m: 1 }}
        >
            <Paper>
                <Toolbar style={{ minHeight: 0, padding: 5 }}>
                    <Box >
                        <IconButton style={iconStyle} edge="end" >
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
                        networks.map(
                            (network) => (renderTree({ id: network, name: network, children: [{ id: Math.random().toString(), name: "192.168.1.1" }] }))
                        )
                    }
                </TreeView>
            </Paper>
        </Box>
    );

    // return (
    //     <>
    //         <List disablePadding
    //             subheader={
    //                 <ListSubheader component="div" id="nested-list-subheader">
    //                     Устройства и сеть
    //                 </ListSubheader>
    //             }>
    //             {networks.map((network, index) => {
    //                 return (
    //                     <><ListItem disablePadding >
    //                         <ListItemButton key={network}>
    //                             <ListItemIcon style={{ minWidth: "30px" }} >
    //                                 <HubIcon />
    //                             </ListItemIcon>
    //                             <ListItemText primary={network} />
    //                             <IconButton id={network} onClick={(event) => {
    //                                 removeNetwork(event.currentTarget.id);
    //                             }} edge="end" aria-label="delete">
    //                                 <DeleteIcon color="error" />
    //                             </IconButton>
    //                         </ListItemButton>
    //                     </ListItem>

    //                         <List component="div" disablePadding>
    //                             <ListItemButton sx={{ pl: 6 }}>
    //                                 <ListItemIcon style={{ minWidth: "30px" }} >
    //                                     <LensIcon sx={{ fontSize: 15 }} style={{ color: "#086CA2" }} />
    //                                 </ListItemIcon>
    //                                 <ListItemText primary="192.168.1.11" />
    //                             </ListItemButton>
    //                         </List>
    //                     </>
    //                 )
    //             }
    //             )}
    //             <Divider />
    //             <ListItemButton key="add-network" >
    //                 <TextField
    //                     id="outlined-basic"
    //                     value={newNetwork}
    //                     onChange={handleNewNetworkChange}
    //                     label="Добавить новую сеть"
    //                     variant="outlined"
    //                 />
    //                 <IconButton id="add-network" onClick={(event) => {
    //                     addNetwork();
    //                 }} edge="end" aria-label="delete">
    //                     <AddIcon />
    //                 </IconButton>
    //             </ListItemButton>
    //         </List>
    //     </>
    // )
}

export default NetworkInfoPane
