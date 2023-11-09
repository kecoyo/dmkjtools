import unittest

from common.string import *


class TestStringCase(unittest.TestCase):
    def test_camel_case(self):
        self.assertEqual(camel_case("testCamelCase"), "testCamelCase")
        self.assertEqual(camel_case("TestCamelCase"), "testCamelCase")
        self.assertEqual(camel_case("test_camel_case"), "testCamelCase")
        self.assertEqual(camel_case("TEST_CAMEL_CASE"), "testCamelCase")
        self.assertEqual(camel_case("test.camel.case"), "testCamelCase")
        self.assertEqual(camel_case("test-camel-case"), "testCamelCase")
        self.assertEqual(camel_case("test/camel/case"), "testCamelCase")
        self.assertEqual(camel_case("test camel case"), "testCamelCase")
        self.assertEqual(camel_case("Test Camel Case"), "testCamelCase")
        self.assertEqual(camel_case("TEST CAMEL CASE"), "testCamelCase")

    def test_pascal_case(self):
        self.assertEqual(pascal_case("testCamelCase"), "TestCamelCase")
        self.assertEqual(pascal_case("TestCamelCase"), "TestCamelCase")
        self.assertEqual(pascal_case("test_camel_case"), "TestCamelCase")
        self.assertEqual(pascal_case("TEST_CAMEL_CASE"), "TestCamelCase")
        self.assertEqual(pascal_case("test.camel.case"), "TestCamelCase")
        self.assertEqual(pascal_case("test-camel-case"), "TestCamelCase")
        self.assertEqual(pascal_case("test/camel/case"), "TestCamelCase")
        self.assertEqual(pascal_case("test camel case"), "TestCamelCase")
        self.assertEqual(pascal_case("Test Camel Case"), "TestCamelCase")
        self.assertEqual(pascal_case("TEST CAMEL CASE"), "TestCamelCase")

    def test_snake_case(self):
        self.assertEqual(snake_case("testCamelCase"), "test_camel_case")
        self.assertEqual(snake_case("TestCamelCase"), "test_camel_case")
        self.assertEqual(snake_case("test_camel_case"), "test_camel_case")
        self.assertEqual(snake_case("TEST_CAMEL_CASE"), "test_camel_case")
        self.assertEqual(snake_case("test-camel-case"), "test_camel_case")
        self.assertEqual(snake_case("test.camel.case"), "test_camel_case")
        self.assertEqual(snake_case("test/camel/case"), "test_camel_case")
        self.assertEqual(snake_case("test camel case"), "test_camel_case")
        self.assertEqual(snake_case("Test Camel Case"), "test_camel_case")
        self.assertEqual(snake_case("TEST CAMEL CASE"), "test_camel_case")

    def test_constant_case(self):
        self.assertEqual(constant_case("testCamelCase"), "TEST_CAMEL_CASE")
        self.assertEqual(constant_case("TestCamelCase"), "TEST_CAMEL_CASE")
        self.assertEqual(constant_case("test_camel_case"), "TEST_CAMEL_CASE")
        self.assertEqual(constant_case("TEST_CAMEL_CASE"), "TEST_CAMEL_CASE")
        self.assertEqual(constant_case("test.camel.case"), "TEST_CAMEL_CASE")
        self.assertEqual(constant_case("test-camel-case"), "TEST_CAMEL_CASE")
        self.assertEqual(constant_case("test/camel/case"), "TEST_CAMEL_CASE")
        self.assertEqual(constant_case("test camel case"), "TEST_CAMEL_CASE")
        self.assertEqual(constant_case("Test Camel Case"), "TEST_CAMEL_CASE")
        self.assertEqual(constant_case("TEST CAMEL CASE"), "TEST_CAMEL_CASE")

    def test_kebab_case(self):
        self.assertEqual(kebab_case("testCamelCase"), "test-camel-case")
        self.assertEqual(kebab_case("TestCamelCase"), "test-camel-case")
        self.assertEqual(kebab_case("test_camel_case"), "test-camel-case")
        self.assertEqual(kebab_case("TEST_CAMEL_CASE"), "test-camel-case")
        self.assertEqual(kebab_case("test.camel.case"), "test-camel-case")
        self.assertEqual(kebab_case("test-camel-case"), "test-camel-case")
        self.assertEqual(kebab_case("test/camel/case"), "test-camel-case")
        self.assertEqual(kebab_case("test camel case"), "test-camel-case")
        self.assertEqual(kebab_case("Test Camel Case"), "test-camel-case")
        self.assertEqual(kebab_case("TEST CAMEL CASE"), "test-camel-case")

    def test_param_case(self):
        self.assertEqual(param_case("testCamelCase"), "test-camel-case")
        self.assertEqual(param_case("TestCamelCase"), "test-camel-case")
        self.assertEqual(param_case("test_camel_case"), "test-camel-case")
        self.assertEqual(param_case("TEST_CAMEL_CASE"), "test-camel-case")
        self.assertEqual(param_case("test.camel.case"), "test-camel-case")
        self.assertEqual(param_case("test-camel-case"), "test-camel-case")
        self.assertEqual(param_case("test/camel/case"), "test-camel-case")
        self.assertEqual(param_case("test camel case"), "test-camel-case")
        self.assertEqual(param_case("Test Camel Case"), "test-camel-case")
        self.assertEqual(param_case("TEST CAMEL CASE"), "test-camel-case")

    def test_dot_case(self):
        self.assertEqual(dot_case("testCamelCase"), "test.camel.case")
        self.assertEqual(dot_case("TestCamelCase"), "test.camel.case")
        self.assertEqual(dot_case("test_camel_case"), "test.camel.case")
        self.assertEqual(dot_case("TEST_CAMEL_CASE"), "test.camel.case")
        self.assertEqual(dot_case("test.camel.case"), "test.camel.case")
        self.assertEqual(dot_case("test-camel-case"), "test.camel.case")
        self.assertEqual(dot_case("test/camel/case"), "test.camel.case")
        self.assertEqual(dot_case("test camel case"), "test.camel.case")
        self.assertEqual(dot_case("Test Camel Case"), "test.camel.case")
        self.assertEqual(dot_case("TEST CAMEL CASE"), "test.camel.case")

    def test_path_case(self):
        self.assertEqual(path_case("testCamelCase"), "test/camel/case")
        self.assertEqual(path_case("TestCamelCase"), "test/camel/case")
        self.assertEqual(path_case("test_camel_case"), "test/camel/case")
        self.assertEqual(path_case("TEST_CAMEL_CASE"), "test/camel/case")
        self.assertEqual(path_case("test.camel.case"), "test/camel/case")
        self.assertEqual(path_case("test-camel-case"), "test/camel/case")
        self.assertEqual(path_case("test/camel/case"), "test/camel/case")
        self.assertEqual(path_case("test camel case"), "test/camel/case")
        self.assertEqual(path_case("Test Camel Case"), "test/camel/case")
        self.assertEqual(path_case("TEST CAMEL CASE"), "test/camel/case")

    def test_title_case(self):
        self.assertEqual(title_case("testCamelCase"), "Test Camel Case")
        self.assertEqual(title_case("TestCamelCase"), "Test Camel Case")
        self.assertEqual(title_case("test_camel_case"), "Test Camel Case")
        self.assertEqual(title_case("TEST_CAMEL_CASE"), "Test Camel Case")
        self.assertEqual(title_case("test-camel-case"), "Test Camel Case")
        self.assertEqual(title_case("test.camel.case"), "Test Camel Case")
        self.assertEqual(title_case("test/camel/case"), "Test Camel Case")
        self.assertEqual(title_case("test camel case"), "Test Camel Case")
        self.assertEqual(title_case("Test Camel Case"), "Test Camel Case")
        self.assertEqual(title_case("TEST CAMEL CASE"), "Test Camel Case")
