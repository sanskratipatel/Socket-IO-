# Socket-IO
Socket-IO for learning purpose 

This project demonstrates how to use **FastAPI** with **Socket.IO** for real-time event communication. It allows multiple users under the same account to receive a file when one user triggers a `/print` API, and stops sending it when any user clicks a "Print" button.

---

##  Features

- FastAPI backend with async routes
- Socket.IO real-time communication
- Room-based broadcasting using `account_id`
- File download and distribution via event
- Simple client integration support (e.g., JS frontend)

---

##  Requirements

- Python 3.8+
- pip

Install dependencies:

```bash
pip install -r requirements.txt
````

---

##  Project Structure

```
.
├── main.py                # FastAPI + Socket.IO setup
├── socket_events.py       # Socket.IO event handlers
├── file_storage/          # Folder to store files like print.pdf
├── .gitignore
└── README.md
```
---

##  Running the Server

```bash
uvicorn main:socket_app --reload
```

Server will be live at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

##  API Endpoints

| Method | Endpoint                      | Description                        |
| ------ | ----------------------------- | ---------------------------------- |
| GET    | `/print/{account_id}`         | Sends file info to connected users |
| POST   | `/print-confirm/{account_id}` | Stops further file sending         |
| GET    | `/download/{filename}`        | File download route                |

---

##  Socket.IO Events

| Event Name          | Direction       | Description                      |
| ------------------- | --------------- | -------------------------------- |
| `join_account_room` | Client → Server | Joins a room by `account_id`     |
| `send_file`         | Server → Client | Sends file metadata (name + URL) |
| `stop_sending`      | Server → Client | Notifies to stop print           |
| `confirm_print`     | Client → Server | User confirms print done         |

