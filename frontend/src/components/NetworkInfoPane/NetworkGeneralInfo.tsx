import { Paper, Typography } from "@mui/material";

export interface INetworkGeneralInfoProps {
    totalHosts: number
    totalNetworks: number
}

export function NetworkGeneralInfo(props: INetworkGeneralInfoProps) {
    return (
        <Paper style={{ padding: 3 }}>
            <Typography>
                Всего подсетей: {props.totalNetworks}
                <br></br>
                Всего устройств: {props.totalHosts}
            </Typography>
        </Paper>
    )
}