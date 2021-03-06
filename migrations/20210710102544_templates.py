from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        self.db.templates.insert_many(
            [
                {
                    "type": "system",
                    "entity": "entity",
                    "customerId": "system",
                    "law": "base",
                    "fields": [
                        {
                            "field": "name",
                            "label": "Name",
                            "data_type": "short-text",
                            "default": "Type name here..",
                            "field_type": "basic_details",
                            "field_type_label": "Basic Details",
                            "is_removable": False,
                            "mandatory": True,
                        },
                        {
                            "field": "description",
                            "label": "Description",
                            "data_type": "long-text",
                            "default": "Type description here..",
                            "field_type": "basic_details",
                            "field_type_label": "Basic Details",
                            "is_removable": False,
                            "mandatory": False,
                        },
                        {
                            "field": "entity_type",
                            "label": "Entity Type",
                            "data_type": "options",
                            "default": "",
                            "field_type": "basic_details",
                            "field_type_label": "Basic Details",
                            "is_removable": False,
                            "mandatory": False,
                            "options_list": [
                                "Affiliate",
                                "Client",
                                "Holding Company",
                                "Regulatory Body",
                                "Subsidiary",
                            ],
                        },
                        {
                            "field": "location",
                            "label": "Location",
                            "data_type": "options",
                            "default": "",
                            "field_type": "basic_details",
                            "field_type_label": "Basic Details",
                            "is_removable": False,
                            "mandatory": False,
                            "options_url": {"url": "dm/geos", "request_type": "GET"},
                        },
                    ],
                },
                {
                    "type": "system",
                    "entity": "entity",
                    "customerId": "system",
                    "law": "GDPR",
                    "fields": [
                        {
                            "field": "address",
                            "label": "Address",
                            "data_type": "longtext",
                            "default": "Type address here..",
                            "field_type": "contact_details",
                            "field_type_label": "Contact Details",
                            "is_removable": False,
                            "mandatory": False,
                        },
                        {
                            "field": "representative",
                            "label": "Representative",
                            "data_type": "options",
                            "default": "Type the representative name here..",
                            "field_type": "contact_details",
                            "field_type_label": "Contact Details",
                            "is_removable": False,
                            "mandatory": False,
                            "options_url": {
                                "url": "dm/customer/<customer_id>/users",
                                "request_type": "GET",
                            },
                        },
                    ],
                },
                {
                    "type": "system",
                    "entity": "entity",
                    "customerId": "system",
                    "law": "CCPA",
                    "fields": [
                        {
                            "field": "representative_contact_details",
                            "label": "Representative Contact Details",
                            "data_type": "long-text",
                            "default": "Type contact details here..",
                            "field_type": "contact_details",
                            "field_type_label": "Contact Details",
                            "is_removable": False,
                            "mandatory": False,
                        },
                        {
                            "field": "data_protection_officer",
                            "label": "Data Protection Officer",
                            "data_type": "options",
                            "default": "Type the data protection officer name here..",
                            "field_type": "contact_details",
                            "field_type_label": "Contact Details",
                            "is_removable": False,
                            "mandatory": False,
                            "options_url": {
                                "url": "dm/customer/<customer_id>/users",
                                "request_type": "GET",
                            },
                        },
                        {
                            "field": "dpo_contact_details",
                            "label": "Data Protection Officer Contact Details",
                            "data_type": "long-text",
                            "default": "Type contact details here..",
                            "field_type": "contact_details",
                            "field_type_label": "Contact Details",
                            "is_removable": False,
                            "mandatory": False,
                        },
                    ],
                }
            ])

    def downgrade(self):
        self.db.templates.remove({})
