import { Host } from "../../api/Host";

export default interface INetworkInfoProps {
    onSelectedHostChanged: (host: Host) => void
}