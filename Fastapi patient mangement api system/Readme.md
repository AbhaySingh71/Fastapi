<h1>🩺 FastAPI Patient Management System</h1>

<p>This project is a RESTful API for managing patient records, built with <strong>FastAPI</strong>. It allows users to perform CRUD operations on patient data stored in a <code>JSON</code> file. The system also computes BMI and gives health verdicts based on BMI values.</p>

<h2>🚀 Features</h2>
<ul>
  <li>Create new patient records</li>
  <li>Read all or specific patient details</li>
  <li>Update existing patient data</li>
  <li>Delete patient records</li>
  <li>Sort patients by <code>height</code>, <code>weight</code>, or <code>BMI</code></li>
  <li>Automatic BMI and health verdict calculation</li>
</ul>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li><strong>Framework:</strong> FastAPI</li>
  <li><strong>Language:</strong> Python</li>
  <li><strong>Data Storage:</strong> JSON file</li>
  <li><strong>Data Validation:</strong> Pydantic</li>
</ul>

<h2>🔍 Role of Pydantic</h2>
<p>
  <strong>Pydantic</strong> is used for data validation and parsing in this project. It ensures that all patient data (such as <code>age</code>, <code>height</code>, and <code>weight</code>) meets the specified constraints. For example:
</p>
<ul>
  <li><code>age</code> must be between 1 and 119</li>
  <li><code>height</code> and <code>weight</code> must be positive numbers</li>
  <li><code>gender</code> must be one of: 'male', 'female', or 'others'</li>
</ul>
<p>
  It also provides advanced features such as:
</p>
<ul>
  <li><strong>Computed fields</strong>: Automatically calculates <code>BMI</code> and generates a health <code>verdict</code> based on it</li>
  <li><strong>Partial updates</strong>: Using <code>Optional</code> fields in the update model to allow flexible edits</li>
  <li><strong>Serialization</strong>: Converts validated patient data into dictionaries for storage</li>
</ul>

<h2>📁 Project Structure</h2>
<pre>
├── main.py              # FastAPI backend logic
├── patients.json        # Database storing patient records
└── README.md            # Project documentation
</pre>

<h2>📦 Installation</h2>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/Abhaysingh71/fastapi-patient-management.git</code></pre>
  </li>
  <li>Navigate into the project:
    <pre><code>cd fastapi-patient-management</code></pre>
  </li>
  <li>Create a virtual environment and activate it (optional but recommended).</li>
  <li>Install the dependencies:
    <pre><code>pip install fastapi uvicorn pydantic</code></pre>
  </li>
  <li>Run the API server:
    <pre><code>uvicorn main:app --reload</code></pre>
  </li>
</ol>

<h2>🌐 API Endpoints</h2>

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Endpoint</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>GET</td><td>/</td><td>Home route</td></tr>
    <tr><td>GET</td><td>/about</td><td>API introduction</td></tr>
    <tr><td>GET</td><td>/view</td><td>View all patients</td></tr>
    <tr><td>GET</td><td>/patient/{patient_id}</td><td>View a specific patient</td></tr>
    <tr><td>GET</td><td>/sort?sort_by=bmi&order=asc</td><td>Sort patients</td></tr>
    <tr><td>POST</td><td>/create</td><td>Create a new patient</td></tr>
    <tr><td>PUT</td><td>/edit/{patient_id}</td><td>Edit an existing patient</td></tr>
    <tr><td>DELETE</td><td>/delete/{patient_id}</td><td>Delete a patient</td></tr>
  </tbody>
</table>

<h2>📌 Example Patient Record</h2>
<pre><code>{
  "id": "P006",
  "name": "John Doe",
  "city": "Delhi",
  "age": 30,
  "gender": "male",
  "height": 1.75,
  "weight": 70.0
}
</code></pre>

<h2>📊 BMI Verdict Logic</h2>
<ul>
  <li><strong>&lt; 18.5</strong> → Underweight</li>
  <li><strong>18.5 - 29.9</strong> → Normal</li>
  <li><strong>&ge; 30</strong> → Obese</li>
</ul>

<hr />
<p>Made with ❤️ using FastAPI and Pydantic</p>
