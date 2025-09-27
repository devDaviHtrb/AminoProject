const socket = io()

socket.on("connect", ()=>{
    socket.emit("joinRoom", document.getElementById("Name").innerText)
    
})
socket.on("message", (data)=>{
    MsgArea = document.getElementById("messagesArea")
    if(socket.id == data["id"]){
        MsgArea.innerHTML = MsgArea.innerHTML + ` <div class="message User">
                
                <div class="message-bubble">
                    ${data["msg"]}
                    <div class="message-time">10:31</div>
                </div>
            </div>`
    }else{
        MsgArea.innerHTML = MsgArea.innerHTML + `<div class="message OtherUser">
        <p>${data["name"]}:</p>
                <div class="message-bubble">
                    ${data["msg"]}
                    <div class="message-time">10:30</div>
                </div>
            </div>`
    }

})

function sendMessage(){
    socket.emit("message", {msg: document.getElementById("messageInput").value})
    document.getElementById("messageInput").value = ""
}