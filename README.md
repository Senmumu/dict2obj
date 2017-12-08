# Dict2obj: transform dict to simpler object

Dict2obj is a Python implementation to transform python dict to object, thus you 
can access json with easier way "dot",I'm sure this little tool can save your life.

# Install
```shell
$pip install dict2obj -U
```
# Usage
```python
>>>from dict2obj import dict2obj
>>>a={"sen":1}
>>>b=dict2obj.Dict2Obj(a)
>>>b.sen
1
```
