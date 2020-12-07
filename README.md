# Stand alone sub package folder example

This is a small example repository you can use when you want to ship a stand-alone python
package inside another python package. It was created as a simple test repository when I
for one of my products needed a meta package that contained multiple packages that could
also be installed individually. While doing so I wanted to make sure I did not have redundant
folders in the package import name_space of the meta package. For example I want users to
have the ability to import the `PythonClass` found under the  `main_package.stand_alone_subpackage.stand_alone_subpackage.subpackage_module.python_module` under a shortened namespace `main_package.stand_alone_subpackage.subpackage_module.python_module`.
Meaning I want to get rid of the redundant `stand_alone_subpackage` namespace that was created
because the subpackage also has to work as a stand alone [pypi](https://pypi.org/) package.

## Current working methods

After asking [a question on stackoverflow](https://stackoverflow.com/questions/63464555/create-name-space-package-that-contains-standalone-installable-sub-packages/63465830#63465830) I came up with a setup that allows getting rid of the redundant folder. The code for this is found in the `setup.py` file. Using this setup.py file you can
install the package with the shortened namespace package using the `pip install .` command. I also looked for a way to put all this logic inside the setup.cfg file [see this issue on setuptools](https://github.com/pypa/setuptools/issues/2467). This however is not yet possible without converting all the sub-packages to [name_space packages](https://packaging.python.org/guides/packaging-namespace-packages/) and using the [recommended name_space packages folder structure](https://github.com/pypa/sample-namespace-packages/tree/master/native). For my solution I did not want to do this since this makes the folder structure more complicated.
