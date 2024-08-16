# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, validator
from dreamcatcher.models.dlp_policy_anonymizer import DlpPolicyAnonymizer

class DlpPolicy(BaseModel):
    """
    DlpPolicy
    """
    active: Optional[StrictBool] = None
    anonymizer: Optional[DlpPolicyAnonymizer] = None
    entities: Optional[conlist(StrictStr)] = None
    id: Optional[Union[StrictFloat, StrictInt]] = None
    name: Optional[StrictStr] = None
    response: Optional[StrictStr] = None
    score_threshold: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["active", "anonymizer", "entities", "id", "name", "response", "score_threshold"]

    @validator('entities')
    def entities_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('MEDICAL_LICENSE', 'CREDIT_CARD', 'US_PASSPORT', 'PERSON', 'URL', 'DATE_TIME', 'IBAN_CODE', 'CRYPTO', 'US_BANK_NUMBER', 'PHONE_NUMBER', 'LOCATION', 'US_DRIVER_LICENSE', 'US_ITIN', 'IP_ADDRESS', 'EMAIL_ADDRESS', 'US_SSN', 'NRP'):
                raise ValueError("each list item must be one of ('MEDICAL_LICENSE', 'CREDIT_CARD', 'US_PASSPORT', 'PERSON', 'URL', 'DATE_TIME', 'IBAN_CODE', 'CRYPTO', 'US_BANK_NUMBER', 'PHONE_NUMBER', 'LOCATION', 'US_DRIVER_LICENSE', 'US_ITIN', 'IP_ADDRESS', 'EMAIL_ADDRESS', 'US_SSN', 'NRP')")
        return value

    @validator('response')
    def response_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('block', 'alert', 'anonymize'):
            raise ValueError("must be one of enum values ('block', 'alert', 'anonymize')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DlpPolicy:
        """Create an instance of DlpPolicy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of anonymizer
        if self.anonymizer:
            _dict['anonymizer'] = self.anonymizer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DlpPolicy:
        """Create an instance of DlpPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DlpPolicy.parse_obj(obj)

        _obj = DlpPolicy.parse_obj({
            "active": obj.get("active"),
            "anonymizer": DlpPolicyAnonymizer.from_dict(obj.get("anonymizer")) if obj.get("anonymizer") is not None else None,
            "entities": obj.get("entities"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "response": obj.get("response"),
            "score_threshold": obj.get("score_threshold")
        })
        return _obj


