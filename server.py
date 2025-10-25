from fastmcp import FastMCP

mcp = FastMCP("Company MCP Server")

COMPANY_PEOPLE = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "position": "CEO",
        "department": "Executive",
        "email": "alice.johnson@company.com",
        "hire_date": "2015-01-15",
        "salary": 250000
    },
    {
        "id": 2,
        "name": "Bob Smith",
        "position": "CTO",
        "department": "Technology",
        "email": "bob.smith@company.com",
        "hire_date": "2016-03-20",
        "salary": 200000
    },
    {
        "id": 3,
        "name": "Carol Martinez",
        "position": "CFO",
        "department": "Finance",
        "email": "carol.martinez@company.com",
        "hire_date": "2016-06-10",
        "salary": 195000
    },
    {
        "id": 4,
        "name": "David Lee",
        "position": "Senior Engineer",
        "department": "Technology",
        "email": "david.lee@company.com",
        "hire_date": "2018-02-14",
        "salary": 140000
    },
    {
        "id": 5,
        "name": "Emma Wilson",
        "position": "Product Manager",
        "department": "Product",
        "email": "emma.wilson@company.com",
        "hire_date": "2019-05-22",
        "salary": 130000
    },
    {
        "id": 6,
        "name": "Frank Chen",
        "position": "Sales Director",
        "department": "Sales",
        "email": "frank.chen@company.com",
        "hire_date": "2017-08-30",
        "salary": 150000
    },
    {
        "id": 7,
        "name": "Grace Kim",
        "position": "HR Manager",
        "department": "Human Resources",
        "email": "grace.kim@company.com",
        "hire_date": "2018-11-05",
        "salary": 110000
    },
    {
        "id": 8,
        "name": "Henry Taylor",
        "position": "Marketing Manager",
        "department": "Marketing",
        "email": "henry.taylor@company.com",
        "hire_date": "2019-01-15",
        "salary": 115000
    },
    {
        "id": 9,
        "name": "Iris Anderson",
        "position": "Junior Engineer",
        "department": "Technology",
        "email": "iris.anderson@company.com",
        "hire_date": "2022-07-01",
        "salary": 85000
    },
    {
        "id": 10,
        "name": "Jack Brown",
        "position": "Operations Manager",
        "department": "Operations",
        "email": "jack.brown@company.com",
        "hire_date": "2020-09-12",
        "salary": 120000
    }
]

LEGAL_DOCUMENTS = {
    "employment-agreement": """
# Employment Agreement

This Employment Agreement ("Agreement") is entered into between Company Inc. ("Employer") and the Employee.

## 1. Position and Duties
The Employee agrees to serve in the capacity specified in the offer letter and perform duties as assigned.

## 2. Compensation
Compensation details are provided in the offer letter and are subject to standard withholdings.

## 3. Term
Employment is at-will and may be terminated by either party with notice as required by law.

## 4. Confidentiality
Employee agrees to maintain confidentiality of all proprietary information.

## 5. Non-Compete
Employee agrees not to compete with Employer during employment and for 12 months thereafter.
""",
    "nda": """
# Non-Disclosure Agreement (NDA)

This Non-Disclosure Agreement is made between Company Inc. and the undersigned party.

## 1. Definition of Confidential Information
All business, technical, and financial information disclosed by Company Inc.

## 2. Obligations
Recipient agrees to keep confidential information secure and not disclose to third parties.

## 3. Duration
This agreement remains in effect for 5 years from the date of signing.

## 4. Return of Materials
Upon termination, all materials must be returned to Company Inc.
""",
    "code-of-conduct": """
# Code of Conduct

Company Inc. is committed to maintaining a professional and respectful workplace.

## 1. Professional Behavior
All employees must treat colleagues with respect and dignity.

## 2. Ethical Standards
Employees must maintain high ethical standards and avoid conflicts of interest.

## 3. Workplace Safety
Maintain a safe working environment and report any concerns immediately.

## 4. Reporting Violations
Report any violations to HR or management without fear of retaliation.
""",
    "intellectual-property-policy": """
# Intellectual Property Policy

This policy governs ownership of intellectual property created during employment.

## 1. Company Ownership
All work product created during employment belongs to Company Inc.

## 2. Disclosure Requirements
Employees must disclose all inventions and creations to management.

## 3. Patent Rights
Company Inc. retains all patent rights for employee inventions related to business.

## 4. Prior Inventions
Employees should disclose any prior inventions at time of hiring.
""",
    "remote-work-policy": """
# Remote Work Policy

Guidelines for employees working remotely.

## 1. Eligibility
Remote work is available to employees whose roles permit such arrangements.

## 2. Equipment
Company will provide necessary equipment for remote work.

## 3. Work Hours
Employees must maintain regular work hours and be available during core business hours.

## 4. Security
Employees must maintain secure work environments and protect company data.
""",
    "data-privacy-policy": """
# Data Privacy Policy

Company Inc. is committed to protecting employee and customer data.

## 1. Data Collection
We collect only necessary data for business operations.

## 2. Data Usage
Data is used only for legitimate business purposes.

## 3. Data Protection
We implement industry-standard security measures to protect data.

## 4. Data Rights
Individuals have rights to access, correct, and delete their personal data.
""",
    "expense-reimbursement-policy": """
# Expense Reimbursement Policy

Guidelines for submitting and approving business expenses.

## 1. Eligible Expenses
Travel, meals, lodging, and other business-related expenses are eligible.

## 2. Submission Process
Submit expense reports within 30 days with proper documentation.

## 3. Approval Process
Expenses require manager approval before reimbursement.

## 4. Reimbursement Timeline
Approved expenses are reimbursed within 14 business days.
""",
    "vacation-leave-policy": """
# Vacation and Leave Policy

Company Inc. provides competitive time off benefits.

## 1. Vacation Accrual
Employees accrue vacation days based on tenure and position.

## 2. Sick Leave
Employees receive separate sick leave allocation.

## 3. Requesting Time Off
Submit requests through HR system at least 2 weeks in advance.

## 4. Carryover
Unused vacation may be carried over subject to annual limits.
""",
    "equal-opportunity-policy": """
# Equal Opportunity Employment Policy

Company Inc. is an equal opportunity employer.

## 1. Non-Discrimination
We do not discriminate based on protected characteristics.

## 2. Reasonable Accommodations
We provide reasonable accommodations for qualified individuals.

## 3. Complaint Procedure
Report discrimination concerns to HR immediately.

## 4. Anti-Retaliation
Retaliation against those who report violations is strictly prohibited.
""",
    "social-media-policy": """
# Social Media Policy

Guidelines for employee use of social media.

## 1. Personal Use
Employees may use social media but must not disclose confidential information.

## 2. Company Representation
Clearly state personal views do not represent Company Inc.

## 3. Professional Conduct
Maintain professional standards when discussing work-related matters.

## 4. Prohibited Content
Do not post disparaging, harassing, or discriminatory content.
"""
}


@mcp.tool()
def calculate(operation: str, a: float, b: float) -> str:
    """
    Perform basic arithmetic operations.

    Args:
        operation: The operation to perform (add, subtract, multiply, divide)
        a: First number
        b: Second number

    Returns:
        Result of the calculation
    """
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else "Error: Division by zero"
    }

    result = operations.get(operation.lower())
    if result is None:
        return f"Error: Unknown operation '{operation}'. Available: add, subtract, multiply, divide"

    return f"{a} {operation} {b} = {result}"


@mcp.tool()
def get_employees(department: str = None) -> list:
    """
    Get list of employees, optionally filtered by department.

    Args:
        department: Optional department name to filter by

    Returns:
        List of employee records
    """
    if department:
        return [emp for emp in COMPANY_PEOPLE if emp["department"].lower() == department.lower()]
    return COMPANY_PEOPLE


@mcp.tool()
def get_employee_by_id(employee_id: int) -> dict:
    """
    Get employee details by ID.

    Args:
        employee_id: The employee ID

    Returns:
        Employee record or error message
    """
    for emp in COMPANY_PEOPLE:
        if emp["id"] == employee_id:
            return emp
    return {"error": f"Employee with ID {employee_id} not found"}


@mcp.resource("legal://employment-agreement")
def get_employment_agreement() -> str:
    """Employment Agreement document"""
    return LEGAL_DOCUMENTS["employment-agreement"]


@mcp.resource("legal://nda")
def get_nda() -> str:
    """Non-Disclosure Agreement document"""
    return LEGAL_DOCUMENTS["nda"]


@mcp.resource("legal://code-of-conduct")
def get_code_of_conduct() -> str:
    """Code of Conduct document"""
    return LEGAL_DOCUMENTS["code-of-conduct"]


@mcp.resource("legal://intellectual-property-policy")
def get_ip_policy() -> str:
    """Intellectual Property Policy document"""
    return LEGAL_DOCUMENTS["intellectual-property-policy"]


@mcp.resource("legal://remote-work-policy")
def get_remote_work_policy() -> str:
    """Remote Work Policy document"""
    return LEGAL_DOCUMENTS["remote-work-policy"]


@mcp.resource("legal://data-privacy-policy")
def get_data_privacy_policy() -> str:
    """Data Privacy Policy document"""
    return LEGAL_DOCUMENTS["data-privacy-policy"]


@mcp.resource("legal://expense-reimbursement-policy")
def get_expense_policy() -> str:
    """Expense Reimbursement Policy document"""
    return LEGAL_DOCUMENTS["expense-reimbursement-policy"]


@mcp.resource("legal://vacation-leave-policy")
def get_vacation_policy() -> str:
    """Vacation and Leave Policy document"""
    return LEGAL_DOCUMENTS["vacation-leave-policy"]


@mcp.resource("legal://equal-opportunity-policy")
def get_equal_opportunity_policy() -> str:
    """Equal Opportunity Employment Policy document"""
    return LEGAL_DOCUMENTS["equal-opportunity-policy"]


@mcp.resource("legal://social-media-policy")
def get_social_media_policy() -> str:
    """Social Media Policy document"""
    return LEGAL_DOCUMENTS["social-media-policy"]


if __name__ == "__main__":
    mcp.run()
