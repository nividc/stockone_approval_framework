from api.user_company_api import UserCompanyAPI
from api.approval_api import ApprovalAPI
from api.workflow_api import WorkflowAPI
from models.approval_process import ApprovalProcess

# Creating users and company
user_company_api = UserCompanyAPI()
aarav = user_company_api.create_user("Aarav", "Approver")
priya = user_company_api.create_user("Priya", "Approver")
rajesh = user_company_api.create_user("Rajesh", "Approver")
sunita = user_company_api.create_user("Sunita", "Approver")
mohan = user_company_api.create_user("Mohan", "Final Approver")

# Creating workflows
workflow_api = WorkflowAPI()
workflow_1 = workflow_api.create_workflow("Workflow 1", 100, [aarav, priya, rajesh, sunita, mohan])
workflow_2 = workflow_api.create_workflow("Workflow 2", 1000, [aarav, priya, rajesh, sunita, mohan])
workflow_3 = workflow_api.create_workflow("Workflow 3", 10000, [aarav, priya, rajesh, sunita, mohan])
approval_type_workflow = workflow_api.create_workflow("Approval Type Workflow", None, [aarav, priya, rajesh, sunita, mohan])

approval_process = ApprovalProcess(workflows=[workflow_1, workflow_2, workflow_3, approval_type_workflow])

approval_api = ApprovalAPI(approval_process)

approval_1 = approval_api.create_approval_request("Header 1", [50, 60, 90], "urgent")

print(approval_api.get_approval_status(approval_1))

approval_api.approve_reject_request(aarav, approval_1, "approve")

print(approval_api.get_approval_status(approval_1))

