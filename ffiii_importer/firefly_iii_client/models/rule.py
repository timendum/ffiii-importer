import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rule_trigger_type import RuleTriggerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rule_action import RuleAction
    from ..models.rule_trigger import RuleTrigger


T = TypeVar("T", bound="Rule")


@_attrs_define
class Rule:
    """
    Attributes:
        title (str):  Example: First rule title..
        rule_group_id (str): ID of the rule group under which the rule must be stored. Either this field or
            rule_group_title is mandatory. Example: 81.
        trigger (RuleTriggerType): Which action is necessary for the rule to fire? Use either store-journal or update-
            journal. Example: store-journal.
        triggers (list['RuleTrigger']):
        actions (list['RuleAction']):
        created_at (Union[Unset, datetime.datetime]):  Example: 2025-10-01T00:00:00+00:00.
        updated_at (Union[Unset, datetime.datetime]):  Example: 2025-10-01T00:00:00+00:00.
        description (Union[Unset, str]):  Example: First rule description.
        rule_group_title (Union[Unset, str]): Title of the rule group under which the rule must be stored. Either this
            field or rule_group_id is mandatory. Example: New rule group.
        order (Union[Unset, int]):  Example: 5.
        active (Union[Unset, bool]): Whether or not the rule is even active. Default is true. Default: True. Example:
            True.
        strict (Union[Unset, bool]): If the rule is set to be strict, ALL triggers must hit in order for the rule to
            fire. Otherwise, just one is enough. Default value is true. Example: True.
        stop_processing (Union[Unset, bool]): If this value is true and the rule is triggered, other rules  after this
            one in the group will be skipped. Default value is false. Default: False.
    """

    title: str
    rule_group_id: str
    trigger: RuleTriggerType
    triggers: list["RuleTrigger"]
    actions: list["RuleAction"]
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    rule_group_title: Union[Unset, str] = UNSET
    order: Union[Unset, int] = UNSET
    active: Union[Unset, bool] = True
    strict: Union[Unset, bool] = UNSET
    stop_processing: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        rule_group_id = self.rule_group_id

        trigger = self.trigger.value

        triggers = []
        for triggers_item_data in self.triggers:
            triggers_item = triggers_item_data.to_dict()
            triggers.append(triggers_item)

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        description = self.description

        rule_group_title = self.rule_group_title

        order = self.order

        active = self.active

        strict = self.strict

        stop_processing = self.stop_processing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "rule_group_id": rule_group_id,
                "trigger": trigger,
                "triggers": triggers,
                "actions": actions,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if description is not UNSET:
            field_dict["description"] = description
        if rule_group_title is not UNSET:
            field_dict["rule_group_title"] = rule_group_title
        if order is not UNSET:
            field_dict["order"] = order
        if active is not UNSET:
            field_dict["active"] = active
        if strict is not UNSET:
            field_dict["strict"] = strict
        if stop_processing is not UNSET:
            field_dict["stop_processing"] = stop_processing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rule_action import RuleAction
        from ..models.rule_trigger import RuleTrigger

        d = dict(src_dict)
        title = d.pop("title")

        rule_group_id = d.pop("rule_group_id")

        trigger = RuleTriggerType(d.pop("trigger"))

        triggers = []
        _triggers = d.pop("triggers")
        for triggers_item_data in _triggers:
            triggers_item = RuleTrigger.from_dict(triggers_item_data)

            triggers.append(triggers_item)

        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = RuleAction.from_dict(actions_item_data)

            actions.append(actions_item)

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

        description = d.pop("description", UNSET)

        rule_group_title = d.pop("rule_group_title", UNSET)

        order = d.pop("order", UNSET)

        active = d.pop("active", UNSET)

        strict = d.pop("strict", UNSET)

        stop_processing = d.pop("stop_processing", UNSET)

        rule = cls(
            title=title,
            rule_group_id=rule_group_id,
            trigger=trigger,
            triggers=triggers,
            actions=actions,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            rule_group_title=rule_group_title,
            order=order,
            active=active,
            strict=strict,
            stop_processing=stop_processing,
        )

        rule.additional_properties = d
        return rule

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
