"""My custom Types"""
from typing import  Union, NamedTuple, NewType, Optional, Tuple, TypedDict
from typing import TYPE_CHECKING


ResMsg = TypedDict(
    'ResMsg', {
        'code': Union[int,str,None],
        'text': str
    })

RespObj = TypedDict(
    'RespObj', {
        'status': str,
        'code': Optional[int],
        'messages': list[ResMsg],
        'result': dict,
    })
