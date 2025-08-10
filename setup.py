import os
from pathlib import Path

def create_project_structure(root_dir):
    """Create the complete project structure for GMF portfolio optimization"""
    
    # Define the directory structure with empty files
    structure = {
        'README.md': None,
        'requirements.txt': None,
        '.gitignore': None,
        'data': {
            'raw': {
                'TSLA.csv': None,
                'BND.csv': None,
                'SPY.csv': None
            },
            'processed': {
                'merged_data.csv': None
            }
        },
        'notebooks': {
            'EDA.ipynb': None,
            'Modeling.ipynb': None,
            'Backtesting.ipynb': None
        },
        'src': {
            'data_fetch.py': None,
            'preprocess.py': None,
            'models.py': None,
            'portfolio_optimization.py': None,
            'backtesting.py': None,
            '__init__.py': None
        },
        'docs': {
            'Investment_Memo.pdf': None
        },
        'images': {}
    }

    # Create the directories and files
    for path, content in structure.items():
        if isinstance(content, dict):
            # It's a directory
            dir_path = os.path.join(root_dir, path)
            os.makedirs(dir_path, exist_ok=True)
            
            # Handle nested directories
            for sub_path, sub_content in content.items():
                if isinstance(sub_content, dict):
                    sub_dir_path = os.path.join(dir_path, sub_path)
                    os.makedirs(sub_dir_path, exist_ok=True)
                    for file_name, file_content in sub_content.items():
                        file_path = os.path.join(sub_dir_path, file_name)
                        with open(file_path, 'w') as f:
                            if file_content is not None:
                                f.write(file_content)
                else:
                    file_path = os.path.join(dir_path, sub_path)
                    with open(file_path, 'w') as f:
                        if sub_content is not None:
                            f.write(sub_content)
        else:
            # It's a file
            file_path = os.path.join(root_dir, path)
            with open(file_path, 'w') as f:
                if content is not None:
                    f.write(content)

    print(f"Project structure created successfully at {root_dir}")

if __name__ == "__main__":
    project_root = os.getcwd()  # Uses current directory
    print(f"Creating project structure in: {project_root}")
    create_project_structure(project_root)