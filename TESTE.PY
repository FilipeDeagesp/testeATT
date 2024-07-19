import os
import shutil

# Criar a estrutura de diretórios
project_dir = '/mnt/data/public-procurement-planning'
os.makedirs(f'{project_dir}/models', exist_ok=True)
os.makedirs(f'{project_dir}/public', exist_ok=True)

# Escrever os arquivos no diretório apropriado
files = {
    'models/AnnualPlan.js': '''
const mongoose = require('mongoose');

const annualPlanSchema = new mongoose.Schema({
    year: { type: Number, required: true },
    description: { type: String, required: true }
});

module.exports = mongoose.model('AnnualPlan', annualPlanSchema);
''',
    'models/Compliance.js': '''
const mongoose = require('mongoose');

const complianceSchema = new mongoose.Schema({
    norms: { type: String, required: true }
});

module.exports = mongoose.model('Compliance', complianceSchema);
''',
    'models/CostEstimate.js': '''
const mongoose = require('mongoose');

const costEstimateSchema = new mongoose.Schema({
    title: { type: String, required: true },
    amount: { type: Number, required: true }
});

module.exports = mongoose.model('CostEstimate', costEstimateSchema);
''',
    'models/Demand.js': '''
const mongoose = require('mongoose');

const demandSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String, required: true },
    attachments: { type: [String], required: true }
});

module.exports = mongoose.model('Demand', demandSchema);
''',
    'models/Security.js': '''
const mongoose = require('mongoose');

const securitySchema = new mongoose.Schema({
    protocols: { type: String, required: true }
});

module.exports = mongoose.model('Security', securitySchema);
''',
    'models/Support.js': '''
const mongoose = require('mongoose');

const supportSchema = new mongoose.Schema({
    issue: { type: String, required: true }
});

module.exports = mongoose.model('Support', supportSchema);
''',
    'models/TechnicalStudy.js': '''
const mongoose = require('mongoose');

const technicalStudySchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true }
});

module.exports = mongoose.model('TechnicalStudy', technicalStudySchema);
''',
    'models/TermReference.js': '''
const mongoose = require('mongoose');

const termReferenceSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true }
});

module.exports = mongoose.model('TermReference', termReferenceSchema);
''',
    'models/User.js': '''
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const userSchema = new mongoose.Schema({
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true }
});

userSchema.pre('save', function (next) {
    if (!this.isModified('password')) {
        return next();
    }

    const salt = bcrypt.genSaltSync(10);
    this.password = bcrypt.hashSync(this.password, salt);
    next();
});

module.exports = mongoose.model('User', userSchema);
''',
    'public/annual_planning.html': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Annual Planning - Public Procurement</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <div class="container mx-auto p-4">
        <h1 class="text-4xl font-bold text-center mb-4">Annual Procurement Planning</h1>
        <div class="bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-bold mb-4">Register Annual Plan</h2>
            <form id="annualPlanForm">
                <div class="mb-4">
                    <label for="year" class="block text-gray-700">Year:</label>
                    <input type="number" id="year" class="w-full p-2 border border-gray-300 rounded" required>
                </div>
                <div class="mb-4">
                    <label for="description" class="block text-gray-700">Description:</label>
                    <textarea id="description" class="w-full p-2 border border-gray-300 rounded" required></textarea>
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded">Submit</button>
            </form>
        </div>
    </div>
    <script src="annual_planning.js"></script>
</body>
</html>
''',
    'public/compliance.html': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Legal Compliance - Public Procurement</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <div class="container mx-auto p-4">
        <h1 class="text-4xl font-bold text-center mb-4">Legal Compliance</h1>
        <div class="bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-bold mb-4">Update Norms</h2>
            <form id="complianceForm">
                <div class="mb-4">
                    <label for="norms" class="block text-gray-700">Norms:</label>
                    <textarea id="norms" class="w-full p-2 border border-gray-300 rounded" required></textarea>
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded">Update</button>
            </form>
        </div>
    </div>
    <script src="compliance.js"></script>
</body>
</html>
''',
    'public/cost_management.html': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cost Management - Public Procurement</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <div class="container mx-auto p-4">
        <h1 class="text-4xl font-bold text-center mb-4">Cost Management</h1>
        <div class="bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-bold mb-4">Estimate Costs</h2>
            <form id="costEstimateForm">
                <div class="mb-4">
                    <label for="costTitle" class="block text-gray-700">Title:</label>
                    <input type="text" id="costTitle" class="w-full p-2 border border-gray-300 rounded" required>
                </div>
                <div class="mb-4">
                    <label for="costAmount" class="block text-gray-700">Amount:</label>
                    <input type="number" id="costAmount" class="w-full p-2 border border-gray-300 rounded" required>
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded">Submit</button>
            </form>
        </div>
    </div>
    <script src="cost_management.js"></script>
</body>
</html>
''',
    'public/dashboard.html': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - Public Procurement Planning</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <div class="container mx-auto p-4">
        <h1 class="text-4xl font-bold text-center mb-4">Public Procurement Planning Dashboard</h1>
        <div class="grid grid-cols-3 gap-4">
            <div class="bg-white p-6 rounded-lg shadow-md">
                <h2 class="text-2xl font-bold mb-4">Annual Planning</h2>
                <a href="annual_planning.html" class="block bg-blue-500 text-white p-2 rounded text-center">Manage</a>
            </div>
            <div class="bg-white p-6 rounded-lg shadow-md">
                <h2 class="text-2xl font-bold mb-4">Demand Formalization</h2>
                <a href="demand_formalization.html" class="block bg-blue-500 text-white p-2 rounded text-center">Manage</a>
            </div>
            <div class="bg-white p-6 rounded-lg shadow-md">
                <h2 class="text-2xl font-bold mb-4">Technical Studies</h2>
                <a href="technical_studies.html" class="block bg-blue-500 text-white p-2 rounded text-center">Manage</a>
            </div>
            <div class="bg-white p-6 rounded-lg shadow-md">
                <h2 class="text-2xl font-bold mb-4">Terms of Reference</h2>
                <a href="terms_reference.html" class="block bg-blue-500 text-white p-2 rounded text-center">Manage</a>
            </div>
            <div class="bg-white p-6 rounded-lg shadow-md">
                <h2 class="text-2xl font-bold mb-4">Cost Management</h2>
                <a href="cost_management.html" class="block bg-blue-500 text-white p-2 rounded text-center">Manage</a>
            </div>
        </div>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const token = localStorage.getItem('token');
            if (!token) {
                window.location.href = 'index.html';
            }
        });
    </script>
</body>
</html>
''',
    'public/demand_formalization.html': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demand Formalization - Public Procurement</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <div class="container mx-auto p-4">
        <h1 class="text-4xl font-bold text-center mb-4">Demand Formalization</h1>
        <div class="bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-bold mb-4">Register Demand</h2>
            <form id="demandForm">
                <div class="mb-4">
                    <label for="demandName" class="block text-gray-700">Demand Name:</label>
                    <input type="text" id="demandName" class="w-full p-2 border border-gray-300 rounded" required>
                </div>
                <div class="mb-4">
                    <label for="demandDescription" class="block text-gray-700">Description:</label>
                    <textarea id="demandDescription" class="w-full p-2 border border-gray-300 rounded" required></textarea>
                </div>
                <div class="mb-4">
                    <label for="attachments" class="block text-gray-700">Attachments:</label>
                    <input type="file" id="attachments" class="w-full p-2 border border-gray-300 rounded" multiple>
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded">Submit</button>
            </form>
        </div>
    </div>
    <script src="demand_formalization.js"></script>
</body>
</html>
''',
    'public/index.html': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Public Procurement Planning</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <div class="container mx-auto p-4">
        <h1 class="text-4xl font-bold text-center mb-4">Welcome to Public Procurement Planning</h1>
        <div class="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-bold mb-4">Login</h2>
            <form id="loginForm">
                <div class="mb-4">
                    <label for="email" class="block text-gray-700">Email:</label>
                    <input type="email" id="email" class="w-full p-2 border border-gray-300 rounded" required>
                </div>
                <div class="mb-4">
                    <label for="password" class="block text-gray-700">Password:</label>
                    <input type="password" id="password" class="w-full p-2 border border-gray-300 rounded" required>
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded">Login</button>
                <p class="text-sm text-center text-gray-500 mt-4">
                    <a href="#" id="forgotPassword" class="text-blue-500">Forgot password?</a>
                </p>
            </form>
        </div>
    </div>
    <script src="login.js"></script>
</body>
</html>
''',
    'public/security.html': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Information Security - Public Procurement</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <div class="container mx-auto p-4">
        <h1 class="text-4xl font-bold text-center mb-4">Information Security</h1>
        <div class="bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-bold mb-4">Data Protection</h2>
            <form id="securityForm">
                <div class="mb-4">
                    <label for="protocols" class="block text-gray-700">Protocols:</label>
                    <textarea id="protocols" class="w-full p-2 border border-gray-300 rounded" required></textarea>
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded">Update</button>
            </form>
        </div>
    </div>
    <script src="security.js"></script>
</body>
</html>
''',
    'public/support.html': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Technical Support - Public Procurement</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <div class="container mx-auto p-4">
        <h1 class="text-4xl font-bold text-center mb-4">Technical Support</h1>
        <div class="bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-bold mb-4">Support Request</h2>
            <form id="supportForm">
                <div class="mb-4">
                    <label for="issue" class="block text-gray-700">Issue:</label>
                    <textarea id="issue" class="w-full p-2 border border-gray-300 rounded" required></textarea>
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded">Submit</button>
            </form>
        </div>
    </div>
    <script src="support.js"></script>
</body>
</html>
''',
    'public/technical_studies.html': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Technical Studies - Public Procurement</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <div class="container mx-auto p-4">
        <h1 class="text-4xl font-bold text-center mb-4">Preliminary Technical Studies</h1>
        <div class="bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-bold mb-4">Create Technical Study</h2>
            <form id="technicalStudyForm">
                <div class="mb-4">
                    <label for="studyTitle" class="block text-gray-700">Title:</label>
                    <input type="text" id="studyTitle" class="w-full p-2 border border-gray-300 rounded" required>
                </div>
                <div class="mb-4">
                    <label for="studyDescription" class="block text-gray-700">Description:</label>
                    <textarea id="studyDescription" class="w-full p-2 border border-gray-300 rounded" required></textarea>
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded">Submit</button>
            </form>
        </div>
    </div>
    <script src="technical_studies.js"></script>
</body>
</html>
''',
    'public/terms_reference.html': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms of Reference - Public Procurement</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <div class="container mx-auto p-4">
        <h1 class="text-4xl font-bold text-center mb-4">Terms of Reference</h1>
        <div class="bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-bold mb-4">Create Term of Reference</h2>
            <form id="termsReferenceForm">
                <div class="mb-4">
                    <label for="referenceTitle" class="block text-gray-700">Title:</label>
                    <input type="text" id="referenceTitle" class="w-full p-2 border border-gray-300 rounded" required>
                </div>
                <div class="mb-4">
                    <label for="referenceDescription" class="block text-gray-700">Description:</label>
                    <textarea id="referenceDescription" class="w-full p-2 border border-gray-300 rounded" required></textarea>
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded">Submit</button>
            </form>
        </div>
    </div>
    <script src="terms_reference.js"></script>
</body>
</html>
''',
    'public/annual_planning.js': '''
document.getElementById('annualPlanForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const year = document.getElementById('year').value;
    const description = document.getElementById('description').value;
    const token = localStorage.getItem('token');

    try {
        const response = await fetch('/api/annual-planning', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ year, description })
        });

        if (response.ok) {
            alert('Annual plan registered successfully');
        } else {
            alert('Failed to register annual plan');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
    }
});
''',
    'public/compliance.js': '''
document.getElementById('complianceForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const norms = document.getElementById('norms').value;
    const token = localStorage.getItem('token');

    try {
        const response = await fetch('/api/compliance', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ norms })
        });

        if (response.ok) {
            alert('Norms updated successfully');
        } else {
            alert('Failed to update norms');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
    }
});
''',
    'public/cost_management.js': '''
document.getElementById('costEstimateForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = document.getElementById('costTitle').value;
    const amount = document.getElementById('costAmount').value;
    const token = localStorage.getItem('token');

    try {
        const response = await fetch('/api/cost-management', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ title, amount })
        });

        if (response.ok) {
            alert('Cost estimate registered successfully');
        } else {
            alert('Failed to register cost estimate');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
    }
});
''',
    'public/demand_formalization.js': '''
document.getElementById('demandForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const demandName = document.getElementById('demandName').value;
    const demandDescription = document.getElementById('demandDescription').value;
    const attachments = document.getElementById('attachments').files;
    const token = localStorage.getItem('token');

    const formData = new FormData();
    formData.append('name', demandName);
    formData.append('description', demandDescription);
    for (let i = 0; i < attachments.length; i++) {
        formData.append('attachments', attachments[i]);
    }

    try {
        const response = await fetch('/api/demand-formalization', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`
            },
            body: formData
        });

        if (response.ok) {
            alert('Demand registered successfully');
        } else {
            alert('Failed to register demand');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
    }
});
''',
    'public/login.js': '''
document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('token', data.token);
            window.location.href = '/dashboard.html';
        } else {
            alert('Login failed');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
    }
});
''',
    'public/security.js': '''
document.getElementById('securityForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const protocols = document.getElementById('protocols').value;
    const token = localStorage.getItem('token');

    try {
        const response = await fetch('/api/security', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ protocols })
        });

        if (response.ok) {
            alert('Security protocols updated successfully');
        } else {
            alert('Failed to update security protocols');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
    }
});
''',
    'public/support.js': '''
document.getElementById('supportForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const issue = document.getElementById('issue').value;
    const token = localStorage.getItem('token');

    try {
        const response = await fetch('/api/support', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ issue })
        });

        if (response.ok) {
            alert('Support request submitted successfully');
        } else {
            alert('Failed to submit support request');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
    }
});
''',
    'public/technical_studies.js': '''
document.getElementById('technicalStudyForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = document.getElementById('studyTitle').value;
    const description = document.getElementById('studyDescription').value;
    const token = localStorage.getItem('token');

    try {
        const response = await fetch('/api/technical-studies', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ title, description })
        });

        if (response.ok) {
            alert('Technical study created successfully');
        } else {
            alert('Failed to create technical study');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
    }
});
''',
    'public/terms_reference.js': '''
document.getElementById('termsReferenceForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = document.getElementById('referenceTitle').value;
    const description = document.getElementById('referenceDescription').value;
    const token = localStorage.getItem('token');

    try {
        const response = await fetch('/api/terms-reference', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ title, description })
        });

        if (response.ok) {
            alert('Term of reference created successfully');
        } else {
            alert('Failed to create term of reference');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
    }
});
''',
    'package.json': '''
{
  "name": "public-procurement-planning",
  "version": "1.0.0",
  "description": "A system for planning public procurement according to Brazilian legislation.",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "bcryptjs": "^2.4.3",
    "express": "^4.17.1",
    "jsonwebtoken": "^8.5.1",
    "mongoose": "^5.11.15",
    "multer": "^1.4.2"
  },
  "author": "",
  "license": "ISC"
}
''',
    'server.js': '''
const express = require('express');
const mongoose = require('mongoose');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });

const User = require('./models/User');
const AnnualPlan = require('./models/AnnualPlan');
const Compliance = require('./models/Compliance');
const CostEstimate = require('./models/CostEstimate');
const Demand = require('./models/Demand');
const Security = require('./models/Security');
const Support = require('./models/Support');
const TechnicalStudy = require('./models/TechnicalStudy');
const TermReference = require('./models/TermReference');

const app = express();
app.use(express.json());
app.use(express.static('public'));

mongoose.connect('mongodb://localhost:27017/public_procurement', { useNewUrlParser: true, useUnifiedTopology: true });

// Middleware para verificar JWT
function authenticateToken(req, res, next) {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];
    if (token == null) return res.sendStatus(401);

    jwt.verify(token, 'secret', (err, user) => {
        if (err) return res.sendStatus(403);
        req.user = user;
        next();
    });
}

app.post('/api/login', async (req, res) => {
    const { email, password } = req.body;
    const user = await User.findOne({ email });

    if (user && bcrypt.compareSync(password, user.password)) {
        const token = jwt.sign({ id: user._id }, 'secret', { expiresIn: '1h' });
        res.json({ token });
    } else {
        res.status(401).send('Invalid credentials');
    }
});

app.post('/api/annual-planning', authenticateToken, async (req, res) => {
    const { year, description } = req.body;
    const newPlan = new AnnualPlan({ year, description });

    try {
        await newPlan.save();
        res.status(201).send('Annual plan registered successfully');
    } catch (error) {
        res.status(400).send('Failed to register annual plan');
    }
});

app.post('/api/demand-formalization', [authenticateToken, upload.array('attachments')], async (req, res) => {
    const { name, description } = req.body;
    const attachments = req.files.map(file => file.path);
    const newDemand = new Demand({ name, description, attachments });

    try {
        await newDemand.save();
        res.status(201).send('Demand registered successfully');
    } catch (error) {
        res.status(400).send('Failed to register demand');
    }
});

app.post('/api/technical-studies', authenticateToken, async (req, res) => {
    const { title, description } = req.body;
    const newStudy = new TechnicalStudy({ title, description });

    try {
        await newStudy.save();
        res.status(201).send('Technical study created successfully');
    } catch (error) {
        res.status(400).send('Failed to create technical study');
    }
});

app.post('/api/terms-reference', authenticateToken, async (req, res) => {
    const { title, description } = req.body;
    const newTerm = new TermReference({ title, description });

    try {
        await newTerm.save();
        res.status(201).send('Term of reference created successfully');
    } catch (error) {
        res.status(400).send('Failed to create term of reference');
    }
});

app.post('/api/cost-management', authenticateToken, async (req, res) => {
    const { title, amount } = req.body;
    const newEstimate = new CostEstimate({ title, amount });

    try {
        await newEstimate.save();
        res.status(201).send('Cost estimate registered successfully');
    } catch (error) {
        res.status(400).send('Failed to register cost estimate');
    }
});

app.post('/api/compliance', authenticateToken, async (req, res) => {
    const { norms } = req.body;
    const newCompliance = new Compliance({ norms });

    try {
        await newCompliance.save();
        res.status(201).send('Norms updated successfully');
    } catch (error) {
        res.status(400).send('Failed to update norms');
    }
});

app.post('/api/security', authenticateToken, async (req, res) => {
    const { protocols } = req.body;
    const newSecurity = new Security({ protocols });

    try {
        await newSecurity.save();
        res.status(201).send('Security protocols updated successfully');
    } catch (error) {
        res.status(400).send('Failed to update security protocols');
    }
});

app.post('/api/support', authenticateToken, async (req, res) => {
    const { issue } = req.body;
    const newSupport = new Support({ issue });

    try {
        await newSupport.save();
        res.status(201).send('Support request submitted successfully');
    } catch (error) {
        res.status(400).send('Failed to submit support request');
    }
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
'''
}

for path, content in files.items():
    with open(f'{project_dir}/{path}', 'w') as file:
        file.write(content)

# Comprimir a pasta em um arquivo zip
shutil.make_archive('/mnt/data/public-procurement-planning', 'zip', project_dir)
