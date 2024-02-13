from src.errors.error_types.http_unprocessable_entity_error import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator

class MockRequest:
    def __init__(self, json: any) -> None:
        self.json = json

def test_tag_creator_validator():
    req = MockRequest(
      json={
        "product_code": "123"
      }
    )
    tag_creator_validator(req)

def test_tag_creator_validator_error():
    req = MockRequest(
      json={
        "product_code": 123
      }
    )
    try:
        tag_creator_validator(req)
        assert False
    except HttpUnprocessableEntityError as error:
        assert isinstance(error, HttpUnprocessableEntityError)
        assert error.name == "UnprocessableEntity"
        assert error.status_code == 422
