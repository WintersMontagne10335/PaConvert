import sys
sys.path.append('tests/code_library/code_case/temp_paddle_code/utils')
import paddle_aux
import paddle
print('#########################case1#########################')
cpu = str('cpu'.replace('cuda', 'gpu'))
a = paddle.randn(shape=[2, 3])
c = paddle.randn(shape=[2, 3], dtype='float64')
b = a.to(cpu, non_blocking=False, copy=False)
print('#########################case2#########################')
b = a.to('cpu')
print('#########################case3#########################')
b = a.to(device=cpu, dtype='float64')
print('#########################case4#########################')
b = a.to('float64')
print('#########################case5#########################')
b = a.to(dtype='float64')
print('#########################case6#########################')
b = a.to(c)
print('#########################case7#########################')
a = a.to('float16')
print('#########################case8#########################')
table = a
b = a.to(table.place)
print('#########################case9#########################')
b = a.to('float32')
print('#########################case10#########################')
device = str('cpu'.replace('cuda', 'gpu'))
b = paddle.to_tensor(data=[-1]).to('bool')
print('#########################case11#########################')
dtype = 'float32'
b = a.to(dtype=dtype)
print('#########################case12#########################')
b = a.to(str('cpu'.replace('cuda', 'gpu')))
