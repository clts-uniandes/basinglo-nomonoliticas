from fastapi import APIRouter, FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

router = APIRouter(
    prefix="/main",
    tags=["main page"],
    responses={404: {"description": "Not found"}},
)

def initialize():
    @router.get("/", response_class=HTMLResponse)
    async def get_main_site():
        html_content = """
        <html>
            <head>
                <title>PDA - Propiedades de los Andes</title>
            </head>
            <body>
                <h1>Look ma! HTML!</h1>
                <h2>Welcome to PDA's web homepage. This site is under construction</h2>
                <h3>ETA</h3>
                <h4>Soon! (tm)</h4>
            </body>
        </html>
        """
        return HTMLResponse(content=html_content, status_code=200)