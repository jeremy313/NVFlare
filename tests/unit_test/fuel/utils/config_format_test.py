# Copyright (c) 2023, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from nvflare.fuel.utils.config import ConfigFormat


class TestConfigFormat:
    def test_config_exts(self):
        exts2fmt_map = ConfigFormat.config_ext_formats()
        assert exts2fmt_map.get(".json") == ConfigFormat.JSON
        assert exts2fmt_map.get(".conf") == ConfigFormat.PYHOCON
        assert exts2fmt_map.get(".yml") == ConfigFormat.OMEGACONF
        assert exts2fmt_map.get(".json.default") == ConfigFormat.JSON
        assert exts2fmt_map.get(".conf.default") == ConfigFormat.PYHOCON
        assert exts2fmt_map.get(".yml.default") == ConfigFormat.OMEGACONF

    def test_config_exts2(self):
        exts2fmt_map = ConfigFormat.config_ext_formats()
        assert "|".join(exts2fmt_map.keys()) == ".json|.conf|.yml|.json.default|.conf.default|.yml.default"
