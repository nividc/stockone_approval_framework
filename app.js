async function makeRequest(url, method = 'GET', body = null) {
    try {
        const response = await fetch(url, {
            method,
            headers: {
                'Content-Type': 'application/json',
                
            },
            body: body ? JSON.stringify(body) : null,
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Error making request:', error.message);
        throw error;
    }
}


function approveRequest(approvalId) {
    makeRequest(`http://localhost:3000/api/approval/approve/${approvalId}`, 'POST')
        .then(data => {
            console.log(`Approval ${approvalId} approved. Response:`, data);
            
            renderWorkflowDetails();
        })
        .catch(error => {
            
        });
}


function rejectRequest(approvalId) {
    makeRequest(`http://localhost:3000/api/approval/reject/${approvalId}`, 'POST')
        .then(data => {
            console.log(`Approval ${approvalId} rejected. Response:`, data);
            
            renderWorkflowDetails();
        })
        .catch(error => {
            
        });
}

// Function to render workflow details
function renderWorkflowDetails() {
    
}

renderWorkflowDetails();

