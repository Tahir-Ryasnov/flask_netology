from flask import jsonify, request
from flask.views import MethodView
from models import Session, Advert
from server import CreateAdvert, app, validate, get_advert


class AdvertView(MethodView):
    def get(self, advert_id: int):
        with Session() as session:
            advert = get_advert(advert_id, session)
            return jsonify({"id": advert_id, "title": advert.title, "description": advert.description,
                            "creation_date": advert.creation_date.strftime("%m.%d.%y"), "owner": advert.owner})

    def post(self):
        json_data = request.json
        json_data = validate(json_data, CreateAdvert)
        with Session() as session:
            advert = Advert(**json_data)
            session.add(advert)
            session.commit()
            return jsonify({"id": advert.id})

    def delete(self, advert_id: int):
        with Session() as session:
            advert = get_advert(advert_id, session)
            session.delete(advert)
            session.commit()
            return jsonify({"status": "deleted"})


app.add_url_rule("/adverts/<int:advert_id>/", view_func=AdvertView.as_view("advert"), methods=["GET", "DELETE"])
app.add_url_rule("/adverts/", view_func=AdvertView.as_view("advert_create"), methods=["POST"])
