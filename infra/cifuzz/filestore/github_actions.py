# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

import filestore
from github_actions_toolkit.artifact import artifact_client

DIRECTORY = os.path.dirname(__file__)

class GithubActionsFilestore(BaseFilestore):

  def upload_directory(self, name, directory):
    directory = os.path.abspath(directory)

    # Get file paths.
    file_paths = []
    for root, _, curr_file_paths in os.walk(directory):
      for file_path in curr_file_paths:
        file_paths.append(os.path.join(root, file_path))

    # !!! Zip?

    return artifact_client.upload_artifact(name, file_paths, directory)