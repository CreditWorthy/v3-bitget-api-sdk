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


class MerchantPersonInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            averagePayment = schemas.StrSchema
            averageRealese = schemas.StrSchema
            email = schemas.StrSchema
            emailBindFlag = schemas.BoolSchema
            kycFlag = schemas.BoolSchema
            merchantId = schemas.StrSchema
            mobile = schemas.StrSchema
            mobileBindFlag = schemas.BoolSchema
            nickName = schemas.StrSchema
            realName = schemas.StrSchema
            registerTime = schemas.StrSchema
            thirtyBuy = schemas.StrSchema
            thirtyCompletionRate = schemas.StrSchema
            thirtySell = schemas.StrSchema
            thirtyTrades = schemas.StrSchema
            totalBuy = schemas.StrSchema
            totalCompletionRate = schemas.StrSchema
            totalSell = schemas.StrSchema
            totalTrades = schemas.StrSchema
            __annotations__ = {
                "averagePayment": averagePayment,
                "averageRealese": averageRealese,
                "email": email,
                "emailBindFlag": emailBindFlag,
                "kycFlag": kycFlag,
                "merchantId": merchantId,
                "mobile": mobile,
                "mobileBindFlag": mobileBindFlag,
                "nickName": nickName,
                "realName": realName,
                "registerTime": registerTime,
                "thirtyBuy": thirtyBuy,
                "thirtyCompletionRate": thirtyCompletionRate,
                "thirtySell": thirtySell,
                "thirtyTrades": thirtyTrades,
                "totalBuy": totalBuy,
                "totalCompletionRate": totalCompletionRate,
                "totalSell": totalSell,
                "totalTrades": totalTrades,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averagePayment"]) -> MetaOapg.properties.averagePayment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averageRealese"]) -> MetaOapg.properties.averageRealese: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailBindFlag"]) -> MetaOapg.properties.emailBindFlag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kycFlag"]) -> MetaOapg.properties.kycFlag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantId"]) -> MetaOapg.properties.merchantId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mobile"]) -> MetaOapg.properties.mobile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mobileBindFlag"]) -> MetaOapg.properties.mobileBindFlag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nickName"]) -> MetaOapg.properties.nickName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realName"]) -> MetaOapg.properties.realName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registerTime"]) -> MetaOapg.properties.registerTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thirtyBuy"]) -> MetaOapg.properties.thirtyBuy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thirtyCompletionRate"]) -> MetaOapg.properties.thirtyCompletionRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thirtySell"]) -> MetaOapg.properties.thirtySell: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thirtyTrades"]) -> MetaOapg.properties.thirtyTrades: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalBuy"]) -> MetaOapg.properties.totalBuy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalCompletionRate"]) -> MetaOapg.properties.totalCompletionRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalSell"]) -> MetaOapg.properties.totalSell: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalTrades"]) -> MetaOapg.properties.totalTrades: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["averagePayment", "averageRealese", "email", "emailBindFlag", "kycFlag", "merchantId", "mobile", "mobileBindFlag", "nickName", "realName", "registerTime", "thirtyBuy", "thirtyCompletionRate", "thirtySell", "thirtyTrades", "totalBuy", "totalCompletionRate", "totalSell", "totalTrades", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averagePayment"]) -> typing.Union[MetaOapg.properties.averagePayment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageRealese"]) -> typing.Union[MetaOapg.properties.averageRealese, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailBindFlag"]) -> typing.Union[MetaOapg.properties.emailBindFlag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kycFlag"]) -> typing.Union[MetaOapg.properties.kycFlag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantId"]) -> typing.Union[MetaOapg.properties.merchantId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mobile"]) -> typing.Union[MetaOapg.properties.mobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mobileBindFlag"]) -> typing.Union[MetaOapg.properties.mobileBindFlag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nickName"]) -> typing.Union[MetaOapg.properties.nickName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realName"]) -> typing.Union[MetaOapg.properties.realName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registerTime"]) -> typing.Union[MetaOapg.properties.registerTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thirtyBuy"]) -> typing.Union[MetaOapg.properties.thirtyBuy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thirtyCompletionRate"]) -> typing.Union[MetaOapg.properties.thirtyCompletionRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thirtySell"]) -> typing.Union[MetaOapg.properties.thirtySell, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thirtyTrades"]) -> typing.Union[MetaOapg.properties.thirtyTrades, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalBuy"]) -> typing.Union[MetaOapg.properties.totalBuy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalCompletionRate"]) -> typing.Union[MetaOapg.properties.totalCompletionRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalSell"]) -> typing.Union[MetaOapg.properties.totalSell, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalTrades"]) -> typing.Union[MetaOapg.properties.totalTrades, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["averagePayment", "averageRealese", "email", "emailBindFlag", "kycFlag", "merchantId", "mobile", "mobileBindFlag", "nickName", "realName", "registerTime", "thirtyBuy", "thirtyCompletionRate", "thirtySell", "thirtyTrades", "totalBuy", "totalCompletionRate", "totalSell", "totalTrades", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        averagePayment: typing.Union[MetaOapg.properties.averagePayment, str, schemas.Unset] = schemas.unset,
        averageRealese: typing.Union[MetaOapg.properties.averageRealese, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        emailBindFlag: typing.Union[MetaOapg.properties.emailBindFlag, bool, schemas.Unset] = schemas.unset,
        kycFlag: typing.Union[MetaOapg.properties.kycFlag, bool, schemas.Unset] = schemas.unset,
        merchantId: typing.Union[MetaOapg.properties.merchantId, str, schemas.Unset] = schemas.unset,
        mobile: typing.Union[MetaOapg.properties.mobile, str, schemas.Unset] = schemas.unset,
        mobileBindFlag: typing.Union[MetaOapg.properties.mobileBindFlag, bool, schemas.Unset] = schemas.unset,
        nickName: typing.Union[MetaOapg.properties.nickName, str, schemas.Unset] = schemas.unset,
        realName: typing.Union[MetaOapg.properties.realName, str, schemas.Unset] = schemas.unset,
        registerTime: typing.Union[MetaOapg.properties.registerTime, str, schemas.Unset] = schemas.unset,
        thirtyBuy: typing.Union[MetaOapg.properties.thirtyBuy, str, schemas.Unset] = schemas.unset,
        thirtyCompletionRate: typing.Union[MetaOapg.properties.thirtyCompletionRate, str, schemas.Unset] = schemas.unset,
        thirtySell: typing.Union[MetaOapg.properties.thirtySell, str, schemas.Unset] = schemas.unset,
        thirtyTrades: typing.Union[MetaOapg.properties.thirtyTrades, str, schemas.Unset] = schemas.unset,
        totalBuy: typing.Union[MetaOapg.properties.totalBuy, str, schemas.Unset] = schemas.unset,
        totalCompletionRate: typing.Union[MetaOapg.properties.totalCompletionRate, str, schemas.Unset] = schemas.unset,
        totalSell: typing.Union[MetaOapg.properties.totalSell, str, schemas.Unset] = schemas.unset,
        totalTrades: typing.Union[MetaOapg.properties.totalTrades, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MerchantPersonInfo':
        return super().__new__(
            cls,
            *args,
            averagePayment=averagePayment,
            averageRealese=averageRealese,
            email=email,
            emailBindFlag=emailBindFlag,
            kycFlag=kycFlag,
            merchantId=merchantId,
            mobile=mobile,
            mobileBindFlag=mobileBindFlag,
            nickName=nickName,
            realName=realName,
            registerTime=registerTime,
            thirtyBuy=thirtyBuy,
            thirtyCompletionRate=thirtyCompletionRate,
            thirtySell=thirtySell,
            thirtyTrades=thirtyTrades,
            totalBuy=totalBuy,
            totalCompletionRate=totalCompletionRate,
            totalSell=totalSell,
            totalTrades=totalTrades,
            _configuration=_configuration,
            **kwargs,
        )
