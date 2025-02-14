import os

import great_expectations as gx

context = gx.get_context()

datasource_name = "ABS datasource"

CREDENTIAL = os.getenv("AZURE_CREDENTIAL", "")
ACCOUNT_URL = "superconductivetesting.blob.core.windows.net"
CONTAINER = "superconductive-public"
NAME_STARTS_WITH = "data/taxi_yellow_tripdata_samples/"


datasource = context.data_sources.add_pandas_abs(
    name=datasource_name,
    azure_options={
        "account_url": ACCOUNT_URL,
        "credential": CREDENTIAL,
    },
)

asset = datasource.add_csv_asset(
    name="taxi_yellow_tripdata_samples",
    abs_container=CONTAINER,
    abs_name_starts_with=NAME_STARTS_WITH,
)

batch_definition = asset.add_batch_definition_path(
    "abs batch definition",
    path=f"{NAME_STARTS_WITH}yellow_tripdata_sample_2019-02.csv",
)

batch_request = batch_definition.build_batch_request()
batch_list = asset.get_batch_list_from_batch_request(batch_request)

assert len(batch_list) == 1
assert batch_list[0].metadata == {
    "path": "data/taxi_yellow_tripdata_samples/yellow_tripdata_sample_2019-02.csv"
}
