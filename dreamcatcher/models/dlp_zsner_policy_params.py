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


from typing import Optional
from pydantic import BaseModel
from dreamcatcher.models.dlp_zsner_policy_params_dlp_zsner_policy import DlpZsnerPolicyParamsDlpZsnerPolicy

class DlpZsnerPolicyParams(BaseModel):
    """
    DlpZsnerPolicyParams
    """
    dlp_zsner_policy: Optional[DlpZsnerPolicyParamsDlpZsnerPolicy] = None
    __properties = ["dlp_zsner_policy"]

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
    def from_json(cls, json_str: str) -> DlpZsnerPolicyParams:
        """Create an instance of DlpZsnerPolicyParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of dlp_zsner_policy
        if self.dlp_zsner_policy:
            _dict['dlp_zsner_policy'] = self.dlp_zsner_policy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DlpZsnerPolicyParams:
        """Create an instance of DlpZsnerPolicyParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DlpZsnerPolicyParams.parse_obj(obj)

        _obj = DlpZsnerPolicyParams.parse_obj({
            "dlp_zsner_policy": DlpZsnerPolicyParamsDlpZsnerPolicy.from_dict(obj.get("dlp_zsner_policy")) if obj.get("dlp_zsner_policy") is not None else None
        })
        return _obj


