from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in appointments_app/__init__.py
from appointments_app import __version__ as version

setup(
	name="appointments_app",
	version=version,
	description="Appointment Web Portal",
	author="Build With Hussain",
	author_email="hussain@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
