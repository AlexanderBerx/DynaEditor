from distutils.core import setup

setup(
    name='DynaEditor',
    version='v0.1.0',
    packages=['dynaeditor', 'dynaeditor.utils', 'dynaeditor.widgets', 'dynaeditor.attributes',
              'dynaeditor.attribute_widgets'],
    url='',
    license='BSD3',
    author='Alexander Berx',
    author_email='alexanderberx@gmail.com',
    description='dynamic attribute editor for Autodesk Maya 2017 and up'
)
