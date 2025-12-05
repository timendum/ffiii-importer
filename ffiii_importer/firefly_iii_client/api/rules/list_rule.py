from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_response import BadRequestResponse
from ...models.internal_exception_response import InternalExceptionResponse
from ...models.not_found_response import NotFoundResponse
from ...models.rule_array import RuleArray
from ...models.unauthenticated_response import UnauthenticatedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    x_trace_id: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_trace_id, Unset):
        headers["X-Trace-Id"] = x_trace_id

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/rules",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[BadRequestResponse, InternalExceptionResponse, NotFoundResponse, RuleArray, UnauthenticatedResponse]
]:
    if response.status_code == 200:
        response_200 = RuleArray.from_dict(response.json())

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
    Union[BadRequestResponse, InternalExceptionResponse, NotFoundResponse, RuleArray, UnauthenticatedResponse]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    x_trace_id: Union[Unset, UUID] = UNSET,
) -> Response[
    Union[BadRequestResponse, InternalExceptionResponse, NotFoundResponse, RuleArray, UnauthenticatedResponse]
]:
    """List all rules.

     List all rules.

    Args:
        limit (Union[Unset, int]):  Example: 10.
        page (Union[Unset, int]):  Example: 1.
        x_trace_id (Union[Unset, UUID]):  Example: 40c71bbb-c676-4f24-83cf-cc725d7d7a00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestResponse, InternalExceptionResponse, NotFoundResponse, RuleArray, UnauthenticatedResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        x_trace_id=x_trace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    x_trace_id: Union[Unset, UUID] = UNSET,
) -> Optional[
    Union[BadRequestResponse, InternalExceptionResponse, NotFoundResponse, RuleArray, UnauthenticatedResponse]
]:
    """List all rules.

     List all rules.

    Args:
        limit (Union[Unset, int]):  Example: 10.
        page (Union[Unset, int]):  Example: 1.
        x_trace_id (Union[Unset, UUID]):  Example: 40c71bbb-c676-4f24-83cf-cc725d7d7a00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestResponse, InternalExceptionResponse, NotFoundResponse, RuleArray, UnauthenticatedResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        page=page,
        x_trace_id=x_trace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    x_trace_id: Union[Unset, UUID] = UNSET,
) -> Response[
    Union[BadRequestResponse, InternalExceptionResponse, NotFoundResponse, RuleArray, UnauthenticatedResponse]
]:
    """List all rules.

     List all rules.

    Args:
        limit (Union[Unset, int]):  Example: 10.
        page (Union[Unset, int]):  Example: 1.
        x_trace_id (Union[Unset, UUID]):  Example: 40c71bbb-c676-4f24-83cf-cc725d7d7a00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestResponse, InternalExceptionResponse, NotFoundResponse, RuleArray, UnauthenticatedResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        x_trace_id=x_trace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    x_trace_id: Union[Unset, UUID] = UNSET,
) -> Optional[
    Union[BadRequestResponse, InternalExceptionResponse, NotFoundResponse, RuleArray, UnauthenticatedResponse]
]:
    """List all rules.

     List all rules.

    Args:
        limit (Union[Unset, int]):  Example: 10.
        page (Union[Unset, int]):  Example: 1.
        x_trace_id (Union[Unset, UUID]):  Example: 40c71bbb-c676-4f24-83cf-cc725d7d7a00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestResponse, InternalExceptionResponse, NotFoundResponse, RuleArray, UnauthenticatedResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            page=page,
            x_trace_id=x_trace_id,
        )
    ).parsed
