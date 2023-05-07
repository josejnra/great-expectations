import json

import great_expectations as ge
from great_expectations import DataContext
from great_expectations.core import ExpectationSuite
from great_expectations.core.batch import RuntimeBatchRequest
from great_expectations.validator.validator import Validator


EXPECTATION_SUITE_PATH = (
    "great_expectations/expectations/transportadora/clientes_expectation_suite.json"
)


# def main1():
#     expectation_suite = json.loads(EXPECTATION_SUITE_PATH)

#     clientes_df = ge.read_table()


def main2():
    context: DataContext = ge.get_context()
    print(context.list_expectation_suite_names())

    suite_name: str = "transportadora.clientes_expectation_suite"

    suite: ExpectationSuite = context.get_expectation_suite(suite_name)

    batch_request = RuntimeBatchRequest(
        datasource_name="transportadora",
        data_connector_name="default_runtime_data_connector_name",
        data_asset_name="any_name",
        runtime_parameters={"query": "SELECT * FROM public.clientes"},
        batch_identifiers={
            "some_key_maybe_pipeline_stage": "validation_stage",
            "some_other_key_maybe_run_id": 1234567890
        },
        batch_spec_passthrough={
            "create_temp_table": False  # if not provided, this defaults to True
        },
    )

    clientes_validator = context.get_validator(
        batch_request=batch_request,
        expectation_suite=suite,
    )

    clientes_validator.active_batch.head()


def main3():
    import pandas as pd
    path = "sample_data/titanic.csv"
    df = pd.read_csv(path)

    context: DataContext = ge.get_context()
    suite_name: str = "titanic_expectation_suite"

    suite: ExpectationSuite = context.get_expectation_suite(suite_name)

    batch_request = RuntimeBatchRequest(
        datasource_name="titanic",
        data_connector_name="default_runtime_data_connector_name",
        data_asset_name="any_name",  # This can be anything that identifies this data_asset for you
        runtime_parameters={"batch_data": df},  # Pass your DataFrame here.
        batch_identifiers={"default_identifier_name": "any_identifier"},
    )

    clientes_validator = context.get_validator(
        batch_request=batch_request,
        expectation_suite=suite,
    )

    print(clientes_validator.active_batch.head())


if __name__ == "__main__":
    main3()
