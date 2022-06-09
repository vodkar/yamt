import SplitPane from "react-split-pane";
import Pane from "react-split-pane";
import { IBaseLayout } from "./BaseLayoutTypes";

const BaseLayout = ({ left, right }: IBaseLayout) => (
  <SplitPane>
    <Pane>{left}</Pane>
    <Pane>{right && right}</Pane>
  </SplitPane>
);

export default BaseLayout;
