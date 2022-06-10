import { Button } from "@mui/material";
import SplitPane from "react-split-pane";
import Pane from "react-split-pane";
import { IBaseLayout } from "./BaseLayoutTypes";
import ManageNetworksHeader from "../../components/ScanNetworkButton/ScanNetworkButton";
// @ts-nocheck
const BaseLayout = ({ left, right }: IBaseLayout) => (
  // @ts-ignore
  <SplitPane split="horizontal">
    <Pane><ManageNetworksHeader></ManageNetworksHeader></Pane>
    <SplitPane>
      <Pane>{left}</Pane>
      <Pane>{right && right}</Pane>
    </SplitPane>
  </SplitPane>
);

export default BaseLayout;
