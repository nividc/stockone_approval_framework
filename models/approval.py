class Approval:
    def __init__(self, header, line_items, approval_type):
        self.header = header
        self.line_items = line_items
        self.approval_type = approval_type
        self.status = "Pending"
        self.current_workflow = None

    def initiate_approval(self, workflow):
        self.current_workflow = workflow
        self.status = "In Progress"

    def update_status(self, new_status):
        self.status = new_status
