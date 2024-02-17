from beauty_admin.views.base import BaseModelView
from beauty_models.beauty_models.models import Offer
from beauty_models.beauty_models.models import WorkingHours


class BusinessView(BaseModelView):
    form_columns = ('name', 'display_name', 'phone_number', 'location', 'owner', 'logo')
    inline_models = (
        (WorkingHours, dict(
            form_columns=('id', 'date', 'opening_time', 'closing_time'),
        )),
        (Offer, dict(
            form_columns=('id', 'name', 'price', 'duration'),
        )),
    )
