# simple fastapi app to test the model
from fastapi import FastAPI, Header
from datetime import datetime
from typing import Optional

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# verify the timestamp in the request header is within 5 seconds
@app.get("/verify")
def verify_timestamp(request_time: Optional[str] = Header(None, alias="request_time")):
    if request_time is None:
        return {"status": "error", "message": "request_time header is missing"}

    try:
        # '%Y-%m-%d %H:%M:%S'
        request_timestamp = datetime.strptime(request_time, '%Y-%m-%d %H:%M:%S').timestamp()
        current_timestamp = datetime.now().timestamp()

        # Check if the timestamp is within 6 seconds
        if abs(current_timestamp - request_timestamp) <= 6:
            return {"status": "success", 'request_time': f'{request_time}',
                    "message": "Timestamp is valid"}
        else:
            return {"status": "error", 'request_time': f'{request_time}',
                    "message": "Timestamp is invalid because it is not within 5 seconds"}
    except ValueError:
        return {"status": "error", "message": "Invalid timestamp format"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
