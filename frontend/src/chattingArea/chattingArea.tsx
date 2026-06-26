import ChatInputComponent from "../components/ChatInputComponent/ChatInputComponent";
import "./chattingArea.css"
function ChatingArea(){
    return <div className="chattingArea">
         <div className="results">Results</div>
         <span className="inputBox"> 
                <ChatInputComponent></ChatInputComponent>
         </span>
    </div>
}



export default ChatingArea ; 