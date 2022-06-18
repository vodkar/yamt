import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import * as React from 'react';
import YamtIcon from './YamtIcon';


export const YamtHeader = () => (
    <Box sx={{ flexGrow: 1, }}>
        <AppBar enableColorOnDark={true} position="sticky">
            <Toolbar>
                <YamtIcon />
            </Toolbar>
        </AppBar>
    </Box>
)
