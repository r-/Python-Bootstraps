import os

def create_project_structure(project_name):
    # Convert spaces to underscores and lowercase the name
    project_slug = project_name.replace(" ", "_").lower()
    
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the full path for the project
    project_base_path = os.path.join(script_dir, project_slug)

    # Define folder structure
    folders = [
        project_base_path,
        os.path.join(project_base_path, "config"),
        os.path.join(project_base_path, project_slug),
        os.path.join(project_base_path, "tests"),
        os.path.join(project_base_path, "docs"),
        os.path.join(project_base_path, "scripts"),
        os.path.join(project_base_path, "data"),
        os.path.join(project_base_path, "assets"),
        os.path.join(project_base_path, "logs"),
    ]
    
    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Define files and their content
    files = {
        os.path.join(project_base_path, "README.md"): generate_readme(project_name),
        os.path.join(project_base_path, "requirements.txt"): generate_requirements(),
        os.path.join(project_base_path, ".gitignore"): "config/secrets.env\n__pycache__/\n*.pyc\n",
        os.path.join(project_base_path, "LICENSE"): "MIT License\n\nCopyright (c) 2025",
        os.path.join(project_base_path, "CHANGELOG.md"): "# Changelog\n\nAll notable changes to this project will be documented here.",
        os.path.join(project_base_path, "config", "secrets.env"): "openrouter_api_key=your_openrouter_api_key_here\nrapid_api_key=your_rapid_api_key_here\n",
        os.path.join(project_base_path, "config", "settings.yaml"): f"project_name: '{project_name}'\n",
        os.path.join(project_base_path, project_slug, "__init__.py"): "",
        os.path.join(project_base_path, project_slug, "main.py"): generate_main_py(),
        os.path.join(project_base_path, project_slug, "api_key_handler.py"): generate_api_key_handler_py(),
        os.path.join(project_base_path, "tests", "__init__.py"): "",
        os.path.join(project_base_path, "tests", "test_api_key_handler.py"): generate_test_api_key_handler_py(project_slug),
        os.path.join(project_base_path, "docs", "index.md"): f"# {project_name} Documentation\n\nDetailed project documentation.",
        os.path.join(project_base_path, "scripts", "data_importer.py"): generate_data_importer_py(),
        os.path.join(project_base_path, "data", "sample_data.json"): '[{"id": 1, "question": "What is the capital of France?", "answer": "Paris"}]\n',
        os.path.join(project_base_path, "logs", "app.log"): "",
    }

    # Write files with UTF-8 encoding
    for file_path, content in files.items():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"Project '{project_name}' created successfully at '{project_base_path}'!")

def generate_requirements():
    """Generate the content for the requirements.txt file."""
    return (
        "certifi==2024.12.14\n"
        "charset-normalizer==3.4.1\n"
        "colorama==0.4.6\n"
        "idna==3.10\n"
        "iniconfig==2.0.0\n"
        "packaging==24.2\n"
        "pluggy==1.5.0\n"
        "pytest==8.3.4\n"
        "python-dotenv==1.0.1\n"
        "PyYAML==6.0.2\n"
        "requests==2.32.3\n"
        "urllib3==2.3.0\n"
    )

def generate_main_py():
    """Generate the content for the main.py file."""
    return (
        "import os\n"
        "import yaml\n"
        "import json\n"
        "from api_key_handler import get_openrouter_api_key, get_rapid_api_key\n\n"
        "\n"
        "# This example of main.py shows how to get info from different config and data files\n"
        "\n"
        "def main():\n"
        "    # Calculate the absolute path to 'config/settings.yaml'\n"
        "    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n"
        "    config_path = os.path.join(base_dir, 'config', 'settings.yaml')\n"
        "    data_path = os.path.join(base_dir, 'data', 'sample_data.json')\n\n"
        "    # Load project name from config.yaml\n"
        "    with open(config_path, 'r') as file:\n"
        "        config = yaml.safe_load(file)\n"
        "    project_name = config['project_name']\n\n"
        "    print(f'Welcome to {project_name}!')\n"
        "    print(f'OpenRouter API Key: {get_openrouter_api_key()}')\n"
        "    print(f'RapidAPI Key: {get_rapid_api_key()}')\n\n"
        "    # Load and print sample data\n"
        "    with open(data_path, 'r') as file:\n"
        "        sample_data = json.load(file)\n"
        "    print('Sample Data:')\n"
        "    for item in sample_data:\n"
        "        print(f\"Question: {item['question']} | Answer: {item['answer']}\")\n\n"
        "if __name__ == '__main__':\n"
        "    main()\n"
    )

def generate_api_key_handler_py():
    """Generate the content for the api_key_handler.py file."""
    return (
        "import os\n"
        "from dotenv import load_dotenv\n\n"
        "# Ensure the correct path to 'secrets.env' is provided\n"
        "load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'secrets.env'))\n\n"
        "def get_openrouter_api_key():\n"
        "    return os.getenv('openrouter_api_key')\n\n"
        "def get_rapid_api_key():\n"
        "    return os.getenv('rapid_api_key')\n"
    )

def generate_test_api_key_handler_py(project_slug):
    """Generate the content for the test_api_key_handler.py file."""
    return (
        f"from {project_slug}.api_key_handler import get_openrouter_api_key, get_rapid_api_key\n\n"
        "def test_get_openrouter_api_key():\n"
        "    key = get_openrouter_api_key()\n"
        "    assert key == 'your_openrouter_api_key_here'\n\n"
        "def test_get_rapid_api_key():\n"
        "    key = get_rapid_api_key()\n"
        "    assert key == 'your_rapid_api_key_here'\n"
    )

def generate_data_importer_py():
    """Generate the content for the data_importer.py file."""
    return (
        "# Script to import data into the system\n\n"
        "def import_data():\n"
        "    print('Importing data...')\n\n"
        "if __name__ == '__main__':\n"
        "    import_data()\n"
    )

def generate_readme(project_name):
    folder_structure = """
    {project_name}/
    │
    ├── config/                    # Configuration files
    │   ├── secrets.env            # Environment file containing API keys
    │   └── settings.yaml          # General project settings
    │
    ├── {project_name}/            # Main package folder
    │   ├── __init__.py            # Package initialization
    │   ├── main.py                # Entry point for the application
    │   ├── api_key_handler.py     # Module for handling API keys
    │
    ├── tests/                     # Test suite - USE pytest: https://docs.pytest.org/
    │   ├── __init__.py            # Indicates this is a package
    │   ├── test_api_key_handler.py # Test for API key handler
    │
    ├── docs/                      # Documentation
    │   ├── index.md               # Main documentation file
    │
    ├── scripts/                   # Standalone scripts
    │   └── data_importer.py       # Example script
    │
    ├── data/                      # Sample data
    │   └── sample_data.json       # Example data file
    │
    ├── assets/                    # Static files or other resources    
    ├── logs/                      # Folder for log files
    │   └── app.log                # Default log file
    │
    ├── .gitignore                 # Git ignore file
    ├── requirements.txt           # List of dependencies
    ├── README.md                  # Project description and overview
    ├── LICENSE                    # License file
    └── CHANGELOG.md               # List of changes and versions
    """.strip().format(project_name=project_name)
    return f"# {project_name}\n\nProject description.\n\n## Folder Structure\n\n```\n{folder_structure}\n```"

def main():
    # Get project name from user
    project_name = input("Enter your project name: ").strip()
    create_project_structure(project_name)

if __name__ == "__main__":
    main()
