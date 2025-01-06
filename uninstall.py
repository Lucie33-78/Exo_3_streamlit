import os
import pkg_resources

# Liste des paquets installés
installed_packages = [d.project_name for d in pkg_resources.working_set]

# Désinstallation de chaque package
for package in installed_packages:
    os.system(f"pip uninstall -y {package}")
