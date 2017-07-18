
## 元类

## 元类验证子类

元类可以验证某个类定义是否正确，保证类的风格协调一致, 确保类属性之间具备某些严格的关系。元类可以获取继承类的名称，其所继承的父类，以及定义在class语句中的全部类属性。

如下, 用类表示任意多边形, 元类验证子类的边数不小于3

```python
class ValidatePolygon(type):
  def __new__(meta, name, bases, class_dict):
    # don't validate the abstract Polygon class
    if bases != (object,):
      if class_dict['sides'] < 3:
        raise ValueError('Polygons need 3+ sides')
    return type.__new__(meta, name, bases, class_dict)


class Polygon(object):
  __meta__ = ValidatePolygon

  # specified by subclass
  sides = None

  @classmethod
  def interior_angles(cls):
    return (cls.sides - 2) * 180


  class Triangle(Polygon):
    sides = 3
```
