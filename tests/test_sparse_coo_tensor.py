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

obj = APIBase("torch.sparse_coo_tensor")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        i = torch.tensor([[0, 1, 1],
                          [2, 0, 2]])
        v = torch.tensor([3, 4, 5], dtype=torch.float32)
        result = torch.sparse_coo_tensor(i, v, [2, 4])
        result = result.to_dense()
        """
    )
    obj.run(pytorch_code, ["result"])


def _test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        i = torch.tensor([[0, 1, 1],
                          [2, 0, 2]])
        v = torch.tensor([3, 4, 5], dtype=torch.float32)
        result = torch.sparse_coo_tensor(i, v, [2, 4], dtype=torch.float64)
        result = result.to_dense()
        """
    )
    obj.run(pytorch_code, ["result"])


def _test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.sparse_coo_tensor(torch.empty([1, 0]), [], [1])
        """
    )
    obj.run(pytorch_code, ["result"])


def _test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.sparse_coo_tensor(torch.empty([1, 0]), torch.empty([0, 2]), [1, 2])
        result = result.to_dense()
        """
    )
    obj.run(pytorch_code, ["result"])
