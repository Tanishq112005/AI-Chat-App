import React from "react";
import "./SideBarItem.css";

interface SideBarItemProps {
  icon?: React.ReactNode; 
  text: string;
}

const showingNumberLimit : number = 11; 
const showingNumberWithoutIcon : number = 26 ; 
function SideBarItem({ icon, text }: SideBarItemProps) {
  let finaltext : string = ""; 
  if(icon){
  if(text.length > showingNumberLimit){
    for(let i = 0 ; i<showingNumberLimit ; i++){
      finaltext += text[i] ; 
    }
    finaltext += "..."
  }
  else{
    finaltext = text; 
  }
}
else{
   if(text.length > showingNumberWithoutIcon){
    for(let i = 0 ; i<showingNumberWithoutIcon; i++){
      finaltext += text[i] ; 
    }
    finaltext += "..."
  }
  else{
    finaltext = text; 
  }
}


  return (
    <div className="sideBarItem">
      {icon && (
        <div className="iconWrapper">
          {icon}
        </div>
      )}

      <div className="textWrapper">
        {finaltext}
      </div>
    </div>
  );
}

export default SideBarItem;