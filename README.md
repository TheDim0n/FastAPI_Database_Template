# TaskX-Backend

![](https://gitlab.com/TheDim0n/taskx-backend/badges/main/pipeline.svg?key_text=tests)

### Python installation
**1.** Create and activate virtual environment:
```
py -m venv venv
```
```
# for Windows
venv\Scripts\activate
# or for Linux
venv/bin/activate
```
**2.** Install requirements:
```
py -m pip install -U pip
pip install -r requirements.txt
```
**3.** Run the project:
```
uvicorn app.main:app
```
> Documentation awailable from http://localhost:8000/docs
