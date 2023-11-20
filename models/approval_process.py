# models/approval_process.py
class ApprovalProcess:
    def __init__(self, workflows=None):
        self.workflows = workflows or []

    def initiate_approval(self, approval):
        for workflow in self.workflows:
            if approval.approval_type == "Approval Type Workflow" or \
                    (workflow.trigger_value and sum(approval.line_items) > workflow.trigger_value):
                approval.initiate_approval(workflow)
                break
        else:
            raise ValueError("No suitable workflow found for approval")

    def approve_request(self, user, approval):
        if user in approval.current_workflow.approval_users:
            approval.update_status("Approved")
            # Additional logic for approval action
        else:
            approval.update_status("Rejected")
            # Additional logic for rejection action

