# create_env.py and activate_env.py
Theese files are made to help you work with virtual environments in python.

The files should be placed in your "envs" folder where you virtual python evironements are placed.

# Working with Python Virtual Environments

A Python virtual environment is a self-contained directory that contains a Python installation and its own set of libraries. Virtual environments are essential for isolating dependencies between projects and ensuring consistent behavior across different systems.

---

## How to Create a Virtual Environment

To create a virtual environment, use the `venv` module:

1. **Command**:
   ```bash
   python -m venv <env_name>
   ```
   Replace `<env_name>` with the desired name for your virtual environment.

2. **Example**:
   ```bash
   python -m venv my_project_env
   ```

This will create a folder named `my_project_env` containing the virtual environment.

---

## How to Activate a Virtual Environment

Once created, the virtual environment must be activated to use it.

### **On Windows**
1. Command:
   ```bash
   .\<env_name>\Scripts\activate
   ```
2. Example:
   ```bash
   .\my_project_env\Scripts\activate
   ```

### **On macOS/Linux**
1. Command:
   ```bash
   source <env_name>/bin/activate
   ```
2. Example:
   ```bash
   source my_project_env/bin/activate
   ```

After activation, your terminal prompt will change to include the name of the environment, indicating it is active.

---

## How to Install Dependencies in a Virtual Environment

After activating the environment, use `pip` to install dependencies:
```bash
pip install <package_name>
```

### Example:
```bash
pip install requests
```

---

## How to Save Installed Dependencies

To save the list of installed dependencies to a file:
```bash
pip freeze > requirements.txt
```

This creates a `requirements.txt` file containing all the installed packages and their versions. This file can be used to recreate the environment later.

---

## How to Load Dependencies from a File

To install all dependencies listed in a `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## How to Deactivate a Virtual Environment

To deactivate the current environment, use:
```bash
deactivate
```

This returns the terminal to the global Python environment.

---

## How to Delete a Virtual Environment

To delete a virtual environment:
1. Ensure the environment is deactivated.
2. Delete the environment directory:
   ```bash
   rm -rf <env_name>
   ```
   Replace `<env_name>` with the name of your virtual environment.

### Example:
```bash
rm -rf my_project_env
```

On Windows, use:
```powershell
Remove-Item -Recurse -Force <env_name>
```

---

## What Are Python Virtual Environments?

A **Python virtual environment** is a tool that helps manage project dependencies by isolating them from the global Python installation. This ensures that each project has its own set of libraries and dependencies, preventing version conflicts.

### Key Benefits:
1. **Dependency Isolation**:
   - Projects can use different versions of the same library without conflicts.
2. **Reproducibility**:
   - Ensures consistent behavior by locking dependencies to specific versions.
3. **Clean Global Python Installation**:
   - Avoids cluttering the global environment with unnecessary packages.

---

## Why Use Virtual Environments?

Using virtual environments is a best practice for Python development because it:
- Simplifies project dependency management.
- Prevents system-wide changes or conflicts.
- Facilitates collaboration by sharing `requirements.txt`.

---

