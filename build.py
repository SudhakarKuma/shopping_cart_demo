from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")

name = "shopping-cart-demo"
version = "1.0"
summary = "A Shopping Cart application"

default_task = "publish"


@init
def set_properties(project):

    project.set_property("unittest_module_glob", "test_*")

    project.set_property("coverage_threshold_warn", 70)
    project.set_property("coverage_break_build", True)
