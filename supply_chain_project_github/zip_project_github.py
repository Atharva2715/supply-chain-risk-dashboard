import os
import zipfile

def create_zip(source_dir, output_filename):
    exclude_dirs = {'.venv', 'AppData', '__pycache__', '.git', '.mypy_cache', '.pytest_cache'}
    exclude_files = {'uv.exe', 'uvw.exe', 'uvx.exe', os.path.basename(output_filename)}
    
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                if file in exclude_files: continue
                file_path = os.path.join(root, file)
                if os.path.abspath(file_path) == os.path.abspath(output_filename): continue
                if file_path.endswith('.zip'): continue
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)

if __name__ == '__main__':
    source_directory = r'c:\Users\Atharva\OneDrive\Desktop\supply chain risk'
    output_zip = r'c:\Users\Atharva\OneDrive\Desktop\supply_chain_project_github.zip'
    create_zip(source_directory, output_zip)
