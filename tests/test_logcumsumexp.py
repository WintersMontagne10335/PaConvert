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

obj = APIBase("torch.logcumsumexp")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[0.56, 0.34, 0.78], [0.98, 0.21, 1.78]])
        result = torch.logcumsumexp(x, 0)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[0.56, 0.34, 0.78], [0.98, 0.21, 1.78]])
        result = torch.logcumsumexp(x, 1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[0.56, 0.34, 0.78], [0.98, 0.21, 1.78]])
        result = torch.logcumsumexp(input=x, dim=1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.logcumsumexp(torch.tensor([[0.56, 0.34, 0.78], [0.98, 0.21, 1.78]]), dim=0)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[0.56, 0.34, 0.78], [0.98, 0.21, 1.78]])
        out = torch.tensor([[0.56, 0.34, 0.78], [0.98, 0.21, 1.78]])
        result = torch.logcumsumexp(x, 1, out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])
