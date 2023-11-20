# api/workflow_api.py
from models.workflow import Workflow

class WorkflowAPI:
    def create_workflow(self, name, trigger_value, approval_users):
        new_workflow = Workflow(name, trigger_value, approval_users)
        # Logic to store the new workflow in a database or data structure
        return new_workflow

