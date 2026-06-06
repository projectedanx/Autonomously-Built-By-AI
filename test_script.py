import pytest
import sys
sys.path.append("system_logic")
pytest.main(["--cov=system_logic.poc_run", "--cov-report=term-missing", "tests/test_poc_run.py"])
