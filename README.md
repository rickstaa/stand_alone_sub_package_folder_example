# Stand alone sub package folder example

This is a small example repository you can use when you want to ship a stand-alone python
package inside another python package. It was created as a simple test repository when I
for one of my products needed a meta package that contained multiple packages that could
also be installed individually. While doing so I wanted to make sure I did not have redundant
folders in the package import name_space of the meta package. For example I want users to
have the ability to import the `PythonClass` found under the  `main_package.stand_alone_subpackage.stand_alone_subpackage.subpackage_module.python_module` under a shortened namespace `main_package.stand_alone_subpackage.subpackage_module.python_module`.
Meaning I want to get rid of the redundant `stand_alone_subpackage` namespace that was created
because the subpackage also has to work as a stand alone [pypi](https://pypi.org/) package.