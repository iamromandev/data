import typing as tp

import fastapi as fa

app = fa.FastAPI()


@app.get("/")
def read_root():
    return {"app": "scrapify"}


if __name__ == "__main__":
    print("Scrapify")
