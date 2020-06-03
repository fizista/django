from django.utils import six

memoryview = memoryview if six.PY3 else buffer
