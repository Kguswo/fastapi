import uvicorn
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

"""
Part 17 -> Request Files
"""


@app.post("/files/")
async def create_file(
        files: list[bytes] = File(
            ...,
            description="A file read as bytes"
        )
):
    # if not file:
    #     return {"message": "No file provided"}
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfile/")
async def create_upload_file(
        files: list[UploadFile] = File(
            ...,
            description="A file read as UploadFile"
        )
):
    # if not file:
    #     return {"message": "No upload file provided"}
    # contents = await file.read()
    return {"filenames": [file.filename for file in files]}


if __name__ == "__main__":
    uvicorn.run("main_request_files:app", host="localhost", port=8000, reload=True)
