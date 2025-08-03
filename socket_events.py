room = {} 

def register_events(sio): 
    @sio.event 
    async def connect(sid,enviorn): 
        print("CLient Connect : ",sid)  
    
    @sio.event
    async def join_account_room(sid,data) : 
        account_id = data.get("account_id") 
        sio.enter_room(sid,account_id) 
        room.setdefault(account_id,[]).append(sid)
        print(f"{sid} joined room {account_id} ") 

    sio.event 
    async def disconnect(sid):
        print("Client Disconnect :",sid) 
        for rooms,sids in room.items(): 
            if sid in sids:
                sid.remove(sid) 

    @sio.event
    async def confirm_print(sid, data):
        account_id = data.get("account_id")
        print(f"Print confirmed by {sid} for account {account_id}")
        await sio.emit("stop_sending", {"message": "Printing done"}, room=account_id)