import { Button, Divider, FormControlLabel, Switch } from "@mui/material";
import { useState } from "react";
import List from '@mui/material/List';
import Collapse from '@mui/material/Collapse';
import ListItemButton from '@mui/material/ListItemButton'
import ListItemText from '@mui/material/ListItemText';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import NetworkButtonsList from "./NetworkButtonsList";

function ManageNetworksHeader() {
    const [open, setOpen] = useState(false);

    const [loading, setLoading] = useState(true);

    function handleToogleMonitoring() {
        setLoading(true);
    }

    const handleClick = () => {
        setOpen(!open);
    };

    return (
        <List >
            <ListItemButton onClick={handleClick}>
                <ListItemText primary="Изменить список сетей" />
                {open ? <ExpandLess /> : <ExpandMore />}
                <Divider style={{ margin: "10px" }} orientation="vertical" flexItem />
                <FormControlLabel
                    sx={{
                        display: 'block',
                    }}
                    control={
                        <Switch
                            checked={loading}
                            onChange={() => setLoading(!loading)}
                            name="loading"
                            color="primary"
                        />
                    }
                    label="Мониторинг сети"
                />
            </ListItemButton>
            <Collapse in={open} timeout="auto" unmountOnExit>
                <NetworkButtonsList />
            </Collapse>
        </List>
    )
}

export default ManageNetworksHeader