
const workflows = [
    { id: 1, name: 'Workflow 1', threshold: 100 },
    { id: 2, name: 'Workflow 2', threshold: 1000 },
    { id: 3, name: 'Workflow 3', threshold: 10000 },
    { id: 4, name: 'Approval Type Workflow', threshold: 0 }
];

const approvalRequests = [
    { id: 1, value: 120, type: 'urgent', status: 'Pending', approvers: ['Aarav', 'Priya', 'Rajesh', 'Sunita', 'Mohan'] },
    // Add more simulated data as needed
];

function renderWorkflowDetails() {
    const workflowContainer = document.getElementById('workflow-container');
    workflowContainer.innerHTML = '';

    workflows.forEach(workflow => {
        const workflowDiv = document.createElement('div');
        workflowDiv.classList.add('workflow');

        const workflowHeader = document.createElement('h2');
        workflowHeader.textContent = workflow.name;
        workflowDiv.appendChild(workflowHeader);

        const approvalList = document.createElement('ul');
        approvalRequests.forEach(approval => {
            if ((workflow.id === 4) || (workflow.id !== 4 && approval.value > workflow.threshold)) {
                const approvalItem = document.createElement('li');
                approvalItem.innerHTML = `
                    <span>Approval ID: ${approval.id}</span>
                    <span>Value: ${approval.value}</span>
                    <span>Type: ${approval.type}</span>
                    <span>Status: ${approval.status}</span>
                    <button onclick="approveRequest(${approval.id})">Approve</button>
                    <button onclick="rejectRequest(${approval.id})">Reject</button>
                `;
                approvalList.appendChild(approvalItem);
            }
        });

        workflowDiv.appendChild(approvalList);
        workflowContainer.appendChild(workflowDiv);
    });
}

function approveRequest(approvalId) {
    
    console.log(`Approval ${approvalId} approved`);
   
    renderWorkflowDetails();
}

function rejectRequest(approvalId) {
  
    console.log(`Approval ${approvalId} rejected`);
    
    renderWorkflowDetails();
}
renderWorkflowDetails();

