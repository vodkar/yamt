import { useState } from "react";
import { default as Pane, default as SplitPane } from "react-split-pane";
import styled from "styled-components";
import { Host } from "../../api/Host";
import HostInfoPane from "../../components/DeviceInfoPane/HostInfoPane";
import NetworkGrid from "../../components/NetworkGrid/NetworkGrid";
import NetworkInfoPane from "../../components/NetworkInfoPane/NetworkInfoPane";

const Wrapper = styled.div`
.Resizer {
  background: #2962FF;
}
`;

function WorkSpacelayout() {
    var [selectedHost, setSelectedHost] = useState<Host | null>(null);


    return (
        <Wrapper>
            <SplitPane>{/*
    // @ts-ignore */}
                <Pane resizerClassName="Resizer" size="20%" >
                    <NetworkInfoPane onSelectedHostChanged={setSelectedHost} />
                </Pane>
                <Pane>
                    <NetworkGrid onHostClick={setSelectedHost} />
                </Pane>{/*
    // @ts-ignore */}
                <Pane size="28%"><HostInfoPane host={selectedHost} /></Pane>
            </SplitPane >
        </Wrapper>
    )
};

export default WorkSpacelayout;
