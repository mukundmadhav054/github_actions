# Copilot Instructions

## Project Overview
This is a **GitHub Actions learning project** that demonstrates CI/CD workflows for multiple programming languages and frameworks.

**Purpose:**
- Learn and practice GitHub Actions workflows
- Test CI/CD pipelines for Node.js and Python projects
- Experiment with automated testing and deployment

**Main Components:**
- `server/` - Node.js/Express backend server
- `python_workstream/` - Python Calculator class with pytest tests
- `.github/workflows/` - GitHub Actions CI/CD workflow definitions

## Architecture

### Project Structure
```
github_actions/
├── .github/
│   ├── workflows/
│   │   └── node-ci.yaml         # Node.js CI workflow
│   └── copilot-instructions.md  # This file
├── server/                      # Node.js Express server
│   ├── index.js                 # Express app entry point
│   ├── package.json             # Node dependencies
│   └── node_modules/
├── python_workstream/           # Python project
│   ├── main.py                  # Calculator class
│   ├── test_main.py             # Pytest test suite
│   ├── requirements.in          # High-level dependencies
│   └── requirements.txt         # Pinned dependencies
└── .venv/                       # Python virtual environment
```

### Key Components

**1. Node.js Server (`server/`)**
- Simple Express.js server on port 3000
- Returns "Hello World!" on root endpoint
- Used to test Node.js CI workflows

**2. Python Calculator (`python_workstream/`)**
- Calculator class with add, sub, multiply, divide methods
- Uses instance methods with `self` parameter
- Includes division by zero error handling
- Comprehensive pytest test suite (7 tests)

**3. GitHub Actions Workflows**
- `node-ci.yaml` - Runs on push/PR to main branch
  - Sets up Node.js 18
  - Installs dependencies from `server/` directory
  - Runs tests and build scripts

## Development Workflow

### Setup

**Node.js Server:**
```bash
cd server
npm install
```

**Python Project:**
```bash
cd python_workstream

# Create virtual environment (if not exists)
python -m venv ../.venv

# Activate virtual environment
# Windows:
../.venv/Scripts/activate
# Linux/Mac:
source ../.venv/bin/activate

# Install pip-tools and dependencies
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
```

### Running the Project

**Node.js Server:**
```bash
cd server
node index.js
# Server runs on http://localhost:3000
```

**Python Calculator:**
```bash
cd python_workstream
python main.py  # (No output - class definition only)
```

### Testing

**Node.js:**
```bash
cd server
npm test  # Currently placeholder: "No tests specified"
```

**Python (pytest):**
```bash
cd python_workstream
pytest test_main.py -v                    # Verbose output
pytest test_main.py --cov=main           # With coverage
pytest test_main.py::TestCalculator::test_add  # Specific test
```

### Building/Deployment

**Node.js:**
```bash
cd server
npm run build  # Currently placeholder: "No build step required"
```

**Python:**
```bash
# Update dependencies
cd python_workstream
pip-compile --upgrade requirements.in
pip install -r requirements.txt
```

**GitHub Actions:**
- Push to `main` branch triggers CI workflows automatically
- Workflows run tests and build steps
- Check Actions tab on GitHub for results

## Conventions & Patterns

### Code Style

**Node.js:**
- Language: JavaScript (ES6+)
- Runtime: Node.js 18
- Framework: Express.js 5.x
- Formatting: Standard JavaScript conventions

**Python:**
- Language: Python 3.13
- Testing: pytest with class-based test organization
- Formatting: Standard Python PEP 8
- Dependency management: pip-tools (requirements.in → requirements.txt)

### Common Patterns

**Python Calculator Class:**
- Instance methods use `self` as first parameter
- Methods accept `a, b` parameters for flexibility
- Division by zero returns error string instead of raising exception
- All tests organized in `TestCalculator` class with descriptive names

**GitHub Actions Workflows:**
- Use `working-directory` to specify context for commands
- Pin action versions (e.g., `@v3`)
- Separate jobs for different languages/frameworks
- Trigger on push/PR to `main` branch

## Important Notes

### Key Dependencies

**Node.js:**
- `express` - Web framework for building APIs
- `cors` - CORS middleware (devDependency)

**Python:**
- `pytest` - Testing framework
- `pytest-cov` - Coverage reporting for tests

### Known Gotchas

1. **GitHub Actions working directory**: Always specify `working-directory: ./server` or `./python_workstream` in workflow steps
2. **Python Calculator**: Methods require both `self` and `(a, b)` parameters - not using `@staticmethod`
3. **npm scripts**: Current test/build scripts are placeholders that don't fail CI
4. **Virtual environment**: Python uses `.venv` in root directory, shared across workspace

### Best Practices

- Keep `requirements.in` minimal with only direct dependencies
- Use `pip-compile` to generate locked `requirements.txt`
- Run pytest before pushing to ensure tests pass
- Check GitHub Actions logs if CI fails
- Node.js dependencies are in `server/` subdirectory, not root

### Future Enhancements

- [ ] Add actual unit tests for Node.js server
- [ ] Add Python CI workflow alongside Node.js workflow
- [ ] Implement real build step for Node.js
- [ ] Add code coverage reports to CI
- [ ] Deploy workflows for staging/production

---
*Last updated: 2025-10-19*
