from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.routes.api_routes import ApiRouter
from app.routes.page_routes import PageRouter

api = FastAPI()

api.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configuração de CORS
api.add_middleware(
    CORSMiddleware,
    allow_origins=["https://weathergo.lukra.work", "http://localhost:8000"], # Adicione aqui a URL do seu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuração de rotas
api.include_router(ApiRouter)
api.include_router(PageRouter)

# --- Execução Direta ---
if __name__ == "__main__":
    import uvicorn
    print("🚀 Iniciando servidor FastAPI...")
    print("📍 URL: http://localhost:8000")
    print("📚 Documentação: http://localhost:8000/docs")
    print("🔄 Hot reload: ATIVO")
    print("\nPressione CTRL+C para parar o servidor\n")

    uvicorn.run(
        "main:api",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )