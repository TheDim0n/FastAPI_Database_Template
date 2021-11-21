from fastapi import FastAPI


app = FastAPI(redoc_url=None)


@app.get('/')
async def main():
    return {'name': 'TheDim0n'}
