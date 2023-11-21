from models.workflow import Workflow

class WorkflowAPI:
    def create_workflow(self, name, trigger_value, approval_users):
        new_workflow = Workflow(name, trigger_value, approval_users)
        return new_workflow

