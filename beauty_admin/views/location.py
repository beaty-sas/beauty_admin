from beauty_admin.views.base import BaseModelView


class LocationView(BaseModelView):
    form_columns = ('name', 'geom')
