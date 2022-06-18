
import { createTheme, CssBaseline, PaletteMode } from '@mui/material';
import { ThemeProvider } from '@mui/material/styles';
import React from "react";
import BaseLayout from "../layouts/BaseLayout/BaseLayout";

const getDesignTokens = (mode: PaletteMode) => ({
    typography: {
        fontFamily: 'Consolas'
    },
    palette: {
        mode,
        ...(mode === 'light' ? {} : {
            primary: {
                main: '#2962ff',
            },
            secondary: {
                main: '#ff3d00',
            },
            error: {
                main: '#b71c1c',
            },
            background: {
                default: '#091631',
                paper: '#0d1843',
            },
            divider: '#2962ff',
        }
        )
    },
});


function MainPage() {
    const [mode, setMode] = React.useState<PaletteMode>('dark');
    const colorMode = React.useMemo(
        () => ({
            // The dark mode switch would invoke this method
            toggleColorMode: () => {
                setMode((prevMode: PaletteMode) =>
                    prevMode === 'light' ? 'dark' : 'light',
                );
            },
        }),
        [],
    );

    const theme = React.useMemo(() => createTheme(getDesignTokens(mode)), [mode]);

    return (
        <ThemeProvider theme={theme}>
            <CssBaseline enableColorScheme />
            <BaseLayout />
        </ThemeProvider>
    )
}
export default MainPage