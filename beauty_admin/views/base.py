from flask import redirect, url_for
from flask_admin import BaseView
from flask_admin.contrib.sqla import ModelView


class _BaseView(BaseView):
    def is_accessible(self):
        return True

    def inaccessible_callback(self, name, **kwargs):
        """Handle the response to inaccessible views."""
        return redirect(url_for('admin.login_view'))


class BaseModelView(ModelView, _BaseView):
    edit_modal = False
