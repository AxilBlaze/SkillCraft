# This can be empty 

from app.routes.auth import bp as auth
from app.routes.chat import bp as chat
from app.routes.recommendations import bp as recommendations
from app.routes.dashboard import bp as dashboard
from app.routes.tutor import bp as tutor
from app.routes.learning_path import bp as learning_path
from app.routes.analytics import bp as analytics
from app.routes.test import bp as test

# Export all blueprints
auth = auth
chat = chat
recommendations = recommendations
dashboard = dashboard
tutor = tutor
learning_path = learning_path
analytics = analytics
test = test 