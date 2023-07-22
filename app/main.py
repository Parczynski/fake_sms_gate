from app.server import app
import uvicorn


from app.config import settings

uvicorn.run( app, host="0.0.0.0", port=settings.port )

