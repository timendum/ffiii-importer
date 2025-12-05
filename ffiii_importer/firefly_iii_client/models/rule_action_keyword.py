from enum import Enum


class RuleActionKeyword(str, Enum):
    ADD_TAG = "add_tag"
    APPEND_DESCRIPTION = "append_description"
    APPEND_NOTES = "append_notes"
    CLEAR_BUDGET = "clear_budget"
    CLEAR_CATEGORY = "clear_category"
    CLEAR_NOTES = "clear_notes"
    CONVERT_DEPOSIT = "convert_deposit"
    CONVERT_TRANSFER = "convert_transfer"
    CONVERT_WITHDRAWAL = "convert_withdrawal"
    DELETE_TRANSACTION = "delete_transaction"
    LINK_TO_BILL = "link_to_bill"
    PREPEND_DESCRIPTION = "prepend_description"
    PREPEND_NOTES = "prepend_notes"
    REMOVE_ALL_TAGS = "remove_all_tags"
    REMOVE_TAG = "remove_tag"
    SET_BUDGET = "set_budget"
    SET_CATEGORY = "set_category"
    SET_DESCRIPTION = "set_description"
    SET_DESTINATION_ACCOUNT = "set_destination_account"
    SET_NOTES = "set_notes"
    SET_SOURCE_ACCOUNT = "set_source_account"
    USER_ACTION = "user_action"

    def __str__(self) -> str:
        return str(self.value)
