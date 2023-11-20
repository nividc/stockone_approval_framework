const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 4000;

app.use(bodyParser.json());


let approvals = [];


app.get('/approval/status/:id', (req, res) => {
    const approvalId = parseInt(req.params.id);
    const approval = approvals.find(approval => approval.id === approvalId);

    if (approval) {
        res.json(approval);
    } else {
        res.status(404).json({ error: 'Approval not found' });
    }
});


app.post('/approval/approve/:id', (req, res) => {
    const approvalId = parseInt(req.params.id);
    const approval = approvals.find(approval => approval.id === approvalId);

    if (approval) {
        approval.status = 'Approved';
        res.json(approval);
    } else {
        res.status(404).json({ error: 'Approval not found' });
    }
});


app.post('/approval/reject/:id', (req, res) => {
    const approvalId = parseInt(req.params.id);
    const approval = approvals.find(approval => approval.id === approvalId);

    if (approval) {
        approval.status = 'Rejected';
        res.json(approval);
    } else {
        res.status(404).json({ error: 'Approval not found' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

