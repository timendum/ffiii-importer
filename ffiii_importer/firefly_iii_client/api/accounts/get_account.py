import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_single import AccountSingle
from ...models.bad_request_response import BadRequestResponse
from ...models.internal_exception_response import InternalExceptionResponse
from ...models.not_found_response import NotFoundResponse
from ...models.unauthenticated_response import UnauthenticatedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    start: Union[Unset, datetime.date] = UNSET,
    end: Union[Unset, datetime.date] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    x_trace_id: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_trace_id, Unset):
        headers["X-Trace-Id"] = x_trace_id

    params: dict[str, Any] = {}

    json_start: Union[Unset, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    json_end: Union[Unset, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/accounts/{id}",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[AccountSingle, BadRequestResponse, InternalExceptionResponse, NotFoundResponse, UnauthenticatedResponse]
]:
    if response.status_code == 200:
        response_200 = AccountSingle.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BadRequestResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UnauthenticatedResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = NotFoundResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = InternalExceptionResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[AccountSingle, BadRequestResponse, InternalExceptionResponse, NotFoundResponse, UnauthenticatedResponse]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.date] = UNSET,
    end: Union[Unset, datetime.date] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    x_trace_id: Union[Unset, UUID] = UNSET,
) -> Response[
    Union[AccountSingle, BadRequestResponse, InternalExceptionResponse, NotFoundResponse, UnauthenticatedResponse]
]:
    """Get single account.

     Returns a single account by its ID.

    Args:
        id (str):  Example: 123.
        start (Union[Unset, datetime.date]):
        end (Union[Unset, datetime.date]):
        date (Union[Unset, datetime.date]):
        x_trace_id (Union[Unset, UUID]):  Example: 40c71bbb-c676-4f24-83cf-cc725d7d7a00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountSingle, BadRequestResponse, InternalExceptionResponse, NotFoundResponse, UnauthenticatedResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        start=start,
        end=end,
        date=date,
        x_trace_id=x_trace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.date] = UNSET,
    end: Union[Unset, datetime.date] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    x_trace_id: Union[Unset, UUID] = UNSET,
) -> Optional[
    Union[AccountSingle, BadRequestResponse, InternalExceptionResponse, NotFoundResponse, UnauthenticatedResponse]
]:
    """Get single account.

     Returns a single account by its ID.

    Args:
        id (str):  Example: 123.
        start (Union[Unset, datetime.date]):
        end (Union[Unset, datetime.date]):
        date (Union[Unset, datetime.date]):
        x_trace_id (Union[Unset, UUID]):  Example: 40c71bbb-c676-4f24-83cf-cc725d7d7a00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountSingle, BadRequestResponse, InternalExceptionResponse, NotFoundResponse, UnauthenticatedResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        start=start,
        end=end,
        date=date,
        x_trace_id=x_trace_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.date] = UNSET,
    end: Union[Unset, datetime.date] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    x_trace_id: Union[Unset, UUID] = UNSET,
) -> Response[
    Union[AccountSingle, BadRequestResponse, InternalExceptionResponse, NotFoundResponse, UnauthenticatedResponse]
]:
    """Get single account.

     Returns a single account by its ID.

    Args:
        id (str):  Example: 123.
        start (Union[Unset, datetime.date]):
        end (Union[Unset, datetime.date]):
        date (Union[Unset, datetime.date]):
        x_trace_id (Union[Unset, UUID]):  Example: 40c71bbb-c676-4f24-83cf-cc725d7d7a00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountSingle, BadRequestResponse, InternalExceptionResponse, NotFoundResponse, UnauthenticatedResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        start=start,
        end=end,
        date=date,
        x_trace_id=x_trace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.date] = UNSET,
    end: Union[Unset, datetime.date] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    x_trace_id: Union[Unset, UUID] = UNSET,
) -> Optional[
    Union[AccountSingle, BadRequestResponse, InternalExceptionResponse, NotFoundResponse, UnauthenticatedResponse]
]:
    """Get single account.

     Returns a single account by its ID.

    Args:
        id (str):  Example: 123.
        start (Union[Unset, datetime.date]):
        end (Union[Unset, datetime.date]):
        date (Union[Unset, datetime.date]):
        x_trace_id (Union[Unset, UUID]):  Example: 40c71bbb-c676-4f24-83cf-cc725d7d7a00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountSingle, BadRequestResponse, InternalExceptionResponse, NotFoundResponse, UnauthenticatedResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            start=start,
            end=end,
            date=date,
            x_trace_id=x_trace_id,
        )
    ).parsed
