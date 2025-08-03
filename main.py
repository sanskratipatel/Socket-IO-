from fastapi import FastAPI, Request 
import socketio 
from fastapi.responses  import FileResponse 
from socket_events import register_events
from fastapi import HTTPException
sio = socketio.AsyncServer(async_handlers='asgi' ,cors_allowed_origin = '*') 
app = FastAPI() 

socket_app = socketio.ASGIApp(sio , other_asgi_app=app) 

register_events(sio) 

@app.get("/print/{account_id}") 
async def trigger_print(account_id :str) : 
    try :
        file_info = { 
            "file_name":"print.pdf" ,
            "url" :f"" 

        }
        await sio.emit("send_file",file_info ,room =account_id) 
        return { 
            "messgae" : "File sent to room" ,
            "account_id" : account_id
        }
    except Exception as e : 
        raise HTTPException ( 
            status_code=500 ,
            detail=f"Internal Server Error {str(e)}"
        )  
    
    
@app.get("/download/{filename}") 
async def download_file(filename:str) : 
    try : 
       file_path = f"file_storage/{filename}" 
       return  FileResponse (
           file_path,
           media_type="application/pdf",
           filename=filename
       )
    except Exception as e : 
        raise HTTPException( 
            status_code=500, 
            detail=f"Internal Server Error {str(e)}"
        )



@app.post("/print-confirm/{account_id}")
async def stop_printing(account_id: str):
    try :
        await sio.emit("stop_sending", {"message": "Printing done"}, room=account_id)
        return {"status": "stopped for all in room"}
    except Exception as e : 
        raise HTTPException( 
            status_code=500, 
            detail=f"Internal Server Error {str(e)}"
        )