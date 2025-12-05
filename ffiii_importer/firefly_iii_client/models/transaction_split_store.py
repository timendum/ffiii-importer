import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.transaction_type_property import TransactionTypeProperty
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionSplitStore")


@_attrs_define
class TransactionSplitStore:
    """
    Attributes:
        type_ (TransactionTypeProperty):  Example: withdrawal.
        date (datetime.datetime): Date of the transaction Example: 2025-10-01T00:00:00+00:00.
        amount (str): Amount of the transaction. Example: 123.45.
        description (str): Description of the transaction. Example: Vegetables.
        order (Union[None, Unset, int]): Order of this entry in the list of transactions.
        currency_id (Union[None, Unset, str]): Currency ID. Default is the source account's currency, or the user's
            financial administration's currency. The value you submit may be overruled by the source or destination account.
            Example: 12.
        currency_code (Union[None, Unset, str]): Currency code. Default is the source account's currency, or the user's
            financial administration's primary currency. The value you submit may be overruled by the source or destination
            account. Example: EUR.
        foreign_amount (Union[None, Unset, str]): The amount in a foreign currency. Example: 123.45.
        foreign_currency_id (Union[None, Unset, str]): Currency ID of the foreign currency. Default is null. Is required
            when you submit a foreign amount. Example: 17.
        foreign_currency_code (Union[None, Unset, str]): Currency code of the foreign currency. Default is NULL. Can be
            used instead of the foreign_currency_id, but this or the ID is required when submitting a foreign amount.
            Example: USD.
        budget_id (Union[None, Unset, str]): The budget ID for this transaction. Example: 4.
        budget_name (Union[None, Unset, str]): The name of the budget to be used. If the budget name is unknown, the ID
            will be used or the value will be ignored. Example: Groceries.
        category_id (Union[None, Unset, str]): The category ID for this transaction. Example: 43.
        category_name (Union[None, Unset, str]): The name of the category to be used. If the category is unknown, it
            will be created. If the ID and the name point to different categories, the ID overrules the name. Example:
            Groceries.
        source_id (Union[None, Unset, str]): ID of the source account. For a withdrawal or a transfer, this must always
            be an asset account. For deposits, this must be a revenue account. Example: 2.
        source_name (Union[None, Unset, str]): Name of the source account. For a withdrawal or a transfer, this must
            always be an asset account. For deposits, this must be a revenue account. Can be used instead of the source_id.
            If the transaction is a deposit, the source_name can be filled in freely: the account will be created based on
            the name. Example: Checking account.
        destination_id (Union[None, Unset, str]): ID of the destination account. For a deposit or a transfer, this must
            always be an asset account. For withdrawals this must be an expense account. Example: 2.
        destination_name (Union[None, Unset, str]): Name of the destination account. You can submit the name instead of
            the ID. For everything except transfers, the account will be auto-generated if unknown, so submitting a name is
            enough. Example: Buy and Large.
        reconciled (Union[Unset, bool]): If the transaction has been reconciled already. When you set this, the amount
            can no longer be edited by the user.
        piggy_bank_id (Union[None, Unset, int]): Optional. Use either this or the piggy_bank_name
        piggy_bank_name (Union[None, Unset, str]): Optional. Use either this or the piggy_bank_id
        bill_id (Union[None, Unset, str]): Optional. Use either this or the bill_name Example: 112.
        bill_name (Union[None, Unset, str]): Optional. Use either this or the bill_id Example: Monthly rent.
        tags (Union[None, Unset, list[str]]): Array of tags.
        notes (Union[None, Unset, str]):  Example: Some example notes.
        internal_reference (Union[None, Unset, str]): Reference to internal reference of other systems.
        external_id (Union[None, Unset, str]): Reference to external ID in other systems.
        external_url (Union[None, Unset, str]): External, custom URL for this transaction.
        sepa_cc (Union[None, Unset, str]): SEPA Clearing Code
        sepa_ct_op (Union[None, Unset, str]): SEPA Opposing Account Identifier
        sepa_ct_id (Union[None, Unset, str]): SEPA end-to-end Identifier
        sepa_db (Union[None, Unset, str]): SEPA mandate identifier
        sepa_country (Union[None, Unset, str]): SEPA Country
        sepa_ep (Union[None, Unset, str]): SEPA External Purpose indicator
        sepa_ci (Union[None, Unset, str]): SEPA Creditor Identifier
        sepa_batch_id (Union[None, Unset, str]): SEPA Batch ID
        interest_date (Union[None, Unset, datetime.datetime]):
        book_date (Union[None, Unset, datetime.datetime]):
        process_date (Union[None, Unset, datetime.datetime]):
        due_date (Union[None, Unset, datetime.datetime]):
        payment_date (Union[None, Unset, datetime.datetime]):
        invoice_date (Union[None, Unset, datetime.datetime]):
    """

    type_: TransactionTypeProperty
    date: datetime.datetime
    amount: str
    description: str
    order: Union[None, Unset, int] = UNSET
    currency_id: Union[None, Unset, str] = UNSET
    currency_code: Union[None, Unset, str] = UNSET
    foreign_amount: Union[None, Unset, str] = UNSET
    foreign_currency_id: Union[None, Unset, str] = UNSET
    foreign_currency_code: Union[None, Unset, str] = UNSET
    budget_id: Union[None, Unset, str] = UNSET
    budget_name: Union[None, Unset, str] = UNSET
    category_id: Union[None, Unset, str] = UNSET
    category_name: Union[None, Unset, str] = UNSET
    source_id: Union[None, Unset, str] = UNSET
    source_name: Union[None, Unset, str] = UNSET
    destination_id: Union[None, Unset, str] = UNSET
    destination_name: Union[None, Unset, str] = UNSET
    reconciled: Union[Unset, bool] = UNSET
    piggy_bank_id: Union[None, Unset, int] = UNSET
    piggy_bank_name: Union[None, Unset, str] = UNSET
    bill_id: Union[None, Unset, str] = UNSET
    bill_name: Union[None, Unset, str] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    notes: Union[None, Unset, str] = UNSET
    internal_reference: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    external_url: Union[None, Unset, str] = UNSET
    sepa_cc: Union[None, Unset, str] = UNSET
    sepa_ct_op: Union[None, Unset, str] = UNSET
    sepa_ct_id: Union[None, Unset, str] = UNSET
    sepa_db: Union[None, Unset, str] = UNSET
    sepa_country: Union[None, Unset, str] = UNSET
    sepa_ep: Union[None, Unset, str] = UNSET
    sepa_ci: Union[None, Unset, str] = UNSET
    sepa_batch_id: Union[None, Unset, str] = UNSET
    interest_date: Union[None, Unset, datetime.datetime] = UNSET
    book_date: Union[None, Unset, datetime.datetime] = UNSET
    process_date: Union[None, Unset, datetime.datetime] = UNSET
    due_date: Union[None, Unset, datetime.datetime] = UNSET
    payment_date: Union[None, Unset, datetime.datetime] = UNSET
    invoice_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        date = self.date.isoformat()

        amount = self.amount

        description = self.description

        order: Union[None, Unset, int]
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order

        currency_id: Union[None, Unset, str]
        if isinstance(self.currency_id, Unset):
            currency_id = UNSET
        else:
            currency_id = self.currency_id

        currency_code: Union[None, Unset, str]
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        foreign_amount: Union[None, Unset, str]
        if isinstance(self.foreign_amount, Unset):
            foreign_amount = UNSET
        else:
            foreign_amount = self.foreign_amount

        foreign_currency_id: Union[None, Unset, str]
        if isinstance(self.foreign_currency_id, Unset):
            foreign_currency_id = UNSET
        else:
            foreign_currency_id = self.foreign_currency_id

        foreign_currency_code: Union[None, Unset, str]
        if isinstance(self.foreign_currency_code, Unset):
            foreign_currency_code = UNSET
        else:
            foreign_currency_code = self.foreign_currency_code

        budget_id: Union[None, Unset, str]
        if isinstance(self.budget_id, Unset):
            budget_id = UNSET
        else:
            budget_id = self.budget_id

        budget_name: Union[None, Unset, str]
        if isinstance(self.budget_name, Unset):
            budget_name = UNSET
        else:
            budget_name = self.budget_name

        category_id: Union[None, Unset, str]
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        category_name: Union[None, Unset, str]
        if isinstance(self.category_name, Unset):
            category_name = UNSET
        else:
            category_name = self.category_name

        source_id: Union[None, Unset, str]
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        else:
            source_id = self.source_id

        source_name: Union[None, Unset, str]
        if isinstance(self.source_name, Unset):
            source_name = UNSET
        else:
            source_name = self.source_name

        destination_id: Union[None, Unset, str]
        if isinstance(self.destination_id, Unset):
            destination_id = UNSET
        else:
            destination_id = self.destination_id

        destination_name: Union[None, Unset, str]
        if isinstance(self.destination_name, Unset):
            destination_name = UNSET
        else:
            destination_name = self.destination_name

        reconciled = self.reconciled

        piggy_bank_id: Union[None, Unset, int]
        if isinstance(self.piggy_bank_id, Unset):
            piggy_bank_id = UNSET
        else:
            piggy_bank_id = self.piggy_bank_id

        piggy_bank_name: Union[None, Unset, str]
        if isinstance(self.piggy_bank_name, Unset):
            piggy_bank_name = UNSET
        else:
            piggy_bank_name = self.piggy_bank_name

        bill_id: Union[None, Unset, str]
        if isinstance(self.bill_id, Unset):
            bill_id = UNSET
        else:
            bill_id = self.bill_id

        bill_name: Union[None, Unset, str]
        if isinstance(self.bill_name, Unset):
            bill_name = UNSET
        else:
            bill_name = self.bill_name

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        internal_reference: Union[None, Unset, str]
        if isinstance(self.internal_reference, Unset):
            internal_reference = UNSET
        else:
            internal_reference = self.internal_reference

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        external_url: Union[None, Unset, str]
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        sepa_cc: Union[None, Unset, str]
        if isinstance(self.sepa_cc, Unset):
            sepa_cc = UNSET
        else:
            sepa_cc = self.sepa_cc

        sepa_ct_op: Union[None, Unset, str]
        if isinstance(self.sepa_ct_op, Unset):
            sepa_ct_op = UNSET
        else:
            sepa_ct_op = self.sepa_ct_op

        sepa_ct_id: Union[None, Unset, str]
        if isinstance(self.sepa_ct_id, Unset):
            sepa_ct_id = UNSET
        else:
            sepa_ct_id = self.sepa_ct_id

        sepa_db: Union[None, Unset, str]
        if isinstance(self.sepa_db, Unset):
            sepa_db = UNSET
        else:
            sepa_db = self.sepa_db

        sepa_country: Union[None, Unset, str]
        if isinstance(self.sepa_country, Unset):
            sepa_country = UNSET
        else:
            sepa_country = self.sepa_country

        sepa_ep: Union[None, Unset, str]
        if isinstance(self.sepa_ep, Unset):
            sepa_ep = UNSET
        else:
            sepa_ep = self.sepa_ep

        sepa_ci: Union[None, Unset, str]
        if isinstance(self.sepa_ci, Unset):
            sepa_ci = UNSET
        else:
            sepa_ci = self.sepa_ci

        sepa_batch_id: Union[None, Unset, str]
        if isinstance(self.sepa_batch_id, Unset):
            sepa_batch_id = UNSET
        else:
            sepa_batch_id = self.sepa_batch_id

        interest_date: Union[None, Unset, str]
        if isinstance(self.interest_date, Unset):
            interest_date = UNSET
        elif isinstance(self.interest_date, datetime.datetime):
            interest_date = self.interest_date.isoformat()
        else:
            interest_date = self.interest_date

        book_date: Union[None, Unset, str]
        if isinstance(self.book_date, Unset):
            book_date = UNSET
        elif isinstance(self.book_date, datetime.datetime):
            book_date = self.book_date.isoformat()
        else:
            book_date = self.book_date

        process_date: Union[None, Unset, str]
        if isinstance(self.process_date, Unset):
            process_date = UNSET
        elif isinstance(self.process_date, datetime.datetime):
            process_date = self.process_date.isoformat()
        else:
            process_date = self.process_date

        due_date: Union[None, Unset, str]
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.datetime):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        payment_date: Union[None, Unset, str]
        if isinstance(self.payment_date, Unset):
            payment_date = UNSET
        elif isinstance(self.payment_date, datetime.datetime):
            payment_date = self.payment_date.isoformat()
        else:
            payment_date = self.payment_date

        invoice_date: Union[None, Unset, str]
        if isinstance(self.invoice_date, Unset):
            invoice_date = UNSET
        elif isinstance(self.invoice_date, datetime.datetime):
            invoice_date = self.invoice_date.isoformat()
        else:
            invoice_date = self.invoice_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "date": date,
                "amount": amount,
                "description": description,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if currency_id is not UNSET:
            field_dict["currency_id"] = currency_id
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if foreign_amount is not UNSET:
            field_dict["foreign_amount"] = foreign_amount
        if foreign_currency_id is not UNSET:
            field_dict["foreign_currency_id"] = foreign_currency_id
        if foreign_currency_code is not UNSET:
            field_dict["foreign_currency_code"] = foreign_currency_code
        if budget_id is not UNSET:
            field_dict["budget_id"] = budget_id
        if budget_name is not UNSET:
            field_dict["budget_name"] = budget_name
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if source_name is not UNSET:
            field_dict["source_name"] = source_name
        if destination_id is not UNSET:
            field_dict["destination_id"] = destination_id
        if destination_name is not UNSET:
            field_dict["destination_name"] = destination_name
        if reconciled is not UNSET:
            field_dict["reconciled"] = reconciled
        if piggy_bank_id is not UNSET:
            field_dict["piggy_bank_id"] = piggy_bank_id
        if piggy_bank_name is not UNSET:
            field_dict["piggy_bank_name"] = piggy_bank_name
        if bill_id is not UNSET:
            field_dict["bill_id"] = bill_id
        if bill_name is not UNSET:
            field_dict["bill_name"] = bill_name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if notes is not UNSET:
            field_dict["notes"] = notes
        if internal_reference is not UNSET:
            field_dict["internal_reference"] = internal_reference
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if sepa_cc is not UNSET:
            field_dict["sepa_cc"] = sepa_cc
        if sepa_ct_op is not UNSET:
            field_dict["sepa_ct_op"] = sepa_ct_op
        if sepa_ct_id is not UNSET:
            field_dict["sepa_ct_id"] = sepa_ct_id
        if sepa_db is not UNSET:
            field_dict["sepa_db"] = sepa_db
        if sepa_country is not UNSET:
            field_dict["sepa_country"] = sepa_country
        if sepa_ep is not UNSET:
            field_dict["sepa_ep"] = sepa_ep
        if sepa_ci is not UNSET:
            field_dict["sepa_ci"] = sepa_ci
        if sepa_batch_id is not UNSET:
            field_dict["sepa_batch_id"] = sepa_batch_id
        if interest_date is not UNSET:
            field_dict["interest_date"] = interest_date
        if book_date is not UNSET:
            field_dict["book_date"] = book_date
        if process_date is not UNSET:
            field_dict["process_date"] = process_date
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if payment_date is not UNSET:
            field_dict["payment_date"] = payment_date
        if invoice_date is not UNSET:
            field_dict["invoice_date"] = invoice_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = TransactionTypeProperty(d.pop("type"))

        date = isoparse(d.pop("date"))

        amount = d.pop("amount")

        description = d.pop("description")

        def _parse_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        order = _parse_order(d.pop("order", UNSET))

        def _parse_currency_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        currency_id = _parse_currency_id(d.pop("currency_id", UNSET))

        def _parse_currency_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        currency_code = _parse_currency_code(d.pop("currency_code", UNSET))

        def _parse_foreign_amount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        foreign_amount = _parse_foreign_amount(d.pop("foreign_amount", UNSET))

        def _parse_foreign_currency_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        foreign_currency_id = _parse_foreign_currency_id(d.pop("foreign_currency_id", UNSET))

        def _parse_foreign_currency_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        foreign_currency_code = _parse_foreign_currency_code(d.pop("foreign_currency_code", UNSET))

        def _parse_budget_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        budget_id = _parse_budget_id(d.pop("budget_id", UNSET))

        def _parse_budget_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        budget_name = _parse_budget_name(d.pop("budget_name", UNSET))

        def _parse_category_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category_id = _parse_category_id(d.pop("category_id", UNSET))

        def _parse_category_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category_name = _parse_category_name(d.pop("category_name", UNSET))

        def _parse_source_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_id = _parse_source_id(d.pop("source_id", UNSET))

        def _parse_source_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_name = _parse_source_name(d.pop("source_name", UNSET))

        def _parse_destination_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        destination_id = _parse_destination_id(d.pop("destination_id", UNSET))

        def _parse_destination_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        destination_name = _parse_destination_name(d.pop("destination_name", UNSET))

        reconciled = d.pop("reconciled", UNSET)

        def _parse_piggy_bank_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        piggy_bank_id = _parse_piggy_bank_id(d.pop("piggy_bank_id", UNSET))

        def _parse_piggy_bank_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        piggy_bank_name = _parse_piggy_bank_name(d.pop("piggy_bank_name", UNSET))

        def _parse_bill_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bill_id = _parse_bill_id(d.pop("bill_id", UNSET))

        def _parse_bill_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bill_name = _parse_bill_name(d.pop("bill_name", UNSET))

        def _parse_tags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_internal_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        internal_reference = _parse_internal_reference(d.pop("internal_reference", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_external_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        def _parse_sepa_cc(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sepa_cc = _parse_sepa_cc(d.pop("sepa_cc", UNSET))

        def _parse_sepa_ct_op(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sepa_ct_op = _parse_sepa_ct_op(d.pop("sepa_ct_op", UNSET))

        def _parse_sepa_ct_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sepa_ct_id = _parse_sepa_ct_id(d.pop("sepa_ct_id", UNSET))

        def _parse_sepa_db(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sepa_db = _parse_sepa_db(d.pop("sepa_db", UNSET))

        def _parse_sepa_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sepa_country = _parse_sepa_country(d.pop("sepa_country", UNSET))

        def _parse_sepa_ep(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sepa_ep = _parse_sepa_ep(d.pop("sepa_ep", UNSET))

        def _parse_sepa_ci(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sepa_ci = _parse_sepa_ci(d.pop("sepa_ci", UNSET))

        def _parse_sepa_batch_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sepa_batch_id = _parse_sepa_batch_id(d.pop("sepa_batch_id", UNSET))

        def _parse_interest_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                interest_date_type_0 = isoparse(data)

                return interest_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        interest_date = _parse_interest_date(d.pop("interest_date", UNSET))

        def _parse_book_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                book_date_type_0 = isoparse(data)

                return book_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        book_date = _parse_book_date(d.pop("book_date", UNSET))

        def _parse_process_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                process_date_type_0 = isoparse(data)

                return process_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        process_date = _parse_process_date(d.pop("process_date", UNSET))

        def _parse_due_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = isoparse(data)

                return due_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        def _parse_payment_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_date_type_0 = isoparse(data)

                return payment_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        payment_date = _parse_payment_date(d.pop("payment_date", UNSET))

        def _parse_invoice_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invoice_date_type_0 = isoparse(data)

                return invoice_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        invoice_date = _parse_invoice_date(d.pop("invoice_date", UNSET))

        transaction_split_store = cls(
            type_=type_,
            date=date,
            amount=amount,
            description=description,
            order=order,
            currency_id=currency_id,
            currency_code=currency_code,
            foreign_amount=foreign_amount,
            foreign_currency_id=foreign_currency_id,
            foreign_currency_code=foreign_currency_code,
            budget_id=budget_id,
            budget_name=budget_name,
            category_id=category_id,
            category_name=category_name,
            source_id=source_id,
            source_name=source_name,
            destination_id=destination_id,
            destination_name=destination_name,
            reconciled=reconciled,
            piggy_bank_id=piggy_bank_id,
            piggy_bank_name=piggy_bank_name,
            bill_id=bill_id,
            bill_name=bill_name,
            tags=tags,
            notes=notes,
            internal_reference=internal_reference,
            external_id=external_id,
            external_url=external_url,
            sepa_cc=sepa_cc,
            sepa_ct_op=sepa_ct_op,
            sepa_ct_id=sepa_ct_id,
            sepa_db=sepa_db,
            sepa_country=sepa_country,
            sepa_ep=sepa_ep,
            sepa_ci=sepa_ci,
            sepa_batch_id=sepa_batch_id,
            interest_date=interest_date,
            book_date=book_date,
            process_date=process_date,
            due_date=due_date,
            payment_date=payment_date,
            invoice_date=invoice_date,
        )

        transaction_split_store.additional_properties = d
        return transaction_split_store

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
