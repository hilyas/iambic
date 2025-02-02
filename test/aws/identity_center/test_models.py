from __future__ import annotations

from iambic.core.template_generation import merge_model
from iambic.plugins.v0_1_0.aws.identity_center.permission_set.models import (
    AwsIdentityCenterPermissionSetTemplate,
)


def test_merge_template_access_rules(aws_accounts):
    existing_properties = {
        "name": "bar",
    }
    existing_access_rules = [
        {
            "users": [
                "user@example.com",
            ],
            "expires_at": "in 3 days",
        }
    ]
    existing_document = AwsIdentityCenterPermissionSetTemplate(
        identifier="bar",
        file_path="foo",
        properties=existing_properties,
        access_rules=existing_access_rules,
    )
    new_properties = {
        "name": "bar",
    }
    new_access_rules = [
        {
            "users": [
                "user@example.com",
            ],
        }
    ]
    new_document = AwsIdentityCenterPermissionSetTemplate(
        identifier="bar",
        file_path="foo",
        properties=new_properties,
        access_rules=new_access_rules,
    )
    merged_document: AwsIdentityCenterPermissionSetTemplate = merge_model(
        new_document, existing_document, aws_accounts
    )
    assert existing_access_rules != new_access_rules
    assert merged_document.access_rules == existing_document.access_rules
