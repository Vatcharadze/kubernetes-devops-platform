import os
from flask import Flask, jsonify

#create app function
def create_app():
    app = Flask(__name__)

    app.config["APP_VERSION"] = os.getenv("APP_VERSION", "1.0.0")
    app.config["APP_ENV"] = os.getenv("APP_ENV", "development")

    @app.get("/")
    def index():
        return jsonify({
            "application": "devops-api",
            "version": app.config["APP_VERSION"],
            "message": "DevOps API is running"
        }), 200

    @app.get("/health")
    def health():
        return jsonify({"status": "healthy"}), 200

    @app.get("/api/info")
    def info():
        return jsonify({
            "application": "devops-api",
            "version": app.config["APP_VERSION"],
            "environment": app.config["APP_ENV"]
        }), 200

    @app.get("/api/status")
    def status():
        return jsonify({
            "status": "ok",
            "application": "devops-api"
        }), 200

    return app

app = create_app()

if __name__ == "__main__":
    # Bind to all interfaces so the app is reachable from a container
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
