# construction-dashboard/README.md

# Construction Project Dashboard

## Overview

The Construction Project Dashboard is a web application designed to manage and track various aspects of construction projects. It provides a comprehensive interface for project stakeholders, including owners, contractors, subcontractors, and design teams, to collaborate effectively and monitor project progress.

## Features

- **User Roles**: Supports multiple user roles including Owner, Owner's Representative, General Contractor, Subcontractor, and Design Team.
- **CRUD Operations**: Create, Read, Update, and Delete functionalities for various project modules.
- **Safety Module**: Manage safety observations and incident reports with detailed tracking and reporting.
- **Engineering Module**: Handle RFIs, submittals, drawings, specifications, and more.
- **Field Module**: Track daily reports, schedules, checklists, and punchlists.
- **Contracts Module**: Manage prime contracts, subcontracts, and professional service agreements.
- **Cost Module**: Budgeting, invoicing, and change order management.
- **BIM Module**: 3D model integration and coordination issue tracking.
- **Closeout Module**: Manage O&M manuals, warranties, and attic stock.
- **Reporting**: Generate reports and export data to PDF.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **SQLAlchemy**: ORM for database management.
- **Bootstrap**: Front-end framework for responsive design.
- **Web3.js**: JavaScript library for interacting with Ethereum blockchain.
- **Supabase**: Backend as a service for database management.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/construction-dashboard.git
   cd construction-dashboard
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   - Create a `.env` file based on the `.env.example` provided.
   - Configure your database connection and other settings.

5. Run the application:
   ```
   python run.py
   ```

## Usage

- Access the application at `http://localhost:5000`.
- Log in with your credentials based on your assigned user role.
- Navigate through the dashboard to access different modules and functionalities.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.