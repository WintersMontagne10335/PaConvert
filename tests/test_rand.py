# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
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

import textwrap

from apibase import APIBase

obj = APIBase("torch.rand")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.empty(2, 3)
        result = torch.rand(input.shape)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        num = 5.
        result = torch.rand(torch.empty(2, 3).shape)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.rand(torch.empty(2, 3).shape, dtype=torch.float64, requires_grad=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        flag = False
        result = torch.rand(torch.empty(2, 3).shape, dtype=torch.float64, requires_grad=flag)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.rand(torch.empty(2, 3).shape, layout=torch.strided, dtype=torch.float64, requires_grad=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)
