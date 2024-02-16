from flask_sqlalchemy import SQLAlchemy

from beauty_models.beauty_models.models import BaseModel

db = SQLAlchemy(model_class=BaseModel)
