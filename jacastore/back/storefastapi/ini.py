import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        #host="0.0.0.0",
        port=8000,
        timeout_keep_alive=120  # Aumenta o timeout keep-alive para 120 segundos
    )
