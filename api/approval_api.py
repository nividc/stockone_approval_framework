from models.approval import Approval
from models.approval_process import ApprovalProcess

class ApprovalAPI:
    def __init__(self, approval_process):
        self.approval_process = approval_process

    def create_approval_request(self, header, line_items, approval_type):
        new_approval = Approval(header, line_items, approval_type)
        self.approval_process.initiate_approval(new_approval)
        return new_approval

    def get_approval_status(self, approval):
        return approval.status

    def approve_reject_request(self, user, approval, decision):
        if decision == "approve":
            self.approval_process.approve_request(user, approval)
        else:
            self.approval_process.approve_request(user, approval)  

