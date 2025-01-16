import setuptools


__version__ = "0.0.0"

REPO_NAME = "Bone_marrow_survival_prediction"
AUTHOR_USER_NAME = "Rohit Pawar"
SRC_REPO = "Bone_marrow_survival_prediction"
AUTHOR_EMAIL = "rppawar491@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "Healthcare machine learning project used to predict the chances of survival of childrens after bone marrow transplant surgery",
    long_description_content = "text/markdown",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)