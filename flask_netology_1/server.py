import pydantic
from flask import Flask, jsonify
from models import Session, Advert


app = Flask('app')


class HttpError(Exception):
    def __init__(self, status_code: int, description: str | dict | list):
        self.status_code = status_code
        self.description = description


@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    response = jsonify({"status": "error", "description": error.description})
    response.status_code = error.status_code
    return response


def get_advert(advert_id: int, session: Session):
    advert = session.get(Advert, advert_id)
    if advert is None:
        raise HttpError(404, 'advert not found')
    return advert


class CreateAdvert(pydantic.BaseModel):
    title: str
    description: str
    owner: str

    @pydantic.validator("title")
    def is_ascii_title(cls, value: str):
        if not value.isascii():
            raise ValueError('incorrect title')
        return value

    @pydantic.validator("description")
    def is_ascii_description(cls, value: str):
        if not value.isascii():
            raise ValueError('incorrect description')
        return value

    @pydantic.validator("owner")
    def is_ascii_owner(cls, value: str):
        if not value.isascii():
            raise ValueError('incorrect owner name')
        return value


def validate(unvalidated_data: dict, validation_model):
    try:
        return validation_model(**unvalidated_data).dict()
    except pydantic.ValidationError as er:
        raise HttpError(400, er.errors())


if __name__ == '__main__':
    app.run(debug=True)
