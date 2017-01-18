# Pytest Notes

### Example 1
```python
import json
import os
import shutil
import tempfile

import pytest

from pipeline.db_ops import services


@pytest.fixture(scope="module")
def test_dir(request):
    """Setup the test_dir."""
    # Create a temporary directory
    test_dir = tempfile.mkdtemp()
    path = os.path.join(test_dir, 'temp_file')
    try:
        with open(path, "w") as tmp:
            json.dump("[{'a': 'A', 'b': (2, 4), 'c': 3.0}]", tmp)
    except IOError as e:
        print('IOError')
        print(e.message)

    def tear_down():
        shutil.rmtree(test_dir)
    request.addfinalizer(tear_down)
    return path


@pytest.mark.usefixtures('test_dir')
def test_read_json(test_dir):
    """Test methods of getting devices from different files."""
    expected = """[{'a': 'A', 'b': (2, 4), 'c': 3.0}]"""
    assert services.read_json(test_dir) == expected
```


### Example 2
```python
from pipeline.rest import csv_to_json

import pytest


@pytest.fixture(scope="function")
def vdp_string_fixture():
    """Setup the virtual datapoint strings to filter."""
    example_vpd_strings = [
        "n/a - VDP;RG00004_WBD_EGEN.H_HP__COW_SUP.PRIM_MEA_T_avg_d;DIMHP_Waermequelleneintritt_avg_d;°C;WP_Regler;VDP;;daily;pipeExpression=\"dp(DatapointCriterium.NAME, 'RG00004_WBD_EGEN.H_HP__COW_SUP.PRIM_MEA_T').mask(dp(DatapointCriterium.NAME, 'RG00004_WBD_EGEN.H_HP_PPU___SIG_STAT.M11'), equalTo(0.0)).fold(day, avg)\"",
        "n/a - VDP;RG00004_WBD_EGEN.H_HP__COW_RET.PRIM_MEA_T.R6_avg_d;DIMHP_Waermequellenaustritt (R6)_avg_d;°C;WP_Regler;VDP;;daily;pipeExpression=\"dp(DatapointCriterium.NAME, 'RG00004_WBD_EGEN.H_HP__COW_RET.PRIM_MEA_T.R6').mask(dp(DatapointCriterium.NAME, 'RG00004_WBD_EGEN.H_HP_PPU___SIG_STAT.M11'), equalTo(0.0)).fold(day, avg)\"",
        "n/a - VDP;RG00004_WBD_EGEN.H_HP_DHWP.HSTO_DHW__MEA_T.R3_avg_d;DIMHP_Warmwassertemperatur (R3)_avg_d;°C;WP_Regler;VDP;;daily;pipeExpression=\"dp(DatapointCriterium.NAME, 'RG00004_WBD_EGEN.H_HP_DHWP.HSTO_DHW__MEA_T.R3').fold(day, avg)\"",
        "n/a - VDP;RG00004_WBD_EGEN.H_HP_COMP.1___CALC_OPH_m;DIMHP_Betriebsstunden_m;h;WP_Regler;VDP;;monthly;pipeExpression=\"dp(DatapointCriterium.NAME, 'RG00004_WBD_EGEN.H_HP_COMP.1___CALC_OPH').diffs().fold(month, sum)\"",
        "pipeExpression=\"dp\" mumbo-jumbo",
        "pipeExpression= mumbo-jumbo"
    ]

    return example_vpd_strings


@pytest.mark.usefixtures('vdp_string_fixture')
def test_mask(vdp_string_fixture):
    """Short explanation."""
    assert csv_to_json.mask(vdp_string_fixture[0]) is True
    assert csv_to_json.mask(vdp_string_fixture[1]) is True
    assert csv_to_json.mask(vdp_string_fixture[2]) is True
    assert csv_to_json.mask(vdp_string_fixture[3]) is True
    assert csv_to_json.mask(vdp_string_fixture[4]) is False
    assert csv_to_json.mask(vdp_string_fixture[5]) is False


@pytest.fixture(scope="function")
def create_expressions_fixture():
    """Fixture for parse_expression."""
    expected_string = ["Datapoint(RG00004_WBD_EGEN.H_HP____CALC_E.H.1).diffs().fold(HOURS, SUM)",
                       "Datapoint(RG00004_WBD_EGEN.H_HP_DHWP.HSTO_DHW__MEA_T.R3).diffs().fold(DAYS, AVG)",
                       "Datapoint(RG00004_WBD_EGEN.H_HP__COW_RET.PRIM_MEA_T.R6).mask(Datapoint(RG00004_WBD_EGEN.H_HP_PPU___SIG_STAT.M11), equalTo(0.0)).fold(DAYS, AVG)"]
    input_string = ["dp(DatapointCriterium.NAME, 'RG00004_WBD_EGEN.H_HP____CALC_E.H.1').diffs().fold(hour, sum)",
                    "dp(DatapointCriterium.NAME, 'RG00004_WBD_EGEN.H_HP_DHWP.HSTO_DHW__MEA_T.R3').diffs().fold(day, avg)",
                    "dp(DatapointCriterium.NAME, 'RG00004_WBD_EGEN.H_HP__COW_RET.PRIM_MEA_T.R6').mask(dp(DatapointCriterium.NAME, 'RG00004_WBD_EGEN.H_HP_PPU___SIG_STAT.M11'), equalTo(0.0)).fold(day, avg)"]
    return [expected_string, input_string]


@pytest.mark.usefixtures('create_expressions_fixture')
def test_create_expressions(create_expressions_fixture):
    """Short explanation."""
    # ex = "dp(DatapointCriterium.NAME, 'RG00004_WBD_EGEN.H_HP__COW_RET.PRIM_MEA_T.R6').mask(dp(DatapointCriterium.NAME, 'RG00004_WBD_EGEN.H_HP_PPU___SIG_STAT.M11'), equalTo(0.0)).fold(day, avg)"
    # print("Example: ", csv_to_json.create_expressions(ex))
    assert create_expressions_fixture[0] == [csv_to_json.create_expressions(x) for x in create_expressions_fixture[1]]
```


### Example 3
```python
import os
import shutil
import tempfile
from pipeline.rest import core

import pytest


@pytest.fixture(scope="module")
def test_dir(request):
    """Setup the test_dir."""
    # Create a temporary directory
    test_dir = tempfile.mkdtemp()

    def tear_down():
        shutil.rmtree(test_dir)
    request.addfinalizer(tear_down)
    return test_dir


@pytest.mark.usefixtures('test_dir')
def test_get_devices(test_dir):
    """Test methods of getting devices from different files."""
    junk_files = ['customer1.csv', 'customer2.csv', 'test.json', 'test.json1', 'test.csv1']

    for f in junk_files:
        path = os.path.join(test_dir, f)
        try:
            with open(path, "w") as tmp:
                tmp.write("secrets!")
        except IOError as e:
            print('IOError')
            print(e.message)

    expected_file_list = ['customer1.csv', 'customer2.csv']
    received_file_list = sorted(core.get_devices(test_dir))

    assert expected_file_list == received_file_list, "get_devices not working properly"
```

# Coverage

`py.test --cov-report term-missing  --cov=shazam tests/ -s -v`
