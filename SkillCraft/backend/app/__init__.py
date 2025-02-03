from flask import Flask
from flask_cors import CORS
from config import Config
from pymongo import MongoClient
from app.utils.helpers import ensure_vector_store_exists

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize CORS
    CORS(app)
    
    # Ensure vector store directory exists
    ensure_vector_store_exists()
    
    try:
        # Initialize MongoDB with TLS configuration
        client = MongoClient(
            app.config['MONGODB_URI'],
            tls=True,
            tlsAllowInvalidCertificates=True
        )
        # Test the connection
        client.admin.command('ping')
        app.db = client.get_default_database()
        print("MongoDB connection successful!")
    except Exception as e:
        print(f"MongoDB connection failed: {str(e)}")
        raise e
    
    # Register blueprints
    from app.routes import auth, chat, recommendations, dashboard, tutor, learning_path, analytics, test
    
    # Register each blueprint
    app.register_blueprint(auth)
    app.register_blueprint(chat)
    app.register_blueprint(recommendations)
    app.register_blueprint(dashboard)
    app.register_blueprint(tutor)
    app.register_blueprint(learning_path)
    app.register_blueprint(analytics)
    app.register_blueprint(test)
    
    return app 