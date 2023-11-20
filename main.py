# main.py
from api.user_company_api import UserCompanyAPI
from api.approval_api import ApprovalAPI
from api.workflow_api import WorkflowAPI
from models.approval_process import ApprovalProcess

# Create users and company
user_company_api = UserCompanyAPI()
aarav = user_company_api.create_user("Aarav", "Approver")
priya = user_company_api.create_user("Priya", "Approver")
rajesh = user_company_api.create_user("Rajesh", "Approver")
sunita = user_company_api.create_user("Sunita", "Approver")
mohan = user_company_api.create_user("Mohan", "Final Approver")

# Create workflows
workflow_api = WorkflowAPI()
workflow_1 = workflow_api.create_workflow("Workflow 1", 100, [aarav, priya, rajesh, sunita, mohan])
workflow_2 = workflow_api.create_workflow("Workflow 2", 1000, [aarav, priya, rajesh, sunita, mohan])
workflow_3 = workflow_api.create_workflow("Workflow 3", 10000, [aarav, priya, rajesh, sunita, mohan])
approval_type_workflow = workflow_api.create_workflow("Approval Type Workflow", None, [aarav, priya, rajesh, sunita, mohan])

# Create an instance of ApprovalProcess with the workflows
approval_process = ApprovalProcess(workflows=[workflow_1, workflow_2, workflow_3, approval_type_workflow])

# Create an instance of ApprovalAPI with the approval_process
approval_api = ApprovalAPI(approval_process)

# Create an approval request
approval_1 = approval_api.create_approval_request("Header 1", [50, 60, 90], "urgent")

# Get the approval status
print(approval_api.get_approval_status(approval_1))

# Approve the request (assuming Aarav is the user)
approval_api.approve_reject_request(aarav, approval_1, "approve")

# Get the updated approval status
print(approval_api.get_approval_status(approval_1))

