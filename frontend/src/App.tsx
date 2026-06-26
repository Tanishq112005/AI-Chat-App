import "./App.css";
import ChatingArea from "./chattingArea/chattingArea";
import SideBar from "./SideBar/SideBar";


function App() {
  return (
    <div className="appContainer">
      <SideBar></SideBar>
      <ChatingArea></ChatingArea>
    </div>
  );
}

export default App;