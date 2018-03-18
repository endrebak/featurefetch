import pytest

import pandas as pd

@pytest.fixture(scope="session")
def gencode_gtf():
    return "test_data/gencode.gtf"


@pytest.fixture(scope="session")
def expected_result_parse_gencode_gtf():
    return pd.read_table("test_data/expected_result_parse_gencode_gtf.txt", sep=" ", header=0)



@pytest.fixture(scope="session")
def ensembl_gtf():
    return "test_data/ensembl.gtf"


@pytest.fixture(scope="session")
def expected_result_parse_ensembl_gtf():
    return pd.read_table("test_data/expected_result_parse_ensembl_gtf.txt", sep=" ", header=0)
