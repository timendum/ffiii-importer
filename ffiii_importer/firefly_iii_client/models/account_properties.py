import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.account_role_property_type_1 import AccountRolePropertyType1
from ..models.account_role_property_type_2_type_1 import AccountRolePropertyType2Type1
from ..models.account_role_property_type_3_type_1 import AccountRolePropertyType3Type1
from ..models.credit_card_type_property_type_1 import CreditCardTypePropertyType1
from ..models.credit_card_type_property_type_2_type_1 import CreditCardTypePropertyType2Type1
from ..models.credit_card_type_property_type_3_type_1 import CreditCardTypePropertyType3Type1
from ..models.interest_period_property_type_1 import InterestPeriodPropertyType1
from ..models.interest_period_property_type_2_type_1 import InterestPeriodPropertyType2Type1
from ..models.interest_period_property_type_3_type_1 import InterestPeriodPropertyType3Type1
from ..models.liability_direction_property_type_1 import LiabilityDirectionPropertyType1
from ..models.liability_direction_property_type_2_type_1 import LiabilityDirectionPropertyType2Type1
from ..models.liability_direction_property_type_3_type_1 import LiabilityDirectionPropertyType3Type1
from ..models.liability_type_property_type_1 import LiabilityTypePropertyType1
from ..models.liability_type_property_type_2_type_1 import LiabilityTypePropertyType2Type1
from ..models.liability_type_property_type_3_type_1 import LiabilityTypePropertyType3Type1
from ..models.short_account_type_property import ShortAccountTypeProperty
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountProperties")


@_attrs_define
class AccountProperties:
    """
    Attributes:
        name (str):  Example: My checking account.
        type_ (ShortAccountTypeProperty): Can only be one one these account types. import, initial-balance and
            reconciliation cannot be set manually. Example: asset.
        created_at (Union[Unset, datetime.datetime]):  Example: 2025-10-01T00:00:00+00:00.
        updated_at (Union[Unset, datetime.datetime]):  Example: 2025-10-01T00:00:00+00:00.
        active (Union[Unset, bool]):  Default: True.
        order (Union[None, Unset, int]): Order of the account. Is NULL if account is not asset or liability. Example: 1.
        account_role (Union[AccountRolePropertyType1, AccountRolePropertyType2Type1, AccountRolePropertyType3Type1,
            None, Unset]): Is only mandatory when the type is asset. Example: defaultAsset.
        object_group_id (Union[None, Unset, str]): The group ID of the group this object is part of. NULL if no group.
            Example: 5.
        object_group_order (Union[None, Unset, int]): The order of the group. At least 1, for the highest sorting.
            Example: 5.
        object_group_title (Union[None, Unset, str]): The name of the group. NULL if no group. Example: Example Group.
        object_has_currency_setting (Union[Unset, bool]): Indicates whether the account has a currency setting. If
            false, the account uses the administration's primary currency. Asset accounts and liability accounts always have
            a currency setting, while expense and revenue accounts do not. Example: True.
        currency_id (Union[Unset, str]): The currency ID of the currency associated with this object. Example: 5.
        currency_name (Union[Unset, str]): The currency name of the currency associated with this object. Example: Euro.
        currency_code (Union[Unset, str]): The currency code of the currency associated with this object. Example: EUR.
        currency_symbol (Union[Unset, str]):  Example: $.
        currency_decimal_places (Union[Unset, int]):  Example: 2.
        primary_currency_id (Union[Unset, str]): The currency ID of the administration's primary currency. Example: 5.
        primary_currency_name (Union[Unset, str]): The currency name of the administration's primary currency. Example:
            Euro.
        primary_currency_code (Union[Unset, str]): The currency code of the administration's primary currency. Example:
            EUR.
        primary_currency_symbol (Union[Unset, str]): The currency symbol of the administration's primary currency.
            Example: $.
        primary_currency_decimal_places (Union[Unset, int]): The currency decimal places of the administration's primary
            currency. Example: 2.
        current_balance (Union[Unset, str]): The current balance of the account in the account's currency. If the
            account has no currency, this is the balance in the administration's primary currency. Either way, the
            `currency_*` fields reflect the currency used. Example: 123.45.
        pc_current_balance (Union[None, Unset, str]): The current balance of the account in the administration's primary
            currency. The `primary_currency_*` fields reflect the currency used. This field is NULL if the user does have
            'convert to primary' set to true in their settings. Example: 123.45.
        balance_difference (Union[Unset, str]): If you submit a start AND end date, this will be the difference between
            those two moments. Example: 123.45.
        pc_balance_difference (Union[None, Unset, str]): If you submit a start AND end date, this will be the difference
            in the currency of the account or the administration's primary currency between those two moments. Example:
            123.45.
        opening_balance (Union[Unset, str]): Represents the opening balance, the initial amount this account holds in
            the currency of the account or the administration's primary currency if the account has no currency. Either way,
            the `currency_*` fields reflect the currency used. Example: -1012.12.
        pc_opening_balance (Union[Unset, str]): The opening balance of the account in the administration's primary
            currency (pc). The `primary_currency_*` fields reflect the currency used. This field is NULL if the user does
            have 'convert to primary' set to true in their settings. Example: -1012.12.
        virtual_balance (Union[Unset, str]): The virtual balance of the account in the account's currency or the
            administration's primary currency if the account has no currency. Example: 123.45.
        pc_virtual_balance (Union[Unset, str]): The virtual balance of the account in the administration's primary
            currency (pc). The `primary_currency_*` fields reflect the currency used. This field is NULL if the user does
            have 'convert to primary' set to true in their settings. Example: 123.45.
        debt_amount (Union[None, Unset, str]): In liability accounts (loans, debts and mortgages), this is the amount of
            debt in the account's currency (see the `currency_*` fields). In asset accounts, this is NULL. Example: 1012.12.
        pc_debt_amount (Union[None, Unset, str]): In liability accounts (loans, debts and mortgages), this is the amount
            of debt in the administration's primary currency (see the `currency_*` fields. In asset accounts, this is NULL.
            Example: 1012.12.
        current_balance_date (Union[Unset, datetime.datetime]): The timestamp for this date is always 23:59:59, to
            indicate it's the balance at the very END of that particular day. Example: 2025-10-31T23:59:59+00:00.
        notes (Union[None, Unset, str]):  Example: Some example notes.
        monthly_payment_date (Union[None, Unset, datetime.datetime]): Mandatory when the account_role is ccAsset. Moment
            at which CC payment installments are asked for by the bank. Example: 2025-10-01T00:00:00+00:00.
        credit_card_type (Union[CreditCardTypePropertyType1, CreditCardTypePropertyType2Type1,
            CreditCardTypePropertyType3Type1, None, Unset]): Mandatory when the account_role is ccAsset. Can only be
            monthlyFull or null. Example: monthlyFull.
        account_number (Union[None, Unset, str]):  Example: 7009312345678.
        iban (Union[None, Unset, str]):  Example: GB98MIDL07009312345678.
        bic (Union[None, Unset, str]):  Example: BOFAUS3N.
        opening_balance_date (Union[None, Unset, datetime.datetime]): Represents the date of the opening balance.
            Example: 2025-10-01T00:00:00+00:00.
        liability_type (Union[LiabilityTypePropertyType1, LiabilityTypePropertyType2Type1,
            LiabilityTypePropertyType3Type1, None, Unset]): Mandatory when type is liability. Specifies the exact type.
            Example: loan.
        liability_direction (Union[LiabilityDirectionPropertyType1, LiabilityDirectionPropertyType2Type1,
            LiabilityDirectionPropertyType3Type1, None, Unset]): 'credit' indicates somebody owes you the liability. 'debit'
            Indicates you owe this debt yourself. Works only for liabilities. Example: credit.
        interest (Union[None, Unset, str]): Mandatory when type is liability. Interest percentage. Example: 5.3.
        interest_period (Union[InterestPeriodPropertyType1, InterestPeriodPropertyType2Type1,
            InterestPeriodPropertyType3Type1, None, Unset]): Mandatory when type is liability. Period over which the
            interest is calculated. Example: monthly.
        include_net_worth (Union[Unset, bool]):  Default: True. Example: True.
        longitude (Union[None, Unset, float]): Latitude of the accounts's location, if applicable. Can be used to draw a
            map. Example: 5.916667.
        latitude (Union[None, Unset, float]): Latitude of the accounts's location, if applicable. Can be used to draw a
            map. Example: 51.983333.
        zoom_level (Union[None, Unset, int]): Zoom level for the map, if drawn. This to set the box right. Unfortunately
            this is a proprietary value because each map provider has different zoom levels. Example: 6.
        last_activity (Union[None, Unset, datetime.datetime]): Last activity of the account. Example:
            2025-10-01T00:00:00+00:00.
    """

    name: str
    type_: ShortAccountTypeProperty
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    active: Union[Unset, bool] = True
    order: Union[None, Unset, int] = UNSET
    account_role: Union[
        AccountRolePropertyType1, AccountRolePropertyType2Type1, AccountRolePropertyType3Type1, None, Unset
    ] = UNSET
    object_group_id: Union[None, Unset, str] = UNSET
    object_group_order: Union[None, Unset, int] = UNSET
    object_group_title: Union[None, Unset, str] = UNSET
    object_has_currency_setting: Union[Unset, bool] = UNSET
    currency_id: Union[Unset, str] = UNSET
    currency_name: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    currency_symbol: Union[Unset, str] = UNSET
    currency_decimal_places: Union[Unset, int] = UNSET
    primary_currency_id: Union[Unset, str] = UNSET
    primary_currency_name: Union[Unset, str] = UNSET
    primary_currency_code: Union[Unset, str] = UNSET
    primary_currency_symbol: Union[Unset, str] = UNSET
    primary_currency_decimal_places: Union[Unset, int] = UNSET
    current_balance: Union[Unset, str] = UNSET
    pc_current_balance: Union[None, Unset, str] = UNSET
    balance_difference: Union[Unset, str] = UNSET
    pc_balance_difference: Union[None, Unset, str] = UNSET
    opening_balance: Union[Unset, str] = UNSET
    pc_opening_balance: Union[Unset, str] = UNSET
    virtual_balance: Union[Unset, str] = UNSET
    pc_virtual_balance: Union[Unset, str] = UNSET
    debt_amount: Union[None, Unset, str] = UNSET
    pc_debt_amount: Union[None, Unset, str] = UNSET
    current_balance_date: Union[Unset, datetime.datetime] = UNSET
    notes: Union[None, Unset, str] = UNSET
    monthly_payment_date: Union[None, Unset, datetime.datetime] = UNSET
    credit_card_type: Union[
        CreditCardTypePropertyType1, CreditCardTypePropertyType2Type1, CreditCardTypePropertyType3Type1, None, Unset
    ] = UNSET
    account_number: Union[None, Unset, str] = UNSET
    iban: Union[None, Unset, str] = UNSET
    bic: Union[None, Unset, str] = UNSET
    opening_balance_date: Union[None, Unset, datetime.datetime] = UNSET
    liability_type: Union[
        LiabilityTypePropertyType1, LiabilityTypePropertyType2Type1, LiabilityTypePropertyType3Type1, None, Unset
    ] = UNSET
    liability_direction: Union[
        LiabilityDirectionPropertyType1,
        LiabilityDirectionPropertyType2Type1,
        LiabilityDirectionPropertyType3Type1,
        None,
        Unset,
    ] = UNSET
    interest: Union[None, Unset, str] = UNSET
    interest_period: Union[
        InterestPeriodPropertyType1, InterestPeriodPropertyType2Type1, InterestPeriodPropertyType3Type1, None, Unset
    ] = UNSET
    include_net_worth: Union[Unset, bool] = True
    longitude: Union[None, Unset, float] = UNSET
    latitude: Union[None, Unset, float] = UNSET
    zoom_level: Union[None, Unset, int] = UNSET
    last_activity: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        active = self.active

        order: Union[None, Unset, int]
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order

        account_role: Union[None, Unset, str]
        if isinstance(self.account_role, Unset):
            account_role = UNSET
        elif isinstance(self.account_role, AccountRolePropertyType1):
            account_role = self.account_role.value
        elif isinstance(self.account_role, AccountRolePropertyType2Type1):
            account_role = self.account_role.value
        elif isinstance(self.account_role, AccountRolePropertyType3Type1):
            account_role = self.account_role.value
        else:
            account_role = self.account_role

        object_group_id: Union[None, Unset, str]
        if isinstance(self.object_group_id, Unset):
            object_group_id = UNSET
        else:
            object_group_id = self.object_group_id

        object_group_order: Union[None, Unset, int]
        if isinstance(self.object_group_order, Unset):
            object_group_order = UNSET
        else:
            object_group_order = self.object_group_order

        object_group_title: Union[None, Unset, str]
        if isinstance(self.object_group_title, Unset):
            object_group_title = UNSET
        else:
            object_group_title = self.object_group_title

        object_has_currency_setting = self.object_has_currency_setting

        currency_id = self.currency_id

        currency_name = self.currency_name

        currency_code = self.currency_code

        currency_symbol = self.currency_symbol

        currency_decimal_places = self.currency_decimal_places

        primary_currency_id = self.primary_currency_id

        primary_currency_name = self.primary_currency_name

        primary_currency_code = self.primary_currency_code

        primary_currency_symbol = self.primary_currency_symbol

        primary_currency_decimal_places = self.primary_currency_decimal_places

        current_balance = self.current_balance

        pc_current_balance: Union[None, Unset, str]
        if isinstance(self.pc_current_balance, Unset):
            pc_current_balance = UNSET
        else:
            pc_current_balance = self.pc_current_balance

        balance_difference = self.balance_difference

        pc_balance_difference: Union[None, Unset, str]
        if isinstance(self.pc_balance_difference, Unset):
            pc_balance_difference = UNSET
        else:
            pc_balance_difference = self.pc_balance_difference

        opening_balance = self.opening_balance

        pc_opening_balance = self.pc_opening_balance

        virtual_balance = self.virtual_balance

        pc_virtual_balance = self.pc_virtual_balance

        debt_amount: Union[None, Unset, str]
        if isinstance(self.debt_amount, Unset):
            debt_amount = UNSET
        else:
            debt_amount = self.debt_amount

        pc_debt_amount: Union[None, Unset, str]
        if isinstance(self.pc_debt_amount, Unset):
            pc_debt_amount = UNSET
        else:
            pc_debt_amount = self.pc_debt_amount

        current_balance_date: Union[Unset, str] = UNSET
        if not isinstance(self.current_balance_date, Unset):
            current_balance_date = self.current_balance_date.isoformat()

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        monthly_payment_date: Union[None, Unset, str]
        if isinstance(self.monthly_payment_date, Unset):
            monthly_payment_date = UNSET
        elif isinstance(self.monthly_payment_date, datetime.datetime):
            monthly_payment_date = self.monthly_payment_date.isoformat()
        else:
            monthly_payment_date = self.monthly_payment_date

        credit_card_type: Union[None, Unset, str]
        if isinstance(self.credit_card_type, Unset):
            credit_card_type = UNSET
        elif isinstance(self.credit_card_type, CreditCardTypePropertyType1):
            credit_card_type = self.credit_card_type.value
        elif isinstance(self.credit_card_type, CreditCardTypePropertyType2Type1):
            credit_card_type = self.credit_card_type.value
        elif isinstance(self.credit_card_type, CreditCardTypePropertyType3Type1):
            credit_card_type = self.credit_card_type.value
        else:
            credit_card_type = self.credit_card_type

        account_number: Union[None, Unset, str]
        if isinstance(self.account_number, Unset):
            account_number = UNSET
        else:
            account_number = self.account_number

        iban: Union[None, Unset, str]
        if isinstance(self.iban, Unset):
            iban = UNSET
        else:
            iban = self.iban

        bic: Union[None, Unset, str]
        if isinstance(self.bic, Unset):
            bic = UNSET
        else:
            bic = self.bic

        opening_balance_date: Union[None, Unset, str]
        if isinstance(self.opening_balance_date, Unset):
            opening_balance_date = UNSET
        elif isinstance(self.opening_balance_date, datetime.datetime):
            opening_balance_date = self.opening_balance_date.isoformat()
        else:
            opening_balance_date = self.opening_balance_date

        liability_type: Union[None, Unset, str]
        if isinstance(self.liability_type, Unset):
            liability_type = UNSET
        elif isinstance(self.liability_type, LiabilityTypePropertyType1):
            liability_type = self.liability_type.value
        elif isinstance(self.liability_type, LiabilityTypePropertyType2Type1):
            liability_type = self.liability_type.value
        elif isinstance(self.liability_type, LiabilityTypePropertyType3Type1):
            liability_type = self.liability_type.value
        else:
            liability_type = self.liability_type

        liability_direction: Union[None, Unset, str]
        if isinstance(self.liability_direction, Unset):
            liability_direction = UNSET
        elif isinstance(self.liability_direction, LiabilityDirectionPropertyType1):
            liability_direction = self.liability_direction.value
        elif isinstance(self.liability_direction, LiabilityDirectionPropertyType2Type1):
            liability_direction = self.liability_direction.value
        elif isinstance(self.liability_direction, LiabilityDirectionPropertyType3Type1):
            liability_direction = self.liability_direction.value
        else:
            liability_direction = self.liability_direction

        interest: Union[None, Unset, str]
        if isinstance(self.interest, Unset):
            interest = UNSET
        else:
            interest = self.interest

        interest_period: Union[None, Unset, str]
        if isinstance(self.interest_period, Unset):
            interest_period = UNSET
        elif isinstance(self.interest_period, InterestPeriodPropertyType1):
            interest_period = self.interest_period.value
        elif isinstance(self.interest_period, InterestPeriodPropertyType2Type1):
            interest_period = self.interest_period.value
        elif isinstance(self.interest_period, InterestPeriodPropertyType3Type1):
            interest_period = self.interest_period.value
        else:
            interest_period = self.interest_period

        include_net_worth = self.include_net_worth

        longitude: Union[None, Unset, float]
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        latitude: Union[None, Unset, float]
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        zoom_level: Union[None, Unset, int]
        if isinstance(self.zoom_level, Unset):
            zoom_level = UNSET
        else:
            zoom_level = self.zoom_level

        last_activity: Union[None, Unset, str]
        if isinstance(self.last_activity, Unset):
            last_activity = UNSET
        elif isinstance(self.last_activity, datetime.datetime):
            last_activity = self.last_activity.isoformat()
        else:
            last_activity = self.last_activity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if active is not UNSET:
            field_dict["active"] = active
        if order is not UNSET:
            field_dict["order"] = order
        if account_role is not UNSET:
            field_dict["account_role"] = account_role
        if object_group_id is not UNSET:
            field_dict["object_group_id"] = object_group_id
        if object_group_order is not UNSET:
            field_dict["object_group_order"] = object_group_order
        if object_group_title is not UNSET:
            field_dict["object_group_title"] = object_group_title
        if object_has_currency_setting is not UNSET:
            field_dict["object_has_currency_setting"] = object_has_currency_setting
        if currency_id is not UNSET:
            field_dict["currency_id"] = currency_id
        if currency_name is not UNSET:
            field_dict["currency_name"] = currency_name
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if currency_symbol is not UNSET:
            field_dict["currency_symbol"] = currency_symbol
        if currency_decimal_places is not UNSET:
            field_dict["currency_decimal_places"] = currency_decimal_places
        if primary_currency_id is not UNSET:
            field_dict["primary_currency_id"] = primary_currency_id
        if primary_currency_name is not UNSET:
            field_dict["primary_currency_name"] = primary_currency_name
        if primary_currency_code is not UNSET:
            field_dict["primary_currency_code"] = primary_currency_code
        if primary_currency_symbol is not UNSET:
            field_dict["primary_currency_symbol"] = primary_currency_symbol
        if primary_currency_decimal_places is not UNSET:
            field_dict["primary_currency_decimal_places"] = primary_currency_decimal_places
        if current_balance is not UNSET:
            field_dict["current_balance"] = current_balance
        if pc_current_balance is not UNSET:
            field_dict["pc_current_balance"] = pc_current_balance
        if balance_difference is not UNSET:
            field_dict["balance_difference"] = balance_difference
        if pc_balance_difference is not UNSET:
            field_dict["pc_balance_difference"] = pc_balance_difference
        if opening_balance is not UNSET:
            field_dict["opening_balance"] = opening_balance
        if pc_opening_balance is not UNSET:
            field_dict["pc_opening_balance"] = pc_opening_balance
        if virtual_balance is not UNSET:
            field_dict["virtual_balance"] = virtual_balance
        if pc_virtual_balance is not UNSET:
            field_dict["pc_virtual_balance"] = pc_virtual_balance
        if debt_amount is not UNSET:
            field_dict["debt_amount"] = debt_amount
        if pc_debt_amount is not UNSET:
            field_dict["pc_debt_amount"] = pc_debt_amount
        if current_balance_date is not UNSET:
            field_dict["current_balance_date"] = current_balance_date
        if notes is not UNSET:
            field_dict["notes"] = notes
        if monthly_payment_date is not UNSET:
            field_dict["monthly_payment_date"] = monthly_payment_date
        if credit_card_type is not UNSET:
            field_dict["credit_card_type"] = credit_card_type
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if iban is not UNSET:
            field_dict["iban"] = iban
        if bic is not UNSET:
            field_dict["bic"] = bic
        if opening_balance_date is not UNSET:
            field_dict["opening_balance_date"] = opening_balance_date
        if liability_type is not UNSET:
            field_dict["liability_type"] = liability_type
        if liability_direction is not UNSET:
            field_dict["liability_direction"] = liability_direction
        if interest is not UNSET:
            field_dict["interest"] = interest
        if interest_period is not UNSET:
            field_dict["interest_period"] = interest_period
        if include_net_worth is not UNSET:
            field_dict["include_net_worth"] = include_net_worth
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if zoom_level is not UNSET:
            field_dict["zoom_level"] = zoom_level
        if last_activity is not UNSET:
            field_dict["last_activity"] = last_activity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = ShortAccountTypeProperty(d.pop("type"))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        active = d.pop("active", UNSET)

        def _parse_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        order = _parse_order(d.pop("order", UNSET))

        def _parse_account_role(
            data: object,
        ) -> Union[AccountRolePropertyType1, AccountRolePropertyType2Type1, AccountRolePropertyType3Type1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_account_role_property_type_1 = AccountRolePropertyType1(data)

                return componentsschemas_account_role_property_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_account_role_property_type_2_type_1 = AccountRolePropertyType2Type1(data)

                return componentsschemas_account_role_property_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_account_role_property_type_3_type_1 = AccountRolePropertyType3Type1(data)

                return componentsschemas_account_role_property_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    AccountRolePropertyType1, AccountRolePropertyType2Type1, AccountRolePropertyType3Type1, None, Unset
                ],
                data,
            )

        account_role = _parse_account_role(d.pop("account_role", UNSET))

        def _parse_object_group_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        object_group_id = _parse_object_group_id(d.pop("object_group_id", UNSET))

        def _parse_object_group_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        object_group_order = _parse_object_group_order(d.pop("object_group_order", UNSET))

        def _parse_object_group_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        object_group_title = _parse_object_group_title(d.pop("object_group_title", UNSET))

        object_has_currency_setting = d.pop("object_has_currency_setting", UNSET)

        currency_id = d.pop("currency_id", UNSET)

        currency_name = d.pop("currency_name", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        currency_symbol = d.pop("currency_symbol", UNSET)

        currency_decimal_places = d.pop("currency_decimal_places", UNSET)

        primary_currency_id = d.pop("primary_currency_id", UNSET)

        primary_currency_name = d.pop("primary_currency_name", UNSET)

        primary_currency_code = d.pop("primary_currency_code", UNSET)

        primary_currency_symbol = d.pop("primary_currency_symbol", UNSET)

        primary_currency_decimal_places = d.pop("primary_currency_decimal_places", UNSET)

        current_balance = d.pop("current_balance", UNSET)

        def _parse_pc_current_balance(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pc_current_balance = _parse_pc_current_balance(d.pop("pc_current_balance", UNSET))

        balance_difference = d.pop("balance_difference", UNSET)

        def _parse_pc_balance_difference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pc_balance_difference = _parse_pc_balance_difference(d.pop("pc_balance_difference", UNSET))

        opening_balance = d.pop("opening_balance", UNSET)

        pc_opening_balance = d.pop("pc_opening_balance", UNSET)

        virtual_balance = d.pop("virtual_balance", UNSET)

        pc_virtual_balance = d.pop("pc_virtual_balance", UNSET)

        def _parse_debt_amount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        debt_amount = _parse_debt_amount(d.pop("debt_amount", UNSET))

        def _parse_pc_debt_amount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pc_debt_amount = _parse_pc_debt_amount(d.pop("pc_debt_amount", UNSET))

        _current_balance_date = d.pop("current_balance_date", UNSET)
        current_balance_date: Union[Unset, datetime.datetime]
        if isinstance(_current_balance_date, Unset):
            current_balance_date = UNSET
        else:
            current_balance_date = isoparse(_current_balance_date)

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_monthly_payment_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                monthly_payment_date_type_0 = isoparse(data)

                return monthly_payment_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        monthly_payment_date = _parse_monthly_payment_date(d.pop("monthly_payment_date", UNSET))

        def _parse_credit_card_type(
            data: object,
        ) -> Union[
            CreditCardTypePropertyType1, CreditCardTypePropertyType2Type1, CreditCardTypePropertyType3Type1, None, Unset
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_credit_card_type_property_type_1 = CreditCardTypePropertyType1(data)

                return componentsschemas_credit_card_type_property_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_credit_card_type_property_type_2_type_1 = CreditCardTypePropertyType2Type1(data)

                return componentsschemas_credit_card_type_property_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_credit_card_type_property_type_3_type_1 = CreditCardTypePropertyType3Type1(data)

                return componentsschemas_credit_card_type_property_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    CreditCardTypePropertyType1,
                    CreditCardTypePropertyType2Type1,
                    CreditCardTypePropertyType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        credit_card_type = _parse_credit_card_type(d.pop("credit_card_type", UNSET))

        def _parse_account_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        account_number = _parse_account_number(d.pop("account_number", UNSET))

        def _parse_iban(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        iban = _parse_iban(d.pop("iban", UNSET))

        def _parse_bic(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bic = _parse_bic(d.pop("bic", UNSET))

        def _parse_opening_balance_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opening_balance_date_type_0 = isoparse(data)

                return opening_balance_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        opening_balance_date = _parse_opening_balance_date(d.pop("opening_balance_date", UNSET))

        def _parse_liability_type(
            data: object,
        ) -> Union[
            LiabilityTypePropertyType1, LiabilityTypePropertyType2Type1, LiabilityTypePropertyType3Type1, None, Unset
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_liability_type_property_type_1 = LiabilityTypePropertyType1(data)

                return componentsschemas_liability_type_property_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_liability_type_property_type_2_type_1 = LiabilityTypePropertyType2Type1(data)

                return componentsschemas_liability_type_property_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_liability_type_property_type_3_type_1 = LiabilityTypePropertyType3Type1(data)

                return componentsschemas_liability_type_property_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    LiabilityTypePropertyType1,
                    LiabilityTypePropertyType2Type1,
                    LiabilityTypePropertyType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        liability_type = _parse_liability_type(d.pop("liability_type", UNSET))

        def _parse_liability_direction(
            data: object,
        ) -> Union[
            LiabilityDirectionPropertyType1,
            LiabilityDirectionPropertyType2Type1,
            LiabilityDirectionPropertyType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_liability_direction_property_type_1 = LiabilityDirectionPropertyType1(data)

                return componentsschemas_liability_direction_property_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_liability_direction_property_type_2_type_1 = LiabilityDirectionPropertyType2Type1(
                    data
                )

                return componentsschemas_liability_direction_property_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_liability_direction_property_type_3_type_1 = LiabilityDirectionPropertyType3Type1(
                    data
                )

                return componentsschemas_liability_direction_property_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    LiabilityDirectionPropertyType1,
                    LiabilityDirectionPropertyType2Type1,
                    LiabilityDirectionPropertyType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        liability_direction = _parse_liability_direction(d.pop("liability_direction", UNSET))

        def _parse_interest(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        interest = _parse_interest(d.pop("interest", UNSET))

        def _parse_interest_period(
            data: object,
        ) -> Union[
            InterestPeriodPropertyType1, InterestPeriodPropertyType2Type1, InterestPeriodPropertyType3Type1, None, Unset
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_interest_period_property_type_1 = InterestPeriodPropertyType1(data)

                return componentsschemas_interest_period_property_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_interest_period_property_type_2_type_1 = InterestPeriodPropertyType2Type1(data)

                return componentsschemas_interest_period_property_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_interest_period_property_type_3_type_1 = InterestPeriodPropertyType3Type1(data)

                return componentsschemas_interest_period_property_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    InterestPeriodPropertyType1,
                    InterestPeriodPropertyType2Type1,
                    InterestPeriodPropertyType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        interest_period = _parse_interest_period(d.pop("interest_period", UNSET))

        include_net_worth = d.pop("include_net_worth", UNSET)

        def _parse_longitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_latitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_zoom_level(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        zoom_level = _parse_zoom_level(d.pop("zoom_level", UNSET))

        def _parse_last_activity(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_type_0 = isoparse(data)

                return last_activity_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_activity = _parse_last_activity(d.pop("last_activity", UNSET))

        account_properties = cls(
            name=name,
            type_=type_,
            created_at=created_at,
            updated_at=updated_at,
            active=active,
            order=order,
            account_role=account_role,
            object_group_id=object_group_id,
            object_group_order=object_group_order,
            object_group_title=object_group_title,
            object_has_currency_setting=object_has_currency_setting,
            currency_id=currency_id,
            currency_name=currency_name,
            currency_code=currency_code,
            currency_symbol=currency_symbol,
            currency_decimal_places=currency_decimal_places,
            primary_currency_id=primary_currency_id,
            primary_currency_name=primary_currency_name,
            primary_currency_code=primary_currency_code,
            primary_currency_symbol=primary_currency_symbol,
            primary_currency_decimal_places=primary_currency_decimal_places,
            current_balance=current_balance,
            pc_current_balance=pc_current_balance,
            balance_difference=balance_difference,
            pc_balance_difference=pc_balance_difference,
            opening_balance=opening_balance,
            pc_opening_balance=pc_opening_balance,
            virtual_balance=virtual_balance,
            pc_virtual_balance=pc_virtual_balance,
            debt_amount=debt_amount,
            pc_debt_amount=pc_debt_amount,
            current_balance_date=current_balance_date,
            notes=notes,
            monthly_payment_date=monthly_payment_date,
            credit_card_type=credit_card_type,
            account_number=account_number,
            iban=iban,
            bic=bic,
            opening_balance_date=opening_balance_date,
            liability_type=liability_type,
            liability_direction=liability_direction,
            interest=interest,
            interest_period=interest_period,
            include_net_worth=include_net_worth,
            longitude=longitude,
            latitude=latitude,
            zoom_level=zoom_level,
            last_activity=last_activity,
        )

        account_properties.additional_properties = d
        return account_properties

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
