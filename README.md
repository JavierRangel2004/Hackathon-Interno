# Backend for Sustainability Certifications Platform

This repository contains the backend code for a platform aimed at helping companies in Mexico achieve sustainability certifications and improve their environmental impact. Our platform offers a comprehensive suite of tools and services including information on certifications, customized consulting, waste management advice, self-assessment tools, a sustainable supplier network, community forums, and more.

## Features

- **Information and Guidelines on Certifications**: Detailed information on various sustainability certifications available in Mexico, including requirements, application processes, and benefits.

- **Customized Consulting**: Tailored consulting services to assist companies in complying with certification requirements through practice assessments and improvement strategies.

- **Waste and Pollution Management**: Solutions and advice for effective waste management, pollution reduction, and resource optimization.

- **Self-Assessment Tools**: In-app tools for companies to evaluate their sustainability performance and identify areas for enhancement.

- **Sustainable Supplier Network**: A network facilitating access to sustainable products and services from vetted suppliers.

- **Forums and Community**: A platform for companies to exchange sustainability challenges, experiences, and solutions.

- **Updates and News**: The latest trends, news, and legislative changes in sustainability and environmental certifications.

- **Trainings and Webinars**: Online educational programs on business sustainability led by field experts.

- **Rewards and Rankings**: A system to recognize companies for their environmental efforts, encouraging a friendly progression towards sustainability without direct competition.

- **Multi-role Logins**: Access for both advisors and companies, tailored to their specific needs and roles within the platform.

## Setting Up the Development Environment

To set up the project's development environment, follow these steps:

### Prerequisites

- Python (3.8 or newer recommended)
- pip (Python package manager)

### 1. Clone the Repository

```bash
git clone https://your-repository-url.git
cd your-repository-directory
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- On Windows:

```bash
.\venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

### 5. Database Migrations

To create or update the database schema, run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The server will start, typically on `http://127.0.0.1:8000/`. You can now access the API endpoints as defined in the project documentation.

## Contribution Guidelines

To contribute to this project, please follow the guidelines provided in `CONTRIBUTING.md`.

## License

This project is licensed under the [LICENSE-NAME]. See the `LICENSE` file for details.
