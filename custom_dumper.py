import yaml

schema = {

    "version": 2,

    "models":
    [{
        'name': 'stg_account_fax_settings',
        'description': '',
        'columns': [
        {
            'name': 'id',
            'description': 'Primary key for account_fax_settings',
            'type': 'integer',
            'meta': {"not_null_count": 9, "not_null_proportion": 1.0, "is_unique": True, "distinct_count": 9, "distinct_proportion": 1.0}
        },
        {
            'name': 'account_id',
            'description': 'Foreign key for accounts',
            'type': 'integer',
            'meta': {"not_null_count": 9, "not_null_proportion": 1.0, "is_unique": False, "distinct_count": 6, "distinct_proportion": 0.67}
        },
        {
            'name': 'encrypted_usernumber',
            'description': '',
            'type': 'character varying'},
        ]
    },
    {
        'name': 'stg_accounts',
        'description': '',
        'columns': [
        {
            'name': 'id',
            'description': 'Primary key for accounts',
            'type': 'integer',
            'meta': {"not_null_count": 9, "not_null_proportion": 1.0, "is_unique": True, "distinct_count": 9, "distinct_proportion": 1.0}
        },
        ]
    },
    ]
}

class CustomDumper(yaml.SafeDumper):

    # def represent_sequence(self, tag, sequence, flow_style=None):
    #     if len(self.indents) > 2:
    #         super().represent_sequence(tag, sequence, flow_style=True)
    #     else:
    #         super().represent_sequence(tag, sequence, flow_style=False)

    def write_line_break(self, data=None):
        super().write_line_break(data)

        if len(self.indents) == 1 or len(self.indents) == 2:
            super().write_line_break()


class Config():
    def __init__(self) -> None:
        pass

    def write_schema_config(self, schema: dict) -> None:

        filename = "custom_config.yml"

        with open(filename, "w") as output:
            yaml.dump(
                schema,
                output,
                default_style=None,
                default_flow_style=False,
                sort_keys=False,
                Dumper=CustomDumper
            )

custom_config = Config()
custom_config.write_schema_config(schema)
