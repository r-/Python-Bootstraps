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
        os.path.join(project_base_path, project_slug),
    ]
    
    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Define files and their content
    files = {
        os.path.join(project_base_path, "README.md"): generate_readme(project_name),
        os.path.join(project_base_path, "requirements.txt"): "",  # Empty for minimal dependencies
        os.path.join(project_base_path, ".gitignore"): "__pycache__/\n*.pyc\n",
        os.path.join(project_base_path, project_slug, "__init__.py"): "",
        os.path.join(project_base_path, project_slug, "main.py"): generate_main_py(),
    }

    # Write files with UTF-8 encoding
    for file_path, content in files.items():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"Basic project '{project_name}' created successfully at '{project_base_path}'!")

def generate_main_py():
    """Generate the content for the main.py file."""
    return (
        "def main():\n"
        "    print('Hello, World! This is a basic template project.')\n\n"
        "if __name__ == '__main__':\n"
        "    main()\n"
    )

def generate_readme(project_name):
    folder_structure = f"""
    {project_name}/
    │
    ├── {project_name}/       # Main package folder
    │   ├── __init__.py       # Package initialization
    │   ├── main.py           # Main application entry point
    │
    ├── .gitignore           # Git ignore file
    ├── requirements.txt     # Dependencies (empty for now)
    ├── README.md            # Project description
    """.strip()
    return f"# {project_name}\n\nBasic project template.\n\n## Folder Structure\n\n```\n{folder_structure}\n```"

def main():
    # Get project name from user
    project_name = input("Enter your project name: ").strip()
    create_project_structure(project_name)

if __name__ == "__main__":
    main()
