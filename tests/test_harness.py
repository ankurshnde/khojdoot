"""Unit tests for Agent Harness execution."""
from app.harness.workflow import execute_workflow


def test_harness_checkpoint1_execution():
    result = execute_workflow({
        "slug": "test-merchant",
        "raw_input": "माझे नाव सुनिता टिफिन सर्व्हिस आहे. नाशिक येथे आमची घरगुती जेवणाची सोय आहे. फोन 9423375197",
        "phase": "checkpoint1",
    })
    assert result["infobin"] is not None
    assert result["infobin"]["name"] != ""
