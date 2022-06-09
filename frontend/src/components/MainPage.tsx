import React, { useState } from "react";
import { Host } from "../api/Host";
import BaseLayout from "../layouts/BaseLayout/BaseLayout";
import HostInfoPane from "./DeviceInfoPane/HostInfoPane";
import NetworkGrid from "./NetworkGrid/NetworkGrid";

function MainPage() {
    var [selectedHost, setSelectedHost] = useState<Host | null>(null)
    return (
        <BaseLayout
            left={<NetworkGrid onHostClick={setSelectedHost} />}
            right={<HostInfoPane host={selectedHost} />}
        />
    )
}
export default MainPage