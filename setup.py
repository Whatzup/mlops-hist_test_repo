from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

__version__="0.0.1"
PKG_NAME = "TestHist"
REPO_NAME = "hist_test_repo"
AUTHOR_USER_NAME = "itzaijaz"
AUTHOR_EMAIL = "a@a.com"
pkg_desc = "Python package for displayiong test Histogram"
url = f"github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
project_urls = {
    "Bug Tracker" : f"github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
}
package_dir={"":"src"}

with open("README.md", 'r', encoding='utf-8') as f:
    long_description=f.read()

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    try:
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n","") for req in requirements]
            print(requirements)
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found.")
        return []
    return requirements


# setup(
#     name=PKG_NAME,
#     version='0.0.1',
#     author=AUTHOR_USER_NAME,
#     author_email=AUTHOR_EMAIL,
#     description=pkg_desc,
#     long_description=long_description,
#     long_description_content="text/markdown",
#     url=url,
#     project_urls=project_urls,
#     package_dir=package_dir,
#     packages=find_packages(where="src"),
#     install_requires=get_requirements("requirements_dev.txt")
# )
if __name__ == "__main__":
    get_requirements("requirements_dev.txt")