import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.account_type_property import AccountTypeProperty
from ..models.transaction_type_property import TransactionTypeProperty
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionSplit")


@_attrs_define
class TransactionSplit:
    """
    Attributes:
        type_ (TransactionTypeProperty):  Example: withdrawal.
        date (datetime.datetime): Date of the transaction Example: 2025-10-01T00:00:00+00:00.
        amount (str): Amount of the transaction. Example: 123.45.
        description (str): Description of the transaction. Example: Vegetables.
        source_id (Union[None, str]): ID of the source account. For a withdrawal or a transfer, this must always be an
            asset account. For deposits, this must be a revenue account. Example: 2.
        destination_id (Union[None, str]): ID of the destination account. For a deposit or a transfer, this must always
            be an asset account. For withdrawals this must be an expense account. Example: 2.
        user (Union[Unset, str]): User ID Example: 3.
        transaction_journal_id (Union[Unset, str]): ID of the underlying transaction journal. Each transaction consists
            of a transaction group (see the top ID) and one or more journals
            making up the splits of the transaction.
             Example: 10421.
        order (Union[None, Unset, int]): Order of this entry in the list of transactions.
        object_has_currency_setting (Union[Unset, bool]): Indicates whether the transaction has a currency setting. For
            transactions this is always true. Example: True.
        currency_id (Union[Unset, str]): Currency ID for the currency of this transaction. Example: 12.
        currency_code (Union[Unset, str]): Currency code for the currency of this transaction. Example: EUR.
        currency_symbol (Union[Unset, str]): Currency symbol for the currency of this transaction. Example: $.
        currency_name (Union[Unset, str]): Currency name for the currency of this transaction. Example: Euro.
        currency_decimal_places (Union[Unset, int]): Number of decimals used in this currency. Example: 2.
        foreign_currency_id (Union[None, Unset, str]): Currency ID of the foreign currency, if this transaction has a
            foreign amount. Example: 17.
        foreign_currency_code (Union[None, Unset, str]): Currency code of the foreign currency. Default is NULL.
            Example: USD.
        foreign_currency_symbol (Union[None, Unset, str]):  Example: $.
        foreign_currency_decimal_places (Union[None, Unset, int]): Number of decimals in the foreign currency. Example:
            2.
        primary_currency_id (Union[None, Unset, str]): Returns the primary currency ID of the administration. This
            currency is used as the currency for all `pc_*` amount and balance fields of this account. Example: 12.
        primary_currency_code (Union[None, Unset, str]): Returns the primary currency code of the administration. This
            currency is used as the currency for all `pc_*` amount and balance fields of this account. Example: EUR.
        primary_currency_symbol (Union[None, Unset, str]): See the other `primary_*` fields. Example: $.
        primary_currency_decimal_places (Union[None, Unset, int]): See the other `primary_*` fields. Example: 2.
        pc_amount (Union[Unset, str]): Amount of the transaction in the primary currency of this administration. The
            `primary_currency_*` fields reflect the currency used. This field is NULL if the user does have 'convert to
            primary' set to true in their settings. Example: 123.45.
        foreign_amount (Union[None, Unset, str]): The amount in the set foreign currency. May be NULL if the transaction
            does not have a foreign amount. Example: 123.45.
        pc_foreign_amount (Union[Unset, str]): Foreign amount of the transaction in the primary currency of this
            administration. The `primary_currency_*` fields reflect the currency used. This field is NULL if the user does
            have 'convert to primary' set to true in their settings. Example: 123.45.
        source_balance_after (Union[None, Unset, str]): The balance of the source account. This is the balance in the
            account's currency which may be different from this transaction, and is not provided in this model. Example:
            123.45.
        pc_source_balance_after (Union[None, Unset, str]): The balance of the source account in the primary currency of
            this administration. The `primary_currency_*` fields reflect the currency used. This field is NULL if the user
            does have 'convert to primary' set to true in their settings. Example: 123.45.
        destination_balance_after (Union[None, Unset, str]): The balance of the destination account. This is the balance
            in the account's currency which may be different from this transaction, and is not provided in this model.
            Example: 123.45.
        pc_destination_balance_after (Union[None, Unset, str]): The balance of the destination account in the primary
            currency of this administration. The `primary_currency_*` fields reflect the currency used. This field is NULL
            if the user does have 'convert to primary' set to true in their settings. Example: 123.45.
        source_name (Union[None, Unset, str]): Name of the source account. For a withdrawal or a transfer, this must
            always be an asset account. For deposits, this must be a revenue account. Can be used instead of the source_id.
            If the transaction is a deposit, the source_name can be filled in freely: the account will be created based on
            the name. Example: Checking account.
        source_iban (Union[None, Unset, str]):  Example: NL02ABNA0123456789.
        source_type (Union[Unset, AccountTypeProperty]):  Example: Asset account.
        destination_name (Union[None, Unset, str]): Name of the destination account. You can submit the name instead of
            the ID. For everything except transfers, the account will be auto-generated if unknown, so submitting a name is
            enough. Example: Buy and Large.
        destination_iban (Union[None, Unset, str]):  Example: NL02ABNA0123456789.
        destination_type (Union[Unset, AccountTypeProperty]):  Example: Asset account.
        budget_id (Union[None, Unset, str]): The budget ID for this transaction. Example: 4.
        budget_name (Union[None, Unset, str]): The name of the budget used. Example: Groceries.
        category_id (Union[None, Unset, str]): The category ID for this transaction. Example: 43.
        category_name (Union[None, Unset, str]): The name of the category to be used. If the category is unknown, it
            will be created. If the ID and the name point to different categories, the ID overrules the name. Example:
            Groceries.
        bill_id (Union[None, Unset, str]): The associated subscription ID for this transaction. `bill` refers to the OLD
            name for subscriptions and this field will be removed. Example: 111.
        bill_name (Union[None, Unset, str]): The associated subscription name for this transaction. `bill` refers to the
            OLD name for subscriptions and this field will be removed. Example: Monthly rent.
        subscription_id (Union[None, Unset, str]): The associated subscription ID for this transaction. Example: 111.
        subscription_name (Union[None, Unset, str]): The associated subscription name for this transaction. Example:
            Monthly rent.
        reconciled (Union[Unset, bool]): If the transaction has been reconciled already. When you set this, the amount
            can no longer be edited by the user.
        notes (Union[None, Unset, str]):  Example: Some example notes.
        tags (Union[None, Unset, list[str]]): Array of tags.
        internal_reference (Union[None, Unset, str]): Reference to internal reference of other systems.
        external_id (Union[None, Unset, str]): Reference to external ID in other systems.
        external_url (Union[None, Unset, str]): External, custom URL for this transaction.
        original_source (Union[None, Unset, str]): System generated identifier for original creator of transaction.
        recurrence_id (Union[None, Unset, str]): Reference to recurrence that made the transaction.
        recurrence_total (Union[None, Unset, int]): Total number of transactions expected to be created by this
            recurrence repetition. Will be 0 if infinite.
        recurrence_count (Union[None, Unset, int]): The # of the current transaction created under this recurrence.
            Example: 12.
        import_hash_v2 (Union[None, Unset, str]): Hash value of original import transaction (for duplicate detection).
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
        latitude (Union[None, Unset, float]): Latitude of the transaction's location, if applicable. Can be used to draw
            a map. Example: 51.983333.
        longitude (Union[None, Unset, float]): Latitude of the transaction's location, if applicable. Can be used to
            draw a map. Example: 5.916667.
        zoom_level (Union[None, Unset, int]): Zoom level for the map, if drawn. This to set the box right. Unfortunately
            this is a proprietary value because each map provider has different zoom levels. Example: 6.
        has_attachments (Union[Unset, bool]): If the transaction has attachments.
    """

    type_: TransactionTypeProperty
    date: datetime.datetime
    amount: str
    description: str
    source_id: Union[None, str]
    destination_id: Union[None, str]
    user: Union[Unset, str] = UNSET
    transaction_journal_id: Union[Unset, str] = UNSET
    order: Union[None, Unset, int] = UNSET
    object_has_currency_setting: Union[Unset, bool] = UNSET
    currency_id: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    currency_symbol: Union[Unset, str] = UNSET
    currency_name: Union[Unset, str] = UNSET
    currency_decimal_places: Union[Unset, int] = UNSET
    foreign_currency_id: Union[None, Unset, str] = UNSET
    foreign_currency_code: Union[None, Unset, str] = UNSET
    foreign_currency_symbol: Union[None, Unset, str] = UNSET
    foreign_currency_decimal_places: Union[None, Unset, int] = UNSET
    primary_currency_id: Union[None, Unset, str] = UNSET
    primary_currency_code: Union[None, Unset, str] = UNSET
    primary_currency_symbol: Union[None, Unset, str] = UNSET
    primary_currency_decimal_places: Union[None, Unset, int] = UNSET
    pc_amount: Union[Unset, str] = UNSET
    foreign_amount: Union[None, Unset, str] = UNSET
    pc_foreign_amount: Union[Unset, str] = UNSET
    source_balance_after: Union[None, Unset, str] = UNSET
    pc_source_balance_after: Union[None, Unset, str] = UNSET
    destination_balance_after: Union[None, Unset, str] = UNSET
    pc_destination_balance_after: Union[None, Unset, str] = UNSET
    source_name: Union[None, Unset, str] = UNSET
    source_iban: Union[None, Unset, str] = UNSET
    source_type: Union[Unset, AccountTypeProperty] = UNSET
    destination_name: Union[None, Unset, str] = UNSET
    destination_iban: Union[None, Unset, str] = UNSET
    destination_type: Union[Unset, AccountTypeProperty] = UNSET
    budget_id: Union[None, Unset, str] = UNSET
    budget_name: Union[None, Unset, str] = UNSET
    category_id: Union[None, Unset, str] = UNSET
    category_name: Union[None, Unset, str] = UNSET
    bill_id: Union[None, Unset, str] = UNSET
    bill_name: Union[None, Unset, str] = UNSET
    subscription_id: Union[None, Unset, str] = UNSET
    subscription_name: Union[None, Unset, str] = UNSET
    reconciled: Union[Unset, bool] = UNSET
    notes: Union[None, Unset, str] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    internal_reference: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    external_url: Union[None, Unset, str] = UNSET
    original_source: Union[None, Unset, str] = UNSET
    recurrence_id: Union[None, Unset, str] = UNSET
    recurrence_total: Union[None, Unset, int] = UNSET
    recurrence_count: Union[None, Unset, int] = UNSET
    import_hash_v2: Union[None, Unset, str] = UNSET
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
    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    zoom_level: Union[None, Unset, int] = UNSET
    has_attachments: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        date = self.date.isoformat()

        amount = self.amount

        description = self.description

        source_id: Union[None, str]
        source_id = self.source_id

        destination_id: Union[None, str]
        destination_id = self.destination_id

        user = self.user

        transaction_journal_id = self.transaction_journal_id

        order: Union[None, Unset, int]
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order

        object_has_currency_setting = self.object_has_currency_setting

        currency_id = self.currency_id

        currency_code = self.currency_code

        currency_symbol = self.currency_symbol

        currency_name = self.currency_name

        currency_decimal_places = self.currency_decimal_places

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

        foreign_currency_symbol: Union[None, Unset, str]
        if isinstance(self.foreign_currency_symbol, Unset):
            foreign_currency_symbol = UNSET
        else:
            foreign_currency_symbol = self.foreign_currency_symbol

        foreign_currency_decimal_places: Union[None, Unset, int]
        if isinstance(self.foreign_currency_decimal_places, Unset):
            foreign_currency_decimal_places = UNSET
        else:
            foreign_currency_decimal_places = self.foreign_currency_decimal_places

        primary_currency_id: Union[None, Unset, str]
        if isinstance(self.primary_currency_id, Unset):
            primary_currency_id = UNSET
        else:
            primary_currency_id = self.primary_currency_id

        primary_currency_code: Union[None, Unset, str]
        if isinstance(self.primary_currency_code, Unset):
            primary_currency_code = UNSET
        else:
            primary_currency_code = self.primary_currency_code

        primary_currency_symbol: Union[None, Unset, str]
        if isinstance(self.primary_currency_symbol, Unset):
            primary_currency_symbol = UNSET
        else:
            primary_currency_symbol = self.primary_currency_symbol

        primary_currency_decimal_places: Union[None, Unset, int]
        if isinstance(self.primary_currency_decimal_places, Unset):
            primary_currency_decimal_places = UNSET
        else:
            primary_currency_decimal_places = self.primary_currency_decimal_places

        pc_amount = self.pc_amount

        foreign_amount: Union[None, Unset, str]
        if isinstance(self.foreign_amount, Unset):
            foreign_amount = UNSET
        else:
            foreign_amount = self.foreign_amount

        pc_foreign_amount = self.pc_foreign_amount

        source_balance_after: Union[None, Unset, str]
        if isinstance(self.source_balance_after, Unset):
            source_balance_after = UNSET
        else:
            source_balance_after = self.source_balance_after

        pc_source_balance_after: Union[None, Unset, str]
        if isinstance(self.pc_source_balance_after, Unset):
            pc_source_balance_after = UNSET
        else:
            pc_source_balance_after = self.pc_source_balance_after

        destination_balance_after: Union[None, Unset, str]
        if isinstance(self.destination_balance_after, Unset):
            destination_balance_after = UNSET
        else:
            destination_balance_after = self.destination_balance_after

        pc_destination_balance_after: Union[None, Unset, str]
        if isinstance(self.pc_destination_balance_after, Unset):
            pc_destination_balance_after = UNSET
        else:
            pc_destination_balance_after = self.pc_destination_balance_after

        source_name: Union[None, Unset, str]
        if isinstance(self.source_name, Unset):
            source_name = UNSET
        else:
            source_name = self.source_name

        source_iban: Union[None, Unset, str]
        if isinstance(self.source_iban, Unset):
            source_iban = UNSET
        else:
            source_iban = self.source_iban

        source_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        destination_name: Union[None, Unset, str]
        if isinstance(self.destination_name, Unset):
            destination_name = UNSET
        else:
            destination_name = self.destination_name

        destination_iban: Union[None, Unset, str]
        if isinstance(self.destination_iban, Unset):
            destination_iban = UNSET
        else:
            destination_iban = self.destination_iban

        destination_type: Union[Unset, str] = UNSET
        if not isinstance(self.destination_type, Unset):
            destination_type = self.destination_type.value

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

        subscription_id: Union[None, Unset, str]
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = self.subscription_id

        subscription_name: Union[None, Unset, str]
        if isinstance(self.subscription_name, Unset):
            subscription_name = UNSET
        else:
            subscription_name = self.subscription_name

        reconciled = self.reconciled

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

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

        original_source: Union[None, Unset, str]
        if isinstance(self.original_source, Unset):
            original_source = UNSET
        else:
            original_source = self.original_source

        recurrence_id: Union[None, Unset, str]
        if isinstance(self.recurrence_id, Unset):
            recurrence_id = UNSET
        else:
            recurrence_id = self.recurrence_id

        recurrence_total: Union[None, Unset, int]
        if isinstance(self.recurrence_total, Unset):
            recurrence_total = UNSET
        else:
            recurrence_total = self.recurrence_total

        recurrence_count: Union[None, Unset, int]
        if isinstance(self.recurrence_count, Unset):
            recurrence_count = UNSET
        else:
            recurrence_count = self.recurrence_count

        import_hash_v2: Union[None, Unset, str]
        if isinstance(self.import_hash_v2, Unset):
            import_hash_v2 = UNSET
        else:
            import_hash_v2 = self.import_hash_v2

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

        latitude: Union[None, Unset, float]
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: Union[None, Unset, float]
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        zoom_level: Union[None, Unset, int]
        if isinstance(self.zoom_level, Unset):
            zoom_level = UNSET
        else:
            zoom_level = self.zoom_level

        has_attachments = self.has_attachments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "date": date,
                "amount": amount,
                "description": description,
                "source_id": source_id,
                "destination_id": destination_id,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if transaction_journal_id is not UNSET:
            field_dict["transaction_journal_id"] = transaction_journal_id
        if order is not UNSET:
            field_dict["order"] = order
        if object_has_currency_setting is not UNSET:
            field_dict["object_has_currency_setting"] = object_has_currency_setting
        if currency_id is not UNSET:
            field_dict["currency_id"] = currency_id
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if currency_symbol is not UNSET:
            field_dict["currency_symbol"] = currency_symbol
        if currency_name is not UNSET:
            field_dict["currency_name"] = currency_name
        if currency_decimal_places is not UNSET:
            field_dict["currency_decimal_places"] = currency_decimal_places
        if foreign_currency_id is not UNSET:
            field_dict["foreign_currency_id"] = foreign_currency_id
        if foreign_currency_code is not UNSET:
            field_dict["foreign_currency_code"] = foreign_currency_code
        if foreign_currency_symbol is not UNSET:
            field_dict["foreign_currency_symbol"] = foreign_currency_symbol
        if foreign_currency_decimal_places is not UNSET:
            field_dict["foreign_currency_decimal_places"] = foreign_currency_decimal_places
        if primary_currency_id is not UNSET:
            field_dict["primary_currency_id"] = primary_currency_id
        if primary_currency_code is not UNSET:
            field_dict["primary_currency_code"] = primary_currency_code
        if primary_currency_symbol is not UNSET:
            field_dict["primary_currency_symbol"] = primary_currency_symbol
        if primary_currency_decimal_places is not UNSET:
            field_dict["primary_currency_decimal_places"] = primary_currency_decimal_places
        if pc_amount is not UNSET:
            field_dict["pc_amount"] = pc_amount
        if foreign_amount is not UNSET:
            field_dict["foreign_amount"] = foreign_amount
        if pc_foreign_amount is not UNSET:
            field_dict["pc_foreign_amount"] = pc_foreign_amount
        if source_balance_after is not UNSET:
            field_dict["source_balance_after"] = source_balance_after
        if pc_source_balance_after is not UNSET:
            field_dict["pc_source_balance_after"] = pc_source_balance_after
        if destination_balance_after is not UNSET:
            field_dict["destination_balance_after"] = destination_balance_after
        if pc_destination_balance_after is not UNSET:
            field_dict["pc_destination_balance_after"] = pc_destination_balance_after
        if source_name is not UNSET:
            field_dict["source_name"] = source_name
        if source_iban is not UNSET:
            field_dict["source_iban"] = source_iban
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if destination_name is not UNSET:
            field_dict["destination_name"] = destination_name
        if destination_iban is not UNSET:
            field_dict["destination_iban"] = destination_iban
        if destination_type is not UNSET:
            field_dict["destination_type"] = destination_type
        if budget_id is not UNSET:
            field_dict["budget_id"] = budget_id
        if budget_name is not UNSET:
            field_dict["budget_name"] = budget_name
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if bill_id is not UNSET:
            field_dict["bill_id"] = bill_id
        if bill_name is not UNSET:
            field_dict["bill_name"] = bill_name
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if subscription_name is not UNSET:
            field_dict["subscription_name"] = subscription_name
        if reconciled is not UNSET:
            field_dict["reconciled"] = reconciled
        if notes is not UNSET:
            field_dict["notes"] = notes
        if tags is not UNSET:
            field_dict["tags"] = tags
        if internal_reference is not UNSET:
            field_dict["internal_reference"] = internal_reference
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if original_source is not UNSET:
            field_dict["original_source"] = original_source
        if recurrence_id is not UNSET:
            field_dict["recurrence_id"] = recurrence_id
        if recurrence_total is not UNSET:
            field_dict["recurrence_total"] = recurrence_total
        if recurrence_count is not UNSET:
            field_dict["recurrence_count"] = recurrence_count
        if import_hash_v2 is not UNSET:
            field_dict["import_hash_v2"] = import_hash_v2
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
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if zoom_level is not UNSET:
            field_dict["zoom_level"] = zoom_level
        if has_attachments is not UNSET:
            field_dict["has_attachments"] = has_attachments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = TransactionTypeProperty(d.pop("type"))

        date = isoparse(d.pop("date"))

        amount = d.pop("amount")

        description = d.pop("description")

        def _parse_source_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        source_id = _parse_source_id(d.pop("source_id"))

        def _parse_destination_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        destination_id = _parse_destination_id(d.pop("destination_id"))

        user = d.pop("user", UNSET)

        transaction_journal_id = d.pop("transaction_journal_id", UNSET)

        def _parse_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        order = _parse_order(d.pop("order", UNSET))

        object_has_currency_setting = d.pop("object_has_currency_setting", UNSET)

        currency_id = d.pop("currency_id", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        currency_symbol = d.pop("currency_symbol", UNSET)

        currency_name = d.pop("currency_name", UNSET)

        currency_decimal_places = d.pop("currency_decimal_places", UNSET)

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

        def _parse_foreign_currency_symbol(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        foreign_currency_symbol = _parse_foreign_currency_symbol(d.pop("foreign_currency_symbol", UNSET))

        def _parse_foreign_currency_decimal_places(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        foreign_currency_decimal_places = _parse_foreign_currency_decimal_places(
            d.pop("foreign_currency_decimal_places", UNSET)
        )

        def _parse_primary_currency_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_currency_id = _parse_primary_currency_id(d.pop("primary_currency_id", UNSET))

        def _parse_primary_currency_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_currency_code = _parse_primary_currency_code(d.pop("primary_currency_code", UNSET))

        def _parse_primary_currency_symbol(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_currency_symbol = _parse_primary_currency_symbol(d.pop("primary_currency_symbol", UNSET))

        def _parse_primary_currency_decimal_places(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        primary_currency_decimal_places = _parse_primary_currency_decimal_places(
            d.pop("primary_currency_decimal_places", UNSET)
        )

        pc_amount = d.pop("pc_amount", UNSET)

        def _parse_foreign_amount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        foreign_amount = _parse_foreign_amount(d.pop("foreign_amount", UNSET))

        pc_foreign_amount = d.pop("pc_foreign_amount", UNSET)

        def _parse_source_balance_after(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_balance_after = _parse_source_balance_after(d.pop("source_balance_after", UNSET))

        def _parse_pc_source_balance_after(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pc_source_balance_after = _parse_pc_source_balance_after(d.pop("pc_source_balance_after", UNSET))

        def _parse_destination_balance_after(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        destination_balance_after = _parse_destination_balance_after(d.pop("destination_balance_after", UNSET))

        def _parse_pc_destination_balance_after(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pc_destination_balance_after = _parse_pc_destination_balance_after(d.pop("pc_destination_balance_after", UNSET))

        def _parse_source_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_name = _parse_source_name(d.pop("source_name", UNSET))

        def _parse_source_iban(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_iban = _parse_source_iban(d.pop("source_iban", UNSET))

        _source_type = d.pop("source_type", UNSET)
        source_type: Union[Unset, AccountTypeProperty]
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = AccountTypeProperty(_source_type)

        def _parse_destination_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        destination_name = _parse_destination_name(d.pop("destination_name", UNSET))

        def _parse_destination_iban(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        destination_iban = _parse_destination_iban(d.pop("destination_iban", UNSET))

        _destination_type = d.pop("destination_type", UNSET)
        destination_type: Union[Unset, AccountTypeProperty]
        if isinstance(_destination_type, Unset):
            destination_type = UNSET
        else:
            destination_type = AccountTypeProperty(_destination_type)

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

        def _parse_subscription_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subscription_id = _parse_subscription_id(d.pop("subscription_id", UNSET))

        def _parse_subscription_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subscription_name = _parse_subscription_name(d.pop("subscription_name", UNSET))

        reconciled = d.pop("reconciled", UNSET)

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

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

        def _parse_original_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        original_source = _parse_original_source(d.pop("original_source", UNSET))

        def _parse_recurrence_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recurrence_id = _parse_recurrence_id(d.pop("recurrence_id", UNSET))

        def _parse_recurrence_total(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        recurrence_total = _parse_recurrence_total(d.pop("recurrence_total", UNSET))

        def _parse_recurrence_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        recurrence_count = _parse_recurrence_count(d.pop("recurrence_count", UNSET))

        def _parse_import_hash_v2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        import_hash_v2 = _parse_import_hash_v2(d.pop("import_hash_v2", UNSET))

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

        def _parse_latitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_zoom_level(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        zoom_level = _parse_zoom_level(d.pop("zoom_level", UNSET))

        has_attachments = d.pop("has_attachments", UNSET)

        transaction_split = cls(
            type_=type_,
            date=date,
            amount=amount,
            description=description,
            source_id=source_id,
            destination_id=destination_id,
            user=user,
            transaction_journal_id=transaction_journal_id,
            order=order,
            object_has_currency_setting=object_has_currency_setting,
            currency_id=currency_id,
            currency_code=currency_code,
            currency_symbol=currency_symbol,
            currency_name=currency_name,
            currency_decimal_places=currency_decimal_places,
            foreign_currency_id=foreign_currency_id,
            foreign_currency_code=foreign_currency_code,
            foreign_currency_symbol=foreign_currency_symbol,
            foreign_currency_decimal_places=foreign_currency_decimal_places,
            primary_currency_id=primary_currency_id,
            primary_currency_code=primary_currency_code,
            primary_currency_symbol=primary_currency_symbol,
            primary_currency_decimal_places=primary_currency_decimal_places,
            pc_amount=pc_amount,
            foreign_amount=foreign_amount,
            pc_foreign_amount=pc_foreign_amount,
            source_balance_after=source_balance_after,
            pc_source_balance_after=pc_source_balance_after,
            destination_balance_after=destination_balance_after,
            pc_destination_balance_after=pc_destination_balance_after,
            source_name=source_name,
            source_iban=source_iban,
            source_type=source_type,
            destination_name=destination_name,
            destination_iban=destination_iban,
            destination_type=destination_type,
            budget_id=budget_id,
            budget_name=budget_name,
            category_id=category_id,
            category_name=category_name,
            bill_id=bill_id,
            bill_name=bill_name,
            subscription_id=subscription_id,
            subscription_name=subscription_name,
            reconciled=reconciled,
            notes=notes,
            tags=tags,
            internal_reference=internal_reference,
            external_id=external_id,
            external_url=external_url,
            original_source=original_source,
            recurrence_id=recurrence_id,
            recurrence_total=recurrence_total,
            recurrence_count=recurrence_count,
            import_hash_v2=import_hash_v2,
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
            latitude=latitude,
            longitude=longitude,
            zoom_level=zoom_level,
            has_attachments=has_attachments,
        )

        transaction_split.additional_properties = d
        return transaction_split

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
