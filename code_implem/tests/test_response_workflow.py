import pytest
from code_implem.src.response_workflow import ResponseWorkflow

def test_trigger_sets_status():
    workflow = ResponseWorkflow("wf001", ["isolate host", "notify admin"])
    result = workflow.trigger()
    assert result == "Workflow wf001 triggered."
    assert workflow.status == "Triggered"   # match actual implementation

def test_execute_runs_actions():
    workflow = ResponseWorkflow("wf002", ["block IP", "log event"])
    workflow.trigger()
    result = workflow.execute()
    assert result == "Workflow wf002 executed: ['block IP', 'log event']"
    assert workflow.status == "Executed"

def test_log_action_appends_log():
    workflow = ResponseWorkflow("wf003", ["quarantine file"])
    workflow.trigger()
    workflow.execute()
    result = workflow.log_action("manual override")  # match method name
    assert "manual override" in result
    assert "manual override" in workflow.actions

