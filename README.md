# FastAPI Learning Project

## Overview
This repository documents my journey learning FastAPI, exploring its core concepts and best practices. FastAPI is a modern, high-performance web framework for building APIs with Python 3.6+ that leverages standard Python type hints.

## Learning Objectives
- Understanding FastAPI fundamentals
- Implementing RESTful API patterns
- Working with request/response models
- Handling different types of parameters
- Data validation and type checking
- API documentation

## Core Concepts Covered

### 1. Basic Route Operations
- HTTP methods (GET, POST, PUT)
- Route declarations
- Async handlers
- Route parameters

### 2. Parameter Types
- Path parameters
- Query parameters
- Request body
- Optional parameters
- Parameter validation

### 3. Data Handling
- Pydantic models
- Data validation
- Type hints
- Enums
- Response models

### 4. Advanced Features
- Parameter validation using Query class
- Custom validations
- Route deprecation
- Schema manipulation
- Hidden parameters
- API documentation customization

## Project Structure
```
fastapi-tutorial/
│
├── main.py          # Main application file
├── README.md        # Project documentation
└── requirements.txt # Project dependencies
```

## Setup and Installation

### Prerequisites
```bash
Python 3.6+
FastAPI
Uvicorn (ASGI server)
```

### Installation Steps
```bash
# Create and activate virtual environment
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

### Accessing API Documentation
Once the server is running:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Key Learning Points

### FastAPI Basics
- Route handling and HTTP methods
- Asynchronous request processing
- Path operations and parameters
- Request/Response cycle

### Data Validation
- Input validation using Pydantic
- Query parameter validation
- Path parameter constraints
- Type checking and conversion

### API Documentation
- Automatic OpenAPI generation
- Swagger UI integration
- ReDoc documentation
- Schema customization

## Development Practices
- Type hints usage
- Modern Python features
- RESTful API conventions
- Clean code principles
- API versioning
- Error handling

## Testing
To run the tests (when implemented):
```bash
pytest
```

## Future Learning Goals
- [ ] Database integration (SQL and NoSQL)
- [ ] Authentication and Authorization
- [ ] WebSocket implementation
- [ ] Background tasks
- [ ] File handling
- [ ] Dependency injection
- [ ] Custom middleware
- [ ] Testing strategies

## Resources
- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Starlette Documentation](https://www.starlette.io/)
- [Python Type Hints Documentation](https://docs.python.org/3/library/typing.html)

## Contributing
This is a personal learning project, but suggestions for improvement are welcome. Feel free to:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.