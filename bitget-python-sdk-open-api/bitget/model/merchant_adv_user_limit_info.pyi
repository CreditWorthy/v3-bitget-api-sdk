# coding: utf-8

"""
    Bitget Open API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from bitget import schemas  # noqa: F401


class MerchantAdvUserLimitInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            allowMerchantPlace = schemas.StrSchema
            country = schemas.StrSchema
            maxCompleteNum = schemas.StrSchema
            minCompleteNum = schemas.StrSchema
            placeOrderNum = schemas.StrSchema
            thirtyCompleteRate = schemas.StrSchema
            __annotations__ = {
                "allowMerchantPlace": allowMerchantPlace,
                "country": country,
                "maxCompleteNum": maxCompleteNum,
                "minCompleteNum": minCompleteNum,
                "placeOrderNum": placeOrderNum,
                "thirtyCompleteRate": thirtyCompleteRate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowMerchantPlace"]) -> MetaOapg.properties.allowMerchantPlace: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxCompleteNum"]) -> MetaOapg.properties.maxCompleteNum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minCompleteNum"]) -> MetaOapg.properties.minCompleteNum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["placeOrderNum"]) -> MetaOapg.properties.placeOrderNum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thirtyCompleteRate"]) -> MetaOapg.properties.thirtyCompleteRate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["allowMerchantPlace", "country", "maxCompleteNum", "minCompleteNum", "placeOrderNum", "thirtyCompleteRate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowMerchantPlace"]) -> typing.Union[MetaOapg.properties.allowMerchantPlace, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxCompleteNum"]) -> typing.Union[MetaOapg.properties.maxCompleteNum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minCompleteNum"]) -> typing.Union[MetaOapg.properties.minCompleteNum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["placeOrderNum"]) -> typing.Union[MetaOapg.properties.placeOrderNum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thirtyCompleteRate"]) -> typing.Union[MetaOapg.properties.thirtyCompleteRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["allowMerchantPlace", "country", "maxCompleteNum", "minCompleteNum", "placeOrderNum", "thirtyCompleteRate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        allowMerchantPlace: typing.Union[MetaOapg.properties.allowMerchantPlace, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        maxCompleteNum: typing.Union[MetaOapg.properties.maxCompleteNum, str, schemas.Unset] = schemas.unset,
        minCompleteNum: typing.Union[MetaOapg.properties.minCompleteNum, str, schemas.Unset] = schemas.unset,
        placeOrderNum: typing.Union[MetaOapg.properties.placeOrderNum, str, schemas.Unset] = schemas.unset,
        thirtyCompleteRate: typing.Union[MetaOapg.properties.thirtyCompleteRate, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MerchantAdvUserLimitInfo':
        return super().__new__(
            cls,
            *args,
            allowMerchantPlace=allowMerchantPlace,
            country=country,
            maxCompleteNum=maxCompleteNum,
            minCompleteNum=minCompleteNum,
            placeOrderNum=placeOrderNum,
            thirtyCompleteRate=thirtyCompleteRate,
            _configuration=_configuration,
            **kwargs,
        )
