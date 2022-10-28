from app import app

#uruchamianie aplikacji
if __name__ == "__main__":
    app.run('0.0.0.0', port=1111, debug=True)
