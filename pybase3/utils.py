#-*- coding: utf-8 -*-

######################################################################################

class SmartDict(dict):
     """SmartDict class with attributes equating dict keys"""

     def __init__(self, d: dict = None, **kw):
         if d:
             super(SmartDict, self).__init__(d, **kw)
         else:
             super(SmartDict, self).__init__({}, **kw)
     
     def __hasattr__(self, attr):
         return hasattr(super(), attr) or not not self.get(attr)
     
     def __getattr__(self, attr):
         parent = super()
         resp = self.get(attr)
         if not resp:
             if hasattr(parent, attr):
                 return getattr(parent, attr)
         return resp
     
     def __setattr__(self, attr, value):
         self[attr]  = value
     
     def __delattr__(self, attr):
         del self[attr]

     def copy(self):
         d = super().copy()
         return SmartDict(d)

     @property
     def parent(self):
         return super()

