#!/usr/bin/env python
# -*- coding: utf-8 -*-
#==============================================================================
#                            SOFTBANK  ROBOTICS
#==============================================================================
# PROJECT : qidata_gui
# FILE : conftest.py
# DESCRIPTION :
"""
Prepare the conditions for proper unit testing
"""
#[MODULES IMPORTS]-------------------------------------------------------------

# Standard libraries
import errno
import os
import shutil

# Third-party libraries
import pytest

# Local modules
from qidata_apps.viewer import app as open_command

#[MODULE GLOBALS]--------------------------------------------------------------

DATA_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/")
SANDBOX_FOLDER = "/tmp/qidata_gui/"

JPG_PHOTO = "SpringNebula.jpg"
JPG_PHOTO_ANNOTATIONS = "SpringNebula.jpg.xmp"
SMALL_DATASET = "small_dataset"
FRAME_DATASET = "dataset_with_frame_and_no_tf"
FRAME_TF_DATASET = "dataset_with_frame_and_tf"
BIG_DATASET = "Michal_Asus_2016-02-19-15-25-46"
ROSBAG_ASUS = "Michal_Asus_2016-02-19-15-25-46.bag"
CALIBRATION_T = "topVGA.yml"
CALIBRATION_D = "asusQVGA.yml"

#[MODULE CONTENT]--------------------------------------------------------------

def sandboxed(path):
	"""
	Makes a copy of the given path in /tmp and returns its path.
	"""
	source_path = os.path.join(DATA_FOLDER,    path)
	tmp_path    = os.path.join(SANDBOX_FOLDER, path)

	try:
		os.mkdir(SANDBOX_FOLDER)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise

	if os.path.isdir(source_path):
		if os.path.exists(tmp_path):
			shutil.rmtree(tmp_path)
		shutil.copytree(source_path, tmp_path)
	else:
		shutil.copyfile(source_path, tmp_path)

	return tmp_path

@pytest.fixture(autouse=True, scope="function")
def begin(request):
	"""
	Add a finalizer to clean tmp folder after each test
	"""
	def fin():
		if os.path.exists(SANDBOX_FOLDER):
			shutil.rmtree(SANDBOX_FOLDER)

	request.addfinalizer(fin)

@pytest.fixture(scope="function")
def jpg_file_path():
	sandboxed(JPG_PHOTO_ANNOTATIONS)
	return sandboxed(JPG_PHOTO)

@pytest.fixture(scope="function")
def big_dataset_path():
	return sandboxed(BIG_DATASET)

@pytest.fixture(scope="function")
def dataset_with_frame_path():
	return sandboxed(FRAME_DATASET)

@pytest.fixture(scope="function")
def dataset_with_frame_and_tf_path():
	return sandboxed(FRAME_TF_DATASET)

@pytest.fixture(scope="function")
def small_dataset_path():
	return sandboxed(SMALL_DATASET)

@pytest.fixture(scope="function")
def rosbag_asus_files():
	return (sandboxed(ROSBAG_ASUS), sandboxed(CALIBRATION_T), sandboxed(CALIBRATION_D))

@pytest.fixture(scope="session")
def open_command_parser():
	return open_command.make_command_parser()