#!/usr/bin/env python
# encoding: utf-8

"""Tests for circlify"""

import unittest

import circlify as circ

# Set this variable to True to get a display of the layout (req matlplotlib)
display_layout = False


def density(solution):
    """Report density of the solution

    The surface of the circle relative to the enclosure

    """
    circ.circ.scale(solution, circ.Circle(0.0, 0.0, 1.0))
    density = sum([c.r * c.r for c in solution if c.r < 1.0])
    return density


class CircleOutputTest(unittest.TestCase):
    """Check behaviour of Circle class"""

    def test_repr_and_str_with_id_(self):
        """Check str() and repr() conversion"""
        expected = "Circle(level=1, datum=2.0, " \
                   "circle=None, ex={'label': '3'})"
        self.assertEqual(expected, str(circ.Circle(1, 2.0, ex={'label': '3'})))

    def test_repr_and_str_with_circle(self):
        """Check str() and repr() conversion"""
        expected = "Circle(level=1, datum=2.0, " \
                   "circle=_Circle(x=0, y=0, r=1), ex=None)"
        self.assertEqual(expected,
                         str(circ.Circle(1, 2.0, circle=circ._Circle(0, 0, 1))))


class SpecialCases(unittest.TestCase):
    """Hedge cases and obvious answers handling."""

    def test_empty_input(self):
        """What do we do when the output is empty?"""
        actual = circ.circlify([])
        self.assertEqual(actual, [])

    def test_single_value(self):
        """If there is only one value, it should occupy the whole circle."""
        actual = circ.circlify([2.0])
        expected = [circ.Circle(1, 2.0, circle=circ._Circle(0.0, 0.0, 1.0))]
        self.assertEqual(actual, expected)

    def test_two_equal_values(self):
        """Two equal circle cases is also trivial."""
        actual = circ.circlify([1.0, 1.0])
        expected = [circ.Circle(1, 1.0, circle=circ._Circle(0.5, 0.0, 0.5)),
                    circ.Circle(1, 1.0, circle=circ._Circle(-0.5, 0.0, 0.5))]
        self.assertEqual(actual, expected)


class TestCaseWithDisplay(unittest.TestCase):
    """Display the result of the placement of the circle."""

    def display(self, circles, labels):
        """Forwards call to circ.circlify.bubbles()."""
        try:
            if display_layout:
                circ.bubbles(circles, labels)
        except AttributeError as err:
            print("%s. %s".format(err, "Did you install matplotlib?"))
            raise


class PrimeSerieTestCase(TestCaseWithDisplay):
    """Consider a simple sequence of prime number for radius to our circles."""

    def setUp(self):
        """Sets up the primes sequence 1, 2, 3, ... up to 19."""
        self.data = [19, 17, 13, 11, 7, 5, 3, 2, 1]

    def test_circlify(self):
        """Check the coordinates of the circles returned are expected."""
        actual = circ.circlify(self.data, show_enclosure=True)
        expected = [
            circ.Circle(0, None, circle=circ._Circle(x=0.0, y=0.0, r=1.0)),
            circ.Circle(1, 1,
                        circle=circ._Circle(x=0.09222041925800777,
                                            y=0.8617116738294696,
                                            r=0.09068624109026069)),
            circ.Circle(1, 2,
                        circle=circ._Circle(x=-0.40283175658099674,
                                            y=0.7512387781681531,
                                            r=0.12824971207048294)),
            circ.Circle(1, 3,
                        circle=circ._Circle(x=0.3252787490004198,
                                            y=0.7776370388468007,
                                            r=0.15707317711577193)),
            circ.Circle(1, 5,
                        circle=circ._Circle(x=0.48296614887228806,
                                            y=0.4541723195782383,
                                            r=0.20278059970175755)),
            circ.Circle(1, 7,
                        circle=circ._Circle(x=-0.6132109517981927,
                                            y=0.4490810687795324,
                                            r=0.23993324126007678)),
            circ.Circle(1, 11, circle=circ._Circle(x=-0.045884607890591435,
                                                   y=-0.6977206243364218,
                                                   r=0.3007722353441051)),
            circ.Circle(1, 13,
                        circle=circ._Circle(x=-0.04661299415374866,
                                            y=0.4678014425767657,
                                            r=0.32697389223002427)),
            circ.Circle(1, 17,
                        circle=circ._Circle(x=-0.411432317820337,
                                            y=-0.13064957525245907,
                                            r=0.3739089508053733)),
            circ.Circle(1, 19,
                        circle=circ._Circle(x=0.35776879346704843,
                                            y=-0.13064957525245907,
                                            r=0.39529216048201216)),
        ]
        self.display(actual, [str(v) for v in self.data])
        self.assertEqual(expected, actual)


class CountSerieTestCase(TestCaseWithDisplay):
    """Consider a simple sequence of number for radius to our circles."""

    def setUp(self):
        """Sets up the primes sequence 1, 2, ..."""
        self.data = list(range(7, 1, -1))

    def test_circlify(self):
        """Check the coordinates of the circles returned are expected."""
        actual = circ.circlify(self.data, show_enclosure=True)
        expected = [
            circ.Circle(0, None, circle=circ._Circle(x=0.0, y=0.0, r=1.0)),
            circ.Circle(1, 2,
                   circle=circ._Circle(x=-0.7680630545906644, y=0.13661056172475666,
                                  r=0.21988250795031175)),
            circ.Circle(1, 3,
                   circle=circ._Circle(x=-0.4586184780594718, y=0.5154819840108337,
                                  r=0.2692999739208646)),
            circ.Circle(1, 4,
                   circle=circ._Circle(x=0.15910532107887837, y=-0.6704181394216174,
                                  r=0.31096082487194077)),
            circ.Circle(1, 5,
                   circle=circ._Circle(x=0.15769153632817096, y=0.5438978793053209,
                                  r=0.34766477137653345)),
            circ.Circle(1, 6, circle=circ._Circle(x=-0.20976457776763055,
                                                    y=-0.08515409741642607,
                                                    r=0.3808476754656075)),
            circ.Circle(1, 7,
                   circle=circ._Circle(x=0.5824456027453089, y=-0.08515409741642607,
                                  r=0.41136250504733196))
        ]
        self.display(actual, [str(v) for v in self.data])
        self.assertEqual(expected, actual)


class GeometricSerieTestCase(TestCaseWithDisplay):
    """Consider a simple sequence of number for radius to our circles."""

    def setUp(self):
        """Sets up the primes sequence 1, 2, ..."""
        self.data = sorted([2 ** n for n in range(4, 12)], reverse=True)

    def test_circlify(self):
        """Check the coordinates of the circles returned are expected."""
        actual = circ.circlify(self.data, show_enclosure=True)
        self.display(actual, [str(v) for v in self.data])
        expected = [
            circ.Circle(0, None, circle=circ._Circle(x=0.0, y=0.0, r=1.0)),
            circ.Circle(1, 16,
                        circle=circ._Circle(x=-0.18045635173699437,
                                            y=-0.22990093891844118,
                                            r=0.051776695296636886)),
            circ.Circle(1, 32,
                        circle=circ._Circle(x=-0.42762855855875753,
                                            y=-0.6656611405645538,
                                            r=0.07322330470336313)),
            circ.Circle(1, 64,
                        circle=circ._Circle(x=-0.5170830169797044,
                                            y=-0.5131885205024093,
                                            r=0.10355339059327377)),
            circ.Circle(1, 128,
                        circle=circ._Circle(x=0.10281914590763144,
                                            y=-0.662720719883036,
                                            r=0.14644660940672627)),
            circ.Circle(1, 256,
                        circle=circ._Circle(x=-0.20710678118654763,
                                            y=-0.49258571550470814,
                                            r=0.20710678118654754)),
            circ.Circle(1, 512,
                        circle=circ._Circle(x=-0.2218254069479773,
                                            y=0.6062444788590926,
                                            r=0.29289321881345254)),
            circ.Circle(1, 1024,
                        circle=circ._Circle(x=-0.5857864376269051, y=0.0,
                                            r=0.4142135623730951)),
            circ.Circle(1, 2048,
                        circle=circ._Circle(x=0.4142135623730951, y=0.0,
                                            r=0.5857864376269051))
        ]
        self.assertEqual(expected, actual)


class EnclosureScalingTestCase(unittest.TestCase):
    """Test circ.circ.scale function"""

    def test_simple_zoom(self):
        """Trivial zoom test when the enclosure is the same as the circle."""
        input = circ._Circle(0, 0, 0.5)
        target = circ._Circle(0, 0, 1.0)
        actual = circ.scale(input, target, input)
        self.assertEqual(target, actual)

    def test_simple_zoom_off_center(self):
        """Zoom test with off center circle equal to enclosure."""
        input = circ._Circle(0.5, 0.5, 0.5)
        target = circ._Circle(0.5, 0.5, 1.0)
        actual = circ.scale(input, target, input)
        self.assertEqual(target, actual)

    def test_simple_zoom_and_translation(self):
        """Pan and zoom test with off center circle equal to enclosure."""
        input = circ._Circle(0.5, 0.5, 0.5)
        target = circ._Circle(-0.5, 0, 1.0)
        actual = circ.scale(input, target, input)
        self.assertEqual(target, actual)

    def test_zoom_with_enclosure(self):
        """Zoom test with off center circle and difference enclosure"""
        input = circ._Circle(1.0, 0.0, 1.0)
        enclosure = circ._Circle(0.0, 0.0, 2.0)
        target = circ._Circle(0.0, 0.0, 1.0)
        actual = circ.scale(input, target, enclosure)
        expected = circ._Circle(0.5, 0.0, 0.5)
        self.assertEqual(expected, actual)


class HandleDataTestCase(unittest.TestCase):
    """Test circlify._handle function."""

    def test_integer(self):
        """handles integer"""
        actual = circ._handle([42], 1)
        self.assertEqual([circ.Circle(1, 42)], actual)

    def test_float(self):
        """Handles float."""
        actual = circ._handle([42.0], 1)
        self.assertEqual([circ.Circle(1, 42)], actual)

    def test_dict_w_datum_only(self):
        """Handles dict with just the data"""
        actual = circ._handle([{'datum': 42}], 1)
        self.assertEqual([circ.Circle(1, 42)], actual)

    def test_dict_w_datum_and_id(self):
        """Handles dict with data and an id"""
        actual = circ._handle([{'datum': 42, 'id': '42'}], 1)
        self.assertEqual([circ.Circle(1, 42, ex={'id': '42'})], actual)

    def test_bad_value_raise_error(self):
        """A set of non-dict, non-numeric input raises ValueError."""
        with self.assertRaises(TypeError):
            circ._handle({'datum', 42}, 1)

    def test_bad_dict_keys_raise_error(self):
        """A dict with the wrong key raises ValueError."""
        with self.assertRaises(TypeError):
            circ._handle({'datatum': 42}, 1)

    def test_handle_children(self):
        """A dict that has children."""
        actual = circ._handle([{'datum': 42, 'children': [1, 2]}], 1)
        expected = [
            circ.Circle(1, 42, None, ex={
                'children': [circ.Circle(2, 2), circ.Circle(2, 1)]}),
        ]
        self.assertEqual(expected, actual)


class MultiLevelInputTestCase(TestCaseWithDisplay):
    """Handles multi-layer input."""

    def setUp(self):
        """Sets up the test case."""
        self.data = [
            0.05,
            {'id': 'a2', 'datum': 0.05},
            {'id': 'a0', 'datum': 0.8,
             'children': [0.3, 0.2, 0.2, 0.1], },
            {'id': 'a1', 'datum': 0.1,
             'children': [{'id': 'a1_1', 'datum': 0.05},
                          {'datum': 0.04},
                          0.01], },
        ]

    def notest_json_input(self):
        """Simple json data."""
        actual = circ.circlify(self.data, show_enclosure=True)
        expected = [
            circ.Circle(level=0, datum=None,
                        circle=circ._Circle(x=0.0, y=0.0, r=1.0)),
            circ.Circle(level=1, datum=0.05,
                        circle=circ._Circle(x=-0.565803075997749,
                                            y=0.41097786651145324,
                                            r=0.18469903125906464)),
            circ.Circle(level=1, datum=0.05, ex={'id': 'a2'},
                        circle=circ._Circle(x=-0.3385727489559141,
                                            y=0.7022188441650276,
                                            r=0.18469903125906464)),
            circ.Circle(level=1, datum=0.1, ex={'id': 'a1'},
                        circle=circ._Circle(x=-0.7387961250362587, y=0.0,
                                            r=0.2612038749637415)),
            circ.Circle(level=1, datum=0.8, ex={'id': 'a1'},
                        circle=circ._Circle(x=0.2612038749637414, y=0.0,
                                            r=0.7387961250362586)),
            circ.Circle(level=2, datum=0.01,
                        circle=circ._Circle(x=-0.7567888163564136,
                                            y=0.14087823651338607,
                                            r=0.0616618704777984)),
            circ.Circle(level=2, datum=0.04,
                        circle=circ._Circle(x=-0.8766762590444033, y=0.0,
                                            r=0.1233237409555968)),
            circ.Circle(level=2, datum=0.05, ex={'id': 'a1_1'},
                        circle=circ._Circle(x=-0.6154723840806618, y=0.0,
                                            r=0.13788013400814464)),
            circ.Circle(level=2, datum=0.1,
                        circle=circ._Circle(x=0.6664952237042423,
                                            y=0.3369290873460549,
                                            r=0.2117455702848763)),
            circ.Circle(level=2, datum=0.2,
                        circle=circ._Circle(x=-0.11288314691830154,
                                            y=-0.230392881357073,
                                            r=0.2994534572692975)),
            circ.Circle(level=2, datum=0.2,
                        circle=circ._Circle(x=0.15631936804871832,
                                            y=0.30460197676548245,
                                            r=0.2994534572692975)),
            circ.Circle(level=2, datum=0.3,
                        circle=circ._Circle(x=0.5533243963620484,
                                            y=-0.230392881357073,
                                            r=0.36675408601105247)),
        ]
        self.display(actual)
        self.assertEqual(expected, actual)

    def test_handle_single_value(self):
        """Typical specification of data with just a value."""
        actual = circ.circlify([self.data[0]])
        expected = [circ.Circle(1, 0.05, circle=circ._Circle(0, 0, 1))]
        self.assertEqual(expected, actual)

    def test_handle_custom_datum_key(self):
        """Specify value as dict with custom keys."""
        actual = circ.circlify([{'value': 0.05}], datum_field='value')
        expected = [circ.Circle(1, 0.05, circle=circ._Circle(0, 0, 1))]
        self.assertEqual(expected, actual)

    def test_handle_custom_id_key(self):
        """Specify value as dict with custom keys."""
        actual = circ.circlify([{'name': 'a2', 'datum': 0.05}], id_field='name')
        expected = [circ.Circle(1, 0.05, ex={'name': 'a2'},
                                circle=circ._Circle(0, 0, 1))]
        self.assertEqual(expected, actual)

    def test_handle_dict(self):
        """Specify value as a dict."""
        actual = circ.circlify([self.data[1]])
        expected = [
            circ.Circle(1, 0.05, ex={'id': 'a2'}, circle=circ._Circle(0, 0, 1))]
        self.assertEqual(expected, actual)

    def test_handle_dict_w_children(self):
        actual = circ.circlify([self.data[1]])
        expected = [
            circ.Circle(1, 0.05, ex={'id': 'a2'}, circle=circ._Circle(0, 0, 1))]
        self.assertEqual(expected, actual)


class HedgeTestCase(unittest.TestCase):

    def test_one_big_two_small(self):
        """Makes sure we get 3 circles in t"""
        actual = circ.circlify([0.998997995991984, 0.000501002004008016,
                                0.000501002004008016])
        self.assertEqual(3, len(actual))


if __name__ == '__main__':
    import logging

    logging.basicConfig(level='INFO')
    unittest.main()
